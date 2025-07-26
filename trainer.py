# trainer.py
from datetime import datetime

def train(topic, source):
    try:
        with open(source, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"❌ File not found: {source}")
        return

    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    brain_entry = f"## 🧠 {topic}  ({now})\n\n{content}\n{'-'*40}\n"

    with open("amanai_brain.md", "a") as f:
        f.write(brain_entry)

    print(f"✅ Trained AmanAI on topic: {topic} from {source}")
