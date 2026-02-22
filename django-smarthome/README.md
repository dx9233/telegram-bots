# Smart Home Landing | Django App

![Smart Home](screenshot.jpg)

- [Design](https://www.figma.com/design/HaPiHEKa8VQasoGUR2dE7M/Landing-page---%D0%A3%D0%BC%D0%BD%D1%8B%D0%B9-%D0%B4%D0%BE%D0%BC?node-id=1-571&t=Z5Zb8fFRk2UyUaeT-1)

## Tech Stack

<p align="left">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" alt="Python" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="40" height="40" alt="Django" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40" height="40" alt="HTML" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40" height="40" alt="CSS" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40" height="40" alt="JS" />
</p>

## Installation

1. **Clone or download** the project:

   ```bash
   git clone https://github.com/dx9233/smarthome-landing-django.git
   cd smarthome-landing-django
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install django
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

7. Open your browser:
   - Home page → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin panel → [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Project Structure

```
django-template/
├── app/
│   ├── settings.py
│   ├── urls.py
│   ├── ...
├── core/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── base.html
├── manage.py
└── db.sqlite3
```

---

## Customization

- Modify `core/templates/base.html` for your main layout.
- Add new apps using:

  ```bash
  python manage.py startapp your_app_name
  ```

- Register new apps in `app/settings.py` under `INSTALLED_APPS`.
