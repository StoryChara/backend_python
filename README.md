# Curso de Backend con Python - Colsubsidio 🚀

**NOTA! Es un repositorio personal. Fue mi desarollo del curso.**

---

## 📚 Estructura del Curso

### [Módulo 1: Fundamentos de Programación y POO](https://github.com/StoryChara/backend_python/tree/main/Modulo%201) 🧱

Este módulo introduce los conceptos básicos de programación y sienta las bases para el desarrollo backend. Aprenderás sobre:

- **Tipos de datos y variables**: Comprender cómo manejar datos en Python.
- **Estructuras de control**: Uso de condicionales y bucles para lógica de programación.
- **Programación Orientada a Objetos (POO)**: Principios como clases, objetos, herencia y encapsulamiento.
- **Buenas prácticas**: Escritura de código limpio y organizado.

---

### [Módulo 2: Desarrollo Web con MVC y Bases de Datos](https://github.com/StoryChara/backend_python/tree/main/Modulo%202) 🌐

En este módulo, exploramos el desarrollo de aplicaciones web utilizando el patrón **MVC (Modelo-Vista-Controlador)**. Los temas clave incluyen:

- **Flask**: Framework ligero de Python para crear aplicaciones web.
- **SQLAlchemy**: Herramienta ORM para gestionar bases de datos relacionales de forma eficiente.
- **Creación de tests**: Introducción a pruebas unitarias con `unittest` y manejo de excepciones con `try-except`.

---

### [Módulo 3: Autenticación, Autorización y APIs](https://github.com/StoryChara/backend_python/tree/main/Modulo%203) 🔒

Este módulo se centra en la seguridad y la creación de interfaces de programación de aplicaciones (APIs). Los temas incluyen:

- **Autenticación y autorización**: Implementación de sistemas de login y control de acceso con JWT y otras técnicas como dotenv.
- **Desarrollo de APIs RESTful**: Diseño y creación de endpoints para interactuar con aplicaciones frontend o externas.
- **Gestión de usuarios**: Manejo de roles y permisos para aplicaciones seguras.

---

### [Módulo 4: Despliegue de Aplicaciones](https://github.com/StoryChara/backend_python/tree/main/Modulo%203) 🚀

El último módulo está dedicado a llevar tus proyectos al mundo real mediante el despliegue en servidores. Contenido principal:

- **Configuración de entornos de producción**: Uso de plataformas como Railway para hosting.
- **Gestión de dependencias**: Asegurar que tu aplicación funcione correctamente en diferentes entornos.
- **Proyectos desplegados**:
  - **[Deploy de Heladería](https://backend-python-proyecto3.up.railway.app/)**: Aplicación web funcional de una heladería.
  - **[Deploy de API de Animales](https://backend-python-api.up.railway.app/)**: API REST para gestionar información de animales.
- **Uso de Comandos para Build y Deploy**:
  - **Instalación de Librerías**: `pip install -r requirements.txt`
  - **Ejecución de la Aplicación**: `python run.py`
- **Variables de Entorno**:
  - **DB**: `mysql+pymysql:://${{MYSQLUSER}}:${{MYSQL_ROOT_PASSWORD}}@${{RAILWAY_TCP_PROXY_DOMAIN}}:${{RAILWAY_TCP_PROXY_PORT}}/${{MYSQL_DATABASE}}`
  - **SECRET_KEY**: `{{SECRET_KEY}}`

---

## 🛠️ Tecnologías Utilizadas

| **Tecnología**     | **Descripción**                          | **Uso Principal**            |
|---------------------|------------------------------------------|------------------------------|
| **Python**          | Lenguaje principal del curso            | Backend y lógica de negocio  |
| **Flask**           | Framework web ligero                    | Desarrollo de aplicaciones web |
| **SQLAlchemy**      | ORM para bases de datos                 | Gestión de datos relacionales |
| **JSON**            | JSON Web Tokens                         | Autenticación y seguridad    |
| **Railway**         | Plataforma de despliegue                | Hosting de aplicaciones      |

---
