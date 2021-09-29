#### Check versions
```
$ python --version
$ pip --version
$ virtualenv --version
```

#### Install virtualenv as needed
```
$ pip install virtualenv
```

#### Inside the project's base directory, create a virtualenv named 'venv'
```
$ virtualenv venv
```

#### Activate the virtualenv (Git Bash in Windows)
```
$ source venv/Scripts/activate
```
#### Activate the virtualenv (Linux)
```
$ source venv/bin/activate
```

#### While virtualenv is activated, install all of the project’s dependencies into the virtualenv instead of into the global Python environment
```
$ pip install -r requirements.txt
```

#### Start the application
```
$ python app.py
```

#### De-activate the virtualenv when you are done
```
$ deactivate
```

## Here are a few additional helpful commands:

#### Review what's installed while virtualenv is activated
```
$ pip list
```

#### Capture what's installed inside the virtualenv in requirements.txt while virtualenv is activated
```
$ pip freeze > requirements.txt
```

#### Remove the virtualenv
```
$ rm -rf venv
```



