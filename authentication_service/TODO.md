# TODO for authentication_service

## Implemented

- JWT authentication endpoints (`/api/token/`, `/api/token/refresh/`)
- User registration with role selection (`/api/register/`)
- User profile endpoint (`/api/profile/`)
- Password change endpoint (`/api/password/change/`)
- Password reset request and confirmation endpoints
- Admin-only user listing endpoint
- PostgreSQL database configuration
- CORS enabled for development
- User roles via `UserProfile` model
- Custom JWT claims (role included in token)
- Swagger/OpenAPI documentation (`/swagger/`, `/redoc/`)
- Basic automated tests for registration, login, and profile

---

## Improvements & Next Steps

- [ ] **Production Email Backend:**  
  Configure a real SMTP backend for password reset emails.
- [ ] **Restrict CORS in Production:**  
  Set `CORS_ALLOW_ALL_ORIGINS = False` and specify allowed origins.
- [ ] **API Rate Limiting:**  
  Add DRF throttling for sensitive endpoints (registration, login, password reset).
- [ ] **Audit Logging:**  
  Log authentication attempts, password changes, and resets for security monitoring.
- [ ] **User Email Verification:**  
  Add email verification after registration.
- [ ] **User Management Enhancements:**  
  - Add endpoints for updating user info (admin/self-service).
  - Add user deactivation or deletion endpoints (admin only).
- [ ] **API Versioning:**  
  Add versioning to API endpoints for future-proofing.
- [ ] **More Tests:**  
  Add tests for password reset, password change, admin user listing, and negative cases.
- [ ] **Security Hardening:**  
  - Enforce HTTPS in production (via Nginx or cloud provider).
  - Review and restrict admin access.
- [ ] **Documentation:**  
  Add usage examples and endpoint descriptions to Swagger docs.

---

## 📝 Notes

- All user and authentication logic is contained within the `users` app for modularity.
- All endpoints are JWT-protected except registration, login, and password reset.
- User roles are included in JWT tokens for downstream microservices to enforce authorization.