# MedEase - Online Telemedicine Application

## Prerequisites
- Docker installed on your machine. If not installed, you can download and install it from [Docker's official website](https://www.docker.com/get-started).

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sidhu2003/medease-devops
   cd medease-devops
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t medease .
   ```

3. **Run the Docker container:**
   ```bash
   docker run -d -p 8000:8000 medease
   ```

   Replace `8000:8000` with the desired port mapping if you want to run the Django server on a different port.

4. **Access the medease application:**
   Once the Docker container is running, you can access the Django application by navigating to `http://localhost:8000` in your web browser.
