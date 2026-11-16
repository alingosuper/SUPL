from setuptools import setup, find_packages

setup(
    name="supl-lang",
    version="2.0.0",                      # urdu/__init__.py کے مطابق
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
    extras_require={
        "web": ["flask", "fastapi", "uvicorn[standard]", "requests"],
        "ml": ["numpy", "pandas", "scikit-learn"],
        "db": ["mysql-connector-python", "psycopg2-binary", "pymongo"],
        "full": [
            "flask", "fastapi", "uvicorn[standard]", "requests",
            "numpy", "pandas", "scikit-learn",
            "mysql-connector-python", "psycopg2-binary", "pymongo",
        ],
        "dev": ["pytest", "mkdocs", "mkdocs-material"],
    },
    entry_points={
        "console_scripts": [
            # ─── پروگرام چلانے کے لیے ───
            "saraiki=supl._root_cli:main",
            "supl=supl._root_cli:main",
            "urdu=supl._root_cli:main",

            # ─── پیکیج مینیجر (pip کا سرائیکی نام) ───
            "سرائیکی=supl.saraiki_pip:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",              # __future__ annotations + list[str] کے لیے لازم
)
