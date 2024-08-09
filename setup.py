import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

about = {}
with io.open(
    os.path.join(here, "tutormailpit", "__about__.py"), "rt", encoding="utf-8"
) as f:
    exec(f.read(), about)

setup(
    name="tutor-contrib-mailpit",
    version=about["__version__"],
    license="AGPLv3",
    author="Abstract-Technology GmbH",
    author_email="support@abstract-technology.de",
    maintainer="Illia Shestakov",
    maintainer_email="i.shestakov@abstract-technology.de",
    description="A Tutor plugin for local email testing",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor>=15.0.0,<19.0.0"],
    entry_points={"tutor.plugin.v1": ["mailpit = tutormailpit.plugin"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
