from setuptools import setup, find_packages

setup(
    name="tradingview-data-fetcher",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tvdatafeed",
        "pandas",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "tvdatafetcher=src.cli:main",
        ],
    },
    author="Neeraj Kumar",
    author_email="neerajrajputa786@gmail.com",
    description="A tool to extract historical market data from TradingView",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/drunktrader/tradingview-data-fetcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
        ]
    },
)