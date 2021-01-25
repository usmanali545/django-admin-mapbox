# django-admin-mapbox

## Problem
A web application to store data about point of interest on the map and showing point of interest on the map.

## Solution
I made a model to store data the model have following fieds.
- Longitude
- latitude
- Active or not active
- Json field to store geo Json
- Category

we use django default admin to store data in the database(Default django database). We have only one view that get the point of interest from the data base if they are active. And passes it to the frontend. On
frontend I have used mapbox api. Javascript takes that data and shows that on the screen using mapbox api. I did this project in about 4 hours.

## How to Setup
- Python should be insatlled
- Pip install pienv
- Pipenv shell
- Activate that virtual environment
- Pip install -r requirements.txt
- Python manage.py createsuperuser
- If you created new database
- Python manage.py makemigrations
- Python manage.py migrate
- Python manage.py runserver
