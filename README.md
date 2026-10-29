# SkillSandbox · Naan Mudhalvan Technical Placement Platform

An intelligent, closed-loop placement readiness ecosystem, adaptive skill diagnostics tracker, and technical training sandbox aligned with the **Naan Mudhalvan** technical skilling mandate.

🌐 **Live Production Website:** [https://naan-mudhalvan-mock-interview-sandbox.onrender.com/](https://naan-mudhalvan-mock-interview-sandbox.onrender.com/)

---

## 📖 Overview

Undergraduate engineers often prepare for campus placements using fragmented resources: watching lectures on video portals, taking quizzes on generic sites, and practicing code on standalone platforms. Without a shared feedback loop, students struggle to identify their conceptual weaknesses or understand how their skills align with corporate hiring standards.

**SkillSandbox** bridges this gap by unifying **Skill Diagnostics**, a **Topic-wise Practice Arena**, a **Curated Learning Hub**, and **Company Recruitment Guides** into a continuous learning cycle:
- When a student struggles in a practice drill or coding problem, the platform detects their weak area ($< 60\%$ accuracy).
- The system surfaces the exact remedial video lesson in the Learning Hub.
- The student's composite **Readiness Index (0–100%)** updates in real time, benchmarked against hiring criteria for top corporate recruiters like **TCS, Zoho, Infosys, and Cognizant**.

---

## 🚀 Key Modules & Features

### 1. 📊 Intelligent Skill Analysis & Improvement Tracker
- **Readiness Radar:** Computes an overall **Readiness Index (0–100%)** based on accuracy, problem-solving speed, and practice consistency.
- **Strength & Weak-Area Detection:** Highlights proficient domains ($\ge 70\%$) and flags critical weak spots ($< 60\%$).
- **Core Syllabus Breakdown:** Interactive progress tracking across 5 foundational placement tracks: **Python, Java, DSA, DBMS, and Web Development**.

### 2. ⚡ Topic-Wise Skill Practice Arena
- **500+ Curated MCQs & Drills:** 105+ questions per technical domain covering foundational syntax, data structures, database normalization, and web protocols.
- **Interactive Practice Modes:**
  - **⏱️ 10-Minute Timed Drills:** Builds speed and accuracy under simulated test conditions.
  - **🎯 MCQ Drills:** Instant visual feedback (green for correct, red for incorrect with correct option highlighted) and in-depth explanations.
  - **💬 Technical Interview Prompts:** Model answers with self-assessment rating controls.
- **Two-Tier Progressive Hints:** Closes knowledge gaps with calibrated score deductions ($-5\text{ pts}$ for Hint 1, $-10\text{ pts}$ for Hint 2).
- **Daily Streak & Bookmarking:** Encourages daily practice with streak counters and personal question bookmarking.

### 3. 💻 Sandboxed Coding Challenges
- **In-Browser Code Editor:** Write and test algorithmic solutions in Python.
- **Subprocess Sandboxing:** Runs student code in an isolated subprocess with a strict **5-second execution limit** to prevent infinite loops and memory leaks.
- **Automated Rubric Grading:** Verifies output against predefined test cases with real-time pass/review feedback.

### 4. 📚 Curated Learning Hub
- **Track-Aligned Video Lessons:** Embedded YouTube video lectures organized by official Naan Mudhalvan syllabus tracks.
- **Timestamped Note-Taking:** Captures exact video timestamps while watching; clicking any saved note seeks the video directly to that second.
- **Course Completion Certificates:** Earn verifiable completion certificates upon finishing course curricula.

### 5. 🏢 Company Recruitment Guide
- **Corporate Hiring Profiles:** Round-by-round assessment breakdowns for **TCS, Zoho Corporation, Infosys, and Cognizant**.
- **Assessment Formats:** Detailed guidance covering Online Aptitude, Technical Coding, System Design, and HR rounds.
- **Preparation Arsenal:** Direct links to practice drills aligned with specific company interview patterns.

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

Technology Stack

SkillSandbox is engineered with dual-architecture flexibility:

### Production Architecture (Python / Flask / Supabase)
- **Backend:** Python 3.12, Flask, Gunicorn 22.0 WSGI server
- **Database:** Supabase Cloud PostgreSQL 15 (with JSONB support and SSL pooling via `psycopg 3`)
- **Frontend:** Semantic HTML5, CSS3 Custom Properties, Vanilla JavaScript (ES6+), Jinja2
- **Hosting:** Render Cloud Platform with automated CI/CD via GitHub webhooks

Alternative Architecture (MERN Monorepo)
- **Backend:** Node.js (v24), Express.js REST API
- **Database:** MongoDB Atlas (Mongoose ODM)
- **Frontend:** React.js (v19) Single Page Application scaffolded with Vite
- **Location:** Available in `/client` and `/server` directories

---

## 💻 Local Setup & Installation

### Option A: Python / Flask Application

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
   DATABASE_URL=your_supabase_postgresql_connection_string
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_ANON_KEY=your_supabase_anon_key
   FLASK_SECRET_KEY=your_secret_key
   FLASK_ENV=development
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

- **SIVARAJ Y (7376242IT307)** — System Architecture, Cloud Database (PostgreSQL/Supabase & MongoDB), Authentication (Google OAuth), and CI/CD Automation.
- **SOLAI MANOJ S (7376242IT309)** — UI/UX Design (Figma), Frontend Engineering, YouTube Media Synchronization, and Responsive Layouts.
- **VENKATESH KUMAR S (7376242IT336)** — Application Backend (Python/Flask & Express.js), REST APIs, Code Sandboxing Engine, and Skill Diagnostics.

---

## 📜 License & Academic Disclaimer

Developed as an academic project aligned with the **Naan Mudhalvan** skilling framework. Automated scoring and readiness indices are indicative benchmarks designed for skill preparation and learning diagnostics.
