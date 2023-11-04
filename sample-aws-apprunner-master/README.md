# Sample AWS App Runner Python Application
This is a sample project that uses Pipenv and Gunicorn to run a Python web application.

## Installation
To install Pipenv, run the following command:

```bash
    pip install pipenv
```
To create a virtual environment for this project, run the following command:
```bash
    pipenv shell
```

This will activate the virtual environment and allow you to install the required libraries.

To install the required libraries for this project, run the following command:
```bash
    pipenv install
```
This will install all the libraries listed in the Pipfile.lock file.

## Running the application
To run the application, run the following command:
```bash
    gunicorn wsgi:app
```
This will start the application on port 8000.

