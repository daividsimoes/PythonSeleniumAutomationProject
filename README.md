# Selenium Automation Project

## Overview
This project is a test automation framework designed to assist those learning test automation using technologies such as 
**Python**, **Pytest**, **Selenium**, and the **Page Object Model (POM)** pattern. 

It provides a hands-on, structured approach to understanding and applying these tools, making it easier for beginners to
grasp key concepts in automated testing.

## Project Structure

```plaintext
SeleniumAutomationProject
|-- drivers
|-- pages
|   |-- login
|   |-- main
|-- test
|-- .env
|-- README.md
|-- requirements.txt
```

# Getting Started

## Prerequisites

- Python 3.12
- Chrome 129

## Installation
This project includes the correct ChromeDriver for Chrome version 129. If you're using a different version of Chrome, please download the appropriate ChromeDriver from:
https://developer.chrome.com/docs/chromedriver/downloads
After downloading, replace the existing driver in the 'drivers' folder with the updated version.

1. Clone the repository:

```plaintext
git clone https://github.com/daividsimoes/SeleniumAutomationProject.git
cd SeleniumAutomationProject
```

2. Install project dependencies:

```plaintext
pip install -r requirements.txt
```

# Running Tests

Execute the following command to run the tests:

```plaintext
pytest tests/[TEST_FILE_NAME_HERE]
```