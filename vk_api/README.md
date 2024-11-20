# Automated Tests for vk.com website

Testing of vk.com interface and vk api. Tests are written in Python using Selenium, PyTest, py_selenium_auto library, requests library.


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

## Installation

1. Clone the repository:

   git clone https://github.com/tquality-education/d.kunakbaev.git


2. Install dependencies:
    pip install -r requirements.txt


3. Edit token, email, password and user_name in config.json file, use your data for run tests.


4. Running Tests
    Run tests using pytest:
    pytest


Author
Denis-Kunakbaev