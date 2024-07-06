# utils.py
import time
from mutagen.mp3 import MP3
import streamlit as st
from config import LOFI_MUSIC, ZEN_MUSIC, COMPLETED_TOPICS_FILE

def load_completed_topics():
    try:
        with open(COMPLETED_TOPICS_FILE, "r") as file:
            completed_topics = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        completed_topics = []
    return completed_topics

def save_completed_topics(completed_topics):
    with open(COMPLETED_TOPICS_FILE, "w") as file:
        file.writelines(f"{topic}\n" for topic in completed_topics)

def play_background_music(audio_path):
    audio_file = open(audio_path, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", loop=True, autoplay=True)

def play_sound_effect(file_path):
    audio = MP3(file_path)
    duration = audio.info.length

    audio_file = open(file_path, "rb")
    audio_bytes = audio_file.read()
    audio_player = st.audio(audio_bytes, format="audio/mp3", autoplay=True)

    time.sleep(duration)
    audio_player.empty()

def play_lofi_music():
    play_background_music(LOFI_MUSIC)

def play_zen_music():
    play_background_music(ZEN_MUSIC)
