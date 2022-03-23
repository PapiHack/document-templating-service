# 🚀 Document Template Processing Service 🚀

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Issues](https://img.shields.io/github/issues/PapiHack/orange-sms-sender-service?style=for-the-badge&logo=appveyor)
![PR](https://img.shields.io/github/issues-pr/PapiHack/orange-sms-sender-service?style=for-the-badge&logo=appveyor)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
[![Open Source Love png](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

This is a simple and lightweight microservice that allow you to process your `Word` documents with a `templating system`, in order to hydrate it by injecting data or variables defined in it and get back its associated `PDF` result.

## Notes

For transforming the `docx` result to `PDF` you'll need have an instance of [Gotenberg](https://gotenberg.dev) up and running and provide its `ROOT URL` as an environment variable to the microservice.

## Installation

### Docker

- First and foremost you'll need to have an instance of Gotenberg. You can easily have one by running the following docker command : 

        docker run --name gotenberg -d -p 3000:3000 gotenberg/gotenberg:7


- After this step done, you have the two (2) options in order to run this service :

    - Direct run by following the steps below :

        - Rename the file `.env.example` at the root level of this project by simply `.env`

        - Set the value of the `GOTENBERG_API_URL` environment variable defined in it with yours (in our example => http://localhost:3000)

        - Install the necessary dependencies by running :
        
                pip install -r requirements.txt (you can create virtual env if you want it)

        - Start the microservice by running:
                
                 uvicorn main:app

        - Visit the `API Documentation` at <http://localhost:8000/docs> or <http://localhost:8000/redoc>

    - Using docker to build and launch a container :

        - In your terminal, at the root of this project, build an image of this service by running : 
        
                docker build -t document-template-processing-service .

        - Start the service by creating a container with : 
        
                docker run -d -p 8000:8000 -e GOTENBERG_API_URL=your-host-ip:3000 --name dtps document-template-processing-service

        - Visit the `API Documentation` at <http://localhost:8000/docs> or <http://localhost:8000/redoc>

### With Docker Compose



## Usage

For now you have an endpoint named `/api/v1/process-template-document` that will allow you to make a `POST HTTP REQUEST` by sending two (2) required parameters :

- The `file` parameter that contains your `Word Document Template`

- The `data` parameter that is a `JSON` object with data or variable that we are going to inject in the `file` parameter

As a response, you'll get back its corresponding `PDF` file as a result.

### Screenshots

![screenshot](./screenshots/swagger-doc.png)

## Contributing

Feel free to make a PR or report an issue 😃

Oh, one more thing, please do not forget to put a description when you make your PR 🙂