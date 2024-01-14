# num_to_english
Django app to convert numbers to string English representations


## To Run
Easiest way to build and run the project is using pynt. To install, do `pip install -r requirements_user.txt` in your local environment.

To use pynt commands, navigate to the directory with build.py (`cd <PROJECT_ROOT>/num_to_english`).

pynt commands:
- `pynt build`: Build the project Docker image. To capture newest code changes, run this command before any others
- `pynt run_dev`: Use Docker to run the Django server using dev settings
- `pynt run_prod`: Use Docker to run the Django server using prod settings (not currently supported)
- `pynt unit_test`: Use Docker to run the project unit tests


## Features Backlog
- Git Hooks
- Integration Testing
- Clarify Error Handling
- Monitoring
- Secret Key Environment Variable
- API Documentation (Swagger, DRF)
- Security (enable https, reverse proxy like Nginx or Apache to handle SSL termination)
- Kubernetes for scaling
