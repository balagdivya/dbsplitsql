import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Here is the module name.
    name="dbsplitsql",

    # version of the module
    version="0.0.8",

    # Name of Author
    author="Divya Goteti",

    # your Email address
    author_email="balagdivya@gmail.com",

    # Small Description about module
    description="It will split all the table and views of a schema in a file, into its respective files",

    long_description=long_description,

    # Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",

    # Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/balagdivya/dbsplitsql",
    packages=setuptools.find_packages(),
    install_requires=['argparse'],
    entry_points={
        'console_scripts': ['dbsplitsql = dbsplitsql.main:main']
    },
    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
