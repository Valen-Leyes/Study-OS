import streamlit as st
from mutagen.mp3 import MP3
import time

music_folder = "audio/music/"
zen_music = music_folder + "zen.mp3"

sfx_folder = "audio/sfx/"
balloons_sfx = sfx_folder + "balloons.mp3"
snow_sfx = sfx_folder + "snow.mp3"

def define_study_plan():
    # Define the study plan
    study_plan = {
        "Día 1: UNIDAD I - Lógica Proposicional y Teoría Intuitiva de Conjuntos 📖": {
            "Mañana (4 horas)": ["🔍 Proposiciones y Conectivos Lógicos", "📊 Propiedades de los Conectivos Lógicos", "🔢 Noción de Conjuntos y Operaciones entre Conjuntos", "🔄 Propiedades de las Operaciones entre Conjuntos"]
        },
        "Día 2: UNIDAD II - Relaciones y UNIDAD III - Funciones 🔗": {
            "Mañana (4 horas)": ["📐 Definición de Relación y Concepto de Dominio, Imagen e Inversa", "🔀 Composición de Relaciones y Propiedades de las Relaciones", "🔄 Relaciones de Equivalencia y Relaciones de Orden", "📊 Representación Cartesiana de Relaciones"],
            "Tarde (4 horas)": ["📈 Definición de Función y Representación Gráfica de Funciones", "📊 Clasificación de Funciones y Composición de Funciones", "🔄 Función Inversa y Funciones Especiales", "📊 Partes de un Conjunto, Partición de un Conjunto, Conjuntos Numéricos (de UNIDAD I)"]
        },
        "Día 3: UNIDAD IV - Conjuntos Numéricos y UNIDAD V - Análisis Combinatorio 🔢": {
            "Mañana (4 horas)": ["🔢 Conjuntos Numéricos (Naturales, Enteros, Racionales, Reales y Complejos)", "🔢 Propiedades Algebraicas Básicas y Principio de Inducción", "🔢 Variante del Principio de Inducción y Algoritmo de la División", "🔢 Divisibilidad, Máximo Común Divisor y Mínimo Común Múltiplo"],
            "Tarde (4 horas)": ["🔢 Variaciones, Combinaciones y Permutaciones, Simples y con Repetición", "📊 Análisis y Aplicaciones", "🔢 Número Combinatorio y Propiedades de los Números Combinatorios", "🔢 Desarrollos s-ádicos y Cambios de Base (de UNIDAD IV)"]
        },
        "Día 4: UNIDAD VI - Polinomios y UNIDAD VII - Matrices y Determinantes 🔲": {
            "Mañana (4 horas)": ["📐 Expresión Formal de Polinomio en una Indeterminada y Grado de un Polinomio", "🔄 Operaciones con Polinomios y Algoritmos de la División", "📈 Teorema de Ruffini y Raíces de un Polinomio", "📝 Teorema del Resto y Teorema Fundamental del Álgebra"],
            "Tarde (4 horas)": ["📊 Definición de Matrices y Operaciones con Matrices", "📊 Matrices Cuadradas y Producto Escalar-Matriz", "🔄 Reducción a una Matriz Escalonada por Filas y Matriz Inversa", "📐 Determinante y Caracterización de las Matrices de Rango Completo"]
        },
        "Día 5: UNIDAD VIII - Sistemas de Ecuaciones Lineales and UNIDAD IX - Nociones de Geometría Analítica 📐": {
            "Mañana (4 horas)": ["📝 Definición de Sistemas de Ecuaciones Lineales y Clasificación", "📊 Conjunto Solución y Teorema Fundamental de Equivalencia", "📈 Teorema de Rouché-Frobenius y Sistemas Cuadrados", "📊 Teorema de Cramer y Regla de Cramer"],
            "Tarde (4 horas)": ["📐 Sistemas de Coordenadas y Ecuación de la Recta", "📈 Ecuación de la Circunferencia y Ecuación de la Elipse", "📉 Ecuación de la Hipérbola y Ecuación de la Parábola", "🔄 Intersecciones y Revisión General"]
        }
    }

    return study_plan

# Function to display the study plan and handle topic completion
def display_study_plan(study_plan):
    completed_topics = load_completed_topics()
    for day, sessions in study_plan.items():
        st.header(day)
        for session, topics in sessions.items():
            st.subheader(session)
            for topic in topics:
                checkbox_key = f"{day}_{session}_{topic}"
                checkbox_placeholder = st.empty()
                if topic in completed_topics:
                    checkbox_placeholder.checkbox(f":green[{topic}]", value=True, disabled=True)
                else:
                    checkbox = checkbox_placeholder.checkbox(topic, key=checkbox_key)
                    if checkbox:
                        completed_topics.append(topic)
                        checkbox_placeholder.checkbox(f":green[{topic}]", value=True, disabled=True)
    return completed_topics

# Function to load completed topics from a file
def load_completed_topics():
    try:
        with open("completed_topics.txt", "r") as file:
            completed_topics = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        completed_topics = []
    return completed_topics

# Function to save completed topics to a file
def save_completed_topics(completed_topics):
    with open("completed_topics.txt", "w") as file:
        file.writelines(f"{topic}\n" for topic in completed_topics)

# Function to play background music
def play_background_music(audio_path):
    audio_file = open(audio_path, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", loop=True, autoplay=True)

# Function to play sound effect
def play_sound_effect(file_path):
    # Get the audio duration
    audio = MP3(file_path)
    duration = audio.info.length

    # Play the sound effect
    audio_file = open(file_path, "rb")
    audio_bytes = audio_file.read()
    audio_player = st.audio(audio_bytes, format="audio/mp3", autoplay=True)

    # Stop the audio after the sound effect's duration
    time.sleep(duration)
    audio_player.empty()

# Function to add visual effects and sound effects
def add_visual_effects_and_sound_effects(completed_topics):
    if len(completed_topics) % 4 == 0:
        # Add balloons effect and play sound effect
        st.balloons()
        play_sound_effect(balloons_sfx)
    else:
        # Add snow effect and play sound effect
        st.snow()
        play_sound_effect(snow_sfx)

# Main function
def main():
    # Set the title
    st.title("Plan de Estudio 📚")

    # Reproduce 🎵 music
    play_background_music(zen_music)

    # Define the study plan
    study_plan = define_study_plan()

    # Display the study plan
    completed_topics = display_study_plan(study_plan)

    # Display a message when all topics are completed
    if len(completed_topics) == sum(len(topics) for sessions in study_plan.values() for topics in sessions.values()):
        st.success("¡Felicidades! Has completado todos los temas del plan de estudio.")

    # Add a footer
    st.markdown("---")
    st.markdown("¡Buena suerte en tu estudio! 🍀")

    # Add 🌟 visual effects and 🔊 sound effects
    if completed_topics != load_completed_topics():
        add_visual_effects_and_sound_effects(completed_topics)

    # Save completed topics to a file
    save_completed_topics(completed_topics)

if __name__ == "__main__":
    main()