# GitLab CI/CD Exercise: Python Project

In this exercise you will create and run your first CI/CD pipeline on GitLab. You will learn how to configure a simple pipeline and how to run it, and also explore some advanced features of GitLab CI/CD.


## Prerequisites

Before starting this exercise, ensure you have:

1. A GitLab account
   - If you do not have one, you can sign up at [GitLab.com](https://gitlab.com/users/sign_up)

2. `Git` installed on your local machine
   - To test if it is installed, open your Command Line Terminal and run:
     ```
     git --version
     ```
   - If not installed, download it from [git-scm.com](  )

3. `Python` installed on your local machine _(Python 3.7 or higher recommended)_
   - To test if it is installed, open your Command Line Terminal and run:
     ```
     python --version
     ```
     or
     ```
     python3 --version
     ```
   - If not installed, you can download Python here:
     - Windows OS: https://www.python.org/downloads/
     - macOS: https://www.python.org/downloads/macos/

_Ensure all prerequisites are met before proceeding with the exercise._


## Objective

Your task is to complete the `.gitlab-ci.yml` file to create a working CI/CD pipeline with two stages: `build` and `test`.

## Brief Instructions Overview  

1. Clone this repository on your local machine.
2. Create a empty repository on your **GitLab account**.
3. Copy the content of this repository into the new empty repository created in GitLab.
4. Open the `.gitlab-ci.yml` file preset in `Week 1/` folder in your preferred text editor.
5. Follow the **TODO** steps in the `.gitlab-ci.yml` file to complete the configuration.

## [1/2] Step-by-Step Guide to complete the `.gitlab-ci.yml` file

Follow this steps to complete the gitlab-ci yaml file:

### TODO-STEP 1: Define the Stages
- Uncomment the `stages:` section.
- Replace `<STAGE_NAME>` with `build` for the first stage and `test` for the second stage.

### TODO-STEP 2: Create the "Build" Stage
- Uncomment the `<JOB_NAME>:` line and replace `<JOB_NAME>` with a descriptive name (e.g., `build_job`).
- For TODO-STEP 2a, uncomment the `stage:` line and replace `<STAGE_NAME>` with `build`.
- For TODO-STEP 2b, uncomment the `pip install` line and replace `<FILE_NAME>` with `requirements`.

### TODO-STEP 3: Create the "Test" Stage
- Uncomment the `<JOB_NAME>:` line and replace `<JOB_NAME>` with a descriptive name (e.g., `test_job`).
- For TODO-STEP 3a, uncomment the `stage:` line and replace `<STAGE_NAME>` with `test`.
- For TODO-STEP 3b, uncomment the command line and replace `<COMMAND_TO_RUN_TESTS>` with `pytest`.

> ## Important Notes
> - Do not change the `image: python:3.9` line in either job.
> - Remember to remove the `#` symbol to uncomment lines when replacing content in the placeholders.
> - Make sure your indentation is correct. YAML is sensitive to indentation.

## [2/2] Executing the CI/CD Pipeline on GitLab

After completing the `.gitlab-ci.yml` file:
1. Commit your changes in your local machine.
2. Push the changes to your GitLab repository.
3. Go to your project on GitLab and navigate to `"Build"` > `"Pipelines"` to see your pipeline running.
    - If you visit `"Build"` > `"Pipeline Editor"`, here you will find the `.gitlab-ci.yml` file. 
    You can edit and make changes to this file and click `"Commit changes"` to see effects of your changes. 
4. Debug any issues that arise and make necessary adjustments to your `.gitlab-ci.yml` file.
5. Once your pipeline run is successful, try making changes to the backend code and pushing the changes to see any changes in pipeline execution or logs.
6. Explore more options of the `.gitlab-ci.yml` configuration, the GitLab CI/CD interface, including job logs and pipeline graphs.

> _Wohoo! You have successfully run your first CI/CD pipeline on GitLab._ 

## Additional Practice Tasks and Challenges

### Basic Tasks: 

1. **Conditional Job Execution:** Implement a job that only runs when changes are made to specific files or directories:
     - **HINT:** Use the `changes` keyword in the `rules` section to run a job only when changes are made to Python files (`*.py`).

2. **Manual Job Execution:** Create a job that requires manual intervention to start the execution of the CI/CD pipeline. 
    - **HINT:** Use the `when: manual` keyword.

3. **Use Variables:** Create a job that uses a custom environment variable, and set its value using the GitLab CI/CD variables feature in the project settings.
    - **HINT:** Refer to `variables` to define CI/CD variables for jobs ([Click Here](https://docs.gitlab.com/ee/ci/yaml/#variables)).


> **NOTE:** A GitLab YAML config with examples for the above tasks will be available on 8th November EOD.

## (OPTIONAL) Explore Intermediate-level challenges:

- **Execute pipeline only in specific branches:** Set up a job that **runs only on specific branches**:
    - Create a job that runs only on the `development` branch using the `$CI_COMMIT_BRANCH` variable.

- **Using Includes:** Create a separate YAML file for test jobs and include it in your main `.gitlab-ci.yml` file.
    - **HINT:** Refer to `include` to split your CI/CD configuration in mutliple files. For more details ([Click Here](https://docs.gitlab.com/ee/ci/yaml/#include)).

- **Create Job Dependencies using needs:** Create a job that depends on the successful completion of another job. 
    - **HINT:** Refer to `needs` by visiting ([Click Here](https://docs.gitlab.com/ee/ci/yaml/#needs)).

- **Parallel Jobs:** Create multiple test jobs that run in parallel to speed up your pipeline.
    - **HINT:** Refer to `parallel` by visiting ([Click Here](https://docs.gitlab.com/ee/ci/yaml/#parallel)).

- **Caching Dependencies:** Implement caching for pip dependencies to speed up subsequent pipeline runs.
    - **HINT:** Refer to `cache` by visiting ([Click Here](https://docs.gitlab.com/ee/ci/yaml/#cache)).

- **Create a Docker Image Job:** Create a job in the `.gitlab-ci.yml` file which builds a Docker image of your Python application and pushes it to DockerHub.

- **Jobs with Artifacts:** Create a job with artifacts by generating a test coverage report and save it as an artifact that can be downloaded after the pipeline completes.

## Some Helpful Links:

- CI/CD YAML syntax reference guide:  https://docs.gitlab.com/ee/ci/yaml/
- Tutorial: Create and run your first GitLab CI/CD pipeline:  https://docs.gitlab.com/ee/ci/quick_start/

## Conclusion

Congratulations! You have finished this exercise of GitLab CI/CD. With this you have learned how to create a basic pipeline, execute the pipeline, and also learn about many more advanced features of the yaml configuration. Continue to explore and read further in the GitLab's documentation to learn more about the best practices and advanced CI/CD configurations.

All the best, and happy learning!

<hr>