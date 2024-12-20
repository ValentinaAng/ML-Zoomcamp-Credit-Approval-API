# ML ZOOMCAMP PROJECT

## Project Name

**Credit Approval Classification Project**

![Project Image](https://www.indostarhfc.com/images/blogs/The-Role-of-Credit-Score-in-Home-Construction-Loan-Approval.jpg)

__________

## Project Description:  
This dataset provides information that helps us identify patterns and develop a model to determine whether a credit application will be approved.   
In this project we are using FastAPI application that includes an endpoint which accepts a InputData model and returns the prediction.
 - **API Endpoint:** `prediction/`

## Table of Contents

- [ML ZOOMCAMP PROJECT](#ml-zoomcamp-project)
  - [Project Name](#project-name)
  - [Project Description:](#project-description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [Usage](#usage)
    - [Running the Project](#running-the-project)
    - [Test App](#test-app)
  - [Deployment to AWS Instructions](#deployment-to-aws-instructions)
  - [Components](#components)
    - [Main Application Files](#main-application-files)
    - [Tests](#tests)
    - [Data](#data)
    - [Models](#models)
    - [Notebooks](#notebooks)
    - [Other Key Files](#other-key-files)

## Installation

To get started with the project, you need to set up the environment and install the required dependencies.

### Prerequisites

- **Python** 3.12
- **Docker** - To containerize the application and deploy it to AWS Beanstalk.
- **AWS CLI** - For interacting with AWS install AWS CLI
- **Git** (optional, if cloning the repository)
- **Task**: To run tasks listed in the Taskfile

For instructions on how to install Task, please refer to the official guide: [Task Installation](https://taskfile.dev/installation/)
  
### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ValentinaAng/ML-Zoomcamp
    cd your-repository
    ```

2. **Install dependencies using Poetry:**

    If you haven't installed Poetry, you can follow the installation guide on the [Poetry website](https://python-poetry.org/docs/#installation).

    ```bash
    poetry install
    ```

3. **Activate the virtual environment:**

    ```bash
    poetry shell
    ```
## Usage

### Running the Project

After setting up the environment, you can run the project by executing the following command in the terminal:

```bash
python main.py
```

### Test App

You can test the application using tools like Postman or Thunder Client. Alternatively, you can visit http://localhost:8000/docs to access the automatically generated API documentation. This interface allows you to interact with the API endpoints directly in your browser.

Test data is provided in the `tests/data/test_data.json` file. You can copy the data from this file and use it with any of the mentioned testing approaches.


## Deployment to AWS Instructions

1. **Create AWS Account** 
2. **Manage IAM user permissions**
3. **Install AWS CLI** - Installation link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
4. **Configure the AWS CLI** - using command: `aws configure`
5. (Optionally) **You can use the commands defined in Taskfile and run them in the terminal**
   
**Deploy using Taskfile** 
  - To run tasks separately, use the following command: `task <task_name>`. Additionally, it can be used to run all three tasks at the same time, with the following command: `task full_deploy`
  
The file will:
 - Build Docker image
 - (Optionally you can push the image to the ECR)
 - Initialize Elastic Beanstalk Application
 - Create environment if it doesn't exists
 - Deploy 
 

## Components

The application consists of the following components:

### Main Application Files
- **main.py**: The entry point for the FastAPI app. It initializes the app and includes routes and other application-wide configurations.
- **config/**: Directory containing configuration files for the application.
  - **logging_config.py**: Configures structured logging using `structlog` to capture detailed logs for monitoring and debugging.
- **routers/routers.py**: Contains the application’s route definitions.
- **schemas/**: Directory containing Pydantic models used for input validation and output formatting.
  - **input.py**: Contains models to validate the data coming from the client (e.g., POST requests).
  - **output.py**: Defines models for structuring the response data returned by the API.
- **services/**: Contains logic and functionalities that handle application operations outside of the routes.
  - **latest_model.py**: Includes the logic for loading and using the latest trained model for making predictions.
  - **status_response.py**: Defines the status of prediction (e.g., 0 Approved, 1 Not Approved).

### Tests
- **tests/**: Contains unit tests for the application logic and API routes.
  - **test_main.py**: The main test suite for testing the API routes, responses
  - **data/**
      - **test_data.json**: Test Data

### Data
- **data/**: Contains unprocessed and processed data
    - **dataset-credit.csv**: Raw data
    - **data_cleaned.csv**: Processed data
  
### Models
- **models/**: Contains train script and best model saved
    - **train.py**: Script that contains data loading, data splitting, data preprocessing and model training functions
    - **best_model_v1.0.pkl**: Best model saved
    - **version.txt**: Latest saved model version
  
### Notebooks
- **notebooks/**: Python notebook
    - **CreditApprovalClassification.ipynb**: This notebook contains full code from data analysis, data preprocessing, eda, data cleaning, hyperparameter optimization, training and saving the best model.


### Other Key Files
- **Dockerfile**: Defines the Docker container to package and run the application in any environment.
- **pyproject.toml**: A configuration file for the Python project, listing dependencies and setup tools.
- **poetry.lock**: Lock file for Python dependencies, ensuring consistent package installations across different environments.
- **ruff.toml**: Configuration file for the `ruff` linter, used for maintaining code quality and enforcing style rules.
- **Taskfile**: Defines tasks to automate common project activities (so far used for building and deploying docker images).
