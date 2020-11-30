import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypi_test-grese", # Replace with your own username
    version="0.0.1",
    author="Grese",
    author_email="johngrese@me.com",
    description="PyPI Test Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grese/pypi_test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

