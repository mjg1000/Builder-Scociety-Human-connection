import speech_recognition as sr

def recognize_speech_with_language_choice():
    """
    Prompts the user to select a language, then captures audio
    from the microphone and returns the recognized text in that language.
    """
    
    # 1. Get language input from the user
    print("Please enter the BCP-47 language code for the language you will be speaking.")
    lang_code = input("Examples: 'en-US' (English), 'es-ES' (Spanish), 'fr-FR' (French), 'hi-IN' (Hindi): ")
    

    if not lang_code:
        print("Language code cannot be empty. Defaulting to 'en-US'.")
        lang_code = "en-US"

    # 2. Initialize the recognizer
    recognizer = sr.Recognizer()

    # 3. Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("\nAdjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print(f"\nListening for '{lang_code}'... Please say something!")
        
        try:
            # 4. Listen for audio input
            audio_data = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            
            print("Recognizing your speech...")
            
            # 5. Use Google's API with the user-specified language
            text = recognizer.recognize_google(audio_data, language=lang_code)
            
            return f"You said: {text}"

        except sr.WaitTimeoutError:
            return "Error: No speech detected. Please try again."
        except sr.UnknownValueError:
            return "Error: Google Speech Recognition could not understand the audio."
        except sr.RequestError as e:
            return f"Error: Could not request results from Google's service; {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

# --- Main part of the script ---
if __name__ == "__main__":
    result = recognize_speech_with_language_choice()
    print(f"\n--- Result ---\n{result}")
