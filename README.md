# Just Eat Greeting Service

Lightweight FastAPI app that returns a random greeting and a visitor counter.

Files:
- [app.py](app.py) (contains `[`load_languages`](app.py)` function)
- [languages.txt](languages.txt)
- [requirements.txt](requirements.txt)
- [Dockerfile](Dockerfile)
- Terraform environments:
  - [infrastructure/environments/dev/main.tf](infrastructure/environments/dev/main.tf)
  - [infrastructure/environments/dev/terraform.tfvars](infrastructure/environments/dev/terraform.tfvars)
  - [infrastructure/environments/dev/variables.tf](infrastructure/environments/dev/variables.tf)
  - [infrastructure/environments/prod/main.tf](infrastructure/environments/prod/main.tf)
  - [infrastructure/environments/prod/terraform.tfvars](infrastructure/environments/prod/terraform.tfvars)
  - [infrastructure/environments/prod/variables.tf](infrastructure/environments/prod/variables.tf)
  - Backend example: [infrastructure/backend.hcl.example](infrastructure/backend.hcl.example)
  - Modules: [infrastructure/modules/network/main.tf](infrastructure/modules/network/main.tf), [infrastructure/modules/compute-instance/main.tf](infrastructure/modules/compute-instance/main.tf)

Prerequisites
- Python 3.12+
- pip
- (Optional) Docker
- (Optional) Terraform

Validate the application

1. Install deps
```sh
pip install -r requirements.txt
```

2. Run locally
```sh
uvicorn app:app --host 0.0.0.0 --port 8080
```

3. Smoke tests
```sh
curl http://localhost:8080/health
curl http://localhost:8080
```

Validate container (optional)

1. Build and run
```sh
docker build -t just-eat-greeting-app .
docker run -p 8080:8080 just-eat-greeting-app
```

2. Smoke tests (after container is running)
```sh
curl http://localhost:8080/health
curl http://localhost:8080
```

Validate Terraform (local backend)

Dev
```sh
cd infrastructure/environments/dev
terraform init
terraform fmt -check -recursive
terraform validate
terraform plan -var-file=terraform.tfvars
```

Prod
```sh
cd infrastructure/environments/prod
terraform init
terraform fmt -check -recursive
terraform validate
terraform plan -var-file=terraform.tfvars
```

Notes
- The app reads greetings from [languages.txt](languages.txt) using `load_languages` in [app.py](app.py).
- The Docker image runs Gunicorn with Uvicorn workers as defined in [Dockerfile](Dockerfile).
- Terraform uses a local backend by default in the environment main.tf files; replace with remote backend per your infrastructure requirements (see [infrastructure/backend.hcl.example](infrastructure/backend.hcl.example)).