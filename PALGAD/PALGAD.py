from Funktsionid import EditData, Eemaldamine, Formaatimine, Keskmine, LeidkeInimesedAlgabTahega, LisaPremia, Lisamine, OtsiPalgaJargi, PalkAllaKeskmine, PalkYleSumma, RenameEveryThird, SarnasedPalgad, Sort, SortByName, SuurimPalk, ToopaevapalgaMuutus, Top, Tulumaks, VaiksemPalk

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]



if __name__ == "__main__":
    while True:
        print("Lisamine-1, Eemaldamine-2, SuurimPalk-3, VäiksemPalk-4, Sorteeri-5, SarnasedPalgad-6, "
              "OtsiPalgaJargi-7, PalkYleSumma-8, Top-9, Keskmine-10, Tulumaks-11, SortByName-12, PalkAllaKeskmine-13, "
              "Formaatimine-14, ToopaevapalgaMuutus-15, RenameEveryThird-16, EditData-17, LeidkeInimesedAlgabTahega-18, "
              "LisaPremia-19, Väljumine-0")
        v = int(input())

        if v == 1:
            k = int(input("Mitu inimest lisame? "))
            inimesed, palgad = Lisamine(inimesed, palgad, k)
            for i in range(len(palgad)):
                print(inimesed[i], "saab kätte", palgad[i])

        elif v == 2:
            inimesed, palgad = Eemaldamine(inimesed, palgad)
            for i in range(len(palgad)):
                print(inimesed[i], "saab kätte", palgad[i])

        elif v == 3:
            maxpalk, nimed = SuurimPalk(inimesed, palgad)
            if nimed:
                print("Suurim palk on", maxpalk, "EUR. Saajad:", ", ".join(nimed))
            else:
                print("Palkade nimekiri on tühi.")

        elif v == 4:
            minpalk, nimed = VaiksemPalk(inimesed, palgad)
            if nimed:
                print("Väikseim palk on", minpalk, "EUR. Saajad:", ", ".join(nimed))
            else:
                print("Palkade nimekiri on tühi.")

        elif v == 5:
            i = int(input("Kasvav järjestus-0, Kahanev järjestus-1: "))
            inimesed, palgad = Sort(inimesed, palgad, i)
            for i in range(len(palgad)):
                print(palgad[i], "on", inimesed[i], "-l")

        elif v == 6:
            SarnasedPalgad(inimesed, palgad)

        elif v == 7:
            nimi = input("Sisestage inimese nimi, kelle palga järele otsite: ")
            leitud_palgad = OtsiPalgaJargi(inimesed, palgad, nimi)

            if leitud_palgad:
                print(f"{nimi} saab järgnevad palgad: {', '.join(map(str, leitud_palgad))} EUR")
            else:
                print(f"{nimi} ei ole nimekirjas.")

        elif v == 8:
            summa = int(input("Sisestage summa: "))
            yle = input("Otsite inimesi, kes teenivad rohkem (jah/ei): ").lower() == 'jah'
            tulemused = PalkYleSumma(inimesed, palgad, summa, yle)
            if tulemused:
                for nimi, palk in tulemused:
                    print(f"{nimi} teenib {palk} EUR")
            else:
                print("Sobivaid inimesi ei leitud.")

        elif v == 9:
            top_tulemused = Top(inimesed, palgad)
            if top_tulemused:
                (madalad_nimed, madalad_palgad), (korged_nimed, korged_palgad) = top_tulemused
                print("Kolm kõige vaesemat:")
                for nimi, palk in zip(madalad_nimed, madalad_palgad):
                    print(f"{nimi}: {palk} EUR")

                print("\nKolm kõige rikkamat:")
                for nimi, palk in zip(korged_nimed, korged_palgad):
                    print(f"{nimi}: {palk} EUR")
            else:
                print("Nimekiri on liiga lühike.")

        elif v == 10:
            keskmine_palk, keskmine_nimi = Keskmine(inimesed, palgad)
            if keskmine_palk and keskmine_nimi:
                print(f"Keskmine palk on {keskmine_palk} EUR, mille teenib {keskmine_nimi}.")
            else:
                print("Nimekiri on tühi.")

        elif v == 11:
            palk = float(input("Sisestage kuupalga summa: "))
            lapsed = int(input("Sisestage laste arv: "))
            netopalk = Tulumaks(palk, lapsed)
            print(f"Netopalk pärast tulumaksu mahaarvamist: {netopalk:.2f} EUR")
            
        elif v == 12:
            i = int(input("Kasvav järjestus-0, Kahanev järjestus-1: "))
            inimesed, palgad = SortByName(inimesed, palgad, i)
            for i in range(len(palgad)):
                print(palgad[i], "on", inimesed[i], "-l")

        elif v == 13:
            inimesed, palgad = PalkAllaKeskmine(inimesed, palgad)

        elif v == 14:
            inimesed, palgad = Formaatimine(inimesed, palgad)
            for i in range(len(palgad)):
                print(inimesed[i], "saab kätte", palgad[i])

        elif v == 15:
            aastad = int(input("Sisestage aastate arv: "))
            inimesed, palgad = ToopaevapalgaMuutus(inimesed, palgad, aastad)

        elif v == 16:
            inimesed = RenameEveryThird(inimesed)

        elif v == 17:
            inimesed, palgad = EditData(inimesed, palgad)

        elif v == 18:
            taht = input("Sisestage täht: ")
            LeidkeInimesedAlgabTahega(inimesed, palgad, taht)
            
        elif v == 19:
            nimi = input("Sisestage inimese nimi: ").capitalize()
            inimesed, palgad = LisaPremia(inimesed, palgad, nimi)

        elif v == 0:
            break
