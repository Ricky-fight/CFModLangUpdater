# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome5_from_dict(json.loads(json_string))

from datetime import datetime
from typing import Any, List, TypeVar, Callable, Type, cast

import dateutil.parser

T = TypeVar("T")


def from_int(x: Any) -> int:
    return x or 0

def from_str(x: Any) -> str:
    return x or ""


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    return x or False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Dependency:
    mod_id: int
    relation_type: int

    def __init__(self, mod_id: int, relation_type: int) -> None:
        self.mod_id = mod_id
        self.relation_type = relation_type

    @staticmethod
    def from_dict(obj: Any) -> 'Dependency':
        assert isinstance(obj, dict)
        mod_id = from_int(obj.get("modId"))
        relation_type = from_int(obj.get("relationType"))
        return Dependency(mod_id, relation_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["modId"] = from_int(self.mod_id)
        result["relationType"] = from_int(self.relation_type)
        return result


class Hash:
    value: str
    algo: int

    def __init__(self, value: str, algo: int) -> None:
        self.value = value
        self.algo = algo

    @staticmethod
    def from_dict(obj: Any) -> 'Hash':
        assert isinstance(obj, dict)
        value = from_str(obj.get("value"))
        algo = from_int(obj.get("algo"))
        return Hash(value, algo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_str(self.value)
        result["algo"] = from_int(self.algo)
        return result


class Module:
    name: str
    fingerprint: int

    def __init__(self, name: str, fingerprint: int) -> None:
        self.name = name
        self.fingerprint = fingerprint

    @staticmethod
    def from_dict(obj: Any) -> 'Module':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        fingerprint = from_int(obj.get("fingerprint"))
        return Module(name, fingerprint)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["fingerprint"] = from_int(self.fingerprint)
        return result


class SortableGameVersion:
    game_version_name: str
    game_version_padded: str
    game_version: str
    game_version_release_date: datetime
    game_version_type_id: int

    def __init__(self, game_version_name: str, game_version_padded: str, game_version: str,
                 game_version_release_date: datetime, game_version_type_id: int) -> None:
        self.game_version_name = game_version_name
        self.game_version_padded = game_version_padded
        self.game_version = game_version
        self.game_version_release_date = game_version_release_date
        self.game_version_type_id = game_version_type_id

    @staticmethod
    def from_dict(obj: Any) -> 'SortableGameVersion':
        assert isinstance(obj, dict)
        game_version_name = from_str(obj.get("gameVersionName"))
        game_version_padded = from_str(obj.get("gameVersionPadded"))
        game_version = from_str(obj.get("gameVersion"))
        game_version_release_date = from_datetime(obj.get("gameVersionReleaseDate"))
        game_version_type_id = from_int(obj.get("gameVersionTypeId"))
        return SortableGameVersion(game_version_name, game_version_padded, game_version, game_version_release_date,
                                   game_version_type_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["gameVersionName"] = from_str(self.game_version_name)
        result["gameVersionPadded"] = from_str(self.game_version_padded)
        result["gameVersion"] = from_str(self.game_version)
        result["gameVersionReleaseDate"] = self.game_version_release_date.isoformat()
        result["gameVersionTypeId"] = from_int(self.game_version_type_id)
        return result


class File:
    id: int
    game_id: int
    mod_id: int
    is_available: bool
    display_name: str
    file_name: str
    release_type: int
    file_status: int
    hashes: List[Hash]
    file_date: datetime
    file_length: int
    download_count: int
    download_url: str
    game_versions: List[str]
    sortable_game_versions: List[SortableGameVersion]
    dependencies: List[Dependency]
    expose_as_alternative: bool
    parent_project_file_id: int
    alternate_file_id: int
    is_server_pack: bool
    server_pack_file_id: int
    file_fingerprint: int
    modules: List[Module]

    def __init__(self, id: int, game_id: int, mod_id: int, is_available: bool, display_name: str, file_name: str,
                 release_type: int, file_status: int, hashes: List[Hash], file_date: datetime, file_length: int,
                 download_count: int, download_url: str, game_versions: List[str],
                 sortable_game_versions: List[SortableGameVersion], dependencies: List[Dependency],
                 expose_as_alternative: bool, parent_project_file_id: int, alternate_file_id: int, is_server_pack: bool,
                 server_pack_file_id: int, file_fingerprint: int, modules: List[Module]) -> None:
        self.id = id
        self.game_id = game_id
        self.mod_id = mod_id
        self.is_available = is_available
        self.display_name = display_name
        self.file_name = file_name
        self.release_type = release_type
        self.file_status = file_status
        self.hashes = hashes
        self.file_date = file_date
        self.file_length = file_length
        self.download_count = download_count
        self.download_url = download_url
        self.game_versions = game_versions
        self.sortable_game_versions = sortable_game_versions
        self.dependencies = dependencies
        self.expose_as_alternative = expose_as_alternative
        self.parent_project_file_id = parent_project_file_id
        self.alternate_file_id = alternate_file_id
        self.is_server_pack = is_server_pack
        self.server_pack_file_id = server_pack_file_id
        self.file_fingerprint = file_fingerprint
        self.modules = modules

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        game_id = from_int(obj.get("gameId"))
        mod_id = from_int(obj.get("modId"))
        is_available = from_bool(obj.get("isAvailable"))
        display_name = from_str(obj.get("displayName"))
        file_name = from_str(obj.get("fileName"))
        release_type = from_int(obj.get("releaseType"))
        file_status = from_int(obj.get("fileStatus"))
        hashes = from_list(Hash.from_dict, obj.get("hashes"))
        file_date = from_datetime(obj.get("fileDate"))
        file_length = from_int(obj.get("fileLength"))
        download_count = from_int(obj.get("downloadCount"))
        download_url = from_str(obj.get("downloadUrl"))
        game_versions = from_list(from_str, obj.get("gameVersions"))
        sortable_game_versions = from_list(SortableGameVersion.from_dict, obj.get("sortableGameVersions"))
        dependencies = from_list(Dependency.from_dict, obj.get("dependencies"))
        expose_as_alternative = None
        parent_project_file_id = None
        alternate_file_id = from_int(obj.get("alternateFileId"))
        is_server_pack = from_bool(obj.get("isServerPack"))
        server_pack_file_id = None
        file_fingerprint = from_int(obj.get("fileFingerprint"))
        modules = from_list(Module.from_dict, obj.get("modules"))
        return File(id, game_id, mod_id, is_available, display_name, file_name, release_type, file_status, hashes,
                    file_date, file_length, download_count, download_url, game_versions, sortable_game_versions,
                    dependencies, expose_as_alternative, parent_project_file_id, alternate_file_id, is_server_pack,
                    server_pack_file_id, file_fingerprint, modules)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["gameId"] = from_int(self.game_id)
        result["modId"] = from_int(self.mod_id)
        result["isAvailable"] = from_bool(self.is_available)
        result["displayName"] = from_str(self.display_name)
        result["fileName"] = from_str(self.file_name)
        result["releaseType"] = from_int(self.release_type)
        result["fileStatus"] = from_int(self.file_status)
        result["hashes"] = from_list(lambda x: to_class(Hash, x), self.hashes)
        result["fileDate"] = self.file_date.isoformat()
        result["fileLength"] = from_int(self.file_length)
        result["downloadCount"] = from_int(self.download_count)
        result["downloadUrl"] = from_str(self.download_url)
        result["gameVersions"] = from_list(from_str, self.game_versions)
        result["sortableGameVersions"] = from_list(lambda x: to_class(SortableGameVersion, x),
                                                   self.sortable_game_versions)
        result["dependencies"] = from_list(lambda x: to_class(Dependency, x), self.dependencies)
        result["exposeAsAlternative"] = from_bool(self.expose_as_alternative)
        result["parentProjectFileId"] = from_int(self.parent_project_file_id)
        result["alternateFileId"] = from_int(self.alternate_file_id)
        result["isServerPack"] = from_bool(self.is_server_pack)
        result["serverPackFileId"] = from_int(self.server_pack_file_id)
        result["fileFingerprint"] = from_int(self.file_fingerprint)
        result["modules"] = from_list(lambda x: to_class(Module, x), self.modules)
        return result


def file_from_dict(s: Any) -> File:
    return File.from_dict(s)


def file_to_dict(x: File) -> Any:
    return to_class(File, x)


if __name__ == '__main__':
    import json

    text1 = """{
        "id": 3040523,
        "gameId": 432,
        "modId": 238222,
        "isAvailable": true,
        "displayName": "jei_1.12.2-4.16.1.301.jar",
        "fileName": "jei_1.12.2-4.16.1.301.jar",
        "releaseType": 1,
        "fileStatus": 4,
        "hashes": [
            {
                "value": "3045e8440ea44071d8b83c4e7b3c190348fdc527",
                "algo": 1
            },
            {
                "value": "1dee4be93d666e2228039c551e927b35",
                "algo": 2
            }
        ],
        "fileDate": "2020-08-24T01:01:39.123Z",
        "fileLength": 653211,
        "downloadCount": 11752168,
        "downloadUrl": "https://edge.forgecdn.net/files/3040/523/jei_1.12.2-4.16.1.301.jar",
        "gameVersions": [
            "1.12.2"
        ],
        "sortableGameVersions": [
            {
                "gameVersionName": "1.12.2",
                "gameVersionPadded": "0000000001.0000000012.0000000002",
                "gameVersion": "1.12.2",
                "gameVersionReleaseDate": "2017-09-18T05:00:00Z",
                "gameVersionTypeId": 628
            }
        ],
        "dependencies": [],
        "alternateFileId": 0,
        "isServerPack": false,
        "fileFingerprint": 3089143260,
        "modules": [
            {
                "name": "META-INF",
                "fingerprint": 2236405288
            },
            {
                "name": "mezz",
                "fingerprint": 2222830911
            },
            {
                "name": "pack.mcmeta",
                "fingerprint": 1488642189
            },
            {
                "name": "mcmod.info",
                "fingerprint": 3528499262
            },
            {
                "name": "assets",
                "fingerprint": 9943101
            }
        ]
    }"""
    text2 = """ {
        "id": 4362072,
        "gameId": 432,
        "modId": 238222,
        "isAvailable": true,
        "displayName": "jei-1.19.3-forge-12.1.1.8.jar",
        "fileName": "jei-1.19.3-forge-12.1.1.8.jar",
        "releaseType": 2,
        "fileStatus": 4,
        "hashes": [
            {
                "value": "7d2b094a659f43e93a059f2720c622da903faa30",
                "algo": 1
            },
            {
                "value": "9c60a45f8d7b36be034ce7d06bd056fc",
                "algo": 2
            }
        ],
        "fileDate": "2023-01-24T05:38:32.66Z",
        "fileLength": 1098563,
        "downloadCount": 0,
        "downloadUrl": "https://edge.forgecdn.net/files/4362/72/jei-1.19.3-forge-12.1.1.8.jar",
        "gameVersions": [
            "1.19.3",
            "Forge"
        ],
        "sortableGameVersions": [
            {
                "gameVersionName": "1.19.3",
                "gameVersionPadded": "0000000001.0000000019.0000000003",
                "gameVersion": "1.19.3",
                "gameVersionReleaseDate": "2022-10-19T00:00:00Z",
                "gameVersionTypeId": 73407
            },
            {
                "gameVersionName": "Forge",
                "gameVersionPadded": "0",
                "gameVersion": "",
                "gameVersionReleaseDate": "2019-08-01T00:00:00Z",
                "gameVersionTypeId": 68441
            }
        ],
        "dependencies": [],
        "alternateFileId": 0,
        "isServerPack": false,
        "fileFingerprint": 2642686792,
        "modules": [
            {
                "name": "META-INF",
                "fingerprint": 1001574736
            },
            {
                "name": "mezz",
                "fingerprint": 3082065147
            },
            {
                "name": "pack.mcmeta",
                "fingerprint": 1550930300
            },
            {
                "name": "assets",
                "fingerprint": 2527914123
            },
            {
                "name": "jei-icon.png",
                "fingerprint": 2007185424
            }
        ]
    }"""
    file1 = file_from_dict(json.loads(text1))
    file2 = file_from_dict(json.loads(text2))