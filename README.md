# num_to_english
Django app to convert numbers to string English representations


## To Run

### Setup for Development
Generate a Django secret key and set your local environment.
1. Run `python num_to_english/scripts/create_dev_django_secret_key.py`
2. Copy the secret key
3. Run `export DJANGO_SECRET_KEY='<PASTE_SECRET_KEY>'` with quotations in terminal or set in bashrc/zshrc.

### Run Steps
- Run unit tests: `python num_to_english/scripts/build.py && python num_to_english/scripts/run_unit_tests.py`
- Run dev server: `python num_to_english/scripts/build.py && python num_to_english/scripts/run_dev.py`


## Features Backlog
- Git Hooks
- Integration Testing
- Clarify Error Handling
- Monitoring
- API Documentation (Swagger, DRF)
- Security (enable https, reverse proxy like Nginx or Apache to handle SSL termination)
- Kubernetes for scaling
