# Description:
The project is about building test automation framework to test the musala soft webpage. 
The automation process includes testing the functionality for contact page, company page  and careers page.

# Concepts Included
- Parallel test runs
- Page object model
- Common web page interaction methods

# Tools
- selenium
- pytest-xdist
- pytest 
- pytest-xdist
- pytest-html

# Requirements:
In order to utilise this project you need to have the following installed locally:
- Python 3.11 version
- Chrome and Chromedriver
- Firefox and Firefoxdriver

# Usage:
- Command used for html regeneration: 
```pytest --html=report.html```
- Command used for parallel execution:
```pytest -n [Number of cores]```
- To run all test execute command:
```pytest```
- The browser selection option is available in config.py. Change the browser variable from chrome to firefox.