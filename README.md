
## How to create FastAPI with MongoDB?
___

<h1 align="center"> 
FastAPI <img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/fastapi-icon.svg" alt="html5" width="40" height="40"/> + Beanie <img src="https://beanie-odm.dev/assets/logo.svg" alt="html5" width="40" height="40"/> + MongoDB <img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/mongodb-icon.svg" alt="html5" width="40" height="40"/>
</h1>

## Here's the directory structure
___

```
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── auth
│       ├── auth_handler.py
│       ├── token_model.py
│       └── user.py
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

### `auth/`
Handles the authentication processes.

### `server/`
___
Contains database schema and API routes.

### `models/`
___
Contains files that define the structure of your database documents.
(This is a NoSQL Database so, there's no tabular schema)

### `routes/`
___
Handles all the requests and responses

![Alt text](image.png)

### `app.py`
___
Registers and handles urls and runs the FastAPI instance.

### `database.py`
___
Handles the connection with the database and as well as all the interactions between MongoDB server and the FastAPI server.

## Installation

* Create Virtual Environment

```bash
virtualenv env
```
* Activate `env`

```bash
source env/Scripts/activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

* Run the project

```bash
python app/main.py
```
<h3 align="center"> Packages </h3>

___

<p align="center"> 
<img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/fastapi-icon.svg" alt="html5" width="40" height="40"/> <img src="https://beanie-odm.dev/assets/logo.svg" alt="html5" width="40" height="40"/><img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/mongodb-icon.svg" alt="html5" width="40" height="40"/> <img src="https://pypi-camo.freetls.fastly.net/77995688c0cf8df7a671a4df729bd2f565ab00fc/68747470733a2f2f7261772e6769746875622e636f6d2f6d6f6e676f64622f6d6f746f722f6d61737465722f646f632f5f7374617469632f6d6f746f722e706e67" alt="html5" width="40" height="40"/> <img src="https://pypi-camo.freetls.fastly.net/a9f3326a04ed20fe759542f5c73a95f8a8770235/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f746f6d63687269737469652f757669636f726e2f6d61737465722f646f63732f757669636f726e2e706e67" alt="html5" width="40" height="40"/>
</p>

___

