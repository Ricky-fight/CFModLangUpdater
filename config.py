from enum import Enum
from pathlib import Path

repoDirRoot = Path(r"D:\code\i18n\Minecraft-Mod-Language-Package")
APPKEY = ""

refDirRoot = Path(r"./cache")


class MaintainVersion(Enum):
    FORGE_118 = "1.18"
    FABRIC_118 = "1.18-fabric"
    FORGE_119 = "1.19"
    # FABRIC_119 = "1.19-fabric"


# curseforge api 相关，不需要动
class SupportLoader:
    FABRIC = "Fabric"
    FORGE = "Forge"


class SupportVersion:
    V1_12 = 628
    V1_16 = 70886
    V1_18 = 73250
    V1_19 = 73407