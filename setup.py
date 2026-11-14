from setuptools import setup, find_packages
from pathlib import Path

long_description = Path("README.md").read_text(encoding="utf-8") if Path("README.md").exists() else ""

setup(
    name="saraiki-lang",
    version="1.0.0",
    author="النگو ڈویلپرز (Alango Developers)",
    author_email="support@alangodevelopers.com",
    description="سرائیکی پروگرامنگ لینگویج — SarakLuk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlangoDevelopers/SarakLuk",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "saraiki=urdu.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Natural Language :: Saraiki",
        "Topic :: Software Development :: Compilers",
    ],
    keywords=["saraiki", "programming language", "سرائیکی", "پروگرامنگ", "SarakLuk"],
)
