FROM python:3.10.2  
COPY . /app 
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app


# FROM cmd-it is taking as the base image 
# COPY cmd - this will copy all the files from the current repository to the base image on dockerhub
# WORKDIR cmd - this is the working directory
# RUN cmd - it will install all the dependency which is required by the app
# EXPOSE cmd - to expose the application inside the dockerimage we require some port
# CMD cmd - to run the entire application
# 0.0.0.0:$PORT - this line means,we are binding the PORT we got from the dockerimage and assigning to the local address on the heroku cloud 