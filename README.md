 ## Scope
The goal of this project is to create a fully functioning API project for the Little Lemon restaurant so that the client application developers can use the APIs to develop web and mobile applications. People with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders.
The next section will walk you through the required endpoints with an authorization level and other helpful notes. Your task is to create these endpoints by following the instructions.

## Structure
Create one single Django app called LittleLemonAPI and implement all API endpoints in it. Use pipenv to manage the dependencies in the virtual environment.

Use function- or class-based views or both in this project. Follow the proper API naming convention throughout the project.

Create the following two user groups and then create some random users and assign them to these groups from the Django admin panel.
Manager
Delivery crew
Users not assigned to a group will be considered customers.

Error check and proper status codes
Display error messages with appropriate HTTP status codes for specific errors. These include when someone requests a non-existing item, makes unauthorized API requests, or
sends invalid data in a POST, PUT or PATCH request. Here is a full list.

![Screenshot of HTTP Status codes](https://github.com/Razz67/Meta-API-Project/assets/6307334/861d3a48-230e-4f95-aa63-21d7c0679d2c)

## API endpoints
Here are all the required API routes for this project grouped into several categories.
User registration and token generation endpoints
You can use Djoser in your project to automatically create the following endpoints and functionalities for you.

![image of API endpoints](https://github.com/Razz67/Meta-API-Project/assets/6307334/79a703a0-8828-46f3-8a59-0616b793108c)


When you include Djoser endpoints, Djoser will create other useful endpoints.

![image menu item endpoints](https://github.com/Razz67/Meta-API-Project/assets/6307334/be110ed0-d7c0-4186-9386-6ce161a6d32c)

![image User group management endpoints](https://github.com/Razz67/Meta-API-Project/assets/6307334/e2747334-2d01-4edc-97bb-f4ebe5d96c41)

![image cart management endpoints](https://github.com/Razz67/Meta-API-Project/assets/6307334/ef8e6ab4-c84f-41be-9671-41fb29211594)

![image order management endpoints](https://github.com/Razz67/Meta-API-Project/assets/6307334/4fe71fac-4ae4-486a-b8b7-8e93eb0f7ca8)

## Additional steps
Implement proper filtering, pagination and sorting capabilities for /api/menu-items and /api/orders endpoints.

Apply throttling for the authenticated users and anonymous or unauthenticated users. 
