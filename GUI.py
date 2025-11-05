import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import main 

Title = "Translator"
SupportedLanguages = ['English','Spanish','French','Hindi']

root = tk.Tk()
root.geometry("1000x400+400+100")
root.title(Title)
root.resizable(False, False)


OriginalText = tk.Text(root, {"height": 15, "width": 48})
TranslatedText = tk.Text(root, {"height": 15, "width": 48})


def texttospeech():
    translate()
    # Text = "blah blah blah"
    # #text to speech
    # newtext = "test"
    # OriginalText.delete("1.0", "end")  # clear existing content
    # OriginalText.insert("1.0", newtext)

def translate():
    Language = lang_inside.get()
    Lang_in = Originlang_inside.get()
    Text = OriginalText.get("1.0","end")
    transcribed, translated = main.full_process(Language, Lang_in)
    
    OriginalText.delete("1.0", "end")  # clear existing content
    OriginalText.insert("1.0", transcribed)
    print(Language , "!" , Text)
    #translate Text variable
    TranslatedText.delete("1.0", "end")  # clear existing content
    TranslatedText.insert("1.0", translated)

values=['Afar', 'Abkhaz', 'Avestan', 'Afrikaans', 'Akan', 'Amharic', 'Aragonese', 'Arabic', 'Assamese', 'Avaric', 'Aymara', 'Azerbaijani', 'Bashkir', 'Belarusian', 'Bulgarian', 'Bihari', 'Bislama', 'Bambara', 'Bengali', 'Tibetan', 'Breton', 'Bosnian', 'Catalan', 'Chechen', 'Chamorro', 'Corsican', 'Cree', 'Czech', 'Slavonic', 'Chuvash', 'Welsh', 'Danish', 'German', 'Divehi', 'Dzongkha', 'Ewe', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Basque', 'Persian', 'Fula', 'Finnish', 'Fijian', 'Faroese', 'French', 'Western Frisian', 'Irish', 'Scottish Gaelic', 'Galician', 'Guarani', 'Gujarati', 'Manx', 'Hausa', 'Hebrew', 'Hindi', 'Hiri Motu', 'Croatian', 'Haitian', 'Hungarian', 'Armenian', 'Herero', 'Interlingua', 'Indonesian', 'Interlingue', 'Igbo', 'Nuosu', 'Inupiaq', 'Ido', 'Icelandic', 'Italian', 'Inuktitut', 'Japanese', 'Javanese', 'Georgian', 'Kongo', 'Kikuyu', 'Kwanyama', 'Kazakh', 'Kalaallisut', 'Khmer', 'Kannada', 'Korean', 'Kanuri', 'Kashmiri', 'Kurdish', 'Komi', 'Cornish', 'Kyrgyz', 'Luxembourgish', 'Latin', 'Ganda', 'Limburgish', 'Lingala', 'Lao', 'Lithuanian', 'Luba-Katanga', 'Latvian', 'Malagasy', 'Marshallese', 'Maori', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Burmese', 'Nauru', 'Norwegian Bokmal', 'North Ndebele', 'Nepali', 'Ndonga', 'Dutch', 'Norwegian Nynorsk', 'Norwegian', 'South Ndebele', 'Navajo', 'Chichewa', 'Occitan', 'Ojibwe', 'Oromo', 'Oriya', 'Ossetian', 'Panjabi', 'Pali', 'Polish', 'Pashto', 'Portuguese', 'Quechua', 'Romansh', 'Kirundi', 'Romanian', 'Russian', 'Kinyarwanda', 'Sanskrit', 'Sardinian', 'Sindhi', 'Northern Sami', 'Sango', 'Sinhala', 'Slovak', 'Slovenian', 'Samoan', 'Shona', 'Somali', 'Albanian', 'Serbian', 'Swati', 'Southern Sotho', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Tajik', 'Thai', 'Tigrinya', 'Turkmen', 'Tagalog', 'Tswana', 'Tonga', 'Turkish', 'Tsonga', 'Tatar', 'Twi', 'Tahitian', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Venda', 'Vietnamese', 'Volapuk', 'Walloon', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zhuang', 'Chinese', 'Zulu']
lang_inside = tk.StringVar(root)

# Set the default value of the variable
lang_inside.set("English")

Originlang_inside = tk.StringVar(root)
Originlang_inside.set("English")
LanguageBox = ttk.Combobox(root, textvariable=lang_inside, values=values, width=30)
LanguageBox.set("English")
LanguageBox.state(["readonly"])  # prevents typing invalid entries

LanguageOriginBox = ttk.Combobox(root, textvariable=Originlang_inside, values=SupportedLanguages, width=30)
LanguageOriginBox.set("English")
LanguageOriginBox.state(["readonly"])  # prevents typing invalid entries


TranslateButton = ttk.Button(root, text="Translate\n       -->", command=translate)
SpeakButton = ttk.Button(root, text="Transcribe \n & \n Translate", command=texttospeech)

SpeakButton.place(relx=0.5,rely=0.5,anchor="center")
OriginalText.place(relx=0.25, rely=0.5,anchor="center")
TranslatedText.place(relx=0.75, rely=0.5,anchor="center")
# TranslateButton.place(relx=0.5,rely=0.5,anchor="center")
LanguageOriginBox.place(relx=0.4,rely=0.1,anchor="center")
LanguageBox.place(relx=0.7,rely=0.1,anchor="center")
root.mainloop()