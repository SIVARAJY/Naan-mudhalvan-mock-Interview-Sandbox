import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

export default function Dashboard() {
  const [analysis, setAnalysis] = useState(null);
  const [courses, setCourses] = useState([]);
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/skills/analysis')
      .then(res => setAnalysis(res.data))
      .catch(() => {});

    axios.get('http://localhost:5000/api/courses')
      .then(res => setCourses(res.data))
      .catch(() => {});

    axios.get('http://localhost:5000/api/companies')
      .then(res => setCompanies(res.data))
      .catch(() => {});
  }, []);

  return (
    <div className="container">
      {/* Hero Banner */}
      <div className="panel" style={{ background: 'var(--teal)', color: '#ffffff', borderBottom: '4px solid var(--gold)' }}>
        <p style={{ fontFamily: 'DM Mono', fontSize: '11px', letterSpacing: '1.5px', color: 'var(--gold)', textTransform: 'uppercase' }}>
          NAAN MUDHALVAN ALIGNED · MERN PLATFORM
        </p>
        <h1 style={{ fontSize: '32px', margin: '8px 0 12px', letterSpacing: '-0.5px' }}>
          Practice. Measure. Secure Your Placement.
        </h1>
        <p style={{ color: 'var(--mint-soft)', maxWidth: '650px', marginBottom: '20px', fontSize: '14px' }}>
          End-to-end placement engineering sandbox powered by MongoDB, Express, React, and Node.js.
          Train across algorithms, evaluate readiness, and close conceptual gaps before campus drives.
        </p>
        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <Link to="/practice" className="button gold">⚡ Launch Practice Arena</Link>
          <Link to="/skills" className="button secondary">📊 Skill Diagnostics</Link>
          <Link to="/companies" className="button" style={{ background: 'rgba(255,255,255,0.15)', border: '1px solid rgba(255,255,255,0.3)' }}>
            🏢 Company Recruitment Guides
          </Link>
        </div>
      </div>

      {/* Stats row */}
      <div className="stats">
        <div className="stat">
          <span>Readiness Score</span>
          <strong>{analysis ? `${analysis.readinessScore}%` : '82%'}</strong>
          <small style={{ color: 'var(--green)', fontWeight: 700 }}>● Placement Ready Benchmark</small>
        </div>
        <div className="stat">
          <span>Target Companies</span>
          <strong>{companies.length || 3}+</strong>
          <small>TCS · Zoho · Infosys · Amazon</small>
        </div>
        <div className="stat">
          <span>Curated Courses</span>
          <strong>{courses.length || 3} Tracks</strong>
          <small>Aligned with Naan Mudhalvan syllabi</small>
        </div>
      </div>

      {/* Workspace Cards */}
      <h2 style={{ fontSize: '20px', marginBottom: '16px', color: 'var(--teal)' }}>Placement Training Workspace</h2>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '16px', marginBottom: '32px' }}>
        <Link to="/skills" className="card" style={{ textDecoration: 'none', color: 'inherit' }}>
          <span style={{ color: 'var(--green)', fontWeight: 800, fontSize: '12px' }}>01 / DIAGNOSTICS</span>
          <h3 style={{ margin: '8px 0 6px', fontSize: '18px' }}>📊 Intelligent Skill Analysis</h3>
          <p style={{ color: 'var(--muted)', fontSize: '13px' }}>Cross-assessment diagnostic: accuracy, weak-area detection, and readiness radar.</p>
          <span style={{ color: 'var(--green)', fontWeight: 700, fontSize: '13px', display: 'inline-block', marginTop: '10px' }}>
            View Readiness Radar →
          </span>
        </Link>

        <Link to="/practice" className="card" style={{ textDecoration: 'none', color: 'inherit' }}>
          <span style={{ color: 'var(--teal)', fontWeight: 800, fontSize: '12px' }}>02 / ARENA</span>
          <h3 style={{ margin: '8px 0 6px', fontSize: '18px' }}>⚡ Skill Practice Arena</h3>
          <p style={{ color: 'var(--muted)', fontSize: '13px' }}>MCQ drills, technical interview prompts, and timed coding rounds.</p>
          <span style={{ color: 'var(--green)', fontWeight: 700, fontSize: '13px', display: 'inline-block', marginTop: '10px' }}>
            Enter Arena →
          </span>
        </Link>

        <Link to="/companies" className="card" style={{ textDecoration: 'none', color: 'inherit' }}>
          <span style={{ color: 'var(--teal)', fontWeight: 800, fontSize: '12px' }}>03 / RECRUITMENT</span>
          <h3 style={{ margin: '8px 0 6px', fontSize: '18px' }}>🏢 Company Recruitment Guide</h3>
          <p style={{ color: 'var(--muted)', fontSize: '13px' }}>Round-by-round assessment breakdown, eligibility standards, and real questions.</p>
          <span style={{ color: 'var(--green)', fontWeight: 700, fontSize: '13px', display: 'inline-block', marginTop: '10px' }}>
            Explore Guides →
          </span>
        </Link>

        <Link to="/learning" className="card" style={{ textDecoration: 'none', color: 'inherit' }}>
          <span style={{ color: 'var(--teal)', fontWeight: 800, fontSize: '12px' }}>04 / LEARNING</span>
          <h3 style={{ margin: '8px 0 6px', fontSize: '18px' }}>📚 Learning Hub</h3>
          <p style={{ color: 'var(--muted)', fontSize: '13px' }}>Video courses, timestamped note-taking, and topic reinforcement.</p>
          <span style={{ color: 'var(--green)', fontWeight: 700, fontSize: '13px', display: 'inline-block', marginTop: '10px' }}>
            Watch Courses →
          </span>
        </Link>
      </div>
    </div>
  );
}
