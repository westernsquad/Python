

class Morse():

    def __init__(self):
        morse1 = {'A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--', 'H': '....',
                 'I': '..',
                 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'p': '.--.',
                 'Q': '--.-',
                 'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                 'Z': '--..',
                 '0': '-----', '1': '.----', '2': '..---', '3': ':...--', '4': '....-', '5': '.....', '6': '-....',
                 '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '-.-.--', '?': '..--..', '"': '.-..-.',
                 '!': '--..--'}
        morse2 = {' ': ' ', '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--': 'M',
                 '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '-.': 'N', '--.--': 'Ñ', '---': 'O', '.--.': 'p',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..--': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', ':...--': '3', '....-': '4',
                 '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '-.-.--': ',',
                 '..--..': '?', '.-..-.': '"', '--..--': '!'}

    def codifica (self,cadena):
        traduccido=[]
        for e in cadena:
            traduccido.append(self.morse1.get(e))
            traduccido.append(" ")
        cadena1 = ''.join(str(traduccido))
        #print(traduccido)
        print(cadena1)

    #codifica('HOLA')

    def descodifica (self,cadena):#preguntar por que no me guarda los espacios¿
        """Funcion que recibe una frase en codigo morse y la traduce"""

        traduccido=[]
       #letras = ' '.join(cadena.split(""))
        palabras= cadena.split("/")
        #print(palabras)
        for e in palabras:
            letra=e.split()
            #print(letra)
            for j in letra:
                traduccido.append(self.morse2.get(j))
            traduccido.append(" ")
        cadena1=''.join(traduccido)
        #print(traduccido)
        print(cadena1)

    #descodifica('.... --- .-.. .-/-.-. .- .-. .-/-.-. --- .-.. .- ')

        c = Morse()
        d= self.codifica("HOLA")
        print(d)