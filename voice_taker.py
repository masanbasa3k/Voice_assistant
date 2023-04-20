# You must downloads
# flac
# !pip install pyaudio
# !pip install SpeechRecognition

import speech_recognition as sr

# ENG_LANG = "en-US"
def recognize():
    TR_LANG = "tr-TR"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Söylemek istediğinizi söyleyin:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language=TR_LANG)
            return text
        except sr.UnknownValueError:
            print("Üzgünüm, anlayamadım. Lütfen tekrarlayın.")
        except sr.RequestError as e:
            print("Sistem şu anda çalışmıyor. Lütfen daha sonra tekrar deneyin.")


if __name__ == "__main__":
    message = recognize()
    print(message)