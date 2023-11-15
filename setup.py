from setuptools import find_packages
import os
from distutils.core import setup

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""
(__version__,) = re.findall(
    '__version__: str = "(.*)"', open("lark/__init__.py").read()
)

setup(
    # Name of the package
    name="jsonofabitch",
    # Packages to include into the distribution
    version=__version__,
    license="MIT",
    # Short description of your library
    description="JSLOB: sloppy json parser. error correcting json parser. standarized low standards",
    # Long description of your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Your name
    author="cmark0v",
    # Your email
    author_email="cmark0v@protonmail.com",
    # Either the link to your github or to your website
    url="https://github.com/cmark0v/jsonofabitch/",
    # Link from which the project can be downloaded
    download_url="",
    # List of keywords
    keywords=[
        "json",
        "parser",
        "linter",
        "autocorrect",
        "formatter",
        "slob",
        "user input",
    ],
    # List of packages to install with this one
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: File Formats :: JSON",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: File Formats",
    ],
    install_requires=[],
    requires=[
        "lark",
    ],
    packages=[
        "jsonofabitch",
    ],
)
