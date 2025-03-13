# StudyMate - Asistente de Estudio Personalizado

**StudyMate** es una aplicación web que utiliza inteligencia artificial (IA) para ayudar a los estudiantes a organizar su tiempo de estudio, generar resúmenes automáticos y crear preguntas de práctica personalizadas. La aplicación está construida con **Python**, utiliza la **API de Gemini** (Google AI Studio) para la generación de contenido y se despliega en **Streamlit**.

---

## Tabla de Contenidos

1. [Funcionalidades](#funcionalidades)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Configuración](#configuración)
5. [Uso](#uso)
6. [Despliegue](#despliegue)
7. [Capturas de Pantalla](#capturas-de-pantalla)
8. [Contribución](#contribución)
9. [Licencia](#licencia)

---

## Funcionalidades

- **Generar Resúmenes Automáticos:**  
  Los usuarios pueden ingresar un texto y la aplicación genera un resumen conciso utilizando la API de Gemini.

- **Crear Preguntas de Práctica:**  
  Los usuarios pueden ingresar un texto y la aplicación genera preguntas de práctica basadas en el contenido.

- **Interfaz Intuitiva:**  
  La aplicación tiene una interfaz fácil de usar, con un menú lateral para navegar entre las funcionalidades.

---

## Requisitos

- Python 3.8 o superior.
- Cuenta en [Google AI Studio](https://aistudio.google.com/) para obtener una API Key.
- Cuenta en [Streamlit](https://streamlit.io/) para el despliegue.
- Extensión de **Codeium** (opcional) para autocompletado de código en Visual Studio Code.

---

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/studymate.git
   cd studymate
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuración

1. **Obtén tu API Key de Gemini:**

   - Ve a [Google AI Studio](https://aistudio.google.com/).
   - Inicia sesión con tu cuenta de Google.
   - Crea un nuevo proyecto y genera una clave de API.
   - Copia la clave y guárdala en un lugar seguro.

2. **Configura la API Key en el código:**
   - Abre el archivo `studymate.py`.
   - Reemplaza `"TU_API_KEY_DE_GEMINI"` con tu API Key en la siguiente línea:
     ```python
     api_key = "TU_API_KEY_DE_GEMINI"
     ```

---

## Uso

1. Ejecuta la aplicación localmente:

   ```bash
   streamlit run studymate.py
   ```

2. Abre tu navegador y ve a `http://localhost:8501`.

3. **Generar Resumen:**

   - Selecciona "Generar resumen" en el menú lateral.
   - Ingresa un texto en el cuadro de texto.
   - Haz clic en "Generar Resumen".
   - La aplicación mostrará un resumen de 3 oraciones.

4. **Crear Preguntas de Práctica:**
   - Selecciona "Crear preguntas de práctica" en el menú lateral.
   - Ingresa un texto en el cuadro de texto.
   - Haz clic en "Generar Preguntas".
   - La aplicación mostrará 3 preguntas basadas en el texto.

---

## Despliegue

1. Sube el proyecto a un repositorio de GitHub.

2. Ve a [Streamlit Community Cloud](https://share.streamlit.io/), inicia sesión y conecta tu repositorio.

3. Configura el despliegue seleccionando el archivo `studymate.py`.

4. ¡Tu aplicación estará disponible en un enlace público de Streamlit!

---
