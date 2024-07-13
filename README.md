# script-house

该仓库是一个方便我日常使用的 python 模块 —— [`script-house`](https://pypi.org/project/script-house/) 。预计我的大部分
python 项目都会依赖这个基础模块。

`script-house` 主要包括两个包：

- `utils`：用于开发的工具类。
- `ops`：用于日常使用的工具类（脚本）。

# 依赖

本模块的依赖是以文件为基准的。如果用户想要使用某个文件内的函数，只需安装对应的依赖即可（没有则会报错）。这里列出所有文件的依赖，用户可以提前安装，避免代码报错：

| 文件                       | 安装依赖的命令                                                   |
|--------------------------|-----------------------------------------------------------|
| `.utils.JsonUtils`       | `pip install pydantic==2.5.3 bson==0.5.10 pymongo==4.6.1` |


# 使用

安装：

```shell
pip install script-house
```

保持最新版本：

```shell
pip install --upgrade script-house
```

# 开发者用

> （提醒我自己如何用）

## 如何构建

```shell
python.exe .\setup.py bdist_wheel sdist
```

## 如何上传到 pypi

1. 拿 `api_token`

2. 创建 .pypirc 文件，放到 `$HOME` 目录（Windows 的话，放到 `C:\Users\用户名` 下）
   .pypirc 格式：

    ```ini
    [pypi]
      username = __token__
      password = <api_token>
    ```

3. `pip install wine`

4. 上传：`twine upload dist/script_house-x.y.z-py3-none-any.whl`

