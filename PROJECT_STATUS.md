# ZİRAVE - Project Status & Roadmap (Supabase Edition)

## Last Update: 2025-01-11

---

## Overall Vision
ZİRAVE is a comprehensive digital ecosystem for the agricultural sector, connecting farmers, suppliers, workers, and engineers. It leverages Supabase for its backend infrastructure and a custom AI service for intelligence, all within a simple, user-friendly interface.

---

## Technical Stack (Supabase-centric)
- **Mobile App:** React Native (with TypeScript)
- **Web Dashboard:** Next.js (with TypeScript)
- **Backend Core:** **Supabase** (PostgreSQL, Auth, Storage, Edge Functions)
- **Custom Backend Logic:** **NestJS** (for complex tasks & interfacing with Supabase/AI)
- **AI Service:** Python with FastAPI
- **Deployment:** Vercel for Web, Supabase for Backend, Docker for AI Service.

---

## Development Roadmap & Status

**[ ] Phase 1: Foundation (Supabase & Frontend Setup)**
    **[✓] 1.1: Project Scaffolding & Supabase Integration**
        **[✓] 1.1.1:** Create root directory structure (`/mobile`, `/web-dashboard`, `/backend-custom`, `/ai-service`).
        **[✓] 1.1.2:** Initialize React Native project (`/mobile`).
        **[ ] 1.1.3:** Initialize Next.js project (`/web-dashboard`).
        **[ ] 1.1.4:** Initialize NestJS project (`/backend-custom`).
        **[ ] 1.1.5:** Install Supabase CLI and initialize Supabase project (`/supabase`). This will contain DB migrations.
        **[ ] 1.1.6:** Create a central `.env` file with placeholders for Supabase URL and ANON_KEY.
    **[ ] 1.2: Supabase Schema & Database Setup**
        **[ ] 1.2.1:** Create first database migration in `/supabase/migrations` to define core tables: `profiles` (with roles), `products`, `conversations`, `messages`.
        **[ ] 1.2.2:** Enable Phone-based Authentication in the Supabase dashboard settings.
        **[ ] 1.2.3:** Setup Row Level Security (RLS) policies for the tables. (e.g., Users can only see their own conversations).
    **[✓] 1.3: Mobile App - Supabase Integration & Auth**
        **[✓] 1.3.1:** Install `@supabase/supabase-js` in the React Native project.
        **[✓] 1.3.2:** Create a Supabase client helper (`/mobile/src/lib/supabase.ts`).
        **[✓] 1.3.3:** Build login/registration screens using Supabase's phone OTP auth (`auth.signInWithOtp`).
        **[✓] 1.3.4:** Implement state management (Redux Toolkit) to handle the Supabase user session.
        **[✓] 1.3.5:** Setup i18n for Turkish language (`tr.json`).

**[ ] Phase 2: Marketplace Activation**
    **[ ] 2.1: Mobile App - Marketplace UI & Logic**
        **[ ] 2.1.1:** Build UI to display products fetched directly from Supabase DB.
        **[ ] 2.1.2:** Implement "My Products" screen for suppliers using Supabase RLS.
    **[ ] 2.2: Backend - Real-time Chat**
        **[ ] 2.2.1:** Utilize Supabase Realtime Subscriptions for the chat system.
        **[ ] 2.2.2:** Create a Supabase Edge Function to run server-side content filtering (Regex) on new messages.

**[ ] Phase 3: Intelligence Integration**
    **[ ] 3.1: AI Service - Scaffolding & First Model**
    **[ ] 3.2: Custom Backend - AI Integration**
    **[ ] 3.3: Mobile App - Diagnostics UI**

**[ ] Phase 4: Operations & Logistics**
    **[ ] 4.1: Custom Backend - Logistics Module**
    **[ ] 4.2: Mobile App - Logistics UI**

---

## Current Focus
Phase 1.3 Complete: Mobile App with Supabase Integration & Auth - Ready for Next.js Web Dashboard

## Next Actions
1. Initialize Next.js project in `/web-dashboard` directory  
2. Initialize NestJS project in `/backend-custom` directory
3. Initialize Supabase project structure with database migrations
4. Setup Supabase authentication and RLS policies

---

## Notes & Decisions