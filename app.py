from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Shyam Sunder Sharma"  # Replace with your full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)  # Convert UTC to IST
    top_output = subprocess.getoutput("top -b -n 1 | head -10")  # Fetch `top` command output

    html_content = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time.strftime("%Y-%m-%d %H:%M:%S")}</p>
    <pre>{top_output}</pre>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
