import re

from setuptools import setup

with open("cfonts/__version__.py") as fp:
    VERSION = re.findall(r"__version__ *= *['\"](.+?)['\"]", fp.read())[0]

setup(
    name="python-cfonts",
    version=VERSION,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*",
    install_requires=[
        "click",
        "colorama",
        "backports.shutil_get_terminal_size;python_version<'3.4'"
    ],
    packages=["cfonts"],
    package_data={"cfonts": ["fonts/*.json"]}
)
