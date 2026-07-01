<div dir="rtl" align="right">

# 🔧 ابزارسرا

**فروشگاه آنلاین ابزارآلات — ساخته‌شده با Python و Flask**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![RTL](https://img.shields.io/badge/رابط_کاربری-فارسی_و_RTL-orange?style=flat-square)]()
[![License](https://img.shields.io/badge/مجوز-MIT-green?style=flat-square)]()

> از دریل بوش تا کمپرسور باد — هر ابزاری که برای پروژه‌ات لازم داری، اینجاست.

---

## 📖 درباره پروژه

**ابزارسرا** یک فروشگاه اینترنتی کامل برای فروش ابزارآلات صنعتی و خانگی است. رابط کاربری کاملاً **فارسی** و **راست‌چین (RTL)** طراحی شده و تمام منطق اصلی برنامه — محصولات، سبد خرید، فیلتر و جستجو — با **Python** پیاده‌سازی شده است.

این پروژه برای یادگیری Flask، ساخت فروشگاه‌های کوچک، یا به‌عنوان پایه‌ای برای توسعه یک e-commerce واقعی مناسب است.

---

## ✨ امکانات

| بخش | توضیح |
|-----|--------|
| 🏠 **صفحه اصلی** | بنر معرفی، آمار فروشگاه، دسته‌بندی‌ها و محصولات پرفروش |
| 🛍️ **کاتالوگ محصولات** | نمایش ۱۲+ محصول با تصویر، قیمت، امتیاز و برچسب تخفیف |
| 🔍 **جستجو و فیلتر** | جستجو بر اساس نام، فیلتر دسته‌بندی، مرتب‌سازی قیمت و امتیاز |
| 📦 **جزئیات محصول** | توضیحات کامل، انتخاب تعداد، محصولات مرتبط |
| 🛒 **سبد خرید** | افزودن/حذف/تغییر تعداد — ذخیره در Session |
| 📬 **تماس با ما** | فرم ارتباط با پیام‌های Flash |
| 📱 **واکنش‌گرا** | سازگار با موبایل، تبلت و دسکتاپ |

---

## 🛠️ تکنولوژی‌ها

```
Python 3.10+  →  منطق برنامه و داده محصولات
Flask 3.0+    →  فریم‌ورک وب
Jinja2        →  قالب‌های HTML
CSS3          →  طراحی RTL مدرن (فونت Vazirmatn)
Session       →  مدیریت سبد خرید
```

---

## 🚀 راه‌اندازی سریع

### پیش‌نیاز

- Python 3.10 یا بالاتر
- pip

### نصب و اجرا

```powershell
# رفتن به پوشه پروژه
cd tools-store

# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرای سرور
python app.py
```

مرورگر را باز کنید:

```
http://127.0.0.1:5000
```
برای باز کردن بهتره shift+ctrl+N 

---

## 📁 ساختار پروژه

```
tools-store/
│
├── app.py                 # 🌐 سرور Flask، مسیرها و سبد خرید
├── products.py            # 📋 داده محصولات و توابع جستجو
├── requirements.txt       # 📦 وابستگی‌های Python
├── README.md              # 📄 همین فایل
│
├── templates/             # 🎨 قالب‌های HTML (Jinja2)
│   ├── base.html          #    قالب پایه (هدر، فوتر، منو)
│   ├── index.html         #    صفحه اصلی
│   ├── products.html      #    لیست محصولات
│   ├── product_detail.html#    جزئیات محصول
│   ├── cart.html          #    سبد خرید
│   ├── contact.html       #    تماس با ما
│   └── _product_card.html #    کامپوننت کارت محصول
│
└── static/
    ├── css/style.css      # 🎭 استایل RTL
    └── js/main.js         # ⚡ منوی موبایل و Flash
```

---

## 🗺️ مسیرهای برنامه

| مسیر | متد | عملکرد |
|------|-----|--------|
| `/` | GET | صفحه اصلی |
| `/products` | GET | لیست محصولات (`?category=&q=&sort=`) |
| `/product/<id>` | GET | جزئیات یک محصول |
| `/cart` | GET | نمایش سبد خرید |
| `/cart/add/<id>` | POST | افزودن به سبد |
| `/cart/update/<id>` | POST | تغییر تعداد |
| `/cart/remove/<id>` | POST | حذف از سبد |
| `/contact` | GET/POST | فرم تماس |

---

## 🏷️ دسته‌بندی محصولات

| آیکون | دسته | شناسه |
|-------|------|--------|
| ⚡ | ابزار برقی | `electric` |
| 🔨 | ابزار دستی | `hand` |
| 📐 | اندازه‌گیری | `measure` |
| 🌿 | باغبانی | `garden` |

---

## 🧩 افزودن محصول جدید

فایل `products.py` را باز کنید و یک دیکشنری جدید به لیست `PRODUCTS` اضافه کنید:

```python
{
    "id": 13,
    "name": "نام محصول",
    "category": "electric",      # electric | hand | measure | garden
    "price": 1_500_000,
    "old_price": None,           # قیمت قبل از تخفیف (اختیاری)
    "rating": 4.5,
    "reviews": 10,
    "badge": "جدید",             # پرفروش | جدید | تخفیف | None
    "image": "https://...",
    "description": "توضیحات محصول...",
}
```

سرور را ری‌استارت کنید — محصول جدید خودکار نمایش داده می‌شود.

---

## 🔮 نقشه راه (ایده‌های توسعه)

- [ ] دیتابیس SQLite / PostgreSQL
- [ ] پنل مدیریت (Admin)
- [ ] ثبت‌نام و ورود کاربر
- [ ] درگاه پرداخت (زرین‌پال / IDPay)
- [ ] آپلود تصویر محصول
- [ ] API RESTful با Flask-RESTX

---

## ⚙️ تنظیمات

| متغیر | محل | توضیح |
|-------|-----|--------|
| `secret_key` | `app.py` | کلید Session — در production حتماً عوض کنید |
| `port` | `app.py` | پورت پیش‌فرض: `5000` |
| `debug` | `app.py` | حالت توسعه — در production خاموش کنید |

---

## 🤝 مشارکت

1. پروژه را Fork کنید
2. یک branch جدید بسازید (`git checkout -b feature/amazing-feature`)
3. تغییرات را commit کنید
4. Pull Request بفرستید

---

## 📄 مجوز

این پروژه تحت مجوز **MIT** منتشر شده — آزادانه استفاده، تغییر و توزیع کنید.

---

<p align="center">
  ساخته‌شده با ❤️ و Python
  <br><br>
  <strong>ابزارسرا</strong> — ابزار درست، کار درست 🔧
</p>

</div>
