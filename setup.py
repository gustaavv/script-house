from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()
    requirements = [r.strip() for r in requirements]

setup(
    name="script_house",
    version="1.0.2",
    description="a python script house containing handy functions for daily use",
    packages=find_packages(),
    url="https://github.com/gustaavv/script-house",
    author="Gustav",
    author_email="gustaavv.git@yahoo.com",
    # python_requires=">=3.11",
    install_requires=requirements,
    classifiers=[
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
