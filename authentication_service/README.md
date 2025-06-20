# Authentication Service — README

This microservice provides authentication and user management for the Drone Command & Control System (DCCS) platform. It is responsible for issuing JWT tokens, managing user registration, roles, and password operations, and exposing user information to other microservices in a secure, scalable way.

---

## How Authentication Works

This service uses **JWT (JSON Web Tokens)** for stateless, secure authentication across all DCCS microservices.

1. **User Registration & Login**
   - Users register via `/api/register/`, selecting a role (`operator`, `admin`, or `monitor`).
   - To log in, users send their credentials to `/api/token/`.
   - On successful login, the service issues a JWT access token (and a refresh token).

2. **JWT Token Structure**
   - The JWT access token contains the user's identity and role as claims.
   - Example payload:
     ```json
     {
       "user_id": 1,
       "username": "alice",
       "role": "admin",
       "exp": 1718900000,
       ...
     }
     ```

3. **Using the Token**
   - The client includes the JWT in the `Authorization` header for all API requests:
     ```
     :Authorization Bearer <access_token>
     ```
   - All protected endpoints require a valid JWT token.

4. **Downstream Service Validation**
   - Other microservices (e.g., telemetry, commands) validate the JWT using the same secret.
   - If the token is valid, the user is authenticated and their role is available for authorization checks.
   - If the token is missing, invalid, or expired, the request is rejected with a 401 Unauthorized error.

5. **Role-Based Access**
   - The user's role (from the JWT) is used by downstream services to enforce permissions (e.g., only admins can list users).

6. **Token Refresh**
   - When the access token expires, clients can obtain a new one using the refresh token at `/api/token/refresh/`.

**Summary:**  
Authentication is centralized, stateless, and secure. All microservices trust the JWT issued by this service and use the embedded role for

## Features

- **JWT Authentication:**  
  Secure login and token refresh endpoints (`/api/token/`, `/api/token/refresh/`).

- **User Registration:**  
  Register new users with role selection (`/api/register/`).

- **User Profile:**  
  Authenticated users can view their profile and role (`/api/profile/`).

- **Password Management:**  
  - Change password (`/api/password/change/`)
  - Request password reset (token sent to email) (`/api/password/reset/`)
  - Confirm password reset with token (`/api/password/reset/confirm/`)

- **Admin User Management:**  
  Admins can list all users (`/api/users/`).

- **Role-Based Access:**  
  Each user has a role (`operator`, `admin`, `monitor`) managed via a `UserProfile` model.  
  The user's role is included as a custom claim in every JWT token, allowing downstream services to enforce authorization.

- **CORS Support:**  
  CORS is enabled for development; restrict origins in production.

- **API Documentation:**  
  Interactive Swagger and Redoc docs available at `/swagger/` and `/redoc/`.

- **PostgreSQL Database:**  
  Uses PostgreSQL for production-ready persistence.

- **Automated Tests:**  
  Basic tests for registration, login, and profile endpoints.

---

## Security & Integration Notes

- **All endpoints are JWT-protected** except registration, login, and password reset.
- **User roles are included in JWT tokens** so other microservices can enforce permissions without direct database access.
- **All user and authentication logic is contained within the `users` app** for modularity and maintainability.

---

## Improvements & Next Steps

- Configure a real SMTP backend for password reset emails.
- Restrict CORS origins in production.
- Add API rate limiting and audit logging for security.
- Implement user email verification after registration.
- Add endpoints for user info update and deactivation (admin/self-service).
- Add API versioning for future-proofing.
- Expand automated test coverage.
- Enforce HTTPS in production.
- Add usage examples and endpoint descriptions to API docs.

---

## Usage

- Register a user: `POST /api/register/`
- Obtain JWT token: `POST /api/token/`
- Refresh JWT token: `POST /api/token/refresh/`
- View profile: `GET /api/profile/` (JWT required)
- Change password: `POST /api/password/change/` (JWT required)
- Request password reset: `POST /api/password/reset/`
- Confirm password reset: `POST /api/password/reset/confirm/`
- List users (admin): `GET /api/users/` (JWT with admin role required)
- API docs: `/swagger/` or `/redoc/`

---

**This service is designed to be the single source of truth for authentication and user roles in the DCCS microservices ecosystem.**