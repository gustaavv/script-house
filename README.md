# script-house


This repo is a handy Python module for my daily use — [`script-house`](https://pypi.org/project/script-house/). Most of my Python projects are expected to depend on this fundamental module.

`script-house` mainly includes two packages:

- `utils`: Tools for development.
- `ops`: Tools(scripts) for daily use.

# Dependencies

Dependencies for this module are file-based. If users want to use functions from a specific file, they only need to install the corresponding dependencies (an exception will be thrown if not installed). Here is a list of dependencies for all files, which users can install in advance to avoid exceptions:

| File                     | Command to Install Dependencies                           |
|--------------------------|-----------------------------------------------------------|
| `.utils.JsonUtils`       | `pip install pydantic==2.5.3 bson==0.5.10 pymongo==4.6.1` |
| `.ops.MarkdownOperation` | `pip install requests markdown beautifulsoup4`            |

# Usage

Installation:

```shell
pip install script-house
```

Keep updated to the latest version:

```shell
pip install --upgrade script-house
```

# For Developers

> (Reminder for myself on how to use)

## How to Build

```shell
python.exe .\setup.py bdist_wheel sdist
```

## How to Upload to PyPI

1. Get `api_token`

2. Create a .pypirc file and place it in the `$HOME` directory (for Windows, place it in `C:\Users\Username`)
   .pypirc format:

    ```ini
    [pypi]
      username = __token__
      password = <api_token>
    ```

3. `pip install wine`

4. Upload: `twine upload dist/script_house-x.y.z-py3-none-any.whl`

