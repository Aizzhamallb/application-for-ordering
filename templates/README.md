-## Blog Rest API test Project

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone ссылку
$ cd web-project/
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:

```sh
(venv)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

**Database schema image**

![linktomyschema](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D0%B2%D0%B5%D0%B1-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D1%8B_12-5-2023_152325_.jpeg)
