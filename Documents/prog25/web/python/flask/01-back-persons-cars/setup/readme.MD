* Setup:

1) Activate the virtual environment:

source setup/venv/bin/activate

If there is not virtual environment, create it:

$ cd setup
$ python3 -m venv venv

After creation, active it:

source venv/bin/activate

Install the libraries (see item )

$ pip3 install -r requirements.txt

* Alternatively, you can install libraries by hand:

$ pip3 install flask
$ pip3 install flask_sqlalchemy
$ pip3 install flask_cors
$ pip3 install pytest

* Maintenance: when necessary, generate new requirements:

pip3 freeze > requirements

2) Configure environment variables

Open the set/env.sh and adjust the absolute PATH inside it. After this, run:

Linux:
. setup/env.sh

Windows:
TODO

Alternatively, you can run steps 2.1 and 2.2, below.

2.1) You MUST configure PYTHONPATH to make the code works: (update the below path to the path where YOUR source code is)

Linux/macOS
export PYTHONPATH=/home/friend/02-gitlab/prog25/web/python/flask/01-back-persons-cars:$PYTHONPATH

Windows
set PYTHONPATH=C:\path\to\your\project;%PYTHONPATH%

2.2) Export the MY_DB environment variable:

Linux:
export MY_DB=SQLITE
or
export MY_DB=MYSQL

3) You can remove the database.db file and re-create the database:

rm src/database.db

python3 setup/create_database.py

4) Run the backend tests:

Goto the "tests" folder

Run:

$ pytest -s

5) If tests are ok, you can run the backend :-)

In folder "src", run:

flask run --debug

6) Call the backend, in the web browser:

localhost:5000