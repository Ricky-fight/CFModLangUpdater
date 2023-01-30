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
#     result = mod_from_dict(json.loads(json_string))

from datetime import datetime
from typing import Any, List, TypeVar, Callable, Type, cast

import dateutil.parser

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    return x or ""


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Author:
    id: int
    name: str
    url: str

    def __init__(self, id: int, name: str, url: str) -> None:
        self.id = id
        self.name = name
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Author':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        url = from_str(obj.get("url"))
        return Author(id, name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["url"] = from_str(self.url)
        return result


class Category:
    id: int
    game_id: int
    name: str
    slug: str
    url: str
    icon_url: str
    date_modified: datetime
    is_class: bool
    class_id: int
    parent_category_id: int
    display_index: int

    def __init__(self, id: int, game_id: int, name: str, slug: str, url: str, icon_url: str, date_modified: datetime,
                 is_class: bool, class_id: int, parent_category_id: int, display_index: int) -> None:
        self.id = id
        self.game_id = game_id
        self.name = name
        self.slug = slug
        self.url = url
        self.icon_url = icon_url
        self.date_modified = date_modified
        self.is_class = is_class
        self.class_id = class_id
        self.parent_category_id = parent_category_id
        self.display_index = display_index

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        game_id = from_int(obj.get("gameId"))
        name = from_str(obj.get("name"))
        slug = from_str(obj.get("slug"))
        url = from_str(obj.get("url"))
        icon_url = from_str(obj.get("iconUrl"))
        date_modified = from_datetime(obj.get("dateModified"))
        is_class = from_bool(obj.get("isClass"))
        class_id = from_int(obj.get("classId"))
        parent_category_id = from_int(obj.get("parentCategoryId"))
        display_index = None
        return Category(id, game_id, name, slug, url, icon_url, date_modified, is_class, class_id, parent_category_id,
                        display_index)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["gameId"] = from_int(self.game_id)
        result["name"] = from_str(self.name)
        result["slug"] = from_str(self.slug)
        result["url"] = from_str(self.url)
        result["iconUrl"] = from_str(self.icon_url)
        result["dateModified"] = self.date_modified.isoformat()
        result["isClass"] = from_bool(self.is_class)
        result["classId"] = from_int(self.class_id)
        result["parentCategoryId"] = from_int(self.parent_category_id)
        result["displayIndex"] = from_int(self.display_index)
        return result


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


class LatestFile:
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
    def from_dict(obj: Any) -> 'LatestFile':
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
        return LatestFile(id, game_id, mod_id, is_available, display_name, file_name, release_type, file_status, hashes,
                          file_date, file_length, download_count, download_url, game_versions, sortable_game_versions,
                          dependencies, expose_as_alternative, parent_project_file_id, alternate_file_id,
                          is_server_pack, server_pack_file_id, file_fingerprint, modules)

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


class LatestFilesIndex:
    game_version: str
    file_id: int
    filename: str
    release_type: int
    game_version_type_id: int
    mod_loader: int

    def __init__(self, game_version: str, file_id: int, filename: str, release_type: int, game_version_type_id: int,
                 mod_loader: int) -> None:
        self.game_version = game_version
        self.file_id = file_id
        self.filename = filename
        self.release_type = release_type
        self.game_version_type_id = game_version_type_id
        self.mod_loader = mod_loader

    @staticmethod
    def from_dict(obj: Any) -> 'LatestFilesIndex':
        assert isinstance(obj, dict)
        game_version = from_str(obj.get("gameVersion"))
        file_id = from_int(obj.get("fileId"))
        filename = from_str(obj.get("filename"))
        release_type = from_int(obj.get("releaseType"))
        game_version_type_id = from_int(obj.get("gameVersionTypeId"))
        mod_loader = None
        return LatestFilesIndex(game_version, file_id, filename, release_type, game_version_type_id, mod_loader)

    def to_dict(self) -> dict:
        result: dict = {}
        result["gameVersion"] = from_str(self.game_version)
        result["fileId"] = from_int(self.file_id)
        result["filename"] = from_str(self.filename)
        result["releaseType"] = from_int(self.release_type)
        result["gameVersionTypeId"] = from_int(self.game_version_type_id)
        result["modLoader"] = from_int(self.mod_loader)
        return result


class Links:
    website_url: str
    wiki_url: str
    issues_url: str
    source_url: str

    def __init__(self, website_url: str, wiki_url: str, issues_url: str, source_url: str) -> None:
        self.website_url = website_url
        self.wiki_url = wiki_url
        self.issues_url = issues_url
        self.source_url = source_url

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        assert isinstance(obj, dict)
        website_url = from_str(obj.get("websiteUrl"))
        wiki_url = from_str(obj.get("wikiUrl"))
        issues_url = from_str(obj.get("issuesUrl"))
        source_url = from_str(obj.get("sourceUrl"))
        return Links(website_url, wiki_url, issues_url, source_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["websiteUrl"] = from_str(self.website_url)
        result["wikiUrl"] = from_str(self.wiki_url)
        result["issuesUrl"] = from_str(self.issues_url)
        result["sourceUrl"] = from_str(self.source_url)
        return result


class Logo:
    id: int
    mod_id: int
    title: str
    description: str
    thumbnail_url: str
    url: str

    def __init__(self, id: int, mod_id: int, title: str, description: str, thumbnail_url: str, url: str) -> None:
        self.id = id
        self.mod_id = mod_id
        self.title = title
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Logo':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        mod_id = from_int(obj.get("modId"))
        title = from_str(obj.get("title"))
        description = from_str(obj.get("description"))
        thumbnail_url = from_str(obj.get("thumbnailUrl"))
        url = from_str(obj.get("url"))
        return Logo(id, mod_id, title, description, thumbnail_url, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["modId"] = from_int(self.mod_id)
        result["title"] = from_str(self.title)
        result["description"] = from_str(self.description)
        result["thumbnailUrl"] = from_str(self.thumbnail_url)
        result["url"] = from_str(self.url)
        return result


class Mod:
    id: int
    game_id: int
    name: str
    slug: str
    links: Links
    summary: str
    status: int
    download_count: int
    is_featured: bool
    primary_category_id: int
    categories: List[Category]
    class_id: int
    authors: List[Author]
    logo: Logo
    screenshots: List[Logo]
    main_file_id: int
    latest_files: List[LatestFile]
    latest_files_indexes: List[LatestFilesIndex]
    date_created: datetime
    date_modified: datetime
    date_released: datetime
    allow_mod_distribution: bool
    game_popularity_rank: int
    is_available: bool
    thumbs_up_count: int

    def __init__(self, id: int, game_id: int, name: str, slug: str, links: Links, summary: str, status: int,
                 download_count: int, is_featured: bool, primary_category_id: int, categories: List[Category],
                 class_id: int, authors: List[Author], logo: Logo, screenshots: List[Logo], main_file_id: int,
                 latest_files: List[LatestFile], latest_files_indexes: List[LatestFilesIndex], date_created: datetime,
                 date_modified: datetime, date_released: datetime, allow_mod_distribution: bool,
                 game_popularity_rank: int, is_available: bool, thumbs_up_count: int) -> None:
        self.id = id
        self.game_id = game_id
        self.name = name
        self.slug = slug
        self.links = links
        self.summary = summary
        self.status = status
        self.download_count = download_count
        self.is_featured = is_featured
        self.primary_category_id = primary_category_id
        self.categories = categories
        self.class_id = class_id
        self.authors = authors
        self.logo = logo
        self.screenshots = screenshots
        self.main_file_id = main_file_id
        self.latest_files = latest_files
        self.latest_files_indexes = latest_files_indexes
        self.date_created = date_created
        self.date_modified = date_modified
        self.date_released = date_released
        self.allow_mod_distribution = allow_mod_distribution
        self.game_popularity_rank = game_popularity_rank
        self.is_available = is_available
        self.thumbs_up_count = thumbs_up_count

    @staticmethod
    def from_dict(obj: Any) -> 'Mod':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        game_id = from_int(obj.get("gameId"))
        name = from_str(obj.get("name"))
        slug = from_str(obj.get("slug"))
        links = Links.from_dict(obj.get("links"))
        summary = from_str(obj.get("summary"))
        status = from_int(obj.get("status"))
        download_count = from_int(obj.get("downloadCount"))
        is_featured = from_bool(obj.get("isFeatured"))
        primary_category_id = from_int(obj.get("primaryCategoryId"))
        categories = from_list(Category.from_dict, obj.get("categories"))
        class_id = from_int(obj.get("classId"))
        authors = from_list(Author.from_dict, obj.get("authors"))
        logo = Logo.from_dict(obj.get("logo"))
        screenshots = from_list(Logo.from_dict, obj.get("screenshots"))
        main_file_id = from_int(obj.get("mainFileId"))
        latest_files = from_list(LatestFile.from_dict, obj.get("latestFiles"))
        latest_files_indexes = from_list(LatestFilesIndex.from_dict, obj.get("latestFilesIndexes"))
        date_created = from_datetime(obj.get("dateCreated"))
        date_modified = from_datetime(obj.get("dateModified"))
        date_released = from_datetime(obj.get("dateReleased"))
        allow_mod_distribution = from_bool(obj.get("allowModDistribution"))
        game_popularity_rank = from_int(obj.get("gamePopularityRank"))
        is_available = from_bool(obj.get("isAvailable"))
        thumbs_up_count = from_int(obj.get("thumbsUpCount"))
        return Mod(id, game_id, name, slug, links, summary, status, download_count, is_featured, primary_category_id,
                   categories, class_id, authors, logo, screenshots, main_file_id, latest_files, latest_files_indexes,
                   date_created, date_modified, date_released, allow_mod_distribution, game_popularity_rank,
                   is_available, thumbs_up_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["gameId"] = from_int(self.game_id)
        result["name"] = from_str(self.name)
        result["slug"] = from_str(self.slug)
        result["links"] = to_class(Links, self.links)
        result["summary"] = from_str(self.summary)
        result["status"] = from_int(self.status)
        result["downloadCount"] = from_int(self.download_count)
        result["isFeatured"] = from_bool(self.is_featured)
        result["primaryCategoryId"] = from_int(self.primary_category_id)
        result["categories"] = from_list(lambda x: to_class(Category, x), self.categories)
        result["classId"] = from_int(self.class_id)
        result["authors"] = from_list(lambda x: to_class(Author, x), self.authors)
        result["logo"] = to_class(Logo, self.logo)
        result["screenshots"] = from_list(lambda x: to_class(Logo, x), self.screenshots)
        result["mainFileId"] = from_int(self.main_file_id)
        result["latestFiles"] = from_list(lambda x: to_class(LatestFile, x), self.latest_files)
        result["latestFilesIndexes"] = from_list(lambda x: to_class(LatestFilesIndex, x), self.latest_files_indexes)
        result["dateCreated"] = self.date_created.isoformat()
        result["dateModified"] = self.date_modified.isoformat()
        result["dateReleased"] = self.date_released.isoformat()
        result["allowModDistribution"] = from_bool(self.allow_mod_distribution)
        result["gamePopularityRank"] = from_int(self.game_popularity_rank)
        result["isAvailable"] = from_bool(self.is_available)
        result["thumbsUpCount"] = from_int(self.thumbs_up_count)
        return result


def mod_from_dict(s: Any) -> Mod:
    return Mod.from_dict(s)


def mod_to_dict(x: Mod) -> Any:
    return to_class(Mod, x)


if __name__ == '__main__':
    import json

    text = """{
        "id": 243121,
        "gameId": 432,
        "name": "Quark",
        "slug": "quark",
        "links": {
            "websiteUrl": "https://www.curseforge.com/minecraft/mc-mods/quark",
            "wikiUrl": "https://quark.vazkii.net/",
            "issuesUrl": "https://github.com/Vazkii/Quark/issues",
            "sourceUrl": "https://github.com/Vazkii/Quark"
        },
        "summary": "A Quark is a very small thing. This m is a collection of small things that improve the vanilla minecraft experience.",
        "status": 4,
        "downloadCount": 99951807,
        "isFeatured": false,
        "primaryCategoryId": 424,
        "categories": [
            {
                "id": 424,
                "gameId": 432,
                "name": "Cosmetic",
                "slug": "cosmetic",
                "url": "https://www.curseforge.com/minecraft/mc-mods/cosmetic",
                "iconUrl": "https://media.forgecdn.net/avatars/6/39/635351497555976928.png",
                "dateModified": "2014-05-08T17:42:35.597Z",
                "isClass": false,
                "classId": 6,
                "parentCategoryId": 6
            },
            {
                "id": 408,
                "gameId": 432,
                "name": "Ores and Resources",
                "slug": "world-ores-resources",
                "url": "https://www.curseforge.com/minecraft/mc-mods/world-gen/world-ores-resources",
                "iconUrl": "https://media.forgecdn.net/avatars/6/23/635351494012336510.png",
                "dateModified": "2014-05-08T17:36:41.233Z",
                "isClass": false,
                "classId": 6,
                "parentCategoryId": 406
            }
        ],
        "classId": 6,
        "authors": [
            {
                "id": 37709,
                "name": "Vazkii",
                "url": "https://www.curseforge.com/members/3852549-vazkii?username=vazkii"
            }
        ],
        "logo": {
            "id": 588295,
            "modId": 243121,
            "title": "637958240318838626.png",
            "description": "",
            "thumbnailUrl": "https://media.forgecdn.net/avatars/thumbnails/588/295/256/256/637958240318838626.png",
            "url": "https://media.forgecdn.net/avatars/588/295/637958240318838626.png"
        },
        "screenshots": [],
        "mainFileId": 4361476,
        "latestFiles": [
            {
                "id": 2322242,
                "gameId": 432,
                "modId": 243121,
                "isAvailable": true,
                "displayName": "Quark-beta-50.jar",
                "fileName": "Quark-beta-50.jar",
                "releaseType": 2,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "12156a71c431020253abef7de77d392fdc5ee920",
                        "algo": 1
                    },
                    {
                        "value": "a0ab8839065da2ff216d2efffab661a8",
                        "algo": 2
                    }
                ],
                "fileDate": "2016-08-10T22:43:50.783Z",
                "fileLength": 1168869,
                "downloadCount": 25798,
                "downloadUrl": "https://edge.forgecdn.net/files/2322/242/Quark-beta-50.jar",
                "gameVersions": [
                    "1.10.2",
                    "1.10",
                    "1.10.1"
                ],
                "sortableGameVersions": [
                    {
                        "gameVersionName": "1.10.2",
                        "gameVersionPadded": "0000000001.0000000010.0000000002",
                        "gameVersion": "1.10.2",
                        "gameVersionReleaseDate": "2016-06-23T05:00:00Z",
                        "gameVersionTypeId": 572
                    },
                    {
                        "gameVersionName": "1.10",
                        "gameVersionPadded": "0000000001.0000000010",
                        "gameVersion": "1.10",
                        "gameVersionReleaseDate": "2016-06-08T05:00:00Z",
                        "gameVersionTypeId": 572
                    },
                    {
                        "gameVersionName": "1.10.1",
                        "gameVersionPadded": "0000000001.0000000010.0000000001",
                        "gameVersion": "1.10.1",
                        "gameVersionReleaseDate": "2016-06-22T05:00:00Z",
                        "gameVersionTypeId": 572
                    }
                ],
                "dependencies": [],
                "alternateFileId": 0,
                "isServerPack": false,
                "fileFingerprint": 1414734886,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 1635035127
                    },
                    {
                        "name": "vazkii",
                        "fingerprint": 1363254361
                    },
                    {
                        "name": "mcmod.info",
                        "fingerprint": 993108626
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 368012656
                    },
                    {
                        "name": "assets",
                        "fingerprint": 386259003
                    }
                ]
            },
            {
                "id": 3708587,
                "gameId": 432,
                "modId": 243121,
                "isAvailable": true,
                "displayName": "Quark-3.2-346.jar",
                "fileName": "Quark-3.2-346.jar",
                "releaseType": 1,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "e31ea1e97deb1ed4bf43fa56727bb7fdfb7274bb",
                        "algo": 1
                    },
                    {
                        "value": "531b3cac46f54551293d2b954a50ea35",
                        "algo": 2
                    }
                ],
                "fileDate": "2022-03-22T20:36:50.127Z",
                "fileLength": 13547205,
                "downloadCount": 0,
                "downloadUrl": "https://edge.forgecdn.net/files/3708/587/Quark-3.2-346.jar",
                "gameVersions": [
                    "1.18.2"
                ],
                "sortableGameVersions": [
                    {
                        "gameVersionName": "1.18.2",
                        "gameVersionPadded": "0000000001.0000000018.0000000002",
                        "gameVersion": "1.18.2",
                        "gameVersionReleaseDate": "2022-02-28T14:23:37.723Z",
                        "gameVersionTypeId": 73250
                    }
                ],
                "dependencies": [
                    {
                        "modId": 250363,
                        "relationType": 3
                    },
                    {
                        "modId": 238222,
                        "relationType": 2
                    },
                    {
                        "modId": 563928,
                        "relationType": 2
                    },
                    {
                        "modId": 407174,
                        "relationType": 2
                    }
                ],
                "alternateFileId": 0,
                "isServerPack": false,
                "fileFingerprint": 3688250912,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 3267610751
                    },
                    {
                        "name": "vazkii",
                        "fingerprint": 817925956
                    },
                    {
                        "name": "proxypack.mcmeta",
                        "fingerprint": 2303534909
                    },
                    {
                        "name": "proxypack.png",
                        "fingerprint": 3491929732
                    },
                    {
                        "name": "data",
                        "fingerprint": 3515308692
                    },
                    {
                        "name": "assets",
                        "fingerprint": 1376131660
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 2899891612
                    },
                    {
                        "name": "quark.mixins.json",
                        "fingerprint": 3675716416
                    },
                    {
                        "name": "quark.mixins.refmap.json",
                        "fingerprint": 3939986502
                    }
                ]
            },
            {
                "id": 3873471,
                "gameId": 432,
                "modId": 243121,
                "isAvailable": true,
                "displayName": "Quark-3.3-beta-367.jar",
                "fileName": "Quark-3.3-beta-367.jar",
                "releaseType": 2,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "5c70fb07e3cd88540f5ea5371d78f0e1fe320356",
                        "algo": 1
                    },
                    {
                        "value": "85ccf5b2dbd5672fec8fcc57ba4d4b67",
                        "algo": 2
                    }
                ],
                "fileDate": "2022-07-13T11:14:22.16Z",
                "fileLength": 13668741,
                "downloadCount": 0,
                "downloadUrl": "https://edge.forgecdn.net/files/3873/471/Quark-3.3-beta-367.jar",
                "gameVersions": [
                    "Forge",
                    "1.19"
                ],
                "sortableGameVersions": [
                    {
                        "gameVersionName": "Forge",
                        "gameVersionPadded": "0",
                        "gameVersion": "",
                        "gameVersionReleaseDate": "2019-08-01T00:00:00Z",
                        "gameVersionTypeId": 68441
                    },
                    {
                        "gameVersionName": "1.19",
                        "gameVersionPadded": "0000000001.0000000019",
                        "gameVersion": "1.19",
                        "gameVersionReleaseDate": "2022-06-07T15:38:07.377Z",
                        "gameVersionTypeId": 73407
                    }
                ],
                "dependencies": [
                    {
                        "modId": 407174,
                        "relationType": 2
                    },
                    {
                        "modId": 563928,
                        "relationType": 2
                    },
                    {
                        "modId": 238222,
                        "relationType": 2
                    },
                    {
                        "modId": 250363,
                        "relationType": 3
                    }
                ],
                "alternateFileId": 0,
                "isServerPack": false,
                "fileFingerprint": 2004797322,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 858314860
                    },
                    {
                        "name": "vazkii",
                        "fingerprint": 1683016595
                    },
                    {
                        "name": "assets",
                        "fingerprint": 906943322
                    },
                    {
                        "name": "data",
                        "fingerprint": 3593997835
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 2899891612
                    },
                    {
                        "name": "proxypack.mcmeta",
                        "fingerprint": 2303534909
                    },
                    {
                        "name": "proxypack.png",
                        "fingerprint": 3491929732
                    },
                    {
                        "name": "quark.mixins.json",
                        "fingerprint": 2449618397
                    },
                    {
                        "name": "quark.mixins.refmap.json",
                        "fingerprint": 943535388
                    }
                ]
            },
            {
                "id": 4361476,
                "gameId": 432,
                "modId": 243121,
                "isAvailable": true,
                "displayName": "Quark-3.4-388.jar",
                "fileName": "Quark-3.4-388.jar",
                "releaseType": 1,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "0656503285248070cb8b6448c18e61463ad6ef2e",
                        "algo": 1
                    },
                    {
                        "value": "f6836f9f9f035b4c432503ba1e42a9a0",
                        "algo": 2
                    }
                ],
                "fileDate": "2023-01-23T20:50:24.627Z",
                "fileLength": 14302809,
                "downloadCount": 0,
                "downloadUrl": "https://edge.forgecdn.net/files/4361/476/Quark-3.4-388.jar",
                "gameVersions": [
                    "Client",
                    "1.19.2",
                    "Forge",
                    "Server"
                ],
                "sortableGameVersions": [
                    {
                        "gameVersionName": "Client",
                        "gameVersionPadded": "0",
                        "gameVersion": "",
                        "gameVersionReleaseDate": "2022-12-08T00:00:00Z",
                        "gameVersionTypeId": 75208
                    },
                    {
                        "gameVersionName": "1.19.2",
                        "gameVersionPadded": "0000000001.0000000019.0000000002",
                        "gameVersion": "1.19.2",
                        "gameVersionReleaseDate": "2022-08-05T14:12:22.413Z",
                        "gameVersionTypeId": 73407
                    },
                    {
                        "gameVersionName": "Forge",
                        "gameVersionPadded": "0",
                        "gameVersion": "",
                        "gameVersionReleaseDate": "2019-08-01T00:00:00Z",
                        "gameVersionTypeId": 68441
                    },
                    {
                        "gameVersionName": "Server",
                        "gameVersionPadded": "0",
                        "gameVersion": "",
                        "gameVersionReleaseDate": "2022-12-08T00:00:00Z",
                        "gameVersionTypeId": 75208
                    }
                ],
                "dependencies": [
                    {
                        "modId": 563928,
                        "relationType": 2
                    },
                    {
                        "modId": 238222,
                        "relationType": 2
                    },
                    {
                        "modId": 250363,
                        "relationType": 3
                    },
                    {
                        "modId": 407174,
                        "relationType": 2
                    }
                ],
                "alternateFileId": 0,
                "isServerPack": false,
                "fileFingerprint": 2652551693,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 3643882767
                    },
                    {
                        "name": "vazkii",
                        "fingerprint": 1976906444
                    },
                    {
                        "name": "assets",
                        "fingerprint": 2458847302
                    },
                    {
                        "name": "data",
                        "fingerprint": 1570435440
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 2899891612
                    },
                    {
                        "name": "proxypack.mcmeta",
                        "fingerprint": 2303534909
                    },
                    {
                        "name": "proxypack.png",
                        "fingerprint": 3491929732
                    },
                    {
                        "name": "quark.mixins.json",
                        "fingerprint": 3427536568
                    },
                    {
                        "name": "quark.mixins.refmap.json",
                        "fingerprint": 2580174205
                    }
                ]
            }
        ],
        "latestFilesIndexes": [
            {
                "gameVersion": "1.19.2",
                "fileId": 4361476,
                "filename": "Quark-3.4-388.jar",
                "releaseType": 1,
                "gameVersionTypeId": 73407,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19",
                "fileId": 3919164,
                "filename": "Quark-3.3-368.jar",
                "releaseType": 1,
                "gameVersionTypeId": 73407,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19",
                "fileId": 3873471,
                "filename": "Quark-3.3-beta-367.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73407,
                "modLoader": 1
            },
            {
                "gameVersion": "1.18.2",
                "fileId": 3840125,
                "filename": "Quark-3.2-358.jar",
                "releaseType": 1,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.18.2",
                "fileId": 3708587,
                "filename": "Quark-3.2-346.jar",
                "releaseType": 1,
                "gameVersionTypeId": 73250,
                "modLoader": null
            },
            {
                "gameVersion": "1.18.1",
                "fileId": 3662309,
                "filename": "Quark-3.1-340.jar",
                "releaseType": 1,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.16.5",
                "fileId": 3642325,
                "filename": "Quark-r2.4-322.jar",
                "releaseType": 1,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.18",
                "fileId": 3578106,
                "filename": "Quark-3.0-334.jar",
                "releaseType": 1,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.16.5",
                "fileId": 3393195,
                "filename": "Quark-r2.4-315.jar",
                "releaseType": 1,
                "gameVersionTypeId": 70886,
                "modLoader": null
            },
            {
                "gameVersion": "1.16.4",
                "fileId": 3208541,
                "filename": "Quark-r2.4-305.jar",
                "releaseType": 1,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.16.3",
                "fileId": 3146131,
                "filename": "Quark-r2.4-283.jar",
                "releaseType": 1,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.16.1",
                "fileId": 3088712,
                "filename": "Quark-r2.3-266.jar",
                "releaseType": 1,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.15.2",
                "fileId": 2980651,
                "filename": "Quark-r2.1-245.jar",
                "releaseType": 1,
                "gameVersionTypeId": 68722,
                "modLoader": null
            },
            {
                "gameVersion": "1.15.2",
                "fileId": 2976581,
                "filename": "Quark-r2.1-244.jar",
                "releaseType": 1,
                "gameVersionTypeId": 68722,
                "modLoader": 1
            },
            {
                "gameVersion": "1.12.2",
                "fileId": 2924091,
                "filename": "Quark-r1.6-179.jar",
                "releaseType": 1,
                "gameVersionTypeId": 628,
                "modLoader": 1
            },
            {
                "gameVersion": "1.14.4",
                "fileId": 2889792,
                "filename": "Quark-r2.0-212.jar",
                "releaseType": 1,
                "gameVersionTypeId": 64806,
                "modLoader": 1
            },
            {
                "gameVersion": "1.12.2",
                "fileId": 2889332,
                "filename": "Quark-r1.6-178.jar",
                "releaseType": 1,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.12.1",
                "fileId": 2517238,
                "filename": "Quark-r1.4-121.jar",
                "releaseType": 1,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.11.2",
                "fileId": 2458404,
                "filename": "Quark-r1.2-93b.jar",
                "releaseType": 1,
                "gameVersionTypeId": 599,
                "modLoader": null
            },
            {
                "gameVersion": "1.12",
                "fileId": 2457771,
                "filename": "Quark-r1.2-104.jar",
                "releaseType": 1,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.10.2",
                "fileId": 2363413,
                "filename": "Quark-r1.1-70.jar",
                "releaseType": 1,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.10",
                "fileId": 2324059,
                "filename": "Quark-r1.0-52.jar",
                "releaseType": 1,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.10.1",
                "fileId": 2324059,
                "filename": "Quark-r1.0-52.jar",
                "releaseType": 1,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.10.2",
                "fileId": 2322242,
                "filename": "Quark-beta-50.jar",
                "releaseType": 2,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.10",
                "fileId": 2322242,
                "filename": "Quark-beta-50.jar",
                "releaseType": 2,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.10.1",
                "fileId": 2322242,
                "filename": "Quark-beta-50.jar",
                "releaseType": 2,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.9.4",
                "fileId": 2309807,
                "filename": "Quark-beta-29.jar",
                "releaseType": 2,
                "gameVersionTypeId": 552,
                "modLoader": null
            },
            {
                "gameVersion": "1.9",
                "fileId": 2294963,
                "filename": "Quark-beta-18.jar",
                "releaseType": 2,
                "gameVersionTypeId": 552,
                "modLoader": null
            }
        ],
        "dateCreated": "2016-03-21T02:13:13.787Z",
        "dateModified": "2023-01-23T21:00:24.927Z",
        "dateReleased": "2023-01-23T20:50:24.627Z",
        "allowModDistribution": true,
        "gamePopularityRank": 15,
        "isAvailable": true,
        "thumbsUpCount": 0
    }"""
    text2 = """{
        "id": 238222,
        "gameId": 432,
        "name": "Just Enough Items (JEI)",
        "slug": "jei",
        "links": {
            "websiteUrl": "https://www.curseforge.com/minecraft/mc-mods/jei",
            "wikiUrl": "",
            "issuesUrl": "https://github.com/mezz/JustEnoughItems/issues?q=is%3Aissue",
            "sourceUrl": "https://github.com/mezz/JustEnoughItems"
        },
        "summary": "View Items and Recipes",
        "status": 4,
        "downloadCount": 209852393,
        "isFeatured": false,
        "primaryCategoryId": 423,
        "categories": [
            {
                "id": 423,
                "gameId": 432,
                "name": "Map and Information",
                "slug": "map-information",
                "url": "https://www.curseforge.com/minecraft/mc-mods/map-information",
                "iconUrl": "https://media.forgecdn.net/avatars/6/38/635351497437388438.png",
                "dateModified": "2014-05-08T17:42:23.74Z",
                "isClass": false,
                "classId": 6,
                "parentCategoryId": 6
            },
            {
                "id": 421,
                "gameId": 432,
                "name": "API and Library",
                "slug": "library-api",
                "url": "https://www.curseforge.com/minecraft/mc-mods/library-api",
                "iconUrl": "https://media.forgecdn.net/avatars/6/36/635351496947765531.png",
                "dateModified": "2014-05-23T03:21:44.06Z",
                "isClass": false,
                "classId": 6,
                "parentCategoryId": 6
            }
        ],
        "classId": 6,
        "authors": [
            {
                "id": 32358,
                "name": "mezz",
                "url": "https://www.curseforge.com/members/17072262-mezz?username=mezz"
            }
        ],
        "logo": {
            "id": 29069,
            "modId": 238222,
            "title": "635838945588716414.jpeg",
            "description": "",
            "thumbnailUrl": "https://media.forgecdn.net/avatars/thumbnails/29/69/256/256/635838945588716414.jpeg",
            "url": "https://media.forgecdn.net/avatars/29/69/635838945588716414.jpeg"
        },
        "screenshots": [
            {
                "id": 31417,
                "modId": 238222,
                "title": "Recipe Completion",
                "description": "",
                "thumbnailUrl": "https://media.forgecdn.net/attachments/thumbnails/31/417/310/172/thzzdin.png",
                "url": "https://media.forgecdn.net/attachments/31/417/thzzdin.png"
            },
            {
                "id": 31419,
                "modId": 238222,
                "title": "Potions",
                "description": "",
                "thumbnailUrl": "https://media.forgecdn.net/attachments/thumbnails/31/419/310/172/t7f7jh6.png",
                "url": "https://media.forgecdn.net/attachments/31/419/t7f7jh6.png"
            },
            {
                "id": 31420,
                "modId": 238222,
                "title": "Itemlist Edit Mode",
                "description": "",
                "thumbnailUrl": "https://media.forgecdn.net/attachments/thumbnails/31/420/310/172/tgafkma.png",
                "url": "https://media.forgecdn.net/attachments/31/420/tgafkma.png"
            },
            {
                "id": 31418,
                "modId": 238222,
                "title": "Big Screen Support",
                "description": "",
                "thumbnailUrl": "https://media.forgecdn.net/attachments/thumbnails/31/418/310/172/9lngh5f.png",
                "url": "https://media.forgecdn.net/attachments/31/418/9lngh5f.png"
            }
        ],
        "mainFileId": 4060770,
        "latestFiles": [
            {
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
            },
            {
                "id": 3272039,
                "gameId": 432,
                "modId": 238222,
                "isAvailable": true,
                "displayName": "jei-1.13.2-5.0.0.31.jar",
                "fileName": "jei-1.13.2-5.0.0.31.jar",
                "releaseType": 3,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "aa15cdea079db8b91d75e3c68216df80a70545d8",
                        "algo": 1
                    },
                    {
                        "value": "1ee1f4fb4c6e199c02c7d15cbd0d2c8a",
                        "algo": 2
                    }
                ],
                "fileDate": "2021-04-11T03:49:47.687Z",
                "fileLength": 690802,
                "downloadCount": 8644,
                "downloadUrl": "https://edge.forgecdn.net/files/3272/39/jei-1.13.2-5.0.0.31.jar",
                "gameVersions": [
                    "1.13.2"
                ],
                "sortableGameVersions": [
                    {
                        "gameVersionName": "1.13.2",
                        "gameVersionPadded": "0000000001.0000000013.0000000002",
                        "gameVersion": "1.13.2",
                        "gameVersionReleaseDate": "2018-10-22T00:00:00Z",
                        "gameVersionTypeId": 55023
                    }
                ],
                "dependencies": [],
                "alternateFileId": 0,
                "isServerPack": false,
                "fileFingerprint": 2700304635,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 1102858494
                    },
                    {
                        "name": "mezz",
                        "fingerprint": 2811918946
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 3652707984
                    },
                    {
                        "name": "assets",
                        "fingerprint": 88833534
                    }
                ]
            },
            {
                "id": 4060770,
                "gameId": 432,
                "modId": 238222,
                "isAvailable": true,
                "displayName": "jei-1.16.5-7.7.1.153.jar",
                "fileName": "jei-1.16.5-7.7.1.153.jar",
                "releaseType": 1,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "cc0289c9b19a0971ba302d854ae409755a0a28fe",
                        "algo": 1
                    },
                    {
                        "value": "c632d0ad38292ad77d1624aa6c97fdac",
                        "algo": 2
                    }
                ],
                "fileDate": "2022-11-01T00:44:52.007Z",
                "fileLength": 828671,
                "downloadCount": 4,
                "downloadUrl": "https://edge.forgecdn.net/files/4060/770/jei-1.16.5-7.7.1.153.jar",
                "gameVersions": [
                    "1.16.5",
                    "Forge"
                ],
                "sortableGameVersions": [
                    {
                        "gameVersionName": "1.16.5",
                        "gameVersionPadded": "0000000001.0000000016.0000000005",
                        "gameVersion": "1.16.5",
                        "gameVersionReleaseDate": "2021-01-15T14:14:48.91Z",
                        "gameVersionTypeId": 70886
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
                "fileFingerprint": 2250457363,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 3086569392
                    },
                    {
                        "name": "mezz",
                        "fingerprint": 1522917925
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 1645019714
                    },
                    {
                        "name": "assets",
                        "fingerprint": 2175482401
                    }
                ]
            },
            {
                "id": 4087656,
                "gameId": 432,
                "modId": 238222,
                "isAvailable": true,
                "displayName": "jei-1.19.2-fabric-11.4.0.286.jar",
                "fileName": "jei-1.19.2-fabric-11.4.0.286.jar",
                "releaseType": 3,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "f4c77ecd8b897a12c2c8a26350d93a93322a8bcd",
                        "algo": 1
                    },
                    {
                        "value": "cbf23483d172a38b71419100e227f017",
                        "algo": 2
                    }
                ],
                "fileDate": "2022-11-15T02:14:24.907Z",
                "fileLength": 1068892,
                "downloadCount": 0,
                "downloadUrl": "https://edge.forgecdn.net/files/4087/656/jei-1.19.2-fabric-11.4.0.286.jar",
                "gameVersions": [
                    "Fabric",
                    "1.19.2"
                ],
                "sortableGameVersions": [
                    {
                        "gameVersionName": "Fabric",
                        "gameVersionPadded": "0",
                        "gameVersion": "",
                        "gameVersionReleaseDate": "2019-08-01T00:00:00Z",
                        "gameVersionTypeId": 68441
                    },
                    {
                        "gameVersionName": "1.19.2",
                        "gameVersionPadded": "0000000001.0000000019.0000000002",
                        "gameVersion": "1.19.2",
                        "gameVersionReleaseDate": "2022-08-05T14:12:22.413Z",
                        "gameVersionTypeId": 73407
                    }
                ],
                "dependencies": [],
                "alternateFileId": 0,
                "isServerPack": false,
                "fileFingerprint": 1613607509,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 2822576509
                    },
                    {
                        "name": "jei.accesswidener",
                        "fingerprint": 3441454662
                    },
                    {
                        "name": "assets",
                        "fingerprint": 224894697
                    },
                    {
                        "name": "fabric.m.json",
                        "fingerprint": 1230897332
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 1550930300
                    },
                    {
                        "name": "jei.mixins.json",
                        "fingerprint": 623960849
                    },
                    {
                        "name": "jei-icon.png",
                        "fingerprint": 2007185424
                    },
                    {
                        "name": "jei-1.19.2-fabric-refmap.json",
                        "fingerprint": 1412800118
                    },
                    {
                        "name": "mezz",
                        "fingerprint": 2346665333
                    }
                ]
            },
            {
                "id": 4087658,
                "gameId": 432,
                "modId": 238222,
                "isAvailable": true,
                "displayName": "jei-1.19.2-forge-11.4.0.286.jar",
                "fileName": "jei-1.19.2-forge-11.4.0.286.jar",
                "releaseType": 3,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "3bab715ae0f56e1b9a3e1ebfb5e9bb3f677e3711",
                        "algo": 1
                    },
                    {
                        "value": "0d458f02d611eafbf29ae36010d03130",
                        "algo": 2
                    }
                ],
                "fileDate": "2022-11-15T02:14:49.103Z",
                "fileLength": 1046401,
                "downloadCount": 0,
                "downloadUrl": "https://edge.forgecdn.net/files/4087/658/jei-1.19.2-forge-11.4.0.286.jar",
                "gameVersions": [
                    "1.19.2",
                    "Forge"
                ],
                "sortableGameVersions": [
                    {
                        "gameVersionName": "1.19.2",
                        "gameVersionPadded": "0000000001.0000000019.0000000002",
                        "gameVersion": "1.19.2",
                        "gameVersionReleaseDate": "2022-08-05T14:12:22.413Z",
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
                "fileFingerprint": 4135756105,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 2624845708
                    },
                    {
                        "name": "mezz",
                        "fingerprint": 1839722990
                    },
                    {
                        "name": "jei-icon.png",
                        "fingerprint": 2007185424
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 1550930300
                    },
                    {
                        "name": "assets",
                        "fingerprint": 224894697
                    }
                ]
            },
            {
                "id": 4362071,
                "gameId": 432,
                "modId": 238222,
                "isAvailable": true,
                "displayName": "jei-1.19.3-fabric-12.1.1.8.jar",
                "fileName": "jei-1.19.3-fabric-12.1.1.8.jar",
                "releaseType": 2,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "d45736e844aeba68719cf06b2faa61d4f036417f",
                        "algo": 1
                    },
                    {
                        "value": "f643f0a46688756456a6c9ca143d91ae",
                        "algo": 2
                    }
                ],
                "fileDate": "2023-01-24T05:38:13.893Z",
                "fileLength": 1125793,
                "downloadCount": 0,
                "downloadUrl": "https://edge.forgecdn.net/files/4362/71/jei-1.19.3-fabric-12.1.1.8.jar",
                "gameVersions": [
                    "1.19.3",
                    "Fabric"
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
                        "gameVersionName": "Fabric",
                        "gameVersionPadded": "0",
                        "gameVersion": "",
                        "gameVersionReleaseDate": "2019-08-01T00:00:00Z",
                        "gameVersionTypeId": 68441
                    }
                ],
                "dependencies": [],
                "alternateFileId": 0,
                "isServerPack": false,
                "fileFingerprint": 4149479825,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 3011457416
                    },
                    {
                        "name": "jei-icon.png",
                        "fingerprint": 2007185424
                    },
                    {
                        "name": "assets",
                        "fingerprint": 2527914123
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 1550930300
                    },
                    {
                        "name": "fabric.m.json",
                        "fingerprint": 2062009985
                    },
                    {
                        "name": "jei.mixins.json",
                        "fingerprint": 698107283
                    },
                    {
                        "name": "jei.accesswidener",
                        "fingerprint": 2720173993
                    },
                    {
                        "name": "jei-1.19.3-fabric-refmap.json",
                        "fingerprint": 1412800118
                    },
                    {
                        "name": "mezz",
                        "fingerprint": 2965302933
                    }
                ]
            },
            {
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
            },
            {
                "id": 4364085,
                "gameId": 432,
                "modId": 238222,
                "isAvailable": true,
                "displayName": "jei_1.12.2-4.16.1.1000.jar",
                "fileName": "jei_1.12.2-4.16.1.1000.jar",
                "releaseType": 2,
                "fileStatus": 4,
                "hashes": [
                    {
                        "value": "96bfc1280a4baf64c0e274bfa2249e1b4394d699",
                        "algo": 1
                    },
                    {
                        "value": "aa8381fcceae902a7a3b99ec79334241",
                        "algo": 2
                    }
                ],
                "fileDate": "2023-01-25T08:14:00.913Z",
                "fileLength": 653212,
                "downloadCount": 0,
                "downloadUrl": "https://edge.forgecdn.net/files/4364/85/jei_1.12.2-4.16.1.1000.jar",
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
                "fileFingerprint": 4227475690,
                "modules": [
                    {
                        "name": "META-INF",
                        "fingerprint": 515971020
                    },
                    {
                        "name": "mezz",
                        "fingerprint": 4125503091
                    },
                    {
                        "name": "pack.mcmeta",
                        "fingerprint": 1488642189
                    },
                    {
                        "name": "assets",
                        "fingerprint": 9943101
                    },
                    {
                        "name": "mcmod.info",
                        "fingerprint": 486422290
                    }
                ]
            }
        ],
        "latestFilesIndexes": [
            {
                "gameVersion": "1.12.2",
                "fileId": 4364085,
                "filename": "jei_1.12.2-4.16.1.1000.jar",
                "releaseType": 2,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.19.3",
                "fileId": 4362072,
                "filename": "jei-1.19.3-forge-12.1.1.8.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73407,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19.3",
                "fileId": 4362071,
                "filename": "jei-1.19.3-fabric-12.1.1.8.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73407,
                "modLoader": 4
            },
            {
                "gameVersion": "1.19.2",
                "fileId": 4354615,
                "filename": "jei-1.19.2-forge-11.5.2.1007.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73407,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19.2",
                "fileId": 4354614,
                "filename": "jei-1.19.2-fabric-11.5.2.1007.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73407,
                "modLoader": 4
            },
            {
                "gameVersion": "1.18.2",
                "fileId": 4352925,
                "filename": "jei-1.18.2-forge-10.2.1.1002.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.18.2",
                "fileId": 4352924,
                "filename": "jei-1.18.2-fabric-10.2.1.1002.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73250,
                "modLoader": 4
            },
            {
                "gameVersion": "1.17.1",
                "fileId": 4351306,
                "filename": "jei-1.17.1-8.3.1.1002.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73242,
                "modLoader": 1
            },
            {
                "gameVersion": "1.16.5",
                "fileId": 4351303,
                "filename": "jei-1.16.5-7.7.1.1004.jar",
                "releaseType": 2,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19.2",
                "fileId": 4087658,
                "filename": "jei-1.19.2-forge-11.4.0.286.jar",
                "releaseType": 3,
                "gameVersionTypeId": 73407,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19.2",
                "fileId": 4087656,
                "filename": "jei-1.19.2-fabric-11.4.0.286.jar",
                "releaseType": 3,
                "gameVersionTypeId": 73407,
                "modLoader": 4
            },
            {
                "gameVersion": "1.16.5",
                "fileId": 4060770,
                "filename": "jei-1.16.5-7.7.1.153.jar",
                "releaseType": 1,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.18.1",
                "fileId": 4060769,
                "filename": "jei-1.18.1-9.4.1.276.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.18.2",
                "fileId": 4030311,
                "filename": "jei-1.18.2-forge-10.1.5.272.jar",
                "releaseType": 3,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.18.2",
                "fileId": 4030310,
                "filename": "jei-1.18.2-fabric-10.1.5.272.jar",
                "releaseType": 3,
                "gameVersionTypeId": 73250,
                "modLoader": 4
            },
            {
                "gameVersion": "1.18.2",
                "fileId": 3940240,
                "filename": "jei-1.18.2-9.7.1.255.jar",
                "releaseType": 1,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19.1",
                "fileId": 3922508,
                "filename": "jei-1.19.1-forge-11.2.0.244.jar",
                "releaseType": 3,
                "gameVersionTypeId": 73407,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19.1",
                "fileId": 3922506,
                "filename": "jei-1.19.1-fabric-11.2.0.244.jar",
                "releaseType": 3,
                "gameVersionTypeId": 73407,
                "modLoader": 4
            },
            {
                "gameVersion": "1.19",
                "fileId": 3903068,
                "filename": "jei-1.19-forge-11.1.1.239.jar",
                "releaseType": 3,
                "gameVersionTypeId": 73407,
                "modLoader": 1
            },
            {
                "gameVersion": "1.19",
                "fileId": 3903066,
                "filename": "jei-1.19-fabric-11.1.1.239.jar",
                "releaseType": 3,
                "gameVersionTypeId": 73407,
                "modLoader": 4
            },
            {
                "gameVersion": "1.18.1",
                "fileId": 3723162,
                "filename": "jei-1.18.1-9.4.1.172.jar",
                "releaseType": 1,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.18",
                "fileId": 3550020,
                "filename": "jei-1.18-9.0.0.40.jar",
                "releaseType": 2,
                "gameVersionTypeId": 73250,
                "modLoader": 1
            },
            {
                "gameVersion": "1.13.2",
                "fileId": 3272039,
                "filename": "jei-1.13.2-5.0.0.31.jar",
                "releaseType": 3,
                "gameVersionTypeId": 55023,
                "modLoader": null
            },
            {
                "gameVersion": "1.15.2",
                "fileId": 3272032,
                "filename": "jei-1.15.2-6.0.3.16.jar",
                "releaseType": 3,
                "gameVersionTypeId": 68722,
                "modLoader": null
            },
            {
                "gameVersion": "1.16.4",
                "fileId": 3245003,
                "filename": "jei-1.16.4-7.6.1.74.jar",
                "releaseType": 2,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.16.3",
                "fileId": 3104018,
                "filename": "jei-1.16.3-7.6.0.51.jar",
                "releaseType": 2,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.16.3",
                "fileId": 3071356,
                "filename": "jei-1.16.3-7.4.0.40.jar",
                "releaseType": 3,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.16.2",
                "fileId": 3060935,
                "filename": "jei-1.16.2-7.3.2.28.jar",
                "releaseType": 3,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.12.2",
                "fileId": 3040523,
                "filename": "jei_1.12.2-4.16.1.301.jar",
                "releaseType": 1,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.14.4",
                "fileId": 3039707,
                "filename": "jei-1.14.4-6.0.1.30.jar",
                "releaseType": 3,
                "gameVersionTypeId": 64806,
                "modLoader": null
            },
            {
                "gameVersion": "1.16.1",
                "fileId": 3028697,
                "filename": "jei-1.16.1-7.0.1.10.jar",
                "releaseType": 3,
                "gameVersionTypeId": 70886,
                "modLoader": 1
            },
            {
                "gameVersion": "1.15.1",
                "fileId": 2855456,
                "filename": "jei-1.15.1-6.0.0.1.jar",
                "releaseType": 3,
                "gameVersionTypeId": 68722,
                "modLoader": null
            },
            {
                "gameVersion": "1.14.3",
                "fileId": 2738328,
                "filename": "jei-1.14.3-6.0.0.8.jar",
                "releaseType": 3,
                "gameVersionTypeId": 64806,
                "modLoader": null
            },
            {
                "gameVersion": "1.14.2",
                "fileId": 2733474,
                "filename": "jei-1.14.2-6.0.0.3.jar",
                "releaseType": 3,
                "gameVersionTypeId": 64806,
                "modLoader": null
            },
            {
                "gameVersion": "1.10.2",
                "fileId": 2561516,
                "filename": "jei_1.10.2-3.14.8.422.jar",
                "releaseType": 2,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.12",
                "fileId": 2485363,
                "filename": "jei_1.12.2-4.7.11.102.jar",
                "releaseType": 2,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.12.1",
                "fileId": 2485363,
                "filename": "jei_1.12.2-4.7.11.102.jar",
                "releaseType": 2,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.12",
                "fileId": 2478647,
                "filename": "jei_1.12.1-4.7.8.95.jar",
                "releaseType": 1,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.12.1",
                "fileId": 2478647,
                "filename": "jei_1.12.1-4.7.8.95.jar",
                "releaseType": 1,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.11.2",
                "fileId": 2461378,
                "filename": "jei_1.11.2-4.5.1.296.jar",
                "releaseType": 2,
                "gameVersionTypeId": 599,
                "modLoader": null
            },
            {
                "gameVersion": "1.11.2",
                "fileId": 2453428,
                "filename": "jei_1.11.2-4.5.0.294.jar",
                "releaseType": 1,
                "gameVersionTypeId": 599,
                "modLoader": null
            },
            {
                "gameVersion": "1.12",
                "fileId": 2442204,
                "filename": "jei_1.12-4.7.0.68.jar",
                "releaseType": 3,
                "gameVersionTypeId": 628,
                "modLoader": null
            },
            {
                "gameVersion": "1.8.9",
                "fileId": 2431977,
                "filename": "jei_1.8.9-2.28.18.187.jar",
                "releaseType": 1,
                "gameVersionTypeId": 4,
                "modLoader": null
            },
            {
                "gameVersion": "1.10.2",
                "fileId": 2428966,
                "filename": "jei_1.10.2-3.14.7.420.jar",
                "releaseType": 1,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.11",
                "fileId": 2360492,
                "filename": "jei_1.11-4.1.1.208.jar",
                "releaseType": 2,
                "gameVersionTypeId": 599,
                "modLoader": null
            },
            {
                "gameVersion": "1.11",
                "fileId": 2350616,
                "filename": "jei_1.11-4.0.4.199.jar",
                "releaseType": 3,
                "gameVersionTypeId": 599,
                "modLoader": null
            },
            {
                "gameVersion": "1.9.4",
                "fileId": 2313650,
                "filename": "jei_1.9.4-3.6.8.225.jar",
                "releaseType": 1,
                "gameVersionTypeId": 552,
                "modLoader": null
            },
            {
                "gameVersion": "1.10",
                "fileId": 2310912,
                "filename": "jei_1.10-3.7.1.219.jar",
                "releaseType": 1,
                "gameVersionTypeId": 572,
                "modLoader": null
            },
            {
                "gameVersion": "1.9.4",
                "fileId": 2306298,
                "filename": "jei_1.9.4-3.6.2.211.jar",
                "releaseType": 2,
                "gameVersionTypeId": 552,
                "modLoader": null
            },
            {
                "gameVersion": "1.9",
                "fileId": 2305823,
                "filename": "jei_1.9.4-3.4.4.208.jar",
                "releaseType": 2,
                "gameVersionTypeId": 552,
                "modLoader": null
            },
            {
                "gameVersion": "1.9",
                "fileId": 2304545,
                "filename": "jei_1.9.4-3.4.3.207.jar",
                "releaseType": 1,
                "gameVersionTypeId": 552,
                "modLoader": null
            },
            {
                "gameVersion": "1.8.9",
                "fileId": 2292565,
                "filename": "jei_1.8.9-2.28.14.182.jar",
                "releaseType": 2,
                "gameVersionTypeId": 4,
                "modLoader": null
            },
            {
                "gameVersion": "1.8.8",
                "fileId": 2275072,
                "filename": "jei_1.8.9-2.16.2.78.jar",
                "releaseType": 1,
                "gameVersionTypeId": 4,
                "modLoader": null
            },
            {
                "gameVersion": "1.8",
                "fileId": 2273901,
                "filename": "jei_1.8-2.14.0.139.jar",
                "releaseType": 1,
                "gameVersionTypeId": 4,
                "modLoader": null
            },
            {
                "gameVersion": "1.8.8",
                "fileId": 2270928,
                "filename": "jei_1.8.8-2.8.3.39.jar",
                "releaseType": 2,
                "gameVersionTypeId": 4,
                "modLoader": null
            },
            {
                "gameVersion": "1.8",
                "fileId": 2270927,
                "filename": "jei_1.8-1.8.3.96.jar",
                "releaseType": 2,
                "gameVersionTypeId": 4,
                "modLoader": null
            }
        ],
        "dateCreated": "2015-11-23T22:55:58.84Z",
        "dateModified": "2023-01-25T08:18:56.34Z",
        "dateReleased": "2023-01-25T08:14:00.913Z",
        "allowModDistribution": true,
        "gamePopularityRank": 1,
        "isAvailable": true,
        "thumbsUpCount": 1
    }"""
    mod1 = mod_from_dict(json.loads(text))
    mod2 = mod_from_dict(json.loads(text2))