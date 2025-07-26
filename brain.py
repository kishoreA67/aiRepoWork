# brain.py
import random
import os
from datetime import datetime

BRAIN_FILE = "amanai_brain.md"

def store_thought(topic, content):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n## 🧠 {topic}  ({now})\n\n{content}\n{'-'*40}\n"

    with open(BRAIN_FILE, "a") as f:
        f.write(entry)
    
    print(f"✅ Thought stored in {BRAIN_FILE} under topic: {topic}")

def read_brain():
    if os.path.exists(BRAIN_FILE):
        with open(BRAIN_FILE, "r") as f:
            print(f.read())
    else:
        print("🧠 Brain is empty. Start storing thoughts!")



def quiz(topic):
    with open("amanai_brain.md", "r") as f:
        content = f.read()

    blocks = content.split("## 🧠 ")
    questions = []

    for block in blocks:
        if topic in block:
            lines = block.strip().split("\n")[1:]  # skip title
            for line in lines:
                if line.strip() and not line.startswith("---"):
                    q = line.strip()
                    questions.append(q)

    if not questions:
        print(f"❌ No content found for topic: {topic}")
        return

    print(f"🧪 Quiz on: {topic}")
    score = 0

    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: What do you remember about this?\n➡️  {q}")
        input("Your answer: ")
        print(f"✅ Stored Info: {q}")
        score += 1

    print(f"\n🧠 Quiz complete: {score}/{len(questions)} questions reviewed.")


def brain_summary():
    if not os.path.exists(BRAIN_FILE):
        print("🧠 Brain is empty.")
        return

    with open(BRAIN_FILE, "r") as f:
        content = f.read()

    blocks = content.split("## 🧠 ")
    summary = {}

    for block in blocks[1:]:
        title_line = block.split("\n")[0]
        topic = title_line.split("  ")[0]
        if topic not in summary:
            summary[topic] = 0
        summary[topic] += 1

    print("\n🧠 Weekly Summary of Learned Topics:")
    for topic, count in summary.items():
        print(f"🔹 {topic} — {count} entries")

    print("\n📅 Summary complete.")
