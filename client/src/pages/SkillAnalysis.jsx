import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

export default function SkillAnalysis() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:5000/api/skills/analysis')
      .then(res => {
        setData(res.data);
        setLoading(false);
      })
      .catch(() => {
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container"><p>Loading skill analytics from MongoDB...</p></div>;

  return (
    <div className="container">
      <div style={{ marginBottom: '24px' }}>
        <p style={{ fontFamily: 'DM Mono', color: 'var(--green)', fontSize: '11px', letterSpacing: '1px' }}>
          INTELLIGENT PERFORMANCE DIAGNOSTICS
        </p>
        <h1 style={{ fontSize: '28px', color: 'var(--teal)' }}>Skill Analysis & Improvement Tracker</h1>
        <p style={{ color: 'var(--muted)', fontSize: '14px' }}>
          Real-time metrics calculated from your interactive practice sessions and algorithmic tasks.
        </p>
      </div>

      {/* Index Banner */}
      <div className="panel" style={{ background: 'var(--teal)', color: '#ffffff', borderBottom: '4px solid var(--gold)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '20px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '24px' }}>
          <div style={{ border: '3px solid var(--gold)', borderRadius: '50%', width: '90px', height: '90px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', background: 'rgba(255,255,255,0.06)' }}>
            <span style={{ fontSize: '26px', fontWeight: 800, color: 'var(--gold)' }}>{data?.readinessScore || 82}%</span>
            <span style={{ fontSize: '9px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>Readiness</span>
          </div>
          <div>
            <span className="pill green" style={{ fontSize: '10px' }}>{data?.readinessStatus || 'Placement Ready'}</span>
            <h2 style={{ fontSize: '20px', margin: '4px 0', color: '#ffffff' }}>{data?.readinessTitle || 'Strong Technical Placement Standing'}</h2>
            <p style={{ color: 'var(--mint-soft)', fontSize: '13px', margin: 0, maxWidth: '500px' }}>
              {data?.readinessDesc || 'Evaluates algorithmic proficiency, coding speed, and conceptual depth.'}
            </p>
          </div>
        </div>
        <div>
          <Link to="/practice" className="button gold">⚡ Practice Weak Areas</Link>
        </div>
      </div>

      {/* Strengths & Weaknesses */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px', marginBottom: '28px' }}>
        <div className="panel" style={{ borderLeft: '4px solid var(--green)' }}>
          <h3 style={{ fontSize: '16px', color: 'var(--green)', marginBottom: '8px' }}>✓ Identified Strengths (≥70%)</h3>
          <p style={{ color: 'var(--muted)', fontSize: '12px', marginBottom: '14px' }}>Domains where you have consistently scored high:</p>
          {(data?.strengths || []).map((s, i) => (
            <div key={i} style={{ background: 'var(--mint-light)', padding: '10px 14px', borderRadius: '8px', marginBottom: '8px', display: 'flex', justifyContent: 'space-between' }}>
              <strong>{s.name}</strong>
              <span className="pill green">{s.accuracy}% Accuracy</span>
            </div>
          ))}
        </div>

        <div className="panel" style={{ borderLeft: '4px solid #d9534f' }}>
          <h3 style={{ fontSize: '16px', color: '#d9534f', marginBottom: '8px' }}>⚠️ Target Improvement Areas</h3>
          <p style={{ color: 'var(--muted)', fontSize: '12px', marginBottom: '14px' }}>Topics requiring focused reinforcement before interviews:</p>
          {(data?.weaknesses || []).map((w, i) => (
            <div key={i} style={{ background: '#FFF5F5', border: '1px solid #FED7D7', padding: '10px 14px', borderRadius: '8px', marginBottom: '8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <strong style={{ color: '#C53030' }}>{w.name}</strong>
                <span style={{ fontSize: '11px', display: 'block', color: 'var(--muted)' }}>{w.accuracy}% average score</span>
              </div>
              <Link to="/practice" className="button" style={{ fontSize: '11px', padding: '4px 8px' }}>Practice</Link>
            </div>
          ))}
        </div>
      </div>

      {/* Topic Matrix */}
      <div className="panel">
        <h3 style={{ fontSize: '18px', color: 'var(--teal)', marginBottom: '16px' }}>Core Syllabus Breakdown</h3>
        {(data?.topicMatrix || []).map((topic, i) => (
          <div key={i} style={{ marginBottom: '18px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
              <strong>{topic.name}</strong>
              <span style={{ fontWeight: 700, color: topic.accuracy >= 70 ? 'var(--green)' : 'var(--teal)' }}>
                {topic.accuracy}%
              </span>
            </div>
            <div className="progress-bar">
              <div className="progress-fill" style={{ width: `${topic.accuracy}%`, background: topic.accuracy >= 70 ? 'var(--green)' : 'var(--teal)' }}></div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
