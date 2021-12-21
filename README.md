# Simple REST API
A demo project in REST API with CRUD operations
## Requirements
 - [Python3.7]
 - [Django 3.2]
 - [Django REST Framework]
## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command
```http
python -m venv env
```
After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)
You can install all the required dependencies by running
```http
pip install -r requirements.txt
```
## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources.

In our case, resource are students and university so we will use the following URLS - /students,/students/id and /university,/university/id for collections and elements, respectively:
| Endpoint	 | HTTP Method | CRUD Method	| Result|
| :-------- | :------- | :----------- |----------|
| `students` | GET | READ | Get all students|
| `students/id` | GET | READ | Get a single students|
| `students` | POST | CREATE | Create a new students|
| `students/id` | PUT | UPDATE | Update a students|
| `students` | DELETE | DELETE | Delete a students|
| `university` | GET | READ | Get all university|
| `university/id` | GET | READ | Get a single university|
| `university` | POST | CREATE | Create a new university|
| `university/id` | PUT | UPDATE | Update a university|
