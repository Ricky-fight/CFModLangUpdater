import pathlib
import shutil
import sys
from json import JSONDecodeError

import requests

from config import MaintainVersion, SupportLoader, SupportVersion, APPKEY
from datamodels import *
from datamodels import File
from translate_difftool import performVersionUpdate

modname = ""

ModFilesDict = dict[MaintainVersion, File]


def get(path, params=None) -> requests.Response:
    headers = {
        'Accept':    'application/json',
        'x-api-key': APPKEY
    }
    base_url = 'https://api.curseforge.com'
    return requests.get(base_url + path, headers=headers, params=params)


def post(path, *, body, params=None) -> requests.Response:
    headers = {
        'Accept':    'application/json',
        'x-api-key': '$2a$10$NeoaZOd7iGYnan3Clojbg.tVk/oLoJYhE9z3fqC/PdJEm0rj12oJy'
    }
    base_url = 'https://api.curseforge.com'
    return requests.post(base_url + path, headers=headers, json=body, params=params)


def getData(r: requests.Response):
    """
    get response json data
    :param r: response fron requests.request()
    :return: dict object from json
    """
    if r.status_code == 200:
        try:
            return r.json()['data']
        except JSONDecodeError as e:
            print(f"获取返回数据失败{e}")


# class ModInfo:
#     def __init__(self, argv):
#         self.modid = argv['id']
#         self.name = argv['name']
#         self.slug = argv['slug']
#         self.sourceUrl = argv['links']['sourceUrl']
#         self.mainFileId = argv['mainFileId']
#         self.latestFiles = argv['latestFiles']
#         self.latestFilesIndex = argv['latestFilesIndexes']
#         self.allowModDistribution = argv['allowModDistribution']


# def modInfoParser(jsonBody):
#     """
#     use for json.loads()
#     :param jsonBody: json object from request response
#     :return: ModInfo object
#     """
#     return ModInfo(jsonBody)


# def getFiles(m: Mod) -> [File]:
#     path = f"/v1/mods/{m.id}/files"
#     params = None
#     r = request(path, params)
#     files = [File.from_dict(file) for file in getData(r)]
#     return files
def getMod(modid: int) -> Mod:
    print("正在获取模组信息……")
    r = get(f"/v1/mods/{modid}")
    if r.status_code != 200:
        print("获取模组数据失败，请检查网络情况且Project ID是否正确")
    m = mod_from_dict(r.json()['data'])
    global modname
    modname = m.slug
    print(f"获取模组数据成功。\n\t模组名：{m.name}\n\t模组地址：https://www.curseforge.com/minecraft/mc-mods/{m.slug}")
    return m


def getFilesToDownload(m: Mod) -> ModFilesDict:
    """
    目前测试版配置为只下载1.18-1.19的模组
    :param m:
    :return:
    """

    def match(f: File, loader, gameversion):
        if loader in f.game_versions:
            for st_version in f.sortable_game_versions:
                if gameversion == st_version.game_version_type_id:
                    return True
        else:
            return False

    latestFileIndexes = m.latest_files_indexes
    body = {"fileIds": [idx.file_id for idx in latestFileIndexes]}
    r = post("/v1/mods/files", body=body)
    # r = get(f"/v1/mods/{m.id}/files")
    # params = {}
    latestFiles = [file_from_dict(filedata) for filedata in getData(r)]
    print("获取最新文件数据成功，文件数据如下：")
    print("\t文件名")
    for f in latestFiles:
        print(f"\t{f.file_name} ")
    # 似乎没有必要，api拿到文件数据本来就是排好序的
    # sorted_latestFiles = sorted(latestFiles, key=lambda f: f.id, reverse=False)
    filesToDownload = {}
    for f in latestFiles:
        # 1.18 Forge
        if MaintainVersion.FORGE_118 not in filesToDownload and match(f, SupportLoader.FORGE,
                                                                      SupportVersion.V1_18):
            filesToDownload[MaintainVersion.FORGE_118] = f
        # 1.18 Fabric
        if MaintainVersion.FABRIC_118 not in filesToDownload and match(f, SupportLoader.FABRIC,
                                                                       SupportVersion.V1_18):
            filesToDownload[MaintainVersion.FABRIC_118] = f
        # 1.19 Forge
        if MaintainVersion.FORGE_119 not in filesToDownload and match(f, SupportLoader.FORGE,
                                                                      SupportVersion.V1_19):
            filesToDownload[MaintainVersion.FORGE_119] = f
        # 1.19 Fabric
        # if MaintainVersion.FABRIC_119 not in filesToDownload and match(f, SupportLoader.FABRIC,
        #                                                                      SupportVersion.V1_19):
        #     filesToDownload[MaintainVersion.FABRIC_119] = f
    # filesTodownload = dict.fromkeys(filesToDownload)
    # for filedata in [file_from_dict(f) for f in getData(r)]:
    #     for version, idx in latestFileIndexes.items():
    #         if filedata.id == idx.file_id:
    #             filesTodownload[version] = filedata
    # assert len(filesTodownload) == len(latestFileIndexes)
    print(f"获取即将下载文件数据成功，获取到{[key.value for key in filesToDownload]}版本的文件")
    return filesToDownload


def download(filesTodownload: ModFilesDict):
    """
    带缓存命中的批量下载，用匹配文件大小的方式判断缓存是否命中
    :param filesTodownload: 一个仓库维护版本与模组文件对应的字典
    :return: None
    """
    if not filesTodownload:
        print("下载了个寂寞……")
        return
    cacheDir = pathlib.Path("cache")
    if not cacheDir.exists():
        cacheDir.mkdir()
    for version, f in filesTodownload.items():
        filePath = cacheDir / version.value / f.file_name
        if filePath.exists():
            if filePath.lstat().st_size == f.file_length:
                # hit cache, skip download
                continue
        url = f.download_url
        print(f"开始下载：[{version.value} - {f.file_name}]")
        r = requests.get(url, stream=True)
        (filePath / '..').mkdir(exist_ok=True)
        with open(filePath, "wb") as outFile:
            shutil.copyfileobj(r.raw, outFile)


def run():
    """
    main func
    :return:
    """
    try:
        modid = int(sys.argv[1])
    except IndexError:
        modid = input("请输入Project ID：")
    moddata = getMod(modid)
    versionFilesDict = getFilesToDownload(moddata)
    download(versionFilesDict)
    # TODO: 提取语言文件，以1.19版本为基准进行diff+merge，自动生成packer-policy.json
    # 策略：plainclone=1, clonemissing=2, backport=3, patch=4
    for version, file in versionFilesDict.items():
        filepath = pathlib.Path("cache") / version.value / file.file_name
        en, us = performVersionUpdate(moddata.slug, version, filepath)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    run()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助