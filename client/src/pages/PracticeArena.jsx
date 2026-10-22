import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function PracticeArena() {
  const [questions, setQuestions] = useState([]);
  const [selectedTopic, setSelectedTopic] = useState('All');
  const [currentIdx, setCurrentIdx] = useState(0);
  const [selectedOpt, setSelectedOpt] = useState(null);
  const [answered, setAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [hintsRevealed, setHintsRevealed] = useState(0);
  const [streak] = useState(5);

  const topics = ['All', 'Python', 'Java', 'DSA', 'DBMS', 'Web Development'];

  useEffect(() => {
    fetchQuestions(selectedTopic);
  }, [selectedTopic]);

  const fetchQuestions = (topic) => {
    const url = topic === 'All'
      ? 'http://localhost:5000/api/practice/questions'
      : `http://localhost:5000/api/practice/questions?topic=${encodeURIComponent(topic)}`;

    axios.get(url)
      .then(res => {
        setQuestions(res.data);
        setCurrentIdx(0);
        setAnswered(false);
        setSelectedOpt(null);
        setHintsRevealed(0);
      })
      .catch(() => {});
  };

  const handleSelectOption = (opt) => {
    if (answered) return;
    setSelectedOpt(opt);
    setAnswered(true);

    const currentQ = questions[currentIdx];
    const isCorrect = opt.trim() === currentQ.correctAnswer.trim();

    if (isCorrect) {
      setScore(prev => prev + 10);
    }

    // Submit attempt to backend
    axios.post('http://localhost:5000/api/practice/submit', {
      topic: currentQ.topic,
      score: isCorrect ? 100 : 0,
      attemptType: 'drill'
    }).catch(() => {});
  };

  const nextQuestion = () => {
    if (currentIdx < questions.length - 1) {
      setCurrentIdx(prev => prev + 1);
      setSelectedOpt(null);
      setAnswered(false);
      setHintsRevealed(0);
    }
  };

  const currentQ = questions[currentIdx];

  return (
    <div className="container">
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <p style={{ fontFamily: 'DM Mono', color: 'var(--green)', fontSize: '11px', letterSpacing: '1px' }}>
            LOW-PRESSURE SKILL DRILL
          </p>
          <h1 style={{ fontSize: '28px', color: 'var(--teal)' }}>Practice Arena</h1>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <span className="pill gold">🔥 {streak} Day Streak</span>
          <span className="pill teal">Score: {score} pts</span>
        </div>
      </div>

      {/* Topic Filter Pills */}
      <div style={{ display: 'flex', gap: '8px', marginBottom: '24px', flexWrap: 'wrap' }}>
        {topics.map(t => (
          <button
            key={t}
            onClick={() => setSelectedTopic(t)}
            className={`button ${selectedTopic === t ? '' : 'secondary'}`}
            style={{ fontSize: '12px', padding: '6px 12px' }}
          >
            {t}
          </button>
        ))}
      </div>

      {/* Question Card */}
      {currentQ ? (
        <div className="panel" style={{ borderTop: '4px solid var(--teal)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '14px' }}>
            <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
              <span className="pill teal">{currentQ.topic}</span>
              <span className="pill gold">{currentQ.difficulty || 'medium'}</span>
              <span style={{ fontSize: '12px', color: 'var(--muted)' }}>Question {currentIdx + 1} of {questions.length}</span>
            </div>
          </div>

          <h2 style={{ fontSize: '19px', color: 'var(--ink)', marginBottom: '12px' }}>{currentQ.title}</h2>
          <p style={{ fontSize: '15px', lineHeight: '1.6', marginBottom: '24px' }}>{currentQ.question}</p>

          {/* Options for MCQ */}
          {currentQ.options && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginBottom: '20px' }}>
              {currentQ.options.map((opt, i) => {
                let bg = '#ffffff';
                let border = '1px solid var(--line)';

                if (answered) {
                  if (opt.trim() === currentQ.correctAnswer.trim()) {
                    bg = 'var(--mint-light)';
                    border = '2px solid var(--green)';
                  } else if (selectedOpt === opt) {
                    bg = '#FFF0F0';
                    border = '2px solid #D32F2F';
                  }
                }

                return (
                  <div
                    key={i}
                    onClick={() => handleSelectOption(opt)}
                    style={{
                      padding: '12px 16px',
                      borderRadius: '8px',
                      background: bg,
                      border: border,
                      cursor: answered ? 'default' : 'pointer',
                      fontWeight: 500,
                      transition: 'all 0.15s'
                    }}
                  >
                    <span style={{ fontFamily: 'DM Mono', marginRight: '10px', fontWeight: 700 }}>
                      {String.fromCharCode(65 + i)}.
                    </span>
                    {opt}
                  </div>
                );
              })}
            </div>
          )}

          {/* Hints Section */}
          {currentQ.hints && currentQ.hints.length > 0 && (
            <div style={{ marginBottom: '20px' }}>
              {hintsRevealed < currentQ.hints.length && (
                <button
                  onClick={() => setHintsRevealed(prev => prev + 1)}
                  className="button secondary"
                  style={{ fontSize: '12px', padding: '6px 12px' }}
                >
                  💡 Need a hint? Reveal Hint {hintsRevealed + 1} (-5 pts)
                </button>
              )}
              {hintsRevealed > 0 && (
                <div style={{ marginTop: '10px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {currentQ.hints.slice(0, hintsRevealed).map((h, idx) => (
                    <div key={idx} style={{ background: '#FFF9E6', border: '1px solid #FDE6A6', borderRadius: '8px', padding: '10px 14px', fontSize: '13px', color: '#7A5500' }}>
                      <strong>Hint {idx + 1}:</strong> {h}
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {/* Explanation Box on Answer */}
          {answered && currentQ.explanation && (
            <div style={{ background: 'var(--mint-light)', border: '1px solid var(--line)', borderRadius: '8px', padding: '14px', marginBottom: '20px' }}>
              <strong style={{ color: 'var(--teal)', display: 'block', marginBottom: '4px' }}>💡 Solution Explanation:</strong>
              <p style={{ fontSize: '13px', margin: 0, color: 'var(--ink)' }}>{currentQ.explanation}</p>
            </div>
          )}

          {/* Next Button */}
          {answered && (
            <div style={{ textAlign: 'right' }}>
              {currentIdx < questions.length - 1 ? (
                <button onClick={nextQuestion} className="button gold">Next Question →</button>
              ) : (
                <p style={{ color: 'var(--green)', fontWeight: 700 }}>✓ Drill completed! Great effort.</p>
              )}
            </div>
          )}
        </div>
      ) : (
        <div className="panel" style={{ textAlign: 'center', padding: '40px' }}>
          <p>No questions found for this topic filter.</p>
        </div>
      )}
    </div>
  );
}
