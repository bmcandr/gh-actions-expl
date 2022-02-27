from setuptools import setup, find_packages
from glob import glob
from os.path import basename, splitext

setup(
    name="pysample",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
)
