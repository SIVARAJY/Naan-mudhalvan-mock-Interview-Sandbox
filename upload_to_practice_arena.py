import os
import json
import psycopg
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

with open("accurate_mcqs.json", "r", encoding="utf-8") as f:
    mcqs_by_cat = json.load(f)

conn = psycopg.connect(DATABASE_URL)
cur = conn.cursor()

print("Connected to PostgreSQL on Supabase.")

# Map topics to official Naan Mudhalvan tracks
track_map = {
    "Python": "Naan Mudhalvan · Software Development",
    "DSA": "Naan Mudhalvan · Advanced Problem Solving",
    "Java": "Naan Mudhalvan · Software Engineering",
    "DBMS": "Naan Mudhalvan · Data Engineering",
    "Web Development": "Naan Mudhalvan · Full Stack Web Track"
}

total_inserted = 0

for topic, q_list in mcqs_by_cat.items():
    track = track_map.get(topic, "Naan Mudhalvan · Technical Track")
    print(f"\nProcessing {len(q_list)} questions for topic: {topic}...")

    for idx, q_obj in enumerate(q_list, 1):
        question_text = q_obj["q"]
        options = q_obj["options"]
        ans_idx = q_obj["answer"]
        
        # Ensure answer string is the exact text of the correct option
        if 0 <= ans_idx < len(options):
            correct_answer_str = options[ans_idx]
        else:
            correct_answer_str = options[0] if options else ""

        # Title: concise preview of question
        title = question_text[:50].strip()
        if len(question_text) > 50:
            title += "..."

        # Progressive difficulty spread
        if idx <= 40:
            difficulty = "easy"
        elif idx <= 80:
            difficulty = "medium"
        else:
            difficulty = "hard"

        # Generate progressive hints
        hints = [
            f"Think about core {topic} syntax and foundational principles.",
            f"Eliminate choices that violate standard {topic} runtime behavior."
        ]
        
        explanation = f"Correct Answer: {correct_answer_str}. This is a fundamental concept in {topic}."

        cur.execute("""
            INSERT INTO prac_questions (
                topic, nm_track, difficulty, q_type, title, question,
                options, correct_answer, explanation, hints, starter_code, test_cases, is_active
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, TRUE)
        """, (
            topic,
            track,
            difficulty,
            "mcq",
            title,
            question_text,
            json.dumps(options),
            correct_answer_str,
            explanation,
            json.dumps(hints),
            "",
            json.dumps([])
        ))
        total_inserted += 1

conn.commit()

# Verify counts in prac_questions
cur.execute("SELECT topic, q_type, COUNT(*) FROM prac_questions GROUP BY topic, q_type ORDER BY topic, q_type")
rows = cur.fetchall()
print("\nUpdated Practice Arena Question Bank Summary:")
for r in rows:
    print(f" - {r[0]} ({r[1]}): {r[2]} questions")

cur.execute("SELECT COUNT(*) FROM prac_questions")
grand_total = cur.fetchone()[0]
print(f"\n🎉 Total Questions in Practice Arena: {grand_total}")

conn.close()
