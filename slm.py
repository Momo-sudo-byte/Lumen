import streamlit as st
import pyttsx3
import openai
import pyaudio
import pywhatkit
import webbrowser
import sympy
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import speech_recognition as sr

# Fonction pour la reconnaissance vocale
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Veuillez parler...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"Vous avez dit : {text}")
            return text
        except sr.UnknownValueError:
            st.write("Je n'ai pas pu comprendre votre audio.")
            return ""
        except sr.RequestError:
            st.write("Erreur de service de reconnaissance vocale.")
            return ""

# Fonction pour la synthèse vocale
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Fonction pour rechercher sur le web
def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    st.write(f"Recherche de '{query}' sur Google.")

# Fonction pour rechercher sur YouTube
def search_youtube(query):
    pywhatkit.playonyt(query)
    st.write(f"Recherche de '{query}' sur YouTube.")

# Fonction pour changer le volume du système
def change_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, 
        1, 
        None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(level, None)
    st.write(f"Volume réglé à {level*100}%")

# Fonction pour résoudre des expressions mathématiques
def solve_math(expression):
    try:
        result = sympy.sympify(expression)
        st.write(f"Résultat : {result}")
    except:
        st.write("Expression mathématique invalide.")

# Interface Streamlit
st.title("Interface d'IA avec Streamlit")

# Choix de l'action
option = st.selectbox("Choisissez une action", [
    "Reconnaissance vocale",
    "Synthèse vocale",
    "Recherche sur le web",
    "Recherche sur YouTube",
    "Changer le volume",
    "Résoudre une expression mathématique"
])

# Interaction en fonction de l'option choisie
if option == "Reconnaissance vocale":
    if st.button("Commencer la reconnaissance vocale"):
        speech_to_text()

elif option == "Synthèse vocale":
    text_input = st.text_input("Entrez le texte à dire")
    if text_input and st.button("Lire le texte"):
        text_to_speech(text_input)

elif option == "Recherche sur le web":
    query = st.text_input("Entrez votre recherche")
    if query and st.button("Rechercher sur le web"):
        search_web(query)

elif option == "Recherche sur YouTube":
    query = st.text_input("Entrez votre recherche")
    if query and st.button("Rechercher sur YouTube"):
        search_youtube(query)

elif option == "Changer le volume":
    level = st.slider("Réglez le volume", 0.0, 1.0, 0.5)
    if st.button("Changer le volume"):
        change_volume(level)

elif option == "Résoudre une expression mathématique":
    expression = st.text_input("Entrez une expression mathématique")
    if expression and st.button("Résoudre l'expression"):
        solve_math(expression)
