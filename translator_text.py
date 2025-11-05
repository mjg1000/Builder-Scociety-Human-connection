from translate import Translator
# import nltk
from nltk.corpus import wordnet
import string   
# nltk.download('wordnet')

import csv
from collections import defaultdict

csv_file = "ISO 639 1 Language Codes.csv"
global language_mapping 
data = {}

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for key, value in row.items():
            # print(row)
            data[row['Language']] = row['ISO_code']

language_mapping = data
def translate_text(transcribed_text, language):
    translator = Translator(to_lang=language_mapping[language])
    translation = translator.translate(transcribed_text)
    bad_words = clean_text(transcribed_text)[1]
    bad_words2 = [] 
    for i in bad_words:
        # print(i)
        if i in translation:
            bad_words2.append(i)

    return translation, bad_words2

def is_word(word):
    return bool(wordnet.synsets(word.lower()))

def clean_text(text):  
    raw_text = text
    cleaner = str.maketrans(" ", " ", string.punctuation)
    clean_text = raw_text.translate(cleaner)
    bad_words = set()
    for i in clean_text.split(" "):
        if not is_word(i):
            print(i)
            bad_words.add(i)
    
    return text, bad_words

# print(is_word("helo"))
# print(is_word("hell"))
# print(is_word("haaasd"))
# print(is_word("he"))
# print(clean_text("hello, how are you? What is your name? How many numbers high can you count to?"))
# translated, bad = translate_text("Helo, how are you? What's your name? what numer is your favourite? gaihsjdasd python is a prograing langage ", "French")
# print(translated)
# print(bad)
# print(translate_text(translated, "English"))
# print(wordnet.synsets("How"))
# translator = Translator(to_lang="es")
# translation = translator.translate("Helo, how are you?")
# print(translation)
