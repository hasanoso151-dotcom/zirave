# ZİRAVE - Digital Agricultural Ecosystem

**ZİRAVE** is a comprehensive digital platform designed to revolutionize the agricultural sector by connecting farmers, suppliers, agricultural workers, and engineers in a unified ecosystem.

## 🌱 Vision
To create the most comprehensive and user-friendly agricultural platform that leverages cutting-edge technology to solve real-world farming challenges while fostering community collaboration.

## 🏗️ Architecture

### Core Components
- **Mobile App** (React Native + TypeScript) - Primary user interface
- **Web Dashboard** (Next.js + TypeScript) - Administrative and analytics interface  
- **Backend API** (NestJS + TypeScript) - Core business logic and data management
- **AI Service** (Python + FastAPI) - Agricultural diagnostics and recommendations
- **Database** (PostgreSQL + PostGIS) - Data persistence with geographical capabilities

### Key Features
- **Identity & Authentication** - Phone-based OTP verification
- **Secure Communications** - End-to-end encrypted chat system
- **Smart Marketplace** - Agricultural product and service trading
- **AI Diagnostics** - Plant disease detection and treatment recommendations
- **Logistics Management** - Supply chain and delivery coordination
- **Multi-language Support** - Turkish language support with i18n ready architecture

## 🚀 Development Status

Currently in **Phase 1: Foundation** - setting up core infrastructure and authentication systems.

See [PROJECT_STATUS.md](./PROJECT_STATUS.md) for detailed roadmap and current progress.

## 🛠️ Getting Started

### Prerequisites
- Node.js 18+
- Docker & Docker Compose
- Android Studio / Xcode (for mobile development)
- PostgreSQL (via Docker)

### Quick Start
```bash
# Clone and setup the project
git clone <repository-url>
cd zirave

# Install dependencies for all sub-projects
npm run install:all

# Start development environment
docker-compose up -d
npm run dev:all
```

## 📁 Project Structure
```
zirave/
├── mobile/           # React Native mobile application
├── web-dashboard/    # Next.js web dashboard
├── backend/          # NestJS API server
├── ai-service/       # Python FastAPI AI service
├── docs/            # Documentation and specifications
├── docker-compose.yml
└── PROJECT_STATUS.md # Live project roadmap and status
```

## 🤝 Contributing

This project follows a structured development approach. Please refer to `PROJECT_STATUS.md` for current development focus and priorities.

## 📄 License

[License details to be added]

---

**Built with 💚 for the agricultural community**