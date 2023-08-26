# Mobile Factory Code Challenge

This project implements an API to create the order of a phone given a list of component codes.

## Requirements

* Python 3.8 or higher

## Installation

1. Install virtualenv
pip install virtualenv
2. Create a virtual environment and activate it
virtualenv mob_fac
3. Install the dependencies:
pip install -r requirements.txt

## Running the project

1. Start the development server:
uvicorn factory_app.app:app --reload
2. Make a POST request to the `/orders` endpoint with the list of component codes as the body:
curl -X POST http://localhost:8000/orders -H "Content-Type: application/json" -d '{ "components": ["I","A","D","F","K"] }'

## Tests

1. Execute tests by running:
pytest tests/

## Design and architecture

The project is designed to be simple and easy to understand. The main components of the project are:

* The `app.py` file, which contains the main application code.
* The `server.py` file that initialises store, and copies the mobile configurations from local JSON.
* The `factory_app/models` folder, which defines the data models for the project. (Database is not implemented at the moment. Out of scope from assesment requirement)
* The `factory_app/urls.py` file, which defines the routes for the API.
* The `tests/` folder, which contains the unit tests for the project.
* The `cache/` folder, which contains the handlers that are used for caching data.
* The `data/` folder, which contains all local data sets.
* The `api/` folder, contains all related handlers like validations, etc.
* The `middlewares/` folder, contains all the middlewares.

## Dataset

The dataset is loaded from local file. The file path can be updated in MOBILE_PARTS_CONFIG_FILE_PATH. (There is no validation implemented to check the schema of this JSON file)

## Caching
* As per requirement the mobile factory config is cached in the memory. The cache is updated every 60 seconds and this can be updated in MOBILE_PARTS_CACHE_INTERVAL env variable

## Required updates

1. API versioning
2. External Logger integration
3. More sophisticated validation module.
4. Request Authorization.
5. Restructure Testing module.

## README.md

This README file explains how the project works and all instructions required to run the project.


