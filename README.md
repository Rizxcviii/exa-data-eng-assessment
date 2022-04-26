# Data Engineer - Technical Assesment

Our tech teams are curious, driven, intelligent, pragmatic, collaborative and open-minded and you should be too.

## My Solution

I have implemented a solution to use RDDs and spark programming to allow for easy configuration of changing of requested data when needed.
Due to the vague types of data required, I therefore created an open ended codebase, for easy changing of required data from the data set.
Currently the dataset retrieves the `fullUrl` and `id` of the required data.

## Technologies Used

- Programming Language + Framework - Python - PySpark
- Storage Layer - CSV

# How To Run

## Prequisites:

- Python3
- Pip
- virtualenv (should already be installed with python)

From the top level directory, perform `source env/bin/activate` to enter into the Virtual environment. (**NOTE: Use `deactivate` to leave the virtual env**)

To install the packages, do `env/bin/python3 -m pip install -r requirements.txt` which will install the dependencies

After intstallation, you can now begin to run the necessary code by doing `env/bin/python3 main.py`
