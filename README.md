# BumpCar - Backend

## What is BumpCar?

Bumpcar is online shop inspired by [AutoDiler](https://www.autodiler.me). Its created as a final project for Developers Lab's [Django Course](https://developers-lab.me/kurs/backend-django-v2). This is it's REST API built with [Django REST Framework](https://www.django-rest-framework.org).

## Setup

To install the project localy you need to do couple of things:

- Make sure you have Python version > 3.0.0 installed on your machine, as well as Git and IDE ([Visual Studio Code](https://code.visualstudio.com) or [PyCharm](https://www.jetbrains.com/pycharm) would be prefered).
- Since this app uses [PostgreSQL](https://www.postgresql.org) as DBSM, you will have to install it localy as well.
- Choose your working directory and clone the project from `main` branch.
- Activate `venv`, then install all the dependencies from `requirements.txt`.
- Using [Psql CLI](https://www.postgresguide.com/utilities/psql) or [PgAdmin](https://www.pgadmin.org) execute `db_setup.sql` and `db_startup.sql` from `sql` folder to setup your database and set the admin user.
- Create `.env` by copying `.env.example` to set all of the necessary enviroment variables. Keep in mind that this `.env` is used ONLY for development, to get production variables ask the owner.
- Run your app using `python manage.py runserver` (this may vary depending of your OS) or `gunicorn bumpcar.wsgi` (recommended).
- Thats it, let us know if you have some issues, happy coding :)

## API Requests

Here you can see all of the available API endpoints, you can test them using this Postman [collection](https://interstellar-meadow-494367.postman.co/workspace/Team-Workspace~d5e9489c-eeba-4cfa-819f-dbb30cd82565/collection/14650526-8df54acd-ceb6-4e80-a903-97c49fe5ebc9?ctx=documentation) (you can only access this if you are a team member).

### User requests

- `GET /users` - Get all users, no authentication required.
- `GET /user/<int:pk>` - Get user info by id, no authentication required.
- `POST /user/create` - Create new user, no authentication required.
- `POST /auth/jwt/create` - Get JWT, no authentication required.
- `PUT /user/update/<int:pk>` - Update user by it's primary key, authentication required.
- `DELETE /user/delete/<int:pk>` - Delete user by it's primary key, authentication required.

### Vehicle

- `GET /vehicles` - Get all the vehicles, no authentication required.
- `GET /vehicle/<int:pk>` - Get vehicle by primary key, no authentication required.
- `GET vehicle/user/<int:pk>` - Get all vehicles by user id, no authentication required.
- `GET /vehicle/<int:pk>/images` - Get all images by vehicle id, no authentication required.
- `POST /vehicle` - Create new vehicle, authentication required.
- `DELETE /vehicle/delete/<int:pk>` - Delete vehicle by id, authentication required.

### Search Fields

- `GET /conditions` - Get all conditions, no authentication required.
- `GET /fuel-types` - Get all fuel types, no authentication required.
- `GET /gear-types` - Get all gear types, no authentication required.
- `GET /colors` - Get all colors, no authentication required.
- `GET /vehicle-types` - Get all vehicle types, no authentication required.
- `GET /drivetrains` - Get all drivetrains, no authentication required.
- `GET /brands` - Get all brands, no authentication required.
- `GET /models/<str:pk>` - Get all models by brand, no authentication required.
- `GET /locations` - Get all locations, no authentication required.

- `POST /condition` - Create condition, authentication required.
- `POST /fuel-type` - Create fuel type, authentication required.
- `POST /gear-type` - Create gear type, authentication required.
- `POST /color` - Create color, authentication required.
- `POST /vehicle-type` - Create vehicle type, authentication required.
- `POST /drivetrain` - Create drivetrain, authentication required.
- `POST /brand` - Create conditbrandion, authentication required.
