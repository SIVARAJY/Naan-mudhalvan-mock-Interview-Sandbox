import re
import json

with open("parse_mcqs.py", "r", encoding="utf-8") as f:
    code = f.read()

raw_text = code.split('raw_text = """')[1].split('"""')[0]

# Split by "Part X: ..."
parts = re.split(r'(Part\s+\d+:.*?\(.*?\))', raw_text)

categorized = {
    "Web Development": [],
    "Java": [],
    "DBMS": [],
    "Python": [],
    "DSA": []
}

# Mapping each part to its corresponding course
current_category = None

for chunk in parts:
    chunk_clean = chunk.strip()
    if not chunk_clean:
        continue
    
    # Check if header
    header_match = re.match(r'Part\s+\d+:\s*(.*?)\s*\(', chunk_clean, re.IGNORECASE)
    if header_match:
        part_name = header_match.group(1).lower()
        if any(w in part_name for w in ["html", "css", "javascript", "frontend", "backend", "http", "security"]):
            current_category = "Web Development"
        elif any(w in part_name for w in ["java basics", "inheritance", "multithreading", "collections", "access modifiers"]) or (part_name in ["operators", "arrays and strings", "conditional statements and loops", "object-oriented programming", "exception handling"] and current_category in ["Java", None]):
            current_category = "Java"
        elif any(w in part_name for w in ["dbms", "sql", "keys", "normalization", "joins", "transactions", "acid", "indexing", "er model"]):
            current_category = "DBMS"
        elif any(w in part_name for w in ["python", "dictionaries and sets", "functions and modules"]):
            current_category = "Python"
        elif any(w in part_name for w in ["data structures", "linked list", "stack", "queue", "tree", "graph", "searching", "sorting", "hashing", "heap"]):
            current_category = "DSA"
        continue

    # Otherwise it's the question block
    lines = chunk_clean.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        q_match = re.match(r"^(\d+)\.\s*(.*)", line)
        if q_match and current_category:
            q_text = q_match.group(2).strip()
            
            # Next line options
            i += 1
            opt_line = lines[i].strip() if i < len(lines) else ""
            
            # Next line answer
            i += 1
            ans_line = lines[i].strip() if i < len(lines) else ""
            
            opt_pattern = r"A\)\s*(.*?)\s*B\)\s*(.*?)\s*C\)\s*(.*?)\s*D\)\s*(.*)"
            m_opt = re.match(opt_pattern, opt_line)
            options = []
            if m_opt:
                options = [m_opt.group(1).strip(), m_opt.group(2).strip(), m_opt.group(3).strip(), m_opt.group(4).strip()]
            else:
                parts_opt = re.split(r"[A-D]\)\s*", opt_line)
                options = [p.strip() for p in parts_opt if p.strip()]
                
            m_ans = re.search(r"Answer:\s*([A-D])\)", ans_line)
            ans_idx = 0
            if m_ans:
                ans_idx = ord(m_ans.group(1).upper()) - ord('A')
                
            categorized[current_category].append({
                "q": q_text,
                "options": options,
                "answer": ans_idx
            })
        i += 1

print({k: len(v) for k, v in categorized.items()})

with open("accurate_mcqs.json", "w", encoding="utf-8") as out:
    json.dump(categorized, out, indent=2)
