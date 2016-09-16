from setuptools import setup

setup(
    name="poc-pip_install",
    url="https://github.com/Junior743/poc-pip_install",
    author="Junior Sousa",
    author_email="carlos.junior@tevec.com.br",
    install_requires=[
        "numpy",
    ],
    dependency_links = ['https://github.com/TEVEC/tevec-corporativo/master#egg=corporativo'],
)
