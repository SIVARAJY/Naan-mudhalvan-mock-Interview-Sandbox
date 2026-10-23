import os
import json
import psycopg
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

with open("accurate_mcqs.json", "r", encoding="utf-8") as f:
    mcqs_by_cat = json.load(f)

# Connect to database
conn = psycopg.connect(DATABASE_URL)
cur = conn.cursor()

print("Connected to Supabase PostgreSQL.")

# 1. Ensure all 5 Courses exist
course_definitions = [
    {
        "id": 1,
        "title": "Python for Placement Coding",
        "description": "Master core Python data structures, OOP paradigms, list comprehensions, and algorithmic problem solving aligned with Naan Mudhalvan placement tracks.",
        "skill_topic": "Python",
        "nm_track": "Naan Mudhalvan · Software Development",
        "thumbnail": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=500&auto=format&fit=crop"
    },
    {
        "id": 2,
        "title": "Data Structures & Algorithms in Java",
        "description": "In-depth training on linear & non-linear data structures, trees, graphs, sorting, searching, and time complexity benchmarks for campus hiring rounds.",
        "skill_topic": "DSA",
        "nm_track": "Naan Mudhalvan · Advanced Problem Solving",
        "thumbnail": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&auto=format&fit=crop"
    },
    {
        "id": 3,
        "title": "Java Object-Oriented Programming & Core Concepts",
        "description": "Comprehensive Java curriculum covering JDK/JVM, OOP inheritance, polymorphism, interfaces, exception handling, and Collections Framework.",
        "skill_topic": "Java",
        "nm_track": "Naan Mudhalvan · Software Engineering",
        "thumbnail": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&auto=format&fit=crop"
    },
    {
        "id": 4,
        "title": "Database Management Systems & SQL Mastery",
        "description": "Foundations of relational databases, SQL queries, DDL/DML, normalization (1NF-BCNF), ACID transactions, indexing, and joins for technical interviews.",
        "skill_topic": "DBMS",
        "nm_track": "Naan Mudhalvan · Data Engineering",
        "thumbnail": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=500&auto=format&fit=crop"
    },
    {
        "id": 5,
        "title": "Full Stack Web Development (HTML, CSS, JS, Backend)",
        "description": "Modern web development covering HTML5 semantics, responsive CSS3/Flexbox/Grid, Vanilla JavaScript DOM, REST APIs, and web security best practices.",
        "skill_topic": "Web Development",
        "nm_track": "Naan Mudhalvan · Full Stack Web Track",
        "thumbnail": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=500&auto=format&fit=crop"
    }
]

for c in course_definitions:
    cur.execute("""
        INSERT INTO lh_courses (id, title, description, skill_topic, nm_track, thumbnail, is_active)
        VALUES (%s, %s, %s, %s, %s, %s, TRUE)
        ON CONFLICT (id) DO UPDATE SET
            title = EXCLUDED.title,
            description = EXCLUDED.description,
            skill_topic = EXCLUDED.skill_topic,
            nm_track = EXCLUDED.nm_track,
            thumbnail = EXCLUDED.thumbnail,
            is_active = TRUE
    """, (c["id"], c["title"], c["description"], c["skill_topic"], c["nm_track"], c["thumbnail"]))

# Update sequence for lh_courses
cur.execute("SELECT setval(pg_get_serial_sequence('lh_courses', 'id'), (SELECT MAX(id) FROM lh_courses))")

# 2. Define Lessons for each course with their exact 100 MCQs (split into lessons)
# Course 1: Python (100 MCQs -> 4 lessons, 25 MCQs each)
python_qs = mcqs_by_cat["Python"]
dsa_qs = mcqs_by_cat["DSA"]
java_qs = mcqs_by_cat["Java"]
dbms_qs = mcqs_by_cat["DBMS"]
web_qs = mcqs_by_cat["Web Development"]

lesson_definitions = [
    # Python (Course 1)
    {
        "id": 1, "course_id": 1, "title": "Python Basics, Data Types & Operators",
        "youtube_url": "https://www.youtube.com/watch?v=rfscVS0vtbw", "video_id": "rfscVS0vtbw",
        "duration_min": 25, "lesson_order": 1, "quiz": python_qs[0:25]
    },
    {
        "id": 2, "course_id": 1, "title": "Python Strings, Lists & Tuples",
        "youtube_url": "https://www.youtube.com/watch?v=_uQrJ0TkZlc", "video_id": "_uQrJ0TkZlc",
        "duration_min": 30, "lesson_order": 2, "quiz": python_qs[25:50]
    },
    {
        "id": 3, "course_id": 1, "title": "Python Dictionaries, Sets, Loops & Functions",
        "youtube_url": "https://www.youtube.com/watch?v=daefaLgNkw0", "video_id": "daefaLgNkw0",
        "duration_min": 35, "lesson_order": 3, "quiz": python_qs[50:75]
    },
    {
        "id": 4, "course_id": 1, "title": "Python OOP, Exceptions & File Handling",
        "youtube_url": "https://www.youtube.com/watch?v=Ej_02ICOIgs", "video_id": "Ej_02ICOIgs",
        "duration_min": 40, "lesson_order": 4, "quiz": python_qs[75:100]
    },

    # DSA (Course 2)
    {
        "id": 5, "course_id": 2, "title": "Arrays, Linked Lists & Complexity Analysis",
        "youtube_url": "https://www.youtube.com/watch?v=8hly31xKli0", "video_id": "8hly31xKli0",
        "duration_min": 30, "lesson_order": 1, "quiz": dsa_qs[0:25]
    },
    {
        "id": 6, "course_id": 2, "title": "Stacks, Queues & Evaluation Algorithms",
        "youtube_url": "https://www.youtube.com/watch?v=wjI1WNcIntg", "video_id": "wjI1WNcIntg",
        "duration_min": 35, "lesson_order": 2, "quiz": dsa_qs[25:50]
    },
    {
        "id": 7, "course_id": 2, "title": "Binary Trees, BST & Graph Traversals (BFS/DFS)",
        "youtube_url": "https://www.youtube.com/watch?v=oSWTXtMglKE", "video_id": "oSWTXtMglKE",
        "duration_min": 45, "lesson_order": 3, "quiz": dsa_qs[50:75]
    },
    {
        "id": 8, "course_id": 2, "title": "Searching, Sorting Algorithms & Heaps",
        "youtube_url": "https://www.youtube.com/watch?v=pkYVOmU3MgA", "video_id": "pkYVOmU3MgA",
        "duration_min": 40, "lesson_order": 4, "quiz": dsa_qs[75:100]
    },

    # Java (Course 3)
    {
        "id": 9, "course_id": 3, "title": "Java Fundamentals, Data Types & Operators",
        "youtube_url": "https://www.youtube.com/watch?v=eIrMbAQSU34", "video_id": "eIrMbAQSU34",
        "duration_min": 30, "lesson_order": 1, "quiz": java_qs[0:25]
    },
    {
        "id": 10, "course_id": 3, "title": "Control Flow, Arrays & String Manipulation",
        "youtube_url": "https://www.youtube.com/watch?v=A74TOX803D0", "video_id": "A74TOX803D0",
        "duration_min": 35, "lesson_order": 2, "quiz": java_qs[25:50]
    },
    {
        "id": 11, "course_id": 3, "title": "OOP Pillars: Inheritance, Polymorphism & Interfaces",
        "youtube_url": "https://www.youtube.com/watch?v=xk4_1vDrzzo", "video_id": "xk4_1vDrzzo",
        "duration_min": 40, "lesson_order": 3, "quiz": java_qs[50:75]
    },
    {
        "id": 12, "course_id": 3, "title": "Exception Handling & Collections Framework",
        "youtube_url": "https://www.youtube.com/watch?v=viTHCJM4G-Q", "video_id": "viTHCJM4G-Q",
        "duration_min": 40, "lesson_order": 4, "quiz": java_qs[75:100]
    },

    # DBMS (Course 4)
    {
        "id": 13, "course_id": 4, "title": "DBMS Architecture, Relational Models & SQL Basics",
        "youtube_url": "https://www.youtube.com/watch?v=HXV3zeQKqGY", "video_id": "HXV3zeQKqGY",
        "duration_min": 35, "lesson_order": 1, "quiz": dbms_qs[0:25]
    },
    {
        "id": 14, "course_id": 4, "title": "Keys, Constraints & Table Structure Modifications",
        "youtube_url": "https://www.youtube.com/watch?v=ztHopE5Wnpc", "video_id": "ztHopE5Wnpc",
        "duration_min": 30, "lesson_order": 2, "quiz": dbms_qs[25:50]
    },
    {
        "id": 15, "course_id": 4, "title": "Database Normalization (1NF-BCNF) & Joins",
        "youtube_url": "https://www.youtube.com/watch?v=UrYLYV7WSHM", "video_id": "UrYLYV7WSHM",
        "duration_min": 40, "lesson_order": 3, "quiz": dbms_qs[50:75]
    },
    {
        "id": 16, "course_id": 4, "title": "ACID Properties, Transactions, Indexing & Views",
        "youtube_url": "https://www.youtube.com/watch?v=7S_tz1z_5bA", "video_id": "7S_tz1z_5bA",
        "duration_min": 35, "lesson_order": 4, "quiz": dbms_qs[75:100]
    },

    # Web Development (Course 5)
    {
        "id": 17, "course_id": 5, "title": "HTML5 Semantic Markup & Web Structure",
        "youtube_url": "https://www.youtube.com/watch?v=kUMe1FH4CHE", "video_id": "kUMe1FH4CHE",
        "duration_min": 25, "lesson_order": 1, "quiz": web_qs[0:25]
    },
    {
        "id": 18, "course_id": 5, "title": "CSS3 Styling, Flexbox, Grid & Responsive Design",
        "youtube_url": "https://www.youtube.com/watch?v=1PnVor36_40", "video_id": "1PnVor36_40",
        "duration_min": 35, "lesson_order": 2, "quiz": web_qs[25:50]
    },
    {
        "id": 19, "course_id": 5, "title": "Vanilla JavaScript ES6+ & DOM Manipulation",
        "youtube_url": "https://www.youtube.com/watch?v=W6NZfCO5SIk", "video_id": "W6NZfCO5SIk",
        "duration_min": 45, "lesson_order": 3, "quiz": web_qs[50:75]
    },
    {
        "id": 20, "course_id": 5, "title": "Frontend React, Node.js Backend & Web Security",
        "youtube_url": "https://www.youtube.com/watch?v=7H_QH9nipNs", "video_id": "7H_QH9nipNs",
        "duration_min": 40, "lesson_order": 4, "quiz": web_qs[75:100]
    }
]

for l in lesson_definitions:
    cur.execute("""
        INSERT INTO lh_lessons (id, course_id, title, youtube_url, video_id, duration_min, lesson_order, quiz_data)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            course_id = EXCLUDED.course_id,
            title = EXCLUDED.title,
            youtube_url = EXCLUDED.youtube_url,
            video_id = EXCLUDED.video_id,
            duration_min = EXCLUDED.duration_min,
            lesson_order = EXCLUDED.lesson_order,
            quiz_data = EXCLUDED.quiz_data
    """, (
        l["id"], l["course_id"], l["title"], l["youtube_url"],
        l["video_id"], l["duration_min"], l["lesson_order"],
        json.dumps(l["quiz"])
    ))
    print(f"Uploaded {len(l['quiz'])} MCQs to Lesson {l['id']}: {l['title']}")

cur.execute("SELECT setval(pg_get_serial_sequence('lh_lessons', 'id'), (SELECT MAX(id) FROM lh_lessons))")

conn.commit()
conn.close()

print("\n SUCCESSFULLY UPLOADED ALL 500 MCQS INTO LEARNING HUB COURSES!")
