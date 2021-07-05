"""Create Morse Letter Dictionary"""
morse_letters = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'L': '.-..',
    'O': '---',
    'R': '.-.',
    'U': '..-',
    'X': '-..-',
    '1': '.----',
    '4': '....-',
    '7': '--...',
    '0': '-----',
    '?': '..--..',
    'K': '-.-',
    'M': '--',
    'N': '-.',
    'P': '.--.',
    'Q': '--.-',
    'S': '...',
    'T': '-',
    'V': '...-',
    'W': '.--',
    'Y': '-.--',
    'Z': '--..',
    '2': '..---',
    '3': '...--',
    '5': '.....',
    '6': '-....',
    '8': '---..',
    '9': '----.',
    '(': '-.--.',
    '-': '-....-',
    ',': '--..--',
    '.': '.-.-.-',
    '/': '-..-.',
    ')': '-.--.-'
}

translated_letters = {value: key for key, value in morse_letters.items()}

def decode(message) -> str:
    """Take a encoded morse message and normalize to word:
    """
    message = message.split(' ')
    cipher = ''
    for code in message:
        if code != '' and code != ' ':
            try:
                cipher += translated_letters[code]
            except KeyError:
                pass
        else:
            cipher += ' '
    return cipher.lower()


def encode(word) -> str:
    """Take a word message and encode it to morse code:"""
    cipher = ''
    for letter in word:
        if letter != ' ':
            try:
                cipher += morse_letters[letter] + ' '
            except KeyError:
                print(f'Opps! Invalid Format {letter}')
                break
        else:
            cipher += ' '
    return cipher


def morse(action):
    if action == 'e':
        word = input('What is your message to encode?: ').upper()
        result = encode(word)
        if result:
            print(f"{word} can encoded: [ {result} ]\n")

    elif action == 'd':
        word = input('What is your message to decode?: ').upper()
        result = decode(word)

        print(f"[ {word} ] can decoded: [ {result} ]\n")


choice = input('What would like to do decode or encode [d/e]:')
morse(action=choice.lower())