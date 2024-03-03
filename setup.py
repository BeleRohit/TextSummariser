import setuptools
with open("README.md", "r",encoding = 'utf-8') as fh:
    long_description = fh.read()



__version__="0.0.0"

REPO_NAME='TextSummariser'
AUTHOR_USER_NAME="BeleRohit",
AUTHOR_EMAIL="rohitnbele@gmail.com",
SRC_REPO="https://github.com/BeleRohit/TextSummariser",


setuptools.setup(
    name=REPO_NAME,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small package for text summarization",
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },


)

