1. Create new environment conda create -n <env-name> python=3.7 -y
2. Activate environment.
3. Create requirements.txt and enter the initial libraries
4. run commmand - pip install -r requirements.txt
5. Create a template file
6. Define the template.py and run it to create the project structure.
7. Download the data.
9. Run git init, dvc init, and then dvc add <data-file>
10. Run git add & git commit command.

Setting up DVC:

- dvc repro    # Sets up pipeline and runs the code as per dvc.yaml
- dvc metrics show # shows the values against different paramets it is tracking
- dvc metrics diff # shows the difference in values of all parameters

Create test:
- create tox.ini file and setup.py. 
- Run 'tox' command which will create a temporary environment for testing
- Run tox -r for reloading the environment.
- after package is built
- pyest -v # command to run the test script

Running Jupyterlab Notebooks:
- install jupyterlab
- jupyter-lab notebooks/  # To run the jupyter notebook

Creating Own Exception Class:
- You can also define your own error exception class and raise exceptions.

Auto-Code formating: 
- Right click on any document and click "Format the document". It will format it as per PEP8 Standards

Type of Model files:
- Pickle - Allows saving model as serialized object
- joblib - Allows running model as pipeline function. If model has more number of arrays, it is better option.

Create Ci-CI workflow in Github for continuous deployment:
- Create .github/workflows/ci-cd.yaml file
- Whenever we'll push our code to main branch, this file will execute the jobs mentioned in it.
- Received error while Git push - ! [remote rejected] ok -> ok (refusing to allow a Personal Access Token to create or update workflow `.github/workflows/checks.yaml` without `workflow` scope)
error: failed to push some refs to
- Resolved by giving 'workflow' access to 'Personal Access Token' from profile --> Setting --> Developer Setting page.
- Create Procfile.

Heroku Deployment Error:
- Original demo has python3.7. The deployment was successful but the page gave error. On Closer look, 
I found out that the Heroku (stack 20, 22) wasn't supporting this version and tried to install python 3.10. 
Since original code was wrtting for 3.7, so it didn't work.

- I tired to update the python version to 3.9, and update the same in runtime.txt suggested in the various forums.
But it was failing the deployment with error message; Requested runtime (Python-3.9.12) is not available for this stack (heroku-20)

- I just removed the runtime file and it worked. Herouku automatically picked the python3.9.13 version.