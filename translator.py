from translate import Translator



# translator=Translator(from_lang='PL',to_lang='EN')
# trans=translator.translate("Pracuję bardzo ciężko od poniedziałku do piątku, natomiast w weekendy odpoczywam.")
# print(trans)



while True:
    c=input('PODAJ JĘZYK WEJŚCIA(PL,DE,EN,RUS,FR: --> ')
    d=input('PODAJ JĘZYK WYJŚCIA(PL,DE,EN,RUS,FR:--> ')
    e=input('Podaj tekst do tłumaczenia:--> ')
    translator=Translator(from_lang=c,to_lang=d)
    trans=translator.translate(e)
    print(trans)