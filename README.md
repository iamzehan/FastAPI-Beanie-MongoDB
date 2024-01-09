<h1 align="center"> FastAPI <img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/fastapi-icon.svg" alt="html5" width="40" height="40"/>+ Beanie <img src="https://beanie-odm.dev/assets/logo.svg" alt="html5" width="40" height="40"/> + MongoDB <img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/mongodb-icon.svg" alt="html5" width="40" height="40"/></h1>

## Here's the directory structure
___

```├── app
│   ├── __init__.py
│   ├── main.py
│   └── server
│       ├── app.py
│       ├── database.py
│       ├── models
│       └── routes
└── requirements.txt
```

### `main.py`
___
Responsible for running the app on server

### `server/`
___
Contains database schema and API routes.

### `models/`
___
Contains files that define the structure of your database documents.
(This is a NoSQL Database so, there's no tabular schema)

### `routes/`
___
Handles all the requests and response
* GET
* POST
* PUT
* PATCH
* DELETE

### `app.py`
___
Registers and handles urls and runs the FastAPI instance.

### `database.py`
___
Handles the connection with the database and as well as all the interactions between MongoDB server and the FastAPI server.

