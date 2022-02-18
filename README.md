# BumpCar - Backend

Bumpcar is....

## User requests

- `GET /users` - Get all users, no authentication required.
- `POST /user/create` - Create new user, no authentication required.
- `PUT /user/update/<int:pk>` - Update user by it's primary key, authentication required.
- `DELETE /user/delete/<int:pk>` - Delete user by it's primary key, authentication required.

## Vehicle requests

- `GET /vehicles` - Get all the vehicles, no authentication required.
- `GET /vehicle/<int:pk>` - Get vehicle by primary key, no authentication required.
- `POST /vehicle` - Create new vehicle, authentication required.

## Fields requests

- `GET /conditions` - Get all conditions, no authentication required.
- `GET /fuel-types` - Get all fuel types, no authentication required.
- `GET /gear-types` - Get all gear types, no authentication required.
- `GET /colors` - Get all colors, no authentication required.
- `GET /vehicle-types` - Get all vehicle types, no authentication required.
- `GET /drivetrains` - Get all drivetrains, no authentication required.
- `GET /brands` - Get all brands, no authentication required.

- `POST /condition` - Create condition, authentication required.
- `POST /fuel-type` - Create fuel type, authentication required.
- `POST /gear-type` - Create gear type, authentication required.
- `POST /color` - Create color, authentication required.
- `POST /vehicle-type` - Create vehicle type, authentication required.
- `POST /drivetrain` - Create drivetrain, authentication required.
- `POST /brand` - Create conditbrandion, authentication required.
