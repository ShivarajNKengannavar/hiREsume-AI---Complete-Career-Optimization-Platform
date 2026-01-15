import os
import sqlite3
import datetime
from app import DB_PATH, get_gemini_response

def run_alerts():
    conn = sqlite3.connect(DB_PATH, timeout=30)
    c = conn.cursor()

    # Ensure table exists
    c.execute("""
    CREATE TABLE IF NOT EXISTS job_alerts (
        id TEXT PRIMARY KEY,
        email TEXT,
        whatsapp TEXT,
        keywords TEXT,
        location TEXT,
        frequency TEXT,
        resume_text TEXT,
        created_at TEXT
    )
    """)
    conn.commit()

    # Fetch saved alerts
    c.execute("SELECT id, email, whatsapp, keywords, location, frequency, resume_text FROM job_alerts")
    alerts = c.fetchall()

    if not alerts:
        print("No alerts found.")
        return

    for alert in alerts:
        alert_id, email, whatsapp, keywords, location, frequency, resume_text = alert

        print(f"\nChecking alerts for: {keywords} | {location}")

        job_prompt = f"""
        Based on these keywords: {keywords}
        And preferred location: {location}
        Give 5 possible job roles that match.
        Resume context:
        {resume_text}

        Respond briefly.
        """

        result = get_gemini_response(job_prompt)

        print("\nSuggestions:")
        print(result)

    conn.close()


if __name__ == "__main__":
    print("Job Alert Runner Started…")
    run_alerts()
