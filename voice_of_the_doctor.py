#setup text to speech-TTS-model(gTTS & Elevenlabs )

#step1a: setup a text to speech-TTS-model with gTTS



#step1a: setup a text to speech-TTS-model with gTTS
import os
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs

# gTTS setup
def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    print(f"Audio saved as {output_filepath}")

# Using gTTS
input_text = "Hi this is Alok Mourya"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")

# ElevenLabs setup
ELEVENLABS_API_KEY = "sk_87f2b8774271fdd34977cf81ed626bfb84b7011274a34d4a"

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Roger",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    print(f"Audio saved as {output_filepath}")


# Using ElevenLabs
#text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing.mp3")


#step2: text to speech model using gTTS and ElevenLabs

import os
import subprocess
import platform
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = "sk_87f2b8774271fdd34977cf81ed626bfb84b7011274a34d4a"

def play_audio(filepath):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', filepath])
        elif os_name == "Windows":  # Windows
             subprocess.run(['start', '', filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    print(f"[gTTS] Audio saved as {output_filepath}")
    play_audio(output_filepath)


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Roger",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    print(f"[ElevenLabs] Audio saved as {output_filepath}")
    play_audio(output_filepath)


# Example usage
input_text = "Hi this is AI with Hassan, autoplay testing!"

# Uncomment one of the two below to test:
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")
text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing_autoplay.mp3")

