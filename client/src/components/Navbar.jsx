import React from 'react';
import { NavLink } from 'react-router-dom';

export default function Navbar() {
  return (
    <header className="topbar">
      <NavLink to="/" className="brand">
        SkillSandbox <span>NAAN MUDHALVAN · MERN EDITION</span>
      </NavLink>
      <nav>
        <NavLink to="/" className={({ isActive }) => isActive ? 'active' : ''}>Dashboard</NavLink>
        <NavLink to="/skills" className={({ isActive }) => isActive ? 'active' : ''}>Skill Analysis</NavLink>
        <NavLink to="/practice" className={({ isActive }) => isActive ? 'active' : ''}>Practice Arena</NavLink>
        <NavLink to="/companies" className={({ isActive }) => isActive ? 'active' : ''}>Company Guide</NavLink>
        <NavLink to="/learning" className={({ isActive }) => isActive ? 'active' : ''}>Learning Hub</NavLink>
      </nav>
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px', fontSize: '13px' }}>
        <span style={{ color: 'var(--mint-soft)' }}>Student Demo</span>
        <span className="pill gold" style={{ fontSize: '10px' }}>MERN Active</span>
      </div>
    </header>
  );
}
