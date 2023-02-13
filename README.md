# TODO LIST FLASK API

### Starting the application

-execute command './env/Scripts/Activate.ps1'
-execute command 'python ./app.py'

### Endpoints

-method='GET' - '/' : returns all tasks
-method='POST' - '/create' : create a new task (takes task name and description name as request body)
-method='PATCH' - '/update/:sno' : updates a task with 'sno' (takes updated task name and description name as request body) - '/markCompleted/:sno' : marks a task completed with 'sno' - '/markInompleted/:sno' : marks a task incomplete with 'sno'
-method='DELETE' - '/delete/:sno' : deletes a task with 'sno'
