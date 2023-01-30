# CurseForge模组翻译更新辅助

- 专为CFPA汉化仓库使用的翻译更新辅助脚本
- 截止目前（2023-01-30）支持1.18-1.19的CFPA维护版本
- 不太会排版，如果你擅长此项工作欢迎发PR：）

## 功能

- 根据CFPA的支持版本自动下载特定CurseForge模组的对应最新版本

## 用法

### 克隆仓库

- 你可以直接克隆仓库，或是fork该仓库然后再克隆自己的仓库
    - `git clone xxxx/xxxx.git`

### 配置 `config.py`

1. 注册登录[CurseForge API](https://console.curseforge.com/)生成APPKEY，填入到`[config.py](config.py)`的`APPKEY`
2. 将你的本地CFPA fork仓库绝对路径填入`repoDirRoot`

### 安装依赖

1. 进入项目根目录并安装虚拟环境 `pip install virtualenv && virtualenv venv && activate venv`，可选但强烈推荐，不会污染你的本地pip
   package lists
2. 安装依赖`pip install -r requirements.txt`
### 下载资源包
1. 在[此处](http://downloader1.meitangdehulu.com:22943/)下载脚本目前支持对应版本的汉化资源包
2. 在项目根目录下建立`resourcepacks`目录并将资源包移动到此目录下，最好每个支持版本都下一个
### Enjoy It:smile:

## Todo

- 重构代码，拆分方法
- 实现汉化资源包自动下载更新
- 支持1.16版本

## 感谢

- Thanks to [CurseForge API](https://docs.curseforge.com/) and [CFPA](https://cfpa.site/)

## 许可证