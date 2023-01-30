import re
import zipfile
from collections import namedtuple
from enum import Enum
from json import dump
from pathlib import Path

from json5 import loads, load

from config import MaintainVersion, repoDirRoot

# from prettytable import MARKDOWN, PrettyTable

enuss = {}
zhcns = {}

# print(jars)
LangDict = dict[str:str]
LangDictTuple = namedtuple("LangDictTuple", ['en', 'zh'])


class Policy(Enum):
    plainclone = 1
    clonemissing = 2
    backport = 3
    patch = 4


def exportjson(file, langdict: LangDict) -> LangDict:
    """
    读取文件并合并到给定的LangDict
    :param file:
    :param langdict:
    :return:
    """
    rst = langdict.copy()
    with open(file) as f:
        if f.readable():
            try:
                modid = file.filename.split('/')[1]
                rst[modid] = langdict.get(modid, {}) | load(f, encoding='utf-8')
            except UnicodeDecodeError:
                print(file.filename + '存在非utf-8编码，请手动操作！')
            except ValueError:
                print(file.filename + '文件不符合json格式，请手动操作！')
    return rst


def mergeTranslationKeys(origin: LangDict, dest: LangDict, mode: Policy = Policy.clonemissing):
    """
    TODO 根据合并策略执行翻译键合并操作
    :param origin:
    :param dest:
    :param mode:
    :return: rst 合并后的dict
    """
    match mode:
        case Policy.plainclone:
            dest.clear()
            dest |= origin
            pass
        case Policy.clonemissing:
            for key in origin:
                if key not in dest:
                    dest[key] = origin[key]
            pass
        case Policy.backport:
            for key in dest:
                if key in origin:
                    dest[key] = origin[key]
            pass
        case Policy.patch:
            # TODO
            pass
    return


def performVersionUpdate(modname: str, version: MaintainVersion, file: Path):
    """
    执行指定版本的语言文件更新操作，解压出模组里的语言文件并与库中进行比对，
    terms:
        ref: 模组内文件
        repo: 汉化仓库内文件
    process:
        if
            该版本 repo_en 或 repo_zh 不存在，则调用库里其他版本的文件，高版本优先
            TODO：加入packer-policy.json软链接的支持，直接调用source指向的文件目录
        ref_en  ->  repo_en with clonemissing
        ref_zh  ->  repo_zh with clonemissing
        repo_en ->  repo_zh with clonemissing
    :param modname:
    :param file: curseforge api 文件数据对象
    :param version: 执行更新的版本
    :return: (new_en, new_zh) : LangDictTuple
    """
    projectPath = repoDirRoot / "projects" / version.value / "assets" / modname
    modid, (ref_en, ref_zh) = extractLang(file)
    if modid:
        fullPath = projectPath / modid / "lang"
        if fullPath.joinpath("en_us.json").exists():
            repo_en = readLangJson(fullPath.joinpath("en_us.json"))
        else:
            print(f"未找到 {version.value} 版本的仓库内 en_us.json，是否在其他版本寻找？（优先高版本）")
            response = input("同意则直接回车，不执行查找则输入任意字符")
            if not response:
                repo_en = findLang(modname, modid, "en_us.json")
            else:
                repo_en = {}
        if fullPath.joinpath("zh_cn.json").exists():
            repo_zh = readLangJson(fullPath.joinpath("zh_cn.json"))
        else:
            print(f"未找到 {version.value} 版本的仓库内 zh_cn.json，是否在其他版本寻找？（优先高版本）")
            response = input("同意则直接回车，不执行查找则输入任意字符")
            if not response:
                repo_zh = findLang(modname, modid, "zh_cn.json")
            else:
                repo_zh = {}
        mergeTranslationKeys(ref_en, repo_en)
        mergeTranslationKeys(ref_zh, repo_zh)
        mergeTranslationKeys(repo_en, repo_zh)
        writeLangJson(repo_en, fullPath / "en_us.json")
        writeLangJson(repo_zh, fullPath / "zh_cn.json")
        return LangDictTuple(repo_en, repo_zh)
    pass


def findLang(modname, modid, filename) -> LangDict:
    """
    从最新版本找到存在的语言文件并加载
    :param filename:
    :param modname: curseforge modname
    :param modid:
    :return:
    """
    for v in reversed(MaintainVersion):
        fullpath = repoDirRoot / "projects" / v.value / "assets" / modname / modid / "lang" / filename
        ld = readLangJson(fullpath)
        if ld != {}:
            return ld
    return {}


def readLangJson(filepath: str or Path) -> LangDict:
    filepath = Path(filepath)
    if filepath.exists() and filepath.suffix == ".json":
        return loads(filepath.read_text(encoding='utf-8'))
    else:
        return {}


def extractLang(jarfilePath: str or Path) -> (str, LangDictTuple):
    """
    从指定的文件名（with path）提取语言文件的翻译键和modid
    :param jarfilePath: can be str or Path from pathlib
    :return:
    """
    if isinstance(jarfilePath, str) or isinstance(jarfilePath, Path):
        jarfilePath = Path(jarfilePath)
        if not zipfile.is_zipfile(jarfilePath):
            raise FileNotFoundError(f"{jarfilePath.name}不存在或不是一个合法的zip格式文件。")
        jarfile = zipfile.ZipFile(jarfilePath)
    else:
        raise TypeError
    zflist = jarfile.filelist
    print(jarfile.filename)
    en, zh = LangDictTuple({}, {})
    for file in zflist:
        if file.filename.split("/")[-1] == "en_us.json":
            en = loads(jarfile.read(file))
            if "_comment" in en:
                del en["_comment"]
        if file.filename.split("/")[-1] == "zh_cn.json":
            zh = loads(jarfile.read(file))
            if "_comment" in zh:
                del zh["_comment"]
    if en or zh:
        modid = ""
        jarPath = zipfile.Path(jarfile)
        if jarPath.joinpath("fabric.mod.json").exists():
            modid = loads(jarPath.joinpath("fabric.mod.json").read_text())["id"]
        elif jarPath.joinpath("META-INF").joinpath("mods.toml").exists():
            temptext = jarPath.joinpath("META-INF").joinpath("mods.toml").read_text()
            modid = re.search(r"(modId *= *\")(.*)(\")", temptext).group(2)
        if modid == "":
            raise ValueError(f"在{jarPath.name}获取 modid 失败")
        return modid, LangDictTuple(en, zh)
    else:
        return "", LangDictTuple({}, {})


def writeLangJson(ld: LangDict, filepath: str or Path):
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    # filepath.touch()
    with open(filepath, 'w', encoding="utf-8") as f:
        dump(ld, f, ensure_ascii=False, indent=2, sort_keys=False)


class PackerPolicyTemplate:
    def __init__(self, policy: Policy, source: str or Path, patch: str or Path):
        # TODO 自动生成packer-policy.json 的模板类
        pass

# TODO
# def reportSetup():
#     # 生成报告
#     rep = PrettyTable()
#     # report.add_autoindex("序号")
#     rep.add_column(fieldname="modid", column=[])
#     # report.add_column(fieldname="未翻译键数",column=for i in key_cnt.sorted().values()[i]key_cnt.sorted().values())
#     # report.add_column(fieldname="中文文件键数",column=enuss.sorted())
#     rep.add_column(fieldname="未翻译键数", column=[])
#     rep.add_column(fieldname="中文文件键数", column=[])
#     rep.add_column(fieldname="英文文件键数", column=[])
#     rep.add_column(fieldname="已翻译比例", column=[])
#     return rep

#
# report = reportSetup()
# report.add_rows(list(key_cnts.values()))
# report.add_autoindex("序号")
# report.set_style(MARKDOWN)
# text = report.get_string()
# with open("report.md", 'w', encoding="utf-8") as f:
#     if f.writable:
#         f.write(text)
#         print("已生成翻译进度报告于report.md")
#     else:
#         print("生成报告失败，请检查report.md是否被其它程序占用．")
# print('任务完成，共有未翻译的键名{}个，模组{}个。'.format(key_all_cnt, mod_cnt))