# python image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy files
COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port
EXPOSE 5000

# run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
