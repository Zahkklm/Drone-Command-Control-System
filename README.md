# Drone Command & Control System (DCCS) — Microservices

A real-time, secure, and scalable platform for drone telemetry, command & control, and analytics, built as independent microservices.

## Microservices Overview

- **Telemetry Service:** Real-time drone data ingestion and processing (Django + Channels + REST/GraphQL)
- **Commands Service:** Command & mission management (Django + REST/GraphQL)
- **Authentication Service:** JWT authentication and user management (Django + DRF SimpleJWT)
- **Dashboard Service:** Operator dashboard and analytics (Django or SPA frontend)
- **(Optional) Analytics Service:** Historical data aggregation and reporting

Each service is a standalone Django project, with its own API, database, and deployment.

## Quick Start

1. **Clone the repo and review each service directory**
    ```sh
    git clone <repo-url>
    cd dccs-microservices
    ```

2. **Build and run all services with Docker Compose**
    ```sh
    docker-compose up --build
    ```

3. **Access services:**
    - Telemetry API: `http://localhost:8001/`
    - Commands API: `http://localhost:8002/`
    - Authentication API: `http://localhost:8003/`
    - Dashboard: `http://localhost:8004/`

4. **Run tests for a service**
    ```sh
    cd telemetry_service
    python manage.py test
    ```

## Repository Structure

- `/telemetry_service/` — Real-time telemetry microservice
- `/commands_service/` — Command & control microservice
- `/authentication_service/` — Auth microservice
- `/dashboard_service/` — Dashboard/analytics microservice
- `/docker-compose.yml` — Orchestrates all services
- `/k8s/` — Kubernetes manifests for production
- `/README.md` — This file
- `/BLUEPRINT.md` — Project blueprint and architecture

---

**Note:** This is a work in progress. See [BLUEPRINT.md](BLUEPRINT.md) for the full architecture and roadmap.