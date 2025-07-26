# Linked List API with Containerized Deployment on AWS

A containerized RESTful API that allows users to perform CRUD operations on a simple Linked List.

This project is designed to showcase the implementation of linked lists and deployment of containerized app on AWS.

## :rocket: Tech Stack
- **Backend :** FastAPI - a modern, high-performance, web framework for building the REST API with Python
- **Containerization :** Docker
- **Deployment :** AWS Elastic Container Service (ECS)
- **Infrasturcture as Code :** AWS Cloud Development Kit (CDK)
- **Container Orchestration :** ECS Fargate

## :hammer_and_wrench: Installation

- To get started, clone this repository to your local machine :

```bash
git clone https://github.com/aparnapwr/LinkedListAPI
cd linked-list-api
```

- Setup the virtual environment :

```bash
python -m venv venv
source venv/bin/activate  #For Linux/macOS
```

- Install the dependencies :

```bash
pip install -r requirements.txt
```

- Run the application locally :

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI app locally on `http://127.0.0.1:8000`. You can access the auto-generated Swagger documentation at `http://127.0.0.1:8000/docs`

## :cloud: Deployment on AWS

  ### Prerequisites
  - AWS Account with sufficient permissions
  - AWS CLI installed and configured
  - AWS CDK installed [`npm install -g aws-cdk`]
  - AWS Environment bootstrapped [`cdk bootstrap aws://<ACCOUNT-NUMBER>/<REGION>`]

If you have met the above prerequisites, you can deploy the project by running the following commands:

```bash
cdk synth
cdk deploy
```
  
This will:
- Build and push the Docker image to Amazon Elastic Container Registry (ECR)
- Deploy the FastAPI app to ECS Fargate
- Set up an Application Load Balancer for external access

_NOTE: The Load Balancer construct in CDK is configured to allow traffic from "anywhere" [`(0.0.0.0/0)`] on the security group._

## :iphone: Accessing the Application

After successful deployment of the AWS CloudFormation Stack, you can access the API via the ALB (Application Load Balancer) URL, provided by the CDK output:
`http://<your-load-balancer-dns>/docs`

## :fire: API Endpoints

- **GET** `/`

  Returns a welcome message (`Linked List API is running`)

- **POST** `/node/{value}`

  Creates a new node at end of the linked list.

  **Request body**: `{ "value" : "some_value" }`

- **GET** `/node`

  Retrieve the current linked list.

- **DELETE** `/node/{position}`

  Deletes the node at specified position.

The API has full Swagger UI integration, accessible at `/docs`.
  
