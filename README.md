# SdGE-FastAPI-practica
API realizada con FastAPI y Python en IntelliJ

---

## Descripción del proyecto
Esta práctica proporciona una API REST que permite consultar información de empleados y departamentos almacenada en una base de datos SQLite.  
La aplicación está desarrollada con FastAPI y organizada en módulos independientes para modelos, rutas y gestión de base de datos.

---

## Funcionalidades principales
- Endpoints para consultar empleados.
- Endpoints para consultar departamentos.
- Creación automática de tablas al iniciar la API.
- Arquitectura modular (rutas, modelos, base de datos).
- Base de datos SQLite integrada en el proyecto.
- Respuestas rápidas y documentación automática generada por FastAPI.

---

## Tecnologías utilizadas
- **Python 3**
- **FastAPI**
- **SQLModel / SQLite**
- **IntelliJ**

---

## Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/DAM-Fran/SdGE-FastAPI-practica
```

### 2. Instalar dependencias
Desde el directorio del proyecto:
```bash
pip install fastapi sqlmodel fastapi[standard]
```

### 3. Ejecutar la API
```bash
fastapi dev main.py
```

### 4. Acceder a la documentación interactiva
- Documentación Swagger UI: http://127.0.0.1:8000/docs (127.0.0.1 in Bing)
- Documentación alternativa ReDoc: http://127.0.0.1:8000/redoc (127.0.0.1 in Bing)

---

## Screenshots de la aplicación en pantalla

![Captura de la aplicación](Captura%20API%20docs.png)

---

## Estructura del proyecto
```
practica/
│
├── models/               → Modelos de datos (Empleado, Departamento)
├── routers/              → Rutas de la API (empleados, departamentos)
│
├── database.py           → Conexión y creación de tablas SQLite
├── database.db           → Base de datos SQLite
├── main.py               → Punto de entrada de la API
├── __init__.py
└── README.md
```
---

## Funcionamiento interno
El archivo `main.py` registra los routers y crea las tablas al iniciar la API:

```python
from fastapi import FastAPI
from practica.database import create_db_and_tables
from practica.routers import departamentos, empleados

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(departamentos.router)
app.include_router(empleados.router)
```

---

## Licencia

Proyecto académico desarrollado para la asignatura de **Sistemas de Gestión Empresarial (SGE)**.

---

## Autor

**Franco Cayo**  
Alumno de 2º de Desarrollo de Aplicaciones Multiplataforma – Curso 2025/2026
