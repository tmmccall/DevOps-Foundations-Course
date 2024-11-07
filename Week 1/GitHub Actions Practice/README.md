# GitHub Actions CI/CD Exercise: Python Backend Project

In this exercise, you will create and run your first CI/CD pipeline on GitHub Actions. You will learn how to configure a simple pipeline and how to run it, and also explore some advanced features of GitHub Actions.

## Some Helpful Links:

- **(Must Read)** Understanding GitHub Actions: https://docs.github.com/en/actions/about-github-actions/understanding-github-actions
- GitHub Actions syntax reference guide: https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions
- Tutorial: Create a GitHub Actions workflow: https://docs.github.com/en/actions/quickstart
- More Information about GitHub-hosted runners: 
    - Public Repositories: ([Click Here](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners#standard-github-hosted-runners-for-public-repositories)) 
    - Private Repositories ([Click Here](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners#standard-github-hosted-runners-for--private-repositories))

- How to use the checkout action in GitHub Actions: ([Click Here](https://graphite.dev/guides/github-actions-checkout))

## Prerequisites

Before starting this exercise, ensure you have:

1. A GitHub account
   - If you do not have one, you can sign up at [GitHub.com](https://github.com/join)

2. `Git` installed on your local machine
   - To test if it's installed, open your Command Line Terminal and run:
     ```
     git --version
     ```
   - If not installed, download it from [git-scm.com](https://git-scm.com/downloads)

3. `Python` installed on your local machine _(Python 3.7 or higher recommended)_
   - To test if it's installed, open your Command Line Terminal and run:
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

Your task is to complete the `.github/workflows/github-ci.yml` file to create a working CI/CD pipeline with two jobs: `build` and `test`.

## Brief Instructions Overview  

1. Fork this repository on your GitHub account.
2. Clone this forked repository on your **GitHub account** to local, 
    **OR** 
    You can edit the `.github/workflows/github-ci.yml` file on the browser version of GitHub.
3. Open the `.github/workflows/github-ci.yml` file in your preferred text editor.
4. Follow the **TODO** steps in the `github-ci.yml` file to complete the configuration.

## [1/2] Step-by-Step Guide to complete the `github-ci.yml` file

Follow these steps to complete the GitHub Actions workflow file:

### TODO-STEP 1: Define the Workflow Name
- Uncomment the `name:` line and replace `<WORKFLOW NAME>` with a descriptive name for your workflow (e.g., Python CI/CD Pipeline).

### TODO-STEP 2: Define the Trigger Events
- Uncomment the `on:` section and the `push:` and `pull_request:` lines to trigger the workflow on push and pull request events.

### TODO-STEP 3: Create the "Build" Job
- Uncomment the `<ENTER JOB NAME 1>:` line and replace it with a suitable job name (e.g., build).
- For TODO-STEP 3a, uncomment the `runs-on:` line.
- For TODO-STEP 3b, enter a name for your step to display on GitHub (e.g., Install dependencies).
- For TODO-STEP 3c, add commands to install dependencies, replacing `<FILE NAME>` with `requirements`.

### TODO-STEP 4: Create the "Test" Job
- Uncomment the `<ENTER JOB NAME 2>:` line and replace it with a suitable job name (e.g., test).
- For TODO-STEP 4a, uncomment the `needs:` line and replace `<ENTER JOB NAME 1>` with the name you used for the first job.
- For TODO-STEP 4b, uncomment the `Install dependencies` step.
- For TODO-STEP 4c, uncomment the `Run tests` step.

> ## Important Notes
> - Make sure to keep the `uses: actions/setup-python@v2` and `uses: actions/checkout@v2` steps as is.
> - Remember to remove the `#` symbol to uncomment lines when replacing content in the placeholders.
> - Make sure your indentation is correct. YAML is sensitive to indentation.

## [2/2] Executing the CI/CD Pipeline on GitHub Actions

After completing the `github-ci.yml` file:
1. Commit your changes in your local machine.
2. Push the changes to your GitHub repository.
3. Go to your project on GitHub and navigate to the `"Actions"` tab to see your workflow running.
4. Debug any issues that arise and make necessary adjustments to your `github-ci.yml` file.
5. Once your workflow run is successful, try making changes to the backend code and pushing the changes to see any changes in workflow execution or logs.
6. Explore more options of the GitHub Actions configuration, including job logs and workflow visualizations.

> _Wohoo! You have successfully run your first CI/CD pipeline on GitHub Actions._ 

## Additional Practice Tasks and Challenges

### Basic Tasks: 

1. **Conditional Job Execution:** Implement a job that only runs when changes are made to specific files or directories:
     - **HINT:** Use the `paths` keyword in the `on` section to run a job only when changes are made to Python files (`'**.py'`). For more details ([Click Here](paths)).

2. **Manual Workflow Dispatch:** Create a workflow that can be triggered manually from the GitHub Actions UI.
    - **HINT:** Use the `workflow_dispatch` event trigger. For more details ([Click Here](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatch)).

3. **Use Environment Variables:** Create a job that uses a custom environment variable, and set its value using GitHub Secrets.
    - **HINT:** Use `env` to define environment variables and `${{ secrets.SECRET_NAME }}` to access GitHub Secrets. 
        - [env](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#env)
        - [jobs.<job_id>.steps[*].env](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsenv)
        - [jobs.<job_id>.container.env](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idcontainerenv)

> **NOTE:** A GitHub Actions workflow with examples for the above tasks will be available on 8th November EOD.

## (OPTIONAL) Explore Intermediate-level challenges:

- **Execute workflow only on specific branches:** Set up a job that runs only on specific branches: i.e. Create a job that runs only on the `development` branch using the `branches` keyword under the `on` section.
    - **HINT:** Refer `on` for more details ([Click Here](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onpull_requestpull_request_targetbranchesbranches-ignore))

- **Create Job Dependencies:** Create a job that depends on the successful completion of another job. 
    - **HINT:** Use the `needs` keyword to specify job dependencies. For more details ([Click Here](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds))

- **Matrix Strategy:** Create a test job that runs on multiple Python versions using a matrix strategy.
    - **HINT:** Use the `strategy` and `matrix` keywords to define multiple Python versions. For more details ([Click Here](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategy))

- **Caching Dependencies:** Implement caching for pip dependencies to speed up subsequent workflow runs.
    - **HINT:** Use the `actions/cache` action to cache pip dependencies. For more details:
        - ([Click Here - github.com/actions/cache](https://github.com/actions/cache))
        - ([Click Here - documentation](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows#using-the-cache-action))

- **Create a Docker Image Job:** Create a job in the workflow file which builds a Docker image of your Python application and pushes it to DockerHub.

- **Jobs with Artifacts:** Create a job that generates a test coverage report and saves it as an artifact that can be downloaded after the workflow completes.

## Conclusion

Congratulations! You have completed this exercise in GitHub Actions. You have learned how to create a basic workflow, run the workflow, and also about many other advanced features of the YAML configuration. Continue to explore and read further in GitHub's documentation to learn more about the best practices and advanced CI/CD configurations.

All the best, and happy learning!

<hr>