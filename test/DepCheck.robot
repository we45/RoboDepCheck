*** Settings ***
Library  /Users/nithinjois/PycharmProjects/github/RoboNodeJSScan/robonodejsscan/RoboDepCheck.py
Library  Collections


*** Variables ***
${CODE_PATH}  /Users/nithinjois/Downloads/HacmeBooks
${RESULT_PATH}  /Users/nithinjois/Downloads/dep_check_report
${NVD_DB_PATH}  /Users/nithinjois/Downloads/data

*** Test Cases ***
RUN OWASP DEP CHECK
    run depcheck against source  ${CODE_PATH}  ${RESULT_PATH}  ${NVD_DB_PATH}