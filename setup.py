from setuptools import setup, find_packages

setup(
    name="alingo-saraiki",
    version="1.0.1",                      # urdu/__init__.py کے مطابق
    description="AlinGo Saraiki - Saraiki-first Programming Language for Urdu, Punjabi, and Saraiki",
    author="AlinGo Developers",
    packages=find_packages(exclude=["tests*", "examples*", "docs*"]),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "alingo=cli:main",
            "saraiki=cli:main",
            "supl=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",              # __future__ annotations + list[str] کے لیے لازم
)
