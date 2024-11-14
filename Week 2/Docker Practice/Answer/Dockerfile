# TODO-STEP 1: Choose a base image
FROM python:3.9-slim

# TODO-STEP 2: Set the working directory
WORKDIR /app

# TODO-STEP 3: Copy the requirements file
COPY requirements.txt .

# TODO-STEP 4: Install the Python dependencies
RUN pip install -r requirements.txt

# TODO-STEP 5: Copy the application code
COPY app.py .

# TODO-STEP 6: Specify the command to run the application
CMD ["python", "app.py"]