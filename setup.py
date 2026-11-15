from setuptools import setup, find_packages

setup(
    name="alingo-saraiki",
    version="1.0.1",                      # urdu/__init__.py کے مطابق
    description="AlinGo Saraiki - Saraiki-first Programming Language for Urdu, Punjabi, and Saraiki",
    long_description=open("README.md", encoding="utf-8").read() if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/alingosuper/SUPL",
    project_urls={
        "Bug Tracker": "https://github.com/alingosuper/SUPL/issues",
        "Documentation": "https://github.com/alingosuper/SUPL/tree/main/docs",
        "Source": "https://github.com/alingosuper/SUPL",
    },
    author="AlinGo Developers",
    packages=find_packages(exclude=["tests*", "examples*", "docs*"]),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "alingo=supl._root_cli:main",
            "saraiki=supl._root_cli:main",
            "supl=supl._root_cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",              # __future__ annotations + list[str] کے لیے لازم
)
