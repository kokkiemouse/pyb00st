from setuptools import setup,find_packages
setup(
    name="pyb00st",
    version="0.0.0.1",
    description="lego boost for python",
    install_requires=["pygatt","pexpect"],
    packages=find_packages()
)