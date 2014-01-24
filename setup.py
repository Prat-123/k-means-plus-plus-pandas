from setuptools import setup
import k_means_plus_plus as kmpp

requirements = []

with open("requirements.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            requirements.append(line)

setup(
    name="k-means-plus-plus",
    version=kmpp.__version__,
    author="Jack Maney",
    author_email="jackmaney@gmail.com",
    description="K-Means++ Clustering for Pandas DataFrames",
    long_description=open("README.md").read(),
    license="MIT",
    url="https://github.com/jackmaney/k-means-plus-plus-pandas",
    download_url="https://github.com/jackmaney/k-means-plus-plus-pandas/archive/v" +
        kmpp.__version__ + ".tar.gz",
    packages=["clustering"],
    install_requires=requirements
)
