# 🚀 ddos-giants | العملاق للاختبار الأمني DDoS

**ddos-giants** is a professional open-source tool for Distributed Denial of Service (DDoS) attacks for **educational and ethical testing** purposes only.  
تم تطوير الأداة بالكامل بواسطة [خالد](https://github.com/nnnzjn-1)، وتتميز بالذكاء، وسهولة التحكم، ودعم الهجمات الحديثة.

---

## 🧠 Features | الميزات

- 🔥 50+ attack methods (Layer 4 / Layer 7) | أكثر من 50 طريقة هجوم
- 🛡️ Cloudflare/OVH bypass | تجاوز حمايات ذكية
- 🌐 Web Dashboard | لوحة تحكم ويب
- 🤖 Telegram Bot (soon) | بوت تيليجرام للتحكم (قريبًا)
- 🔌 Proxy System: HTTP/SOCKS | نظام بروكسيات متكامل
- 💾 SQLite DB for logs and stats | قاعدة بيانات لحفظ الإحصائيات
- 🧩 Modular Plugin System | دعم الإضافات المخصصة

---

## ⚙️ Requirements | المتطلبات

- Python 3.8+
- pip
- Git
- Linux / Termux / Pydroid / VPS

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

## 🚦 Usage (Layer 7 Attack) | طريقة التشغيل

```bash
# Example: Bypass attack with 100 threads and SOCKS5 proxies
# مثال: هجوم Bypass بـ 100 خيط وبروكسي SOCKS5
python3 core/runner.py bypass https://example.com 60 100 proxy/socks5.txt
```

---

## 🌍 Web Interface (soon) | واجهة الويب (قريبًا)

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

## ⚠️ Legal Warning | ⚠️ تحذير قانوني

This tool is for **ethical testing and education only** with explicit permission from the system owner.  
هذه الأداة لأغراض اختبارية وتعليمية شرعية فقط، ويُمنع استخدامها ضد أي جهة دون إذن.

---

## 🧾 License | الترخيص

MIT License  
Developed by **Khaled** – [GitHub: nnnzjn-1](https://github.com/nnnzjn-1)
