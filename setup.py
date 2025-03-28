import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chest-Cancer-Classification-Project"
AUTHOR_USER_NAME = "deepak"
SRC_REPO = "chestcancer"
AUTHOR_EMAIL = "deepakreddybora@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/deepakreddybora99/Chest_Cancer_Classification",
    project_urls={
        "Bug Tracker": f"https://github.com/deepakreddybora99/Chest_Cancer_Classification",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)