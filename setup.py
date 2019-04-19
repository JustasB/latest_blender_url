import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latest_blender_url",
    version="0.1.1",
    author="Justas Birgiolas",
    author_email="justas@asu.edu",
    description="A python package that retrieves the latest Blender download URL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/justasb/latest_blender_url",
    packages=setuptools.find_packages(),
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
