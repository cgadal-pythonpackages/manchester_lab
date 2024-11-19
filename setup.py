from setuptools import find_packages, setup

setup(
    name="manchester_lab",
    version="0.1",
    author="Cyril Gadal",
    author_email="cyril.gadal@manchester.ac.uk",
    license="GNU",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3",
    install_requires=["numpy", "matplotlib", "datetime", "scipy"],
)
