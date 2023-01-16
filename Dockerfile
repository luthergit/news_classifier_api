#pull in python image as a basis for your docker image
FROM --platform=arm64 python

#create a working dir called 'app' in my docker
WORKDIR /app

#copy the relevant files in the app folder
COPY model_joblib ten_notes.py news_dataset.json 10_notes_api.py requirements.txt /app/

#install the requirements from the txt file 
RUN pip install -r requirements.txt

# export and exposes to local server in docker container
EXPOSE 8000

#run the file
CMD [ "uvicorn","10_notes_api:app", "--host", "0.0.0.0", "--port", "8000"]

#Next step: command shift p