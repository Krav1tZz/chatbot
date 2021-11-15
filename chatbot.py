def izglitibas_programmas():
    print("Izglītības programmas no pirmsskolas izglītības līdz pieaugušo izglītībai.")


def direktori():
    print("Artūrs Krīgers - 1946 - 1960 \nAnna Piebalga - 1962 - 1983")



def tradicijas():
    pass


def skolas_eka():
    pass


def izvelne(vards):
    print(vards + ", Izvelies par ko gribi uzzinat? Izvelies un ievadi")
    izvele = input("1 - Izglitibas programmas \n2 - Direktori \n3 - Tradicijas \n4 - Skolas eka")
    lietotaja_izvele=  int(izvele)
    if lietotaja_izvele == 1:
        izglitibas_programmas()
    if lietotaja_izvele == 2:
        direktori()
    if lietotaja_izvele == 3:
        tradicijas()
    if lietotaja_izvele == 4:
        skolas_eka()
    else:
        exit(0)



def sasveicinaties(vards):
    return print("Sveiki, " + vards)


if __name__ == '__main__':
    print("Sveiki es esmu V2V catbots Vjaceslavs")
    vards = input("Ka tevi sauc")
    sasveicinaties(vards)
    izvelne(vards)




