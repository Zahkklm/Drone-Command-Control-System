# Commands Service — README

This microservice is responsible for issuing, tracking, and managing drone commands and missions in the Drone Command & Control System (DCCS) platform. It exposes a secure API for operators and other services to create, update, and monitor commands sent to drones.

---

## Purpose

- **Central Command Management:**  
  Acts as the single source of truth for all drone commands and mission plans.
- **Secure Command Issuance:**  
  Only authenticated and authorized users (e.g., operators, admins) can issue or modify commands.
- **Integration Point:**  
  Interfaces with telemetry, dashboard, and authentication services for full workflow support.

---

## Planned Features

- **Command Model:**  
  Store command details (type, parameters, status, timestamps, target drone, issued by, etc.).
- **Mission Plan Model:**  
  Support for multi-step or scheduled missions.
- **REST API:**  
  CRUD endpoints for commands and missions, secured with JWT authentication.
- **Role-Based Access:**  
  Only users with appropriate roles (from JWT) can issue or modify commands.
- **Command Status Tracking:**  
  Track command execution status (pending, sent, acknowledged, completed, failed).
- **Audit Logging:**  
  Log all command actions for traceability and compliance.
- **Admin Interface:**  
  Django admin for manual review and management.
- **API Documentation:**  
  Swagger/OpenAPI docs for all endpoints.
- **Testing:**  
  Automated tests for all models and endpoints.

---

## Security & Integration

- **JWT Authentication:**  
  All endpoints require a valid JWT token issued by the Authentication Service.
- **Role Enforcement:**  
  The user's role (from the JWT) is checked for each action.
- **Service-to-Service Security:**  
  Internal APIs can be protected with service tokens or mTLS if needed.
- **Audit Trail:**  
  All command actions are logged for security and troubleshooting.

---

## API Endpoints

- `POST /api/commands/` — Issue a new command (operator/admin only)
- `GET /api/commands/` — List all commands (filtered by user/role)
- `GET /api/commands/{id}/` — Get command details
- `PATCH /api/commands/{id}/` — Update command status (system or admin)
- `POST /api/missions/` — Create a new mission plan
- `GET /api/missions/` — List all mission plans

---

## TODO

- Integrate with Telemetry Service for real-time command feedback.
- Add Celery for async command scheduling and retries.
- Implement fine-grained permissions (e.g., per-drone access).
- Add API rate limiting and monitoring.
- Harden security for production (HTTPS, CORS, etc.).

---

## Usage

- All endpoints are under `/api/` and require JWT authentication.
- Use the Swagger docs (`/swagger/`) for interactive API exploration.

---

**This service is the authoritative source for all drone command and mission activity in the DCCS microservices ecosystem.**