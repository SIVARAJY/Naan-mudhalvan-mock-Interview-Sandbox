import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(DATABASE_URL)
cur = conn.cursor()

print("Connected to PostgreSQL on Supabase.")

# Reset quiz_data for all lessons in Learning Hub
cur.execute("UPDATE lh_lessons SET quiz_data = '[]'::jsonb")
conn.commit()

cur.execute("SELECT COUNT(*) FROM lh_lessons WHERE quiz_data != '[]'::jsonb")
remaining = cur.fetchone()[0]
print(f"Lessons with quizzes remaining: {remaining}")

cur.execute("SELECT COUNT(*) FROM lh_lessons")
total_lessons = cur.fetchone()[0]
print(f"Total Learning Hub lessons now updated: {total_lessons}")

conn.close()
print("Successfully removed all MCQs from Learning Hub.")
