FROM python:latest

RUN mkdir -p /usr/src/app

# copy the current directory contents into the container at /app
COPY ./app /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application.
CMD ["python", "app.py"]
