# Automated Tests for UI + API task

This project was developed to test the web interface and API requests to the database. 
Tests are written in Python using Selenium, PyTest, py_selenium_auto library, requests library.
The tests cover user authentication, data retrieval, CRUD operations on resources, and database interactions.


## Requirements

- PyHamcrest==2.1.0
- pytest==7.4.4
- allure-pytest==2.13.5
- selenium==4.11.2
- webdriver-manager==4.0.1
- dependency-injector-fork==4.42.1
- py-selenium-auto==0.4.6
- pytest-xdist==3.5.0
- imagehash==4.3.1
- dataclasses-json==0.5.7
- xmltodict==0.13.0
- requests==2.32.3

## Installation

1. Clone the repository:

   git clone https://github.com/tquality-education/d.kunakbaev.git


2. Install dependencies:
    pip install -r requirements.txt


3. **To successfully connect to the database, you need to create environment variables in the format key : value.**:
- LOGIN: 'Your database username'

- PASSWORD: 'Your database password'.


4. Running Tests
    Run tests using pytest:
    pytest


Author
Denis-Kunakbaev