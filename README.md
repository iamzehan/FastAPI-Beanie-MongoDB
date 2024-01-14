
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

<button style="background-color: #61affe; border-radius: 8px; border: none; height: 40px; width: 70px; font-weight: bold;">GET</button>
<button style="background-color: #49cc90; border-radius: 8px; border: none; height: 40px; width: 70px; font-weight: bold;">POST</button>
<button style="background-color: #fca130; border-radius: 8px; border: none; height: 40px; width: 70px; font-weight: bold;">PUT</button>
<button style="background-color: #f93e3e; border-radius: 8px; border: none; height: 40px; width: 70px; font-weight: bold;">DELETE</button>
<button style="background-color: #fff; border-radius: 8px; border-color: #49cc90; height: 40px; width: 120px; font-weight: bold; color: #49cc90;">Authorize<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 2 20 20" width="20" height="10" aria-hidden="true" focusable="false" style="fill: #49cc90; vertical-align: middle"><path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V6h2v-.801C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8z"></path></svg></button>

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

