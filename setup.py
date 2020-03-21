import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="generic-switcher-DMANHAUS",
  version="0.0.1",
  author="Dave Hausler",
  author_email="dmanhaus@gmail.com",
  description="A package to standardize and layer switching behavior",
  long_description=long_description,
  long_description_content_type="text/markdown",
  # url= <https://github.com/pypa/>,
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.7.3',
)