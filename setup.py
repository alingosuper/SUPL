from setuptools import setup, find_packages

setup(
    name="sarakluk",
    version="1.0.0",
    description="SarakLuk - Multilingual Programming Language Engine for Urdu, Punjabi, and Saraiki",
    author="Alango Developers",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # اگر کوئی بیرونی ڈیپینڈنسی ہو تو یہاں لکھی جاتی ہے
    ],
    entry_points={
        "console_scripts": [
            "saraiki=cli:main",
            "supl=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
