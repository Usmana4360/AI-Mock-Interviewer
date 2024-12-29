import streamlit as st
from streamlit_mic_recorder import speech_to_text

if "recording_key" not in st.session_state:
    # For unique speech_to_text widget keys
    st.session_state["recording_key"] = 0

def process_audio_input():
    """Capture audio from mic and convert it to text using speech-to-text."""

    # Generate a unique key for this recording session based on the recording key in session state
    unique_key = f"STT-{st.session_state['recording_key']}"

    # Capture audio input from the mic and convert it to text (using Urdu as the language)
    transcribed_text = speech_to_text(
        language='en',               # Set language to Urdu for speech recognition
        # Ensure the widget adapts to the container width in the UI
        use_container_width=True,
        just_once=True,              # Capture audio only once for simplicity
        key=unique_key               # Unique key for this specific recording session
    )

    # Return the transcribed text for further use
    return transcribed_text


transcribed_text = process_audio_input()
st.write("Transcribed Text:", transcribed_text)