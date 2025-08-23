# ZİRAVE - Project Status & Roadmap

## Last Update: 2025-01-11

---

## Overall Vision
ZİRAVE is a comprehensive digital ecosystem for the agricultural sector, connecting farmers, suppliers, workers, and engineers. It leverages AI for diagnostics and recommendations, all within a simple, user-friendly interface.

---

## Technical Stack
- **Mobile App:** React Native (with TypeScript)
- **Web Dashboard:** Next.js (with TypeScript)
- **Backend API:** NestJS (Node.js with TypeScript)
- **AI Service:** Python with FastAPI
- **Database:** PostgreSQL with PostGIS extension
- **Real-time Comms:** Socket.IO
- **Deployment:** Docker containers for all services.

---

## Development Roadmap & Status

**[ ] Phase 1: Foundation (Identity & Communication Core)**
    **[✓] 1.1: Project Scaffolding & Environment Setup**
        **[✓] 1.1.1:** Create root directory structure.
        **[ ] 1.1.2:** Initialize React Native project (`/mobile`).
        **[ ] 1.1.3:** Initialize Next.js project (`/web-dashboard`).
        **[ ] 1.1.4:** Initialize NestJS project (`/backend`).
        **[ ] 1.1.5:** Create Docker Compose file for PostgreSQL & Redis.
    **[ ] 1.2: Backend - User & Auth Module**
        **[ ] 1.2.1:** Setup Prisma and connect to PostgreSQL.
        **[ ] 1.2.2:** Create `User` model with roles (FARMER, SUPPLIER, etc.).
        **[ ] 1.2.3:** Implement phone-based OTP authentication (registration/login).
        **[ ] 1.2.4:** Implement JWT for session management.
        **[ ] 1.2.5:** Implement Role-Based Access Control (RBAC) guards.
    **[ ] 1.3: Backend - Secure Chat Module**
        **[ ] 1.3.1:** Create DB models for `Conversation` and `Message`.
        **[ ] 1.3.2:** Implement Socket.IO Gateway in NestJS.
        **[ ] 1.3.3:** Implement server-side content filtering (Regex for contacts).
    **[ ] 1.4: Mobile App - Core UI & Auth**
        **[ ] 1.4.1:** Setup i18n for Turkish language (`tr.json`).
        **[ ] 1.4.2:** Implement navigation (React Navigation).
        **[ ] 1.4.3:** Build login/registration screens using OTP flow.
        **[ ] 1.4.4:** Implement state management (Redux Toolkit) for user session.

**[ ] Phase 2: Marketplace Activation**
    **[ ] 2.1: Backend - Marketplace Module**
    **[ ] 2.2: Mobile App - Marketplace UI**

**[ ] Phase 3: Intelligence Integration**
    **[ ] 3.1: AI Service - Scaffolding & First Model**
    **[ ] 3.2: Backend - AI Service Integration**
    **[ ] 3.3: Mobile App - Diagnostics UI**

**[ ] Phase 4: Operations & Logistics**
    **[ ] 4.1: Backend - Logistics Module**
    **[ ] 4.2: Mobile App - Logistics UI**

---

## Current Focus
Starting Phase 1: Foundation - Project Scaffolding & Environment Setup

## Next Actions
1. Initialize React Native project in `/mobile` directory
2. Initialize Next.js project in `/web-dashboard` directory  
3. Initialize NestJS project in `/backend` directory
4. Create Docker Compose configuration

---

## Notes & Decisions
- Starting with foundation layer to establish solid architectural base
- Using TypeScript across all projects for type safety
- Implementing phone-based OTP authentication as primary auth method
- Planning for Turkish localization from the start