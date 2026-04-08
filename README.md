# Stepik Test Course Final Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-7.0%2B-blue)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-green)](https://www.selenium.dev/)

## Project Goal

This is my final project for the Stepik automated testing course.  
The main goal is to demonstrate my skills in UI test automation using Python, Selenium, and Pytest as part of my QA Engineer portfolio.

##  Technologies Used

- Python 3.10+
- Selenium WebDriver
- Pytest testing framework
- Page Object Model design pattern

## Application Under Test

A demo e‑commerce website used for educational purposes:  
[http://selenium1py.pythonanywhere.com/](http://selenium1py.pythonanywhere.com/)

## Setup and How to Run the Tests

Follow these steps to run the tests on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/ElviraFaizullina/stepik_test_course_final_project.git
cd stepik_test_course_final_project

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate        # On Linux / macOS
# venv\Scripts\activate         # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run all tests
pytest -v

# 5. Run tests with an HTML report
pytest --html=report.html
