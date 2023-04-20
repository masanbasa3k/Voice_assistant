from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
# need to install ffmpeg

def speak(text):
    # Ses dosyasını oluşturun
    tts = gTTS(text=text, lang="tr")

    # Ses dosyasını bellekte saklayın
    audio = BytesIO()
    tts.write_to_fp(audio)

    # Ses dosyasını çalın
    audio.seek(0)
    sound = AudioSegment.from_file(audio, format="mp3")
    play(sound)

    # Bellekten ses dosyasını silin
    audio.close()


if __name__ == "__main__":
    text = "selamlar"
    speak(text)