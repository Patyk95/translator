import sys
from translate import Translator

while True:
    b = int(input('''
    WYBIERZ 0 ABY KONTYNUOWAĆ
    WYBIERZ 1 ABY PRZERWAĆ
    PODAJ DZIAŁANIE -->:  '''))
    if b == 1:
        c= input('PLEASE CHOOSE LANGUGE WHICH SYS WILL TRANSLATE FROM: ')
        d= input('PLEASE CHOOSE LANGUGE  WHICH SYS WILL TRNASLATE FOR: ')
        e= input('PLEASE PROVIDE TEXT: ')
        translator = Translator(from_lang=c, to_lang=d)
        trans = translator.translate(e)
        print(trans.upper())
    if b == 0:
        sys.exit()