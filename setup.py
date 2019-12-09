from setuptools import find_packages, setup

setup(
    name="hanuka",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": (
            "hanuka=hanuka.main:main",
        )
    },
)
