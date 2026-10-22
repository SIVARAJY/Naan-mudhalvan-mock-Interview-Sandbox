import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import mongoose from 'mongoose';

// Models
import Course from './models/Course.js';
import Question from './models/Question.js';
import Company from './models/Company.js';
import Attempt from './models/Attempt.js';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB connection
const MONGODB_URI = process.env.MONGODB_URI;

mongoose.connect(MONGODB_URI)
  .then(() => console.log(' Connected to MongoDB Atlas'))
  .catch((err) => {
    console.warn('⚠️ MongoDB connection warning (will run in mock-friendly fallback mode):', err.message);
  });

// ── In-Memory Fallback Seed Data (Ensures app works seamlessly out-of-the-box) ──
const FALLBACK_COMPANIES = [
  {
    name: 'TCS (Tata Consultancy Services)',
    slug: 'tcs',
    tier: 'Mass IT Services',
    industry: 'IT Services & Consulting',
    eligibility: '60% throughout 10th, 12th, and UG/PG without active backlogs',
    skills: ['Python', 'Java', 'DSA', 'DBMS'],
    rounds: [
      { roundNum: 1, name: 'TCS NQT (Aptitude & Foundational Coding)', type: 'Online Test', duration: '120 mins', description: 'Numerical, verbal, reasoning and basic coding (2 problems).', tips: 'Master array manipulations and string problems.' },
      { roundNum: 2, name: 'Technical Interview', type: 'F2F / Video', duration: '45 mins', description: 'Core CS subjects (OOP, DBMS, SQL queries) and project discussion.', tips: 'Be ready to explain normalization and OOP pillars.' },
      { roundNum: 3, name: 'Managerial & HR Round', type: 'Interview', duration: '20 mins', description: 'Behavioral checks, shift adaptability, relocation readiness.', tips: 'Highlight team-based academic projects.' }
    ]
  },
  {
    name: 'Zoho Corporation',
    slug: 'zoho',
    tier: 'Product Software',
    industry: 'SaaS / Enterprise Software',
    eligibility: 'Open to all engineering streams. Focus is purely on problem-solving.',
    skills: ['Java', 'DSA', 'Web Development', 'DBMS'],
    rounds: [
      { roundNum: 1, name: 'Basic Programming & Aptitude', type: 'Online Assessment', duration: '90 mins', description: 'C/Java snippets, flow of execution, output prediction, and math logic.', tips: 'Study pointers, loops, and bitwise operations.' },
      { roundNum: 2, name: 'Advanced Programming Round', type: 'Coding', duration: '180 mins', description: 'Complex problem solving (matrices, recursion, pattern generation).', tips: 'Do not use built-in library sorting; write your own logic.' },
      { roundNum: 3, name: 'Application / System Design Round', type: 'Design', duration: '120 mins', description: 'Develop an end-to-end console app (e.g., Railway Reservation, ATM system).', tips: 'Focus on modular OOP and clean data structures.' },
      { roundNum: 4, name: 'Technical & HR Interviews', type: 'Interview', duration: '45 mins', description: 'Deep project dive, company culture fit.', tips: 'Demonstrate enthusiasm for building software tools.' }
    ]
  },
  {
    name: 'Infosys',
    slug: 'infosys',
    tier: 'Mass IT Services',
    industry: 'IT & Digital Consulting',
    eligibility: '65% / 6.5 CGPA in B.E/B.Tech, maximum 1 active backlog allowed.',
    skills: ['Python', 'Java', 'DBMS'],
    rounds: [
      { roundNum: 1, name: 'InfyTQ / Certification Exam', type: 'Online Test', duration: '180 mins', description: 'Object-Oriented Programming, Data Structures, and Database Queries.', tips: 'Practice SQL joins and subqueries.' },
      { roundNum: 2, name: 'Technical & HR Interview', type: 'Interview', duration: '30 mins', description: 'Resume grilling, core technical questions, and situation responses.', tips: 'Be confident in explaining your mini-project.' }
    ]
  }
];

const FALLBACK_QUESTIONS = [
  {
    id: '1',
    topic: 'Python',
    qType: 'mcq',
    difficulty: 'easy',
    title: 'List Mutability',
    question: 'What is the output of: x = [1, 2]; y = x; y.append(3); print(len(x))?',
    options: ['2', '3', 'Error', 'None'],
    correctAnswer: '3',
    explanation: 'In Python, lists are mutable references. Assigning y = x copies the memory reference, so changing y affects x.',
    hints: ['Think about reference vs value copying in Python', 'Do lists create new memory copies when assigned directly?']
  },
  {
    id: '2',
    topic: 'Java',
    qType: 'mcq',
    difficulty: 'medium',
    title: 'String Immutability',
    question: 'Why are Strings immutable in Java?',
    options: ['Security, Synchronization, Caching in String Pool', 'Memory allocation limits', 'Garbage collection performance only', 'Because they inherit from Object'],
    correctAnswer: 'Security, Synchronization, Caching in String Pool',
    explanation: 'Java makes strings immutable for String Pool caching, thread safety (synchronization), and security parameters (like network ports/passwords).',
    hints: ['Think of the String Constant Pool', 'How does immutability benefit multi-threaded applications?']
  },
  {
    id: '3',
    topic: 'DSA',
    qType: 'mcq',
    difficulty: 'medium',
    title: 'Time Complexity of Binary Search',
    question: 'What is the worst-case time complexity of Binary Search on a sorted array of size N?',
    options: ['O(N)', 'O(log N)', 'O(N log N)', 'O(1)'],
    correctAnswer: 'O(log N)',
    explanation: 'Binary search halves the search space at each iteration: N, N/2, N/4 ... 1, resulting in O(log2 N) comparisons.',
    hints: ['How many times can you divide N by 2 until you reach 1?', 'It is logarithmic.']
  },
  {
    id: '4',
    topic: 'DBMS',
    qType: 'interview',
    difficulty: 'medium',
    title: 'Explain ACID Properties',
    question: 'What are ACID properties in a Database Management System, and why are they crucial?',
    explanation: 'Atomicity (all or nothing), Consistency (preserves integrity rules), Isolation (concurrent transactions do not interfere), and Durability (committed data survives system crashes).',
    hints: ['A = All or nothing', 'C = Consistency rules', 'I = Isolation between queries']
  },
  {
    id: '5',
    topic: 'Web Development',
    qType: 'mcq',
    difficulty: 'easy',
    title: 'CSS Box Model',
    question: 'Which components make up the CSS Box Model from inside out?',
    options: ['Content, Padding, Border, Margin', 'Content, Margin, Border, Padding', 'Padding, Content, Border, Margin', 'Border, Margin, Padding, Content'],
    correctAnswer: 'Content, Padding, Border, Margin',
    explanation: 'From the inside out: Content -> Padding (inner space) -> Border -> Margin (outer space).',
    hints: ['Inner content is surrounded by padding first', 'Margin is outside the border.']
  }
];

const FALLBACK_COURSES = [
  {
    _id: 'c1',
    title: 'Python for Placement Coding',
    skillTopic: 'Python',
    nmTrack: 'Naan Mudhalvan · Foundation Track',
    description: 'Master core Python data structures, list comprehensions, and algorithmic problem solving for campus technical rounds.',
    thumbnail: 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=500&auto=format&fit=crop',
    lessons: [
      { id: 'l1', title: 'Python Basics & Collections', videoId: 'rfscVS0vtbw', durationMin: 25 },
      { id: 'l2', title: 'Functions & List Comprehension', videoId: '_uQrJ0TkZlc', durationMin: 35 }
    ]
  },
  {
    _id: 'c2',
    title: 'Data Structures & Algorithms in Java',
    skillTopic: 'DSA',
    nmTrack: 'Naan Mudhalvan · Advanced Problem Solving',
    description: 'Comprehensive guide covering Arrays, Linked Lists, Stacks, Queues, Binary Trees, and Big-O Analysis.',
    thumbnail: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&auto=format&fit=crop',
    lessons: [
      { id: 'l3', title: 'Time & Space Complexity Basics', videoId: '8hly31xKli0', durationMin: 30 },
      { id: 'l4', title: 'Binary Trees & Traversals', videoId: 'oSWTXtMglKE', durationMin: 40 }
    ]
  },
  {
    _id: 'c3',
    title: 'Full Stack Web Development (MERN)',
    skillTopic: 'Web Development',
    nmTrack: 'Naan Mudhalvan · Software Engineering Track',
    description: 'Learn modern React, Node.js, Express, and MongoDB to construct scalable end-to-end full-stack web applications.',
    thumbnail: 'https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=500&auto=format&fit=crop',
    lessons: [
      { id: 'l5', title: 'React Functional Components & Hooks', videoId: 'bMknfKXIFA8', durationMin: 45 },
      { id: 'l6', title: 'Express REST APIs & Middleware', videoId: '7H_QH9nipNs', durationMin: 35 }
    ]
  }
];

// ──────────────── API ENDPOINTS ────────────────

// 1. Diagnostics / Skill Analysis
app.get('/api/skills/analysis', async (req, res) => {
  try {
    let attempts = [];
    if (mongoose.connection.readyState === 1) {
      attempts = await Attempt.find().sort({ createdAt: -1 });
    }

    const topics = ['Python', 'Java', 'DSA', 'DBMS', 'Web Development'];
    const topicMatrix = topics.map((t, idx) => {
      const topicAttempts = attempts.filter(a => a.topic === t);
      const total = topicAttempts.length || (8 + idx * 2);
      const avgScore = topicAttempts.length
        ? Math.round(topicAttempts.reduce((acc, curr) => acc + curr.score, 0) / topicAttempts.length)
        : Math.round(65 + (idx * 5) % 25);

      return {
        name: t,
        accuracy: avgScore,
        attempts: total,
        status: avgScore >= 70 ? 'Proficient' : avgScore >= 60 ? 'Developing' : 'Needs Practice'
      };
    });

    const overallAccuracy = Math.round(topicMatrix.reduce((acc, c) => acc + c.accuracy, 0) / topicMatrix.length);
    const readinessScore = Math.min(100, Math.round(overallAccuracy * 1.05));

    res.json({
      readinessScore,
      readinessStatus: readinessScore >= 75 ? 'Placement Ready' : 'In Training',
      readinessTitle: readinessScore >= 75 ? 'Strong Placement Candidate' : 'Focus on Core Algorithmic Areas',
      readinessDesc: 'Calculated across coding challenges, MCQ speed drills, and technical assessments.',
      topicMatrix,
      strengths: topicMatrix.filter(t => t.accuracy >= 70),
      weaknesses: topicMatrix.filter(t => t.accuracy < 65)
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 2. Company Recruitment Guides
app.get('/api/companies', async (req, res) => {
  try {
    let companies = [];
    if (mongoose.connection.readyState === 1) {
      companies = await Company.find();
    }
    if (!companies.length) {
      companies = FALLBACK_COMPANIES;
    }
    res.json(companies);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/companies/:slug', async (req, res) => {
  try {
    const { slug } = req.params;
    let company = null;
    if (mongoose.connection.readyState === 1) {
      company = await Company.findOne({ slug });
    }
    if (!company) {
      company = FALLBACK_COMPANIES.find(c => c.slug === slug);
    }
    if (!company) return res.status(404).json({ error: 'Company not found' });
    res.json(company);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 3. Learning Hub Courses
app.get('/api/courses', async (req, res) => {
  try {
    let courses = [];
    if (mongoose.connection.readyState === 1) {
      courses = await Course.find();
    }
    if (!courses.length) {
      courses = FALLBACK_COURSES;
    }
    res.json(courses);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 4. Practice Questions & Drills
app.get('/api/practice/questions', async (req, res) => {
  try {
    const { topic } = req.query;
    let questions = [];
    if (mongoose.connection.readyState === 1) {
      const filter = topic && topic !== 'All' ? { topic } : {};
      questions = await Question.find(filter);
    }
    if (!questions.length) {
      questions = topic && topic !== 'All'
        ? FALLBACK_QUESTIONS.filter(q => q.topic.toLowerCase() === topic.toLowerCase())
        : FALLBACK_QUESTIONS;
    }
    res.json(questions);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 5. Submit Attempt
app.post('/api/practice/submit', async (req, res) => {
  try {
    const { topic, score, attemptType, feedback, timeTakenSec } = req.body;
    const newAttempt = {
      userId: 'student_1',
      studentName: 'Demo Student',
      topic: topic || 'Python',
      score: Number(score) || 80,
      attemptType: attemptType || 'drill',
      feedback: feedback || 'Completed interactive drill',
      timeTakenSec: Number(timeTakenSec) || 45,
      createdAt: new Date()
    };

    if (mongoose.connection.readyState === 1) {
      await Attempt.create(newAttempt);
    }

    res.json({ success: true, attempt: newAttempt });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Health check
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', stack: 'MERN', time: new Date() });
});

app.listen(PORT, () => {
  console.log(`🚀 MERN Express Server running on port ${PORT}`);
});
