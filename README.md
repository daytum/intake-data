# Intake Catalogue for US Oil and Gas Production Data

[![Build Status](https://travis-ci.org/daytum/intake-data.svg?branch=master)](https://travis-ci.org/daytum/intake-data)
[![PyPI version](https://badge.fury.io/py/daytum-data.svg)](https://badge.fury.io/py/daytum-data)

## Installation

```
pip install daytum-data
```

## Usage

To avoid explicitly providing a username/password to every API call set the following environment variables in your shell

```bash
BAZEAN_POSTGRES_USERNAME
BAZEAN_POSTGRES_PASSWORD
```

Then import the catalogues

```python
from intake import cat
```

e.g. to get the historical production data by API number

```python
cat.production.production_by_api(api='33001000050000')
```
