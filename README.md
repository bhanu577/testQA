## Requirements

- Python 3.9 or later
- `requests` library (pip install requests)
- `unittest` (included in Python standard library)
- minikube (to be installed in the local system that creates a virtual nodes)
- docker

## Steps to Run

- start minikube and then run backend.yml and frontend.yml deployment files so that the pod serives will be up and running for our testing
- now list down the serives with "kubectl get services"
- now get the URL's by running the below command minikube service <<backendserive>> -n default , minikube service <<frontendserive>> -n default
- now in the python file replace the replace backend url in backend variables and frontend url with frontend variables
- trying executing python3 main.py