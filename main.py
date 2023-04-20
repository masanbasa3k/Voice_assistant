from gpt_api import take_response
from voice_taker import recognize
from dubbing import speak

def main():
    run = True
    while run:
        my_message = recognize()

        if my_message:
            if my_message and "çıkış":
                run = False
                print("Çıkış yapılıyor!")
                break
        
            print(f"You: {my_message}")

            bot_message = take_response(my_message)
            print(f"Bot: {bot_message}")
            speak(bot_message)

if __name__ == "__main__":
    main()