# Comparative Process Mining
## Setup
### Requirements
[docker-desktop](https://www.docker.com/products/docker-desktop)

### Start project
* Build the container using `docker build . -t <name>` 
* Run the container using `docker run -d -p 8000:8000 <name>`
* Visit `localhost:8000`. The project is now available.

## Project structure
````
├── cpm         Django settings
├── helpers     Help functions
├── logs        Main project
├── media       saved logs
├── static      css / js / img
├── templates   HTML templates
└── tests       (Unit) Tests
````
# Further information
* We use the [PEP-8](https://www.python.org/dev/peps/pep-0008/) coding convention.
