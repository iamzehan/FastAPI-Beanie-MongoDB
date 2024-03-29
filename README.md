
## How to create FastAPI with MongoDB?
___

<h1 align="center" style="vertical-align:middle"> 
FastAPI <img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/fastapi-icon.svg" alt="html5" width="40" height="40" style="vertical-align:middle" /> + Beanie <img src="https://beanie-odm.dev/assets/logo.svg" alt="html5" width="40" height="40" style="vertical-align:middle"/> + MongoDB <img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/mongodb-icon.svg" alt="html5" width="40" height="40" style="vertical-align:middle"/>
</h1>

## Here's the directory structure
___

```
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── auth
│   │   ├── auth_handler.py
│   │   ├── auth_token.py
│   │   └── auth_user.py
│   └── server
│       ├── app.py
│       ├── database.py
│       ├── models
│       └── routes
└── requirements.txt
```

### <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="20" height="20" style="vertical-align: middle"/> [`main.py`](https://github.com/iamzehan/FastAPI-Beanie-MongoDB/blob/main/app/main.py)
___
Responsible for running the app on server

### [📁 `auth/`](https://github.com/iamzehan/FastAPI-Beanie-MongoDB/tree/main/app/auth)
Handles the authentication processes.

### [📁 `server/`](https://github.com/iamzehan/FastAPI-Beanie-MongoDB/tree/main/app/server)
___
Contains database schema and API routes.

#### [📁 `models/`](https://github.com/iamzehan/FastAPI-Beanie-MongoDB/tree/main/app/server/models)
___
Contains files that define the structure of your database documents.
(This is a NoSQL Database so, there's no tabular schema)

#### [📁 `routes/`](https://github.com/iamzehan/FastAPI-Beanie-MongoDB/tree/main/app/server/routes)
___
Handles all the requests and responses

![Screenshot 2024-01-15 001300](https://github.com/iamzehan/FastAPi-Beanie-MongoDB/assets/43857150/30c312cd-4c4b-4638-9524-f32171fb17a0)


#### <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="20" height="20" style="vertical-align: middle"/> `app.py`
___
Registers and handles urls and runs the FastAPI instance.

#### <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="20" height="20" style="vertical-align: middle"/> `database.py`
___
Handles the connection with the database and as well as all the interactions between MongoDB server and the FastAPI server.

<h2 align = "center"> <img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="30" height="30" style="vertical-align: middle;"/> Setting up the Development Environment </h2>

<img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="20" height="20" style="vertical-align: middle;"/> Create Virtual Environment

```bash
virtualenv env
```
<img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="20" height="20" style="vertical-align: middle;"/> Activate `env`

```bash
source env/Scripts/activate
```

<img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="20" height="20" style="vertical-align: middle;"/> Install requirements 

```bash
pip install -r requirements.txt
```

<img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="20" height="20" style="vertical-align: middle;"/> Run the project

```bash
python app/main.py
```
or 

```powershell
$ cd app/server

$ uvicorn app:app --reload
```

<h3 align="center"> Technologies & Links </h3>


___

<p align="center"> 
<a href="https://fastapi.tiangolo.com/learn/" title="FastAPI" target="_blank"><img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/fastapi-icon.svg" alt="html5" width="40" height="40"/></a> <a href="https://beanie-odm.dev/" title="Beanie-ODM" target="_blank"><img src="https://beanie-odm.dev/assets/logo.svg" alt="html5" width="40" height="40"/></a> <a href="https://pymongo.readthedocs.io/en/stable/" title="PyMongo" target="_blank"><img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/mongodb-icon.svg" alt="html5" width="40" height="40"/></a> <a href="https://motor.readthedocs.io/en/stable/" title="Motor" target="_blank"><img src="https://pypi-camo.freetls.fastly.net/77995688c0cf8df7a671a4df729bd2f565ab00fc/68747470733a2f2f7261772e6769746875622e636f6d2f6d6f6e676f64622f6d6f746f722f6d61737465722f646f632f5f7374617469632f6d6f746f722e706e67" alt="html5" width="40" height="40"/> 
<a href="https://www.uvicorn.org/" title="Uvicorn" target="_blank"><img src="https://pypi-camo.freetls.fastly.net/a9f3326a04ed20fe759542f5c73a95f8a8770235/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f746f6d63687269737469652f757669636f726e2f6d61737465722f646f63732f757669636f726e2e706e67" alt="html5" width="40" height="40"/></a>
<a href="https://jwt.io/" title="JWT" target="_blank"><img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/jwt-icon.svg" alt="html5" width="40" height="40"/></a>

</p>

___

