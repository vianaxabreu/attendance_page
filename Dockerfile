# python image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy requirements
COPY requirements.txt requirements.txt

# copy files
COPY ./app .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# run the Flask app
ENV FLASK_APP=page:app
CMD ["flask", "run", "--host=0.0.0.0"]
