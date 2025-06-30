# ToDoNow 📝

**ToDoNow** es una aplicación web de lista de tareas (*to‑do list*) desarrollada en Django (versión 5.2.2) que permite a los usuarios registrarse, iniciar sesión y gestionar sus tareas personales con fechas de vencimiento, prioridad y estado de completado.  

> ⚙️ **Stack técnico**  
> - **Backend**: Python 3.10+ · Django 5.2.2 · Django REST Framework 3.16.0  
> - **Base de datos**: SQLite (por defecto) / PostgreSQL (opcional)  
> - **Depósito de estáticos**: WhiteNoise · Gunicorn para producción  
> - **Autenticación**: Forms de Django (`UserCreationForm`) y sistema de sesiones  
> - **CORS**: django‑cors‑headers  
> - **Tipado estático**: django‑stubs · mypy_extensions  

---

## 🚀 Características (2025)

- **Registro y login** de usuarios con validación y mensajes de éxito/error.  
- **CRUD completo** de tareas: crear, listar, editar, marcar como completada y eliminar.  
- **Campos de tarea**:  
  - Título y descripción libre.  
  - Fecha y hora de vencimiento (`datetime-local`).  
  - Marcar prioridad.  
  - Estado de completado.  
- **Filtrado** por sección:  
  - Todas las tareas  
  - Pendientes  
  - Completadas  
- **Despliegue preparado**:  
  - Configurable via variables de entorno (`SECRET_KEY`, `DEBUG`, `DATABASE_URL`, `PA_USERNAME`).  
  - Soporta SQLite para desarrollo y PostgreSQL en producción.  
  - WhiteNoise para servir archivos estáticos con `CompressedManifestStaticFilesStorage`.  
  - Gunicorn como servidor WSGI.  

---

## 🔧 Instalación y ejecución local

1. **Clonar el repositorio**  
   
   ```bash
   git clone https://github.com/Artarexces/ToDoNow.git
   cd ToDoNow 
   ```

2. **Crear entorno virtual e instalar dependencias**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. **Configurar variables de entorno**
  Crea un archivo .env en la raíz con al menos:

```ini
SECRET_KEY="tu-secret-key-de-Django"
DEBUG=True
DATABASE_URL="sqlite:///$(pwd)/db.sqlite3"
PA_USERNAME="tu-usuario-pythonanywhere"   # sólo si despliegas en PythonAnywhere
```

4. **Migraciones y superusuario**

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Levantar servidor de desarrollo**

```bash
python manage.py runserver
Accede en tu navegador a http://localhost:8000/.
```

--- 

## ⚙️ Despliegue en producción
1. **Configura DEBUG=False y DATABASE_URL apuntando a tu base PostgreSQL.**

2. **Recolecta estáticos**

```bash
python manage.py collectstatic --no-input
```

4. **Levanta con Gunicorn**

```bash
gunicorn todonow.wsgi:application --bind 0.0.0.0:$PORT
```

5. **Configura tu host (Heroku, PythonAnywhere, AWS, etc.) usando las variables de entorno.** 

---

## 📂 Estructura del proyecto

```bash
ToDoNow/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── tasks/
│   ├── migrations/
│   ├── templates/tasks/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── todonow/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── static/      # CSS, imágenes, JS
```
---

## 🤝 Contribuciones
¡Todas las contribuciones son bienvenidas! Para nuevas funcionalidades o correcciones:

1. **Haz un fork del repositorio.**

2. **Crea una rama para tu feature:**
```bash
git checkout -b feature/nombre-descriptivo
```

3. **Realiza tus cambios y commits.**

4. **Sube tu rama y abre un Pull Request.**

---

## 📬 Contacto
Autor: Martin Rodriguez (@Artarexces)

Email: martinrodriguezdev96@gmail.com

¡Gracias por usar ToDoNow! 🎉