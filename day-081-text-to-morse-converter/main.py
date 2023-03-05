encrypt_morse_codes = {
    'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....',
    'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__.',
    'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
    'Y': '_.__', 'Z': '__..',
    '1': '.____', '2': '..___', '3': '...__', '4': '...._',
    '5': '.....', '6': '_....', '7': '__...', '8': '___..',
    '9': '____.', '0': '_____',
    ' ': '.......'
}
decrypt_morse_codes = {value: key for key,
                       value in encrypt_morse_codes.items()}
print(decrypt_morse_codes['._'])


def text_to_morse(text):
    morse = ''
    for letter in text:
        morse += encrypt_morse_codes[letter.upper()] + ' '
    return morse


def morse_to_text(morse):
    text = ''
    for letter in morse.split(' '):
        if letter != '':
            text += decrypt_morse_codes[letter]
    return text


incorrect = True
while incorrect:
    text = input("Please enter a string to convert to morse code: \n")
    if text != '':
        morse = text_to_morse(text=text)
        incorrect = False
    else:
        incorrect = True

print(morse)
