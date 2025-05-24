# 🚀 ddos-giants | العملاق للاختبار الأمني DDoS

**ddos-giants** is a professional open-source tool for Distributed Denial of Service (DDoS) attacks for **educational and ethical testing** purposes only.  
تم تطوير الأداة بالكامل بواسطة [خالد](https://github.com/nnnzjn-1)، وتتميز بالذكاء، وسهولة التحكم، ودعم الهجمات الحديثة.

---
## Features | المميزات

- Multiple attack modes: GET, POST, bypass, proxy_get, proxy_post  
- أوضاع هجوم متعددة: GET، POST، تجاوز الحماية، هجوم بـ proxy GET و proxy POST  
- Support for SOCKS5 and HTTP proxies  
- دعم لبروكسيات SOCKS5 و HTTP  
- Customizable POST data input  
- إمكانية إضافة بيانات POST مخصصة  
- High concurrency and performance using asyncio and aiohttp  
- أداء عالي باستخدام asyncio و aiohttp  
- Easy to use CLI interface  
- واجهة سطر أوامر سهلة الاستخدام

---
## Requirements | المتطلبات

- Python 3.8+  
- مكتبات Python: `aiohttp`, `async-timeout`  
يمكن تثبيتها عبر:

```bash
pip install aiohttp async-timeout

## 🛠️ Installation | التثبيت

```bash
# Update system & install essentials | تحديث النظام
apt update && apt install -y git python3 python3-pip

# Clone the project | استنساخ المشروع
git clone https://github.com/nnnzjn-1/ddos-giants.git
cd ddos-giants

# Install Python libraries | تثبيت المكتبات
pip3 install -r requirements.txt
```

---

## Usage | طريقة التشغيل

### Available Attack Modes | أوضاع الهجوم المتاحة:

| Mode        | Description (EN)                       | الوصف (عربي)                             |
|-------------|--------------------------------------|-----------------------------------------|
| GET         | Simple GET attack without proxy      | هجوم GET بسيط بدون استخدام بروكسي      |
| POST        | POST attack without proxy with data  | هجوم POST بدون بروكسي مع بيانات         |
| bypass      | Layer 7 bypass attack with proxies   | هجوم تجاوز طبقة 7 باستخدام البروكسي     |
| proxy_get   | GET attack with proxies               | هجوم GET باستخدام البروكسيات             |
| proxy_post  | POST attack with proxies and data    | هجوم POST باستخدام البروكسيات مع بيانات  |

---

### Usage Examples | أمثلة التشغيل:

```bash
# Simple GET attack for 60 seconds with 100 threads
python3 core/runner.py GET https://example.com 60 100

# POST attack for 60 seconds with 100 threads and POST data
python3 core/runner.py POST https://example.com 60 100 "" "param1=value1&param2=value2"

# Bypass attack with 60 seconds, 100 threads, using SOCKS5 proxies file
python3 core/runner.py bypass https://example.com 60 100 proxy/socks5.txt

# GET attack with 60 seconds, 100 threads, using HTTP proxies file
python3 core/runner.py proxy_get https://example.com 60 100 proxy/http.txt

# POST attack with 60 seconds, 100 threads, using HTTP proxies file and POST data
python3 core/runner.py proxy_post https://example.com 60 100 proxy/http.txt "param1=value1&param2=value2"
```

---

## 🌍 Web Interface  | واجهة الويب 

```bash
uvicorn web.app:app --host 0.0.0.0 --port 8000 --reload
```
Then open:  
ثم افتح: `http://localhost:8000`

---

## 🤖 Telegram Bot (soon) | بوت تيليجرام (قريبًا)

Remotely control and monitor attacks via Telegram.  
تحكم عن بعد واستلم الإشعارات عبر تيليجرام.

---

Notes | ملاحظات:
	•	For proxy modes (bypass, proxy_get, proxy_post), you must provide a proxy file containing proxies list.
	•	في أوضاع البروكسي، يجب توفير ملف يحتوي على قائمة البروكسيات.
	•	POST data should be URL encoded (e.g. param1=value1&param2=value2).
	•	بيانات POST يجب أن تكون مشفرة بصيغة URL.


## ⚠️ Legal Warning | ⚠️ تحذير قانوني

This tool is for **ethical testing and education only** with explicit permission from the system owner.  
هذه الأداة لأغراض اختبارية وتعليمية شرعية فقط، ويُمنع استخدامها ضد أي جهة دون إذن.

---

## 🧾 License | الترخيص

MIT License  
Developed by **Khaled** – [GitHub: nnnzjn-1](https://github.com/nnnzjn-1)
