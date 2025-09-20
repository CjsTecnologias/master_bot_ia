from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

# List of Cython files to compile
cython_extensions = [
    Extension(
        name="qtradex.indicators.utilities",
        sources=["qtradex/indicators/utilities.pyx"],
    ),
    Extension(
        name="qtradex.indicators.qi",
        sources=["qtradex/indicators/qi.py"],
    ),
]

# Compile Cython extensions (skip if build tools not available)
try:
    ext_modules = cythonize(cython_extensions)
except Exception:
    ext_modules = []

setup(
    name="QTradeX",
    version="1.2.0",
    setup_requires=["Cython>=0.29.21", "setuptools>=80"],
    description="AI-powered SDK featuring algorithmic trading, backtesting, deployment on 100+ exchanges, and multiple optimization engines.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.12.9",
    classifiers=[            
        "Programming Language :: Python :: 3.12.9",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "ccxt>=4.0.0",
        "jsonpickle>=3.0.0",
        "setuptools>=64",
        "cachetools>=5.0.0",
        "yfinance>=0.2.0",
        "pandas-ta>=0.4.67b0",
        "finance-datareader>=0.9.0",
        "numpy>=2.2.6",
        "matplotlib>=3.5.0",
        "scipy>=1.7.0",
        "ttkbootstrap>=1.10.0",        
    ],
    entry_points={
        "console_scripts": [
            "qtradex-tune-manager=qtradex.core.tune_manager:main",
        ],
    },
    ext_modules=[],
    url="https://github.com/CjsTecnologias/master_bot_ia",
    project_urls={
        "Homepage": "https://github.com/CjsTecnologias/master_bot_ia",
        "Issues": "https://github.com/CjsTecnologias/master_bot_ia/issues",
    },
)