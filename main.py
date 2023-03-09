import base64
import binascii

# Konversi dari teks ke bentuk lain
def encode(text, mode):
    if mode == 'base64':
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')
    elif mode == 'base32':
        return base64.b32encode(text.encode('utf-8')).decode('utf-8')
    elif mode == 'hex':
        return binascii.hexlify(text.encode('utf-8')).decode('utf-8')
    elif mode == 'ascii':
        return ' '.join(str(ord(c)) for c in text)
    elif mode == 'binary':
        return ' '.join(format(ord(c), 'b') for c in text)
    elif mode == 'morse':
        MORSE_CODE_DICT = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
            'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
            '!': '-.-.--', '-': '-....-', '/': '-..-.', '@': '.--.-.', '(': '-.--.', ')': '-.--.-'
        }
        return ' '.join(MORSE_CODE_DICT.get(c.upper(), '') for c in text)

# Konversi dari bentuk lain ke teks
def decode(text, mode):
    if mode == 'base64':
        return base64.b64decode(text.encode('utf-8')).decode('utf-8')
    elif mode == 'base32':
        return base64.b32decode(text.encode('utf-8')).decode('utf-8')
    elif mode == 'hex':
        return binascii.unhexlify(text.replace(' ', '').encode('utf-8')).decode('utf-8')
    elif mode == 'ascii':
        return ''.join(chr(int(c)) for c in text.split())
    elif mode == 'binary':
        return ''.join(chr(int(c, 2)) for c in text.split())
    elif mode == 'morse':
        MORSE_CODE_DICT = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
            '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
            '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.',
        '--..--': ',', '..--..': '?', '-.-.--': '!', '-....-': '-', '-..-.': '/', '.--.-.': '@',
        '-.--.': '(', '-.--.-': ')'
    }
    return ''.join(MORSE_CODE_DICT.get(c, '') for c in text.split())
#FUNGSI UTAMA
def main():
    while True:
        print('Pilih mode:')
        print('1. Base64')
        print('2. Base32')
        print('3. Hexadesimal')
        print('4. ASCII')
        print('5. Binary')
        print('6. Morse')
        print('0. Keluar')
        choice = input('Masukkan pilihan Anda: ')
        print('\n' * 100) # Membersihkan layar

        if choice == '1':
            text = input('Masukkan teks yang akan dienkripsi: ')
            encoded_text = encode(text, 'base64')
            print(f'Teks yang sudah dienkripsi: {encoded_text}')
            input('Tekan enter untuk melanjutkan...')
            print('\n' * 100) # Membersihkan layar
        elif choice == '2':
            text = input('Masukkan teks yang akan dienkripsi: ')
            encoded_text = encode(text, 'base32')
            print(f'Teks yang sudah dienkripsi: {encoded_text}')
            input('Tekan enter untuk melanjutkan...')
            print('\n' * 100) # Membersihkan layar
        elif choice == '3':
            text = input('Masukkan teks yang akan dienkripsi: ')
            encoded_text = encode(text, 'hex')
            print(f'Teks yang sudah dienkripsi: {encoded_text}')
            input('Tekan enter untuk melanjutkan...')
            print('\n' * 100) # Membersihkan layar
        elif choice == '4':
            text = input('Masukkan teks yang akan dienkripsi: ')
            encoded_text = encode(text, 'ascii')
            print(f'Teks yang sudah dienkripsi: {encoded_text}')
            input('Tekan enter untuk melanjutkan...')
            print('\n' * 100) # Membersihkan layar
        elif choice == '5':
            text = input('Masukkan teks yang akan dienkripsi: ')
            encoded_text = encode(text, 'binary')
            print(f'Teks yang sudah dienkripsi: {encoded_text}')
            input('Tekan enter untuk melanjutkan...')
            print('\n' * 100) # Membersihkan layar
        elif choice == '6':
            text = input('Masukkan teks yang akan dienkripsi: ')
            encoded_text = encode(text, 'morse')
            print(f'Teks yang sudah dienkripsi: {encoded_text}')
            input('Tekan enter untuk melanjutkan...')
            print('\n' * 100) # Membersihkan layar
        elif choice == '0':
            print('Terima kasih!')
            break
        else:
            print('Pilihan tidak valid. Silakan pilih angka dari 0-6.')
            input('Tekan enter untuk melanjutkan...')
            print('\n' * 100) # Membersihkan layar

if __name__ == '__main__':
    main()
