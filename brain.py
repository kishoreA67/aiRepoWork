# brain.py

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

