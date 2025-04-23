# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# Step1: Setup Audio recorder (ffmpeg & portaudio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")
            return True

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False

# Step2: Setup Speech to text–STT–model for transcription
from groq import Groq

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )
    return transcription.text

# Main execution
if __name__ == "__main__":
    # Configuration
    audio_filepath = "patient_voice_test_for_patient.mp3"
    GROQ_API_KEY = "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"
    stt_model = "whisper-large-v3"
    
    # 1. Record audio
    print("Starting audio recording... Speak now!")
    record_success = record_audio(file_path=audio_filepath)
    
    if record_success:
        # 2. Transcribe audio
        print("Transcribing audio...")
        try:
            transcription = transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)
            print("\nTranscription Result:")
            print(transcription)
        except Exception as e:
            print(f"Error during transcription: {e}")
    else:
        print("Audio recording failed. Cannot transcribe.")