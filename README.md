# my-first-repo
## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-repo-env python=3.11

conda activate my-first-repo-env
```

Install packages:

```sh
#pip install pytest

pip install -r requirements.txt
```


## Usage

Play a game of rock, paper, scissors:

```sh
#python app/rps.py
python -m app.rps
```

### Web App

Run the web app:

```sh
FLASK_APP = web_app flask run
```

Visit in the browser, either:

  + http://127.0.0.1:5000
  + http://localhost:5000/


## Tests

Run the tests:

```sh
# find all the tests and run them:
pytest
```
