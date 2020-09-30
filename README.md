 Run locally

**Highly encouraged to create a python environment first.**

Clone the repository:

	$ git clone https://github.com/AmanShrivastav/ModeltoJsonAPI.git

Move into the cloned folder and install the required libraries:

	$ cd useractivitymodel
	$ pip install -r requirements.txt

After that run with:

	$ python manage.py

Visit the below URL to view the flask app:

	127.0.0.1:8000

**NOTE:** When running locally all redirects will also be local.

# Deploying

If you do not have a dedicated server, I highly recommend using [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python), [PythonAnywhere](https://www.pythonanywhere.com/) or [AWS](https://aws.amazon.com/getting-started/projects/deploy-python-application/) to host your application.

Before deploying, in the file:

	useractivitymodel/manage.py  

set running in debug mode to False:

	app.run(debug=False)
