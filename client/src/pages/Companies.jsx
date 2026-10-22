import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Companies() {
  const [companies, setCompanies] = useState([]);
  const [selectedCompany, setSelectedCompany] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/companies')
      .then(res => {
        setCompanies(res.data);
        if (res.data.length > 0) setSelectedCompany(res.data[0]);
      })
      .catch(() => {});
  }, []);

  return (
    <div className="container">
      <div style={{ marginBottom: '24px' }}>
        <p style={{ fontFamily: 'DM Mono', color: 'var(--green)', fontSize: '11px', letterSpacing: '1px' }}>
          CAMPUS HIRING PATTERNS
        </p>
        <h1 style={{ fontSize: '28px', color: 'var(--teal)' }}>Company Recruitment Guide</h1>
        <p style={{ color: 'var(--muted)', fontSize: '14px' }}>
          Round-by-round assessment formats, eligibility standards, and preparation strategies for top recruiters.
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '24px' }}>
        {/* Company List */}
        <div>
          <h3 style={{ fontSize: '16px', marginBottom: '12px', color: 'var(--teal)' }}>Select Target Company</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {companies.map(c => (
              <div
                key={c.slug}
                onClick={() => setSelectedCompany(c)}
                className="card"
                style={{
                  cursor: 'pointer',
                  border: selectedCompany?.slug === c.slug ? '2px solid var(--teal)' : '1px solid var(--line)',
                  background: selectedCompany?.slug === c.slug ? 'var(--mint-light)' : 'var(--card-bg)'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <strong style={{ fontSize: '15px' }}>{c.name}</strong>
                  <span className="pill teal">{c.tier}</span>
                </div>
                <p style={{ fontSize: '12px', color: 'var(--muted)', margin: '4px 0 0' }}>{c.industry}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Selected Company Details */}
        {selectedCompany && (
          <div className="panel" style={{ borderTop: '4px solid var(--gold)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '16px' }}>
              <div>
                <span className="pill gold" style={{ fontSize: '11px' }}>{selectedCompany.tier}</span>
                <h2 style={{ fontSize: '24px', color: 'var(--teal)', margin: '6px 0 2px' }}>{selectedCompany.name}</h2>
                <p style={{ color: 'var(--muted)', fontSize: '13px' }}>{selectedCompany.industry}</p>
              </div>
            </div>

            <div style={{ background: 'var(--mint-light)', padding: '12px 16px', borderRadius: '8px', marginBottom: '20px' }}>
              <strong style={{ fontSize: '13px', color: 'var(--teal)', display: 'block', marginBottom: '4px' }}>
                📋 Eligibility Criteria:
              </strong>
              <p style={{ fontSize: '13px', margin: 0, color: 'var(--ink)' }}>{selectedCompany.eligibility}</p>
            </div>

            <h3 style={{ fontSize: '16px', marginBottom: '12px', color: 'var(--teal)' }}>Recruitment Rounds Breakdown</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {(selectedCompany.rounds || []).map(r => (
                <div key={r.roundNum} style={{ border: '1px solid var(--line)', borderRadius: '8px', padding: '14px', background: '#ffffff', borderLeft: '4px solid var(--teal)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '6px' }}>
                    <strong style={{ color: 'var(--teal)' }}>Round {r.roundNum}: {r.name}</strong>
                    <span className="pill teal">{r.duration}</span>
                  </div>
                  <p style={{ fontSize: '13px', margin: '0 0 6px', color: 'var(--ink)' }}>{r.description}</p>
                  <p style={{ fontSize: '12px', margin: 0, color: 'var(--green)', fontWeight: 600 }}>💡 Tip: {r.tips}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
