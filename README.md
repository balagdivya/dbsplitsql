# dbsplitsql

A lightweight Python utility package to split and process large SQL scripts into manageable SQL statements.

## Overview

`dbsplitsql` is a Python package designed to help developers and database engineers split large SQL files into individual executable SQL statements. It is useful for:

* Database migration scripts
* SQL deployment automation
* ETL workflows
* SQL parsing utilities
* Handling large SQL dump files

This package was originally created and published on PyPI in 2019.

---

## Features

* Split large SQL scripts into separate queries
* Lightweight and easy to use
* Supports automation workflows
* Useful for database maintenance and migrations
* Open-source Python utility package

---

## Installation

Install directly from PyPI:

```bash
pip install dbsplitsql
```

---

## Usage


## Project Links

* GitHub Repository: [https://github.com/balagdivya/dbsplitsql](https://github.com/balagdivya/dbsplitsql)
* PyPI Package: [https://pypi.org/project/dbsplitsql/](https://pypi.org/project/dbsplitsql/)

---

## Technologies Used

* Python
* SQL
* PyPI Packaging
* GitHub

---

## Contributing

Contributions are welcome.

### Steps to Contribute

1. Fork the repository

```bash
git clone https://github.com/your-username/dbsplitsql.git
```

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Make your changes

4. Commit changes

```bash
git commit -m "Added new feature"
```

5. Push the branch

```bash
git push origin feature-name
```

6. Create a Pull Request on GitHub

---

## Publishing to PyPI

### Build the package

```bash
python setup.py sdist bdist_wheel
```

### Install Twine

```bash
pip install twine
```

### Upload to PyPI

```bash
twine upload dist/*
```

---

## Future Enhancements

* Better SQL parsing support
* Multi-database compatibility
* Advanced SQL delimiter handling
* CLI support
* Integration with migration pipelines

---

## License

MIT License

---

## Author

Divya Goteti
