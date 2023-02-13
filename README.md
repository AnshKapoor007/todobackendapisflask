# TODO LIST FLASK API

### Starting the application

1. execute command 'virtualenv env'
2. execute command './env/Scripts/Activate.ps1'
3. execute command 'python ./app.py'

### Endpoints

1. method='GET'
  * '/' : returns all tasks
2. method='POST'
  * '/create' : create a new task (takes task name and description name as request body)
3. method='PATCH'
  * '/update/:sno' : updates a task with 'sno' (takes updated task name and description name as request body)
  * '/markCompleted/:sno' : marks a task completed with 'sno'
  * '/markInompleted/:sno' : marks a task incomplete with 'sno'
4. method='DELETE'
  * '/delete/:sno' : deletes a task with 'sno'
