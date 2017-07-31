# Mors alfabesi
alfabe = {
    "a": ".-", 
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "ı": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": " / ",
    # Mors alfabesine ait sayılar.
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

def yazdir(*metin):
    kelime = ""
    for oku in metin:
        if oku in alfabe:
            kelime += alfabe[oku]
        else:
            return "Türkçe karakter veya olmayan bir işaret kullandınız."
    return kelime
        
metin = input("Metin: ")
print(yazdir(*metin))




