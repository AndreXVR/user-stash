# user-stash
Python package for the user stash server

# Instructions
1. Use "docker-compose up" to start application

2. Use "docker exec -it user-stash_backend_1 flask --app user_stash/app.py db upgrade" to run the migrations (having issues running automatically in docker)

3. Access "http://localhost:4200/"
