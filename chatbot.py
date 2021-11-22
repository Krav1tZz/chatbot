def izglitibas_programmas():
    x = input(
        "Ko tu gribi zināt? \n1 - Pirmsskolas izglītības \n2 - Vispārējā izglītība")
    izvele = int(x)
    if izvele == 1:
        print(
            "Pirmsskolas izglītības iestāde ir dibināta 1961.gadā, Valmieras 2. vidusskolas paspārnē darbojas kopš 2000. gada. \nPirmsskolas izglītība ir obligāta bērniem no 5 gadu vecuma. \n"
              "Mūsu pieredzējušie skolotāji palīdz skolēniem attīstīt pašapziņu, attīstīt fiziskās, intelektuālās un radošās prasmes, rūpēties par savu veselību un sagatavot tālākām mācībām \nPar ko vēl gribi uzzināt?")
        return izvelne(vards)
    elif izvele == 2:
       print(
           "Vispārējā izglītība pavisam ilgst 12 gadus, ietverot obligāto 9-gadīgo pamatizglītību un 3-gadīgo vidējo izglītību \nPar ko vēl gribi uzzināt?")
       return izvelne(vards)


    else:
        print("Izvēlieties 1-2")
        izglitibas_programmas()


def direktori():
    print(
        "Artūrs Krīgers - 1946 - 1960 \nAnna Piebalga - 1962 - 1983 \nEdīte Endola - 1983 - 1984 \nGunārs Bergmanis - 1984 - 1986 \nEdmunds Jansons - 1984 - 1986 \nAnastasija Vībāne - 1989 - 2009 \nPašreizējais direktors Andrejs Gluhovs - 2009 - xxxx \nPar ko vēl gribi uzzināt?")
        return izvelne(vards)


def tradicijas():
    print(
        "Tradīcija ir tas, kas mums un mūsu kultūrai ir svarīgs. Dažas no mūsu skolas tradīcijām: Latvijas Valsts proklamēšanas diena, Zinību diena, Sporta svētki dažādās vecuma grupās."
          "\nJa vēlaties uzzināt vairāk par mūsu tradīcijām, sekojiet saitei http://v2v.edu.lv/par-skolu/tradicijas/ \nPar ko vēl gribi uzzināt?" )
    return izvelne(vards)


def skolas_eka():
     return


def izvelne(vards):
    izvele = input(
        "1 - Izglitibas programmas \n2 - Direktori \n3 - Tradicijas \n4 - Skolas eka")
    lietotaja_izvele =  int(izvele)
    if lietotaja_izvele == 1:
        izglitibas_programmas()
    if lietotaja_izvele == 2:
        direktori()
    if lietotaja_izvele == 3:
        tradicijas()
    if lietotaja_izvele == 4:
        skolas_eka()
    else:
         print("Izvēlieties 1-4")
         izvelne(vards)



def sasveicinaties(vards):
     return print("Sveiki, " + vards)


if __name__ == '__main__':
    print(
        "Sveiki es esmu V2V catbots Vjaceslavs")
    vards = input(
        "Ka tevi sauc")
    vards = vards.title()
    sasveicinaties(vards)
    print(
        vards + ", izvelies par ko gribi uzzinat? Izvelies un ievadi")
    izvelne(vards)
