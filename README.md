# MedEase - Online Telemedicine Application

## MedEase Architecture - MULTI TIER
![a1ac85c7906e3e76a4a46df6e974942a.png](https://imgtr.ee/images/2024/04/19/a1ac85c7906e3e76a4a46df6e974942a.png)

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
   docker-compose -f docker-compose-production.yml up -d
   ```

3. **Bring down the Docker container:**
   ```bash
   docker-compose -f docker-compose-production.yml down
   ```

   Replace `8000:8000` with the desired port mapping if you want to run the Django server on a different port.

4. **Access the medease application:**
   Once the Docker container is running, you can access the Django application by navigating to `http://localhost` in your web browser.

   ## Local Dev Environment Setup

   1. **Clone the repository:**
   ```bash
   git clone https://github.com/sidhu2003/medease-devops
   cd medease-devops
   ```

2. **Bring up the Docker container:**
   ```bash
   docker-compose -f docker-compose-development.yml up -d
   ```

3. **Bring down the Docker container:**
   ```bash
   docker-compose -f docker-compose-development.yml down
   ```
   4. **Access the medease application:**
   Once the Docker container is running, you can access the Django application by navigating to `http://localhost:8000` in your web browser.
