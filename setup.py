from setuptools import setup

setup(
    name="poc-pip_install",
    url="https://github.com/Junior743/poc-pip_install",
    author="Junior Sousa",
    author_email="carlos.junior@tevec.com.br",
    install_requires=[
        "numpy",
        "poc-travis==1.0.0",
    ],
    dependency_links = ['https://github.com/Junior743/poc-travis/tarball/master#egg=poc-travis-1.0.0'],
)
