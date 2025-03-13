import streamlit as st
import google.generativeai as genai

# Configuración de la API de Gemini
def setup_gemini():
    # Reemplaza con tu API Key de Google AI Studio
    genai.configure(api_key=st.secrets["api_key"])

# Función para generar resúmenes
def generar_resumen(texto):
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = f"Resume el siguiente texto en 3 oraciones:\n\n{texto}"
    response = model.generate_content(prompt)
    return response.text

# Función para generar preguntas de práctica
def generar_preguntas(texto):
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = f"Genera 3 preguntas de práctica basadas en el siguiente texto:\n\n{texto}"
    response = model.generate_content(prompt)
    return response.text

# Interfaz de la aplicación
def main():
    st.title("StudyMate - Asistente de Estudio Personalizado")
    st.write("Organiza tu tiempo de estudio y genera recursos personalizados con IA.")

    # Menú de opciones
    opcion = st.sidebar.selectbox(
        "¿Qué deseas hacer?",
        ["Generar resumen", "Crear preguntas de práctica"]
    )

    if opcion == "Generar resumen":
        st.header("Generar Resumen Automático")
        texto = st.text_area("Ingresa el texto que deseas resumir:")
        if st.button("Generar Resumen"):
            if texto:
                resumen = generar_resumen(texto)
                st.success("Resumen generado:")
                st.write(resumen)
            else:
                st.error("Por favor, ingresa un texto.")

    elif opcion == "Crear preguntas de práctica":
        st.header("Crear Preguntas de Práctica")
        texto = st.text_area("Ingresa el texto para generar preguntas:")
        if st.button("Generar Preguntas"):
            if texto:
                preguntas = generar_preguntas(texto)
                st.success("Preguntas generadas:")
                st.write(preguntas)
            else:
                st.error("Por favor, ingresa un texto.")

if __name__ == "__main__":
    setup_gemini()
    main()