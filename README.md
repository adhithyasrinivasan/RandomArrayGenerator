# RandomArrayGenerator

FastAPI Random Array Generator
Overview
This FastAPI project provides an API endpoint for generating a random array of floats based on input sentences.

# FastAPI Random Array Generator

## Overview

This FastAPI project provides an API endpoint for generating a random array of floats based on input sentences.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/adhithyasrinivasan/RandomArrayGenerator.git
    cd RandomArrayGenerator
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - On Unix or MacOS:

      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running Unit Tests

Ensure that you have activated the virtual environment before running tests.

```bash
pytest --cov=app
```

## Starting the App

Ensure that you have activated the virtual environment before starting the app.

```bash
python runner.py --reload
```

## Sending Requests to the APIs

After starting the app, you can use tools like `curl` and `jq` or platforms like [Postman](https://www.postman.com/) to send requests to the API endpoints.

Example using `curl`:

```bash
# Get a valid token
TOKEN=$(curl -X POST "http://localhost:8010/random_array_generator/token" | jq -r .access_token)

# Send a request with a valid token
curl -X POST "http://localhost:8010/random_array_generator" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"sentence": "This is a valid sentence."}'
```

## Considerations for Production Deployment

1. **Security:**
   - Use HTTPS to encrypt communication between clients and the server.
   - Oauth based basic authentication enabled with token being required for authorized transactions.

2. **Environment Configuration:**
   - Use environment variables for sensitive information like secret keys and configuration parameters.

3. **Error Handling:**
   - Implement robust error handling to provide meaningful responses to clients.
   - Log errors and exceptions for debugging purposes.

4. **Production WSGI Server:**
   - Consider using a production-grade WSGI server (e.g., Gunicorn) for deployment.

5. **Scalability:**
   - Configure your deployment for scalability, considering load balancing and horizontal scaling.

6. **Monitoring and Logging:**
   - Implement logging for monitoring and debugging.
   - Use tools like Prometheus and Grafana for monitoring.

7. **Documentation:**
   - Generate comprehensive API documentation using tools like Swagger UI or ReDoc.

8. **Testing in Production-Like Environment:**
   - Test your application in an environment that closely resembles the production environment.

9. **Backup and Recovery:**
   - Implement backup and recovery mechanisms for critical data.

10. **Continuous Integration/Continuous Deployment (CI/CD):**
    - Set up CI/CD pipelines for automated testing and deployment.

11. **Rate Limiting:**
    - Implement rate limiting to protect against abuse and ensure fair usage.