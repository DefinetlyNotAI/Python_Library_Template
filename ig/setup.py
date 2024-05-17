from setuptools import setup, find_packages

setup(
    name="ig",
    version="0.1",
    packages=find_packages(),
    description="A simple Python library for IGCSE Computer Science.",
    author="Shahm Najeeb",
    author_email="Nirt_12023@outlook.com",
    url="https://github.com/DefinetlyNotAI/IG_Python_Library",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Students",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="igcse computer science",
    install_requires=[
        # List your project's dependencies here.
    ],
    extras_require={
        # Optional dependencies
    },
    python_requires='>=3.6',
)
