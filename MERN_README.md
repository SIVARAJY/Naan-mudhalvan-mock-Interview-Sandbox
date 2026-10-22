# Naan Mudhalvan SkillSandbox · MERN Edition

A full-stack placement preparation, practice arena, and skill diagnostic ecosystem implemented using the **MERN Stack** (MongoDB, Express.js, React.js, Node.js).

---

## 🏗️ Architecture

```
naan_mudhalvan_supabase/
├── client/                     # React Frontend (Vite, React Router, Axios)
│   ├── src/
│   │   ├── components/Navbar.jsx
│   │   ├── pages/Dashboard.jsx
│   │   ├── pages/SkillAnalysis.jsx
│   │   ├── pages/PracticeArena.jsx
│   │   ├── pages/Companies.jsx
│   │   └── pages/LearningHub.jsx
│   └── package.json
│
├── server/                     # Express & Node.js Backend API
│   ├── models/                 # Mongoose Schemas (User, Course, Question, Company, Attempt)
│   ├── server.js               # Express Server & REST API Endpoints
│   └── package.json
│
├── app.py                      # (Preserved) Python/Flask + Supabase Backend
└── templates/                  # (Preserved) Jinja2 Templates
```

---

## 🚀 Running the MERN Stack

### 1. Start the Express Backend (Port 5000)
```bash
cd server
npm install
npm start
```
The server connects to MongoDB (configured via `MONGODB_URI` in `server/.env`) with automatic fallback data to ensure smooth offline testing.

### 2. Start the React Frontend (Port 5173)
```bash
cd client
npm install
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## 🎨 Theme & Features
- **Official Naan Mudhalvan Theme:** Dark Teal (`#304443`), Gold Accent (`#F3C12C`), Forest Green (`#0C823C`), Mint Soft (`#DCEEE8`), and Card Surface (`#F5F5F5`).
- **Skill Analysis & Readiness Radar:** Real-time benchmark scores and strength/weakness tracking.
- **Interactive Practice Arena:** Multi-topic MCQ drills, instant feedback, progressive hints, and streak indicators.
- **Company Recruitment Guide:** Round-by-round breakdown for TCS, Zoho, Infosys.
- **Learning Hub:** Embedded YouTube curriculum aligned with technical hiring tracks.
