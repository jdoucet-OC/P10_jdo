# P10_jdo

## Introduction

This python project is a django-rest framework based API allowing users to manage "projects".  
Any authentified user ( JWT Token ) can browse through the API, with limited access depending on the endpoints and their role on the projects.

## Install
1.Download the github project, unzip it in the folder of your choosing  
2.Using a terminal, place yourself in the project folder and create a virtual environnement using :  
`python -m venv env`  
3.Activate the virtual environnement using :  
windows : `env/Scripts/activate.bat`  
linux / mac : `source env/bin/activate`  
4.Install the python packages needed to run the program using :  
`pip install -r requirements.txt`  
5.Run the web server using :  
`python manage.py runserver`  
6.You can now access the web application locally using the given link in the console ( usually, http://127.0.0.1:8000 )  
7.Refer to the PostMan documentation to see how to use the API : https://www.postman.com/ocjdo/workspace/my-workspace/overview

## Flake-8 Report
To generate a Flake8-html report, use :  
`flake8 --format=html --htmldir=flake-report`  
Some files in the report show errors, which I cannot correct since those are django managed files.

