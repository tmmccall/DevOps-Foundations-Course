# Docker Containerization Exercise: Python Flask API

This exercise guides you through the process of containerizing a Python Flask API using Docker. After sucessfully completing this exercise you will have learnt how to create a Dockerfile, build a Docker image, and run a container.

## Prerequisites

Before starting this exercise, ensure you have:

1. **Docker** installed on your local machine:
   - To test if it is installed, open your Command Line Terminal and run:
     ```bash
     docker --version
     ```
   - If not installed, download it from here:
        - Windows: [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
        - macOS: [Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
        - Linux: [Docker Engine for Linux](https://docs.docker.com/desktop/setup/install/linux/)

        For convenience, please find the video tutorials to guide through the installation process:

        - [Windows Tutorial](https://www.youtube.com/watch?v=ZyBBv1JmnWQ)
        - [macOS Tutorial](https://www.youtube.com/watch?v=uDkf1fSPlYQ)
        - Linux Tutorials: [Option 1](https://www.youtube.com/watch?v=cqbh-RneBlk) or [Option 2](https://www.youtube.com/watch?v=PtwHLvfiyks)

2. A [**DockerHub account**](https://hub.docker.com/), if you do not have one, you can sign up [here](https://hub.docker.com/signup)

3. **Python** installed on your local machine _(Python 3.7 or higher recommended)_
   - To test if it is installed, open your Command Line Terminal and run:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```
   - If not installed, you can download Python here:
     - [Windows OS](https://www.python.org/downloads/)
     - [macOS](https://www.python.org/downloads/macos/)

_Ensure all prerequisites are met before proceeding with the exercise._


## Objective

The objective of this practice task is to complete the `Dockerfile` file to containerize the provided Python Flask Calculator API.

Provided Code Structure:
- `app.py`: This is the Python Flask Calculator API.
- `requirements.txt`: File containing list of libraries or packages which need to be installed for running the `app.py`.
- `Dockerfile`: Template file which is to be completed.

## [1/2] Step-by-Step Guide to Complete the `Dockerfile`

Open the `Dockerfile` and follow these steps to complete it:

### TODO-STEP 1: Choose a base image
- Replace `<BASE_IMAGE>` with an appropriate Python base image (e.g., `python:3.9-slim`).

    _Official Python images available on [DockerHub Here](https://hub.docker.com/_/python)._

### TODO-STEP 2: Create a dedicated working directory for our application
- Replace `<WORKING_DIRECTORY>` with a appropriate folder name (e.g., `/app`)

### TODO-STEP 3: Copy the dependencies (requirements) file into the container
- Replace `<SOURCE>` with `requirements.txt`
- Replace `<DESTINATION>` based on the folder name set in STEP-2 (e.g.,`requirements.txt`)

### TODO-STEP 4: Install the Python dependencies
- Replace `<COMMAND_TO_INSTALL_DEPENDENCIES>` with `pip install -r requirements.txt`

### TODO-STEP 5: Copy the application code `app.py`
- Apply the same principle as STEP-3 for `app.py` in this step.

### TODO-STEP 6: Specify the command to run the application
- Replace `<COMMAND_TO_RUN_APP>` with `["python", "app.py"]`

> **TIP**: If there is any confusion between `RUN`, `CMD`, and `ENTRYPOINT` commands then refer to these helpful resources:
> - [Docker best practices in choosing between RUN, CMD, ENTRYPOINT ](https://www.docker.com/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/)
> - [Stack Overflow: Difference Between RUN, CMD, ENTRYPOINT](https://stackoverflow.com/questions/37461868/difference-between-run-and-cmd-in-a-dockerfile)

> ## Important Notes
> - Make sure to remove the `<` and `>` symbols when replacing the placeholders.
> - Double-check your indentation and syntax.


## [2/2] Building and Running the Docker Container

After completing the above `Dockerfile` steps:

1. **Open a terminal** in the directory containing your `Dockerfile` and application files (in our case `app.py`).

2. To **build a Docker image**, use the following syntax: 
    ```bash
    docker build -t <IMAGE_NAME> .
    ```
    - `<IMAGE_NAME>`: Replace this with a valid name for the image.
    - `.` at the end of the command specifies the "build context" to be the "current directory". _(i.e. build our Dockerfile present in the current directory)_

    _For example_, to build an image named "calculator-api":
    ```bash
    docker build -t calculator-api .
    ```

3. To **run a Docker container**, use the following syntax:
    ```
    docker run -p <HOST_PORT>:<CONTAINER_PORT> <IMAGE_NAME>
    ```
    - The above command starts running the container, and maps port on which the application which runs inside the container to the port on the local host machine.
    - `<HOST_PORT>`: The port on the local host machine.
    - `<CONTAINER_PORT>`: The port inside the Docker container.
    - `<IMAGE_NAME>`: The name of the image you built.

    _For example_, execute the following command to run the "calculator-api" container image:

        ```bash
        docker run -p 5000:6000 calculator-api
        ```
    - This command:
        1. Starts running a container from the "calculator-api" image
        2. Maps port 6000 in the container (this is the port on which the calculator api `app.py` runs) **to** port 5000 of the host machine (this is the port on which we can call the API to reach our application).

    - For more information on these commands, refer to the Docker documentation:
        - [`docker run` documentation](https://docs.docker.com/engine/containers/run/)
        - [`-p` flag documentation](https://docs.docker.com/engine/containers/run/#exposed-ports)

4. **Testing the Application**: Use a tool like cURL or Postman to test the API endpoints:
    - Test endpoint: `GET http://localhost:5000/api/test`
    
        (_This endpoint can be tested on the browser visit: [http://localhost:5000/api/test](http://localhost:5000/api/test)_)

    - Addition endpoint: `POST http://localhost:5000/api/add`
        ```json
        {
            "number_1": 5,
            "number_2": 3
        }
        ```

5. **Stopping the Container**: Press `Ctrl+C` in the terminal where the container is running to stop it.

> Congratulations! You've successfully containerized your Python Calculator API using Docker.

> **SOLUTION:** The solution for the above tasks can be found in the file [`Answer/Dockerfile`](https://github.com/shiftkey-labs/DevOps-Foundations-Course/blob/master/Week%202/Docker%20Practice/Answer/Dockerfile).
It is highly recommended that you attempt to complete the exercise independently before reviewing the solution, as this will enhance your learning experience. If you encounter any difficulties, feel free to consult the solution for guidance.

## Additional Topics and Further Practice

1. **Environment Variables**: Modify the Dockerfile to use an environment variable for configuring the port number on which the application runs. _For example_:
 
    - Use the `ENV` instruction in your Dockerfile to set a default port, and update the `CMD` instruction to use this environment variable.
        - In Dockerfile use `ENV PORT=5000` and then use `CMD ["python", "app.py", "--port", "$PORT"]`
    - Learn more: [Docker ENV instruction](https://docs.docker.com/reference/dockerfile/#env)

2. **Multi-stage Build**: Create a Dockerfile with separate stages for 'building' and 'testing' the application. To achieve this:
    - Use multiple `FROM` statements to define different stages.
    - Create a stage for installing dependencies and running tests.
    - Copy only necessary files to the final stage.
    - Learn more: [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

3. **Docker Compose**: Create a `docker-compose.yml` file to run your application along with multiple other services (e.g., your backend application and a database). 
    - Learn more: [Docker compose overview](https://docs.docker.com/compose/)

4. **Health Checks**: Implement a health check in the `Dockerfile` to ensure the application is running correctly. To achieve this:
    - Create a simple endpoint in the application for health checks.
    - Use the `HEALTHCHECK` instruction in the Dockerfile.
    - Configure the check interval, timeout, and retries.
    - _For example:_
    ```Dockerfile
    HEALTHCHECK --interval=5m --timeout=3s \
        CMD curl -f http://localhost:5000/health || exit 1
    ```
    - Learn more: [Docker HEALTHCHECK ](https://docs.docker.com/reference/dockerfile/#healthcheck)

5. **Custom Network**: Explore Docker networking (`docker network create`) to create a custom network. 
    - Learn more: [Docker networking guide](https://docs.docker.com/engine/network/)

Remember to explore the Docker documentation for more advanced features and best practices!


## Conclusion

Congratulations! You have successfully containerized a Python Flask API using Docker. This exercise introduced you to key Docker concepts and practices. Continue exploring Docker's documentation and experiment with more complex configurations to deepen your understanding.

All the best, and happy learning!

---