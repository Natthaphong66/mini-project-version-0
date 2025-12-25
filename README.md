# EzShop - Mini Project Version 0

ระบบซื้อ-ขายสินค้าออนไลน์ พัฒนาด้วย Django Framework

## ความสามารถของระบบ

- แสดงหน้าแรกของระบบ (Homepage)
- คลิกไปหน้ารายการสินค้า (Products Page)
- ออกแบบ UI สวยงามด้วย Tailwind CSS

## การติดตั้งและใช้งาน

### 1. Clone โปรเจค

```bash
git clone https://github.com/Natthaphong66/mini-project-version-0.git
cd mini-project-version-0
```

### 2. สร้าง Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# หรือ
source .venv/bin/activate  # macOS/Linux
```

### 3. ติดตั้ง Dependencies

```bash
pip install django
```

### 4. รัน Server

```bash
cd mysite
python manage.py runserver
```

### 5. เปิดใช้งาน

เปิดเบราว์เซอร์ไปที่: http://127.0.0.1:8000/

## โครงสร้างโปรเจค

```
mini-project-version-0/
├── mysite/                    # Django Project
│   ├── mysite/               # Project Settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── myapp/                # Main Application
│   │   ├── views.py          # View functions
│   │   ├── urls.py           # URL patterns
│   │   └── templates/        # HTML Templates
│   │       └── myapp/
│   │           ├── home.html
│   │           └── products.html
│   └── manage.py
└── README.md
```

## หน้าเว็บที่มี

| URL          | หน้า     | คำอธิบาย                              |
| ------------ | -------- | ------------------------------------- |
| `/`          | Home     | หน้าแรก แสดง banner และหมวดหมู่สินค้า |
| `/products/` | Products | หน้ารายการสินค้าทั้งหมด               |

## เทคโนโลยีที่ใช้

- **Backend:** Django 6.0
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (default)

## ผู้พัฒนา

- **Name:** Natthaphong
- **GitHub:** [Natthaphong66](https://github.com/Natthaphong66)

## License

MIT License
