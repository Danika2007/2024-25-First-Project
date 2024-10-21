def fajlBeolv(fájlNév):
    try:
        with open(fájlNév, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"A {fájlNév} nincs ilyen nevű fájl.")
        return None

def is_number(adat):
    try:
        [float(item) for item in adat]
        return True
    except ValueError:
        return False

def buborekRend(lista, fordit=False):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if fordit:
                if lista[j] < lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def quickSort(lista, fordit=False):
    if len(lista) <= 1:
        return lista
    else:
        tam = lista[len(lista) // 2]
        bal = [x for x in lista if x < tam]
        kozep = [x for x in lista if x == tam]
        jobb = [x for x in lista if x > tam]
        
        if fordit:
            return quickSort(jobb, fordit=True) + kozep + quickSort(bal, fordit=True)
        else:
            return quickSort(bal, fordit=False) + kozep + quickSort(jobb, fordit=False)

def beszúras(lista, ujAdat, fordit=False):
    for i, item in enumerate(lista):
        if fordit:
            if ujAdat > item:
                lista.insert(i, ujAdat)
                return lista
        else:
            if ujAdat < item:
                lista.insert(i, ujAdat)
                return lista
    lista.append(ujAdat)
    return lista

def main():
    fájlNév = "ki.txt"
    adat = fajlBeolv(fájlNév)
    
    if adat is None or len(adat) == 0:
        print("A fájl üres vagy nem olvasható.")
        return

    szam = is_number(adat)
    if szam:
        adat = [float(item) for item in adat]
        print("A fájl számokat tartalmaz.")
    else:
        print("A fájl számokat és szövegeket is tartalmaz.")

    irany = input("Válaszd ki a rendezés irányát (n - növekvő, c - csökkenő): ").lower()
    fordit = irany == 'c'

    rendAlgorit = input("Válasz a két rendezési módszer közzül (b - buborékrendezés(boublesort), q - gyorsrendezés(quicksort)): ").lower()

    if rendAlgorit == 'b':
        rendeAdat = buborekRend(adat, fordit=fordit)
        print("Buborékrendezés eredménye:")
    elif rendAlgorit == 'q':
        rendeAdat = quickSort(adat, fordit=fordit)
        print("Quicksort eredménye:")
    else:
        print("Nincs ilyen rendezés")
        return

    print(rendeAdat)

    ujUjAdat = input("Adj meg egy új elemet: ")
    if szam:
        try:
            ujUjAdat = float(ujUjAdat)
        except ValueError:
            print("Érvénytelen szám.")
            return

    beszurAdat = beszúras(rendeAdat, ujUjAdat, fordit=fordit)
    print("Az új elem beszúrása után így néz ki a rendezés:")
    print(beszurAdat)

if __name__ == "__main__":
    main()
