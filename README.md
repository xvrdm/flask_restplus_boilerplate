# Basic Flask_Restplus API boilerplate

## Before you run the app

Install the pip requirements.

```bash
pip install -r requirements.txt
```

## How to run

The app is based on the [application factory
pattern](http://flask.pocoo.org/docs/0.12/patterns/appfactories/).

Make sure you export the `FLASK_APP` env var to the `run.py` script and use
`flask run`.

```bash
# from the app dir
export FLASK_APP=run.py
python -m flask run
```

## How to see Swagger doc

As said on [flask-restplus
documentation](http://flask-restplus.readthedocs.io/en/stable/swagger.html),

> By default flask-restplus provides Swagger UI documentation, served from the root URL of the API.

So just visit `127.0.0.1:5000/api/v1`.
