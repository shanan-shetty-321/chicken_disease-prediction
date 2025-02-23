import setuptools  #
with open("README.md","r",encoding="utf-8") as f: # for the long_description use readme in write mode
#so print everything in readme.md file
    long_description = f.read()
#if we want to publish this as pypi package to publish and hosting it as a local package
#
__version__="0.0.0"


REPO_NAME="chicken_disease-prediction"
AUTHOR_USER_NAME='shanan-shetty-321'
SRC_REPO="srcchickendisease"
AUTHOR_EMAIL="shananshetty@gmail.com"



setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="packages for cnn app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)