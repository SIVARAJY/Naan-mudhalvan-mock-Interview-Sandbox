import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function LearningHub() {
  const [courses, setCourses] = useState([]);
  const [activeLesson, setActiveLesson] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/courses')
      .then(res => {
        setCourses(res.data);
        if (res.data.length > 0 && res.data[0].lessons?.length > 0) {
          setActiveLesson(res.data[0].lessons[0]);
        }
      })
      .catch(() => {});
  }, []);

  return (
    <div className="container">
      <div style={{ marginBottom: '24px' }}>
        <p style={{ fontFamily: 'DM Mono', color: 'var(--green)', fontSize: '11px', letterSpacing: '1px' }}>
          STRUCTURED VIDEO CURRICULUM
        </p>
        <h1 style={{ fontSize: '28px', color: 'var(--teal)' }}>Learning Hub</h1>
        <p style={{ color: 'var(--muted)', fontSize: '14px' }}>
          Industry tracks curated to bridge conceptual weak areas identified during skill diagnostics.
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px', alignItems: 'start' }}>
        {/* Video Player Section */}
        <div className="panel" style={{ padding: '16px' }}>
          {activeLesson ? (
            <div>
              <div style={{ position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', borderRadius: '8px', background: '#000000', marginBottom: '14px' }}>
                <iframe
                  style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0 }}
                  src={`https://www.youtube.com/embed/${activeLesson.videoId}?rel=0`}
                  title={activeLesson.title}
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                ></iframe>
              </div>
              <h3 style={{ fontSize: '18px', color: 'var(--teal)', margin: '4px 0 6px' }}>{activeLesson.title}</h3>
              <span className="pill teal">{activeLesson.durationMin || 30} mins lesson</span>
            </div>
          ) : (
            <p>Select a lesson from below to start learning.</p>
          )}
        </div>

        {/* Course Modules List */}
        <div>
          <h3 style={{ fontSize: '18px', color: 'var(--teal)', marginBottom: '14px' }}>Available Skill Tracks</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
            {courses.map(course => (
              <div key={course._id || course.title} className="panel" style={{ padding: '18px', borderLeft: '4px solid var(--teal)' }}>
                <span className="pill gold" style={{ fontSize: '10px' }}>{course.nmTrack}</span>
                <h4 style={{ fontSize: '16px', color: 'var(--teal)', margin: '6px 0 4px' }}>{course.title}</h4>
                <p style={{ fontSize: '13px', color: 'var(--muted)', marginBottom: '12px' }}>{course.description}</p>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  {(course.lessons || []).map((lesson, idx) => (
                    <div
                      key={lesson.id || idx}
                      onClick={() => setActiveLesson(lesson)}
                      style={{
                        padding: '8px 12px',
                        borderRadius: '6px',
                        background: activeLesson?.videoId === lesson.videoId ? 'var(--mint-light)' : '#ffffff',
                        border: activeLesson?.videoId === lesson.videoId ? '1px solid var(--teal)' : '1px solid var(--line)',
                        cursor: 'pointer',
                        fontSize: '13px',
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center'
                      }}
                    >
                      <span>▶ {lesson.title}</span>
                      <small style={{ color: 'var(--muted)' }}>{lesson.durationMin}m</small>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
