from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="simulator",
    description="A basic simulator for soft-body dynamics.",
    license="MIT",
    packages=find_packages(include="simulator"),
    install_requires=requirements,
)
