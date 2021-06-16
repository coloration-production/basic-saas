# Use the Python3.7.2 image
FROM python:3.9-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

CMD ["python", "main.py"]

