import SpeechRecognisationToText
import translator_text

def full_process(language_out, language_in):
    language_in_map = {"English":'en-US', "Spanish":'es-ES', "French":'fr-FR', "Hindi":'hi-IN'}
    lang_in_code = language_in_map[language_in]

    transcribed_text = SpeechRecognisationToText.recognize_speech_with_language_choice(lang_in_code)
    
    print(transcribed_text)
    t_text = translator_text.translate_text(transcribed_text, language_out)
    print(t_text)
    return transcribed_text, t_text[0]
