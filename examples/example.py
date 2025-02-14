"""
    Examples of GET/POST requests.
"""


# ============================ Example of a POST request:
"""
POST / HTTP/1.1
Content-Type: application/json
{
    "title": "Test",
    "is_completed": false
}
"""

# --------------------------- Response example:
"""
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 7,
    "title": "Test",
    "is_completed": false
}
"""


# ============================ Response of a GET request:

"""
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "title": "Забрать товар со склада",
        "is_completed": false
    },
    {
        "id": 2,
        "title": "Забрать товар со склада",
        "is_completed": false
    },
    {
        "id": 3,
        "title": "Забрать товар со склада",
        "is_completed": false
    },
    {
        "id": 4,
        "title": "Забрать товар со склада",
        "is_completed": false
    },
    {
        "id": 5,
        "title": "Забрать товар со склада",
        "is_completed": false
    },
    {
        "id": 6,
        "title": "Забрать товар со склада",
        "is_completed": false
    },
    {
        "id": 7,
        "title": "Тест",
        "is_completed": false
    },
    {
        "id": 8,
        "title": "Тест",
        "is_completed": false
    },
    {
        "id": 9,
        "title": "Тест",
        "is_completed": false
    }
]
"""

