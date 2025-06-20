# TODO for commands_service

## Implemented

- Command and MissionPlan models
- JWT authentication and role-based permissions
- CRUD API endpoints for commands and missions
- Admin registration for models
- PostgreSQL database configuration
- CORS enabled for development
- Swagger/OpenAPI documentation (`/swagger/`, `/redoc/`)

---

## Improvements & Next Steps

- [ ] **Integrate with Telemetry Service:**  
  Enable real-time command feedback and status updates.
- [ ] **Celery Integration:**  
  Add async command scheduling, retries, and background processing.
- [ ] **Fine-Grained Permissions:**  
  Implement per-drone or per-mission access control.
- [ ] **API Rate Limiting:**  
  Add DRF throttling for sensitive endpoints.
- [ ] **Audit Logging:**  
  Log all command actions for traceability and compliance.
- [ ] **Security Hardening:**  
  - Restrict CORS in production.
  - Enforce HTTPS (via Nginx or cloud provider).
- [ ] **Testing:**  
  Add automated tests for all endpoints and business logic.
- [ ] **API Versioning:**  
  Add versioning to API endpoints for future-proofing.
- [ ] **Documentation:**  
  Add usage examples and endpoint descriptions to Swagger docs.

---

## Notes

- All endpoints are JWT-protected and require a valid token from the Authentication Service.
- Only users with `operator` or `admin` roles can issue or modify commands and missions.
- This service is the authoritative source for all drone command and mission activity in the DCCS ecosystem.