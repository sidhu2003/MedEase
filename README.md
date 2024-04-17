# MedEase - Online Telemedicine Application

## Prerequisites
- Docker installed on your machine. If not installed, you can download and install it from [Docker's official website](https://www.docker.com/get-started).

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sidhu2003/medease-devops
   cd medease-devops
   ```

2. **Bring up the Docker container:**
   ```bash
   docker-compose up -d
   ```

3. **Bring down the Docker container:**
   ```bash
   docker-compose down
   ```

   Replace `8000:8000` with the desired port mapping if you want to run the Django server on a different port.

4. **Access the medease application:**
   Once the Docker container is running, you can access the Django application by navigating to `http://localhost:8000` in your web browser.

## Running Legacy Version

1. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where your Terraform configuration files are located.

2. **Initialize Terraform**: Run the following command to initialize Terraform in the directory containing your configuration files:

```bash
terraform init
```

This command initializes the current directory as a Terraform working directory and downloads any necessary plugins.

3. **Review Terraform Plan (Optional)**: You can review the execution plan to ensure that Terraform will create the resources as expected. Run:

```bash
terraform plan
```

This command shows you a summary of what Terraform will do when you apply your configuration.

4. **Apply Terraform Configuration**: If the plan looks good, apply the Terraform configuration to create the infrastructure:

```bash
terraform apply
```

Terraform will ask for confirmation before proceeding. Type `yes` and press Enter to apply the configuration.
