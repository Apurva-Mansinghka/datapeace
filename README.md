# datapeace
Backend Developer assignment by DataPeeace
Download all files and folders on local drive

On command prompt after checking is django is installed and activating virtual environmet in root directory of project 
Go to the directory where manage.py file is saved and run command on command promt-
  python manage.py runserver
now we test it in browser by typing the command 
  http://localhost:8000/
It will then provide link to view all users

URL's to be used to test the API on localhost
  http://localhost:8000/api/users/   - To get list of all users with filter button and search option on fisrtName and lastName(subtring match and case insensitive)
  http://localhost:8000/users/2/ - how details of user with id 2
  http://localhost:8000/api/users/new - To add a new user
  http://localhost:8000/api/users/1/delete - To delete user with id 1
  http://localhost:8000/api/users/1/update - Update details of user with id 1
  http://localhost:8000/users/2/ - how details of user with id 2


