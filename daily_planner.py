# daily_planner.py

from datetime import datetime

def generate_plan():
    today = datetime.now().strftime("%A, %d %B %Y")
    plan = f"""🧠 AmanAI Daily Plan – {today}

📌 Morning:
- ✅ Review yesterday's log
- 📖 Study 1 topic from core field (e.g., Web Dev / DSA / ML)
- ✍️ Summarize learnings into brain module

📌 Afternoon:
- 💻 Work on a live project
- 🧪 Add notes to 'scientist' log

📌 Evening:
- 📓 Log daily learnings
- 🚀 Push to GitHub
- 🌍 Optional: Write or post something publicly

🛠️ Status: [ ] Planned   [ ] In Progress   [ ] Completed

"""
    with open("today_plan.md", "w") as f:
        f.write(plan)
    print("✅ Daily plan created as 'today_plan.md'")
