import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import SkillAnalysis from './pages/SkillAnalysis';
import PracticeArena from './pages/PracticeArena';
import Companies from './pages/Companies';
import LearningHub from './pages/LearningHub';

export default function App() {
  return (
    <BrowserRouter>
      <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
        <Navbar />
        <main style={{ flex: 1 }}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/skills" element={<SkillAnalysis />} />
            <Route path="/practice" element={<PracticeArena />} />
            <Route path="/companies" element={<Companies />} />
            <Route path="/learning" element={<LearningHub />} />
          </Routes>
        </main>
        <footer>
          Naan Mudhalvan SkillSandbox · MERN Stack Edition (MongoDB, Express, React, Node.js)
        </footer>
      </div>
    </BrowserRouter>
  );
}
