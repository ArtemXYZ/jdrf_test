> # <p align="center">Test implementation of API (GET/POST)</p>

## About the project

    Implementing a minimal API using the Django REST Framework (DMF), which supports two HTTP methods:
        1. GET — to get a list of issues.
        2. POST — to create a new task.

    ==================================================================================================
    What is implemented
    ==================================================================================================

    1. The "Task" Model:    
        Described the data structure (task name and completion status).
        It is stored in the database.    

    2. The "TaskSerializer" Serializer:    
        Converts data from the model to JSON (and vice versa). 

    3. View "Task" List:    
        Processes GET requests (returns a list of tasks).    
        Processes POST requests (creates a new task).  

    4.Route URL:    
        It is configured so that requests to / are processed by your view.

    5.Testing:    
        The API has been tested through the browser.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Examples of GET/POST requests.

```python
# Creating a task (example of POST request):
{
    "title": "Забрать товар со склада",
    "is_completed": false
}
```

```python
# Response
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 7,
    "title": "Test",
    "is_completed": false
}
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Instruction manual:

1. Make sure that you have Python, Django, and Django REST Framework installed.
2. Clone the repository
3. Install the dependencies:
```python
pip install -r requirements.txt
```
4. Apply migrations:

```python
.\manage.py makemigrations 
```
```python
.\manage.py migrate 
```
5. Start the server:
```python
.\manage.py runserver
```
 - _Before executing commands in the console, do not forget to go to the Django project directory._

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project scheme

    jdrf/
    ├── jdrf/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   └── wsgi.py
    ├── tasks/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── requirements.txt
    └── README.md