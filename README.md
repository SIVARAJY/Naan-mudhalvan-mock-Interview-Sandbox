# SkillSandbox · Naan Mudhalvan Technical Placement Platform

An intelligent, closed-loop placement readiness ecosystem, adaptive skill diagnostics tracker, and technical training sandbox aligned with the **Naan Mudhalvan** technical skilling mandate.

🌐 **Live Production Website:** [https://naan-mudhalvan-mock-interview-sandbox.onrender.com/](https://naan-mudhalvan-mock-interview-sandbox.onrender.com/)

---

## 📖 Overview

Undergraduate engineers often prepare for campus placements using fragmented resources: watching lectures on video portals, taking quizzes on generic sites, and practicing code on standalone platforms. Without a shared feedback loop, students struggle to identify their conceptual weaknesses or understand how their skills align with corporate hiring standards.

**SkillSandbox** bridges this gap by unifying **Skill Diagnostics**, a **Topic-wise Practice Arena**, a **Curated Learning Hub**, a **Multi-Language Coding Sandbox**, and **Company Recruitment Guides** into a continuous learning cycle:
- When a student struggles in a practice drill or coding problem, the platform detects their weak area ($< 60\%$ accuracy).
- The system surfaces the exact remedial video lesson in the Learning Hub.
- The student's composite **Readiness Index (0–100%)** updates in real time, benchmarked against hiring criteria for top corporate recruiters like **TCS, Zoho, Infosys, and Cognizant**.

---

## 🚀 Key Modules & Capabilities

### 1. 📊 Intelligent Skill Analysis & Improvement Tracker (`/analysis`)
- **Readiness Radar:** Computes an overall **Readiness Index (0–100%)** based on accuracy, problem-solving speed, and practice consistency.
- **Strength & Weak-Area Detection:** Highlights proficient domains ($\ge 70\%$) and flags critical weak spots ($< 60\%$).
- **Core Syllabus Breakdown:** Interactive progress tracking across foundational placement tracks: **Python, Java, DSA, DBMS, and Web Development**.

### 2. ⚡ Topic-Wise Skill Practice Arena (`/practice`)
- **500+ Curated MCQs & Algorithmic Drills:** Structured technical questions covering foundational syntax, data structures, database normalization, and web protocols.
- **Interactive Practice Modes:**
  - **⏱️ 10-Minute Timed Drills:** Builds speed and accuracy under simulated test conditions.
  - **🎯 MCQ Drills:** Instant visual feedback (green for correct, red for incorrect with correct option highlighted) and in-depth explanations.
  - **💬 Technical Interview Prompts:** Model answers with self-assessment rating controls.
- **Two-Tier Progressive Hints:** Closes knowledge gaps with calibrated score deductions ($-5\text{ pts}$ for Hint 1, $-10\text{ pts}$ for Hint 2).
- **Daily Streak & Bookmarking:** Encourages daily practice with streak counters and personal question bookmarking.

### 3. 💻 Multi-Language Coding Sandbox & Multi-Factor Evaluator (`/coding`)
- **Multi-Language Selector:** Choose between **Python 3.12**, **JavaScript (Node.js)**, **Java**, and **C++** with pre-configured starter templates and signature definitions.
- **Real-Time "Run Code" Sandbox:** Test algorithmic solutions instantaneously against sample test vectors in an isolated subprocess with latency measurement (`/coding/api/run`) before committing a final submission.
- **Multi-Factor Evaluation Engine:** Comprehensive algorithmic grading on submission across four distinct dimensions:
  1. **Factor 1: Functional Test Correctness (60 pts):** Automated vector assertions testing edge cases, boundary conditions, and typical inputs.
  2. **Factor 2: Runtime Latency & Execution Speed (15 pts):** Strict execution time measurement with scaled latency scoring.
  3. **Factor 3: Syntax, Structure & Signatures (15 pts):** Static AST syntax analysis, structural pattern validation, and method signature compliance.
  4. **Factor 4: Algorithmic Efficiency Heuristic (10 pts):** Evaluation of loop nesting, recursion depth, and algorithmic complexity.
- **Visual Evaluation Report (`/coding_result`):** High-impact results dashboard with score hero ring, 4-factor progress breakdowns, test vector input/output logs, and recommended drills.

### 4. 📚 Curated Learning Hub (`/learning`)
- **Track-Aligned Video Lessons:** Embedded YouTube video lectures organized by official Naan Mudhalvan syllabus tracks.
- **Timestamped Note-Taking:** Captures exact video timestamps while watching; clicking any saved note seeks the video directly to that second.
- **Course Completion Certificates:** Earn verifiable completion certificates upon finishing course curricula.

### 5. 🏢 Company Recruitment Guide (`/companies`)
- **Corporate Hiring Profiles:** Round-by-round assessment breakdowns for **TCS, Zoho Corporation, Infosys, and Cognizant**.
- **Assessment Formats:** Detailed guidance covering Online Aptitude, Technical Coding, System Design, and HR rounds.
- **Preparation Arsenal:** Direct links to practice drills aligned with specific company interview patterns.

### 6. 🔐 Admin & Course Management Portal (`/admin/login`, `/admin/learning`)
- **Super Admin Access Control:** Dedicated administrative authentication restricted to verified administrative emails (`sivarajy.it24@bitsathy.ac.in`).
- **Curriculum Authoring:** Add, update, and manage courses and lessons with embedded video IDs, durations, and syllabi.

---

## 📂 Codebase & File Structure

```
├── app.py                         # Main Flask application (routes, DB pooling, auth, admin, sandbox)
├── coding_challenges.py           # Multi-language algorithmic challenges, starters, and test vectors
├── sandbox_evaluator.py           # Multi-factor coding evaluator (subprocess runners & static analyzers)
├── requirements.txt               # Python production dependencies (Flask, psycopg 3, gunicorn, etc.)
├── .env.example                   # Template for environment configuration
│
├── templates/                     # Jinja2 presentation templates
│   ├── base.html                  # Core layout, topbar navigation, official institutional branding
│   ├── login.html                 # Supabase email/password and Google OAuth authentication
│   ├── admin_login.html           # Dedicated Super Admin master login portal
│   ├── admin_learning.html        # Course and lesson management dashboard
│   ├── admin_add_course.html      # Create new learning hub courses
│   ├── admin_add_lesson.html      # Add video lessons to existing courses
│   ├── dashboard.html             # Student progress overview, recent attempts, quick actions
│   ├── skill_analysis.html        # Readiness radar, weak area diagnostics, syllabus progress
│   ├── practice_arena.html        # Practice hub with topic categories and question modes
│   ├── practice_drill.html        # Interactive 10-minute timed MCQ drills with progressive hints
│   ├── practice_bookmarks.html    # Saved bookmarked questions review
│   ├── practice_history.html      # Practice drill attempts and historical accuracy
│   ├── coding.html                # Multi-language coding sandbox with Run Code & Submit controls
│   ├── coding_result.html         # Multi-factor evaluation report and score breakdown
│   ├── learning_hub.html          # Curated video courses catalog
│   ├── course_detail.html         # Course syllabus, lesson playlist, certificate unlock
│   ├── lesson_player.html         # Embedded video player with timestamped personal notes
│   ├── certificate.html           # Verifiable course completion certificate view
│   ├── companies_list.html        # Corporate hiring guide index (TCS, Zoho, Infosys, Cognizant)
│   ├── company_detail.html        # Detailed round-by-round interview pattern breakdown
│   └── history.html               # Complete student submission audit trail
│
├── static/
│   └── style.css                  # Custom styling implementing Naan Mudhalvan design specifications
│
├── data & scripts/
│   ├── upload_to_practice_arena.py # Populates practice arena questions in Supabase
│   ├── upload_mcqs_to_db.py       # DB ingestion helper for practice MCQs
│   ├── parse_mcqs.py              # Parsing utility for question document sets
│   ├── split_mcqs.py              # Categorization script for practice MCQs
│   └── remove_learning_hub_quizzes.py # Data maintenance script
│
├── client/                        # MERN Stack Alternative: React 19 Frontend (Vite)
│   ├── src/
│   │   ├── components/            # Reusable UI components (Navbar, etc.)
│   │   ├── pages/                 # React views (Dashboard, PracticeArena, SkillAnalysis, etc.)
│   │   └── App.jsx                # Client routing and layout
│   └── package.json
│
└── server/                        # MERN Stack Alternative: Express.js & MongoDB Backend
    ├── models/                    # Mongoose schemas (User, Course, Question, Attempt, Company)
    ├── server.js                  # Express API server entry point
    └── package.json
```

---

## 🎨 Official Naan Mudhalvan Design System

The platform strictly implements the official institutional color palette:
- **Dark Teal (`#304443`):** Primary buttons, top navigation bar, table headers.
- **Deep Hover Teal (`#273635`):** Interactive button hover states.
- **Gold Accent (`#F3C12C`):** Topbar accent line, timer displays, focus accessibility rings.
- **Forest Green (`#0C823C`):** Hyperlinks, pass indicators, accuracy tags.
- **Mint Light (`#F0F8F7`) & Mint Soft (`#DCEEE8`):** Header bands, callout cards, progress bars.
- **Surface Gray (`#F5F5F5`):** Content cards and panels.
- **Ink Charcoal (`#202838`):** High-contrast primary text.

---

## 🛠️ Technology Stack

SkillSandbox is engineered with dual-architecture flexibility:

### Production Architecture (Python / Flask / Supabase)
- **Backend:** Python 3.12, Flask, Gunicorn 22.0 WSGI server
- **Database:** Supabase Cloud PostgreSQL 15 (with JSONB support and SSL connection pooling via `psycopg 3`)
- **Frontend:** Semantic HTML5, CSS3 Custom Properties, Vanilla JavaScript (ES6+), Jinja2
- **Execution Sandboxing:** Subprocess isolation with process timeout management, syntax verification, and multi-factor grading
- **Hosting:** Render Cloud Platform with automated CI/CD via GitHub webhooks

### Alternative Architecture (MERN Monorepo)
- **Backend:** Node.js (v24), Express.js REST API
- **Database:** MongoDB Atlas (Mongoose ODM)
- **Frontend:** React.js (v19) Single Page Application scaffolded with Vite
- **Location:** Available in `/client` and `/server` directories

---

## 💻 Local Setup & Installation

### Option A: Python / Flask Application (Production Platform)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SIVARAJY/Naan-mudhalvan-mock-Interview-Sandbox.git
   cd Naan-mudhalvan-mock-Interview-Sandbox
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file based on `.env.example`:
   ```env
   DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/postgres
   SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
   SUPABASE_ANON_KEY=your-supabase-anon-or-publishable-key
   FLASK_SECRET_KEY=your_secret_key
   FLASK_ENV=development

   # Super Admin Configuration
   ADMIN_EMAILS=sivarajy.it24@bitsathy.ac.in
   ADMIN_MASTER_PASSWORD=YourAdminMasterPassword
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   Open [http://localhost:5000](http://localhost:5000) in your browser.

---

### Option B: MERN Stack Application

1. **Start the Express API server:**
   ```bash
   cd server
   npm install
   npm start
   ```
   *(Runs on port 5000)*

2. **Start the React client:**
   ```bash
   cd client
   npm install
   npm run dev
   ```
   *(Runs on port 5173)*

---

## 👥 Project Team & Contributors

**Bannari Amman Institute of Technology, Sathyamangalam**  
*Department of Information Technology*

- **SIVARAJ Y (7376242IT307)** — System Architecture, Cloud Database (PostgreSQL/Supabase & MongoDB), Authentication (Google OAuth), Multi-Factor Sandbox Engine, and CI/CD Automation.
- **SOLAI MANOJ S (7376242IT309)** — UI/UX Design (Figma), Frontend Engineering, YouTube Media Synchronization, and Responsive Layouts.
- **VENKATESH KUMAR S (7376242IT336)** — Application Backend (Python/Flask & Express.js), REST APIs, Code Sandboxing Engine, and Skill Diagnostics.

---

## 📜 License & Academic Disclaimer

Developed as an academic project aligned with the **Naan Mudhalvan** skilling framework. Automated scoring and readiness indices are indicative benchmarks designed for skill preparation and learning diagnostics.
