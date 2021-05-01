# laske tunnit ja minuutit kun syötetään työn aloitus ja lopetus aika
# import time ????
# tarviiko antaa 12 vai 24 tuntisen kellon

print("Käytä 24H kelloa")

while True:

    print("Aloitus aika: ")
    aloitus_aika = float(input())
    print("Lopetus aika: ")
    lopetus_aika = float(input())

    if aloitus_aika == 666:
        break

    else:
        kokonais_aika = lopetus_aika - aloitus_aika
        formatted_kokonais_aika = "{:.2f}".format(kokonais_aika)
        print("Tunnit:", formatted_kokonais_aika)
        continue
