# ---------------------------------------------------------------------------------------
# Abgabegruppe:
# Personen:
#
# -------------------------------------------------------------------------------------
from pathlib import Path
from typing import Dict, Union, Tuple, List

# Die Eingabedatei muss im gleichen Verzeichnis liegen wie die Skriptdatei exercise_2
input_file = Path("todesursachen.csv")


entries = [] # ( int Jahr; String Geschlecht; String Altersgruppe;  Todesursache; int Anzahl)

with input_file.open(mode="r", encoding="UTF-8") as input_stream:
    for i, line in enumerate(input_stream.readlines()):
        line = line.strip()
        if not line or i == 0:
            continue

        columns = line.split(";") # Trenne Zeilenwerte durch “;”
#                           Jahr            Geschlecht   Altersgruppe  Todesursache Anzahl
        entries.append((int(columns[0]), columns[1], columns[2], columns[3], int(columns[4])))

def aufgabe_a1() -> int:
    """
    Ermitteln Sie die Anzahl an verschiedenen (“unique”) Todesursachen, die im Datensatz erfasst werden.

    :return: Anzahl der verschiedenen Todesursachen im Datensatz (als int)
    """

    todesursachen = []

    for i, entry in enumerate(entries): # für jedes Tupel

        isNew = True
        for j, ursache in enumerate(todesursachen):     # für jede schon bekannte Todesursache

            if entry[3] == ursache:  # wenn die ursache im tupel gleich der bekannten ursache ist
                isNew = False
                break                                 # schaue nächstes tupel an

        if isNew:
            todesursachen.append(entry[3])                  # wenn wir nicht rausgesprungen sind heißt das: neue todesursache

    return len(todesursachen)


def aufgabe_a2() -> Dict[str, Union[int, float]]:
    """
    Geben Sie den Durchschnitt (mean), den Median (med), die Standardabweichung (stddev), den minimalen Wert (min),
    den maximalen Wert (max), den Interquartilsabstand (iqr) und das 90%-Perzentil (90p) der Verstorbenen pro Jahr
    an.

    Die Rückgabe der Kennzahlen erfolgt als Dictionary mit folgendem Aufbau:
    {
        "mean": <Durchschnitt (float)>,
        "med": <Median (int)>,
        "stddev": <Standardabweichung (float)>,
        "min": <Minimaler-Wert (float)>,
        "max": <Maximaler-Wert (int)>,
        "iqr": <Interquartilsabstand (float)>,
        "90p": <90%-Perzentil (int)>
    }

    Die Kennzahlen sind entweder als float oder als int anzugeben (siehe Aufbaubeschreibung)

    :return: Dictionary mit den Kennzahlen
    """

    data: Dict[str, Union[int, float]] = dict()

    verstorbeneProJahr: Dict[int, int] = dict()

    for i, entry in enumerate(entries):                                         # für jeden entry
        if entry[0] in verstorbeneProJahr:                                      # falls es schon einen gibt: 1 draufaddieren
            verstorbeneProJahr[entry[0]] = verstorbeneProJahr[entry[0]] + entry[4]
        else:                                                                   # falls es noch kein index gibt von der jahreszahl des entry´s
            verstorbeneProJahr[entry[0]] = entry[4]

    "mean"
    verstorbeneGesamt = 0

    for i, jahr in enumerate(verstorbeneProJahr):
        verstorbeneGesamt += verstorbeneProJahr[jahr]

    data["mean"] = verstorbeneGesamt/len(verstorbeneProJahr)


    #med: Die Anzahl Verstorbener ...
    sortierteListe = []
    for i, jahr in enumerate(verstorbeneProJahr):
        sortierteListe.append(verstorbeneProJahr[jahr])

    sortierteListe.sort()

    data["med"] = sortierteListe[int(len(sortierteListe)/2)]

    for i, jahr in enumerate(verstorbeneProJahr):
        if verstorbeneProJahr[jahr] == data["med"]:
            print(jahr)

    return data





def aufgabe_a3() -> Dict[int, int]:
    """
    Ermitteln Sie die Anzahl der Kinder bzw. Heranwachsenden (< 15 Jahre), welche an einer Ursache verstorben sind,
    an welcher in dem jeweiligen Jahr auch mindestens 10 andere Kinder / Heranwachsende verstorben sind.
    Ermitteln Sie diese Kennzahl für jedes im Datensatz erfasste Jahr.

    Die Rückgabe erfolgt als Dictionary, welches ein Jahr (int) auf die Anzahl an verstorbenen Kindern (int)
    abbildet.

    {
        1980: 101234,
        1981: 12456,
        1982: 9876,
        ....

    }
    (Beispiel zeigt exemplarische, nicht-korrekte Werte!)

    :return: Dictionary, welches ein Jahr (int) auf die Anzahl an verstorbenen Kindern (int) abbildet.
    """

    raise NotImplementedError("ToDo: Funktion muss noch implementiert werden!")


def aufgabe_b1() -> int:
    """
    In welchem Jahr sind die meisten Männer durch Stürze ums Leben gekommen?

    Als Rückgabe wird ein int erwartet, welcher das jeweilige Jahr angibt.

    :return: Jahr (int) in dem am meisten Männer durch Stürze ums Leben gekommen sind
    """

    raise NotImplementedError("ToDo: Funktion muss noch implementiert werden!")


def aufgabe_b2() -> Tuple[float, float]:
    """
    Ertrinken im Durchschnitt mehr Kinder bzw. Heranwachsende (< 15 Jahre) oder mehr Menschen im
    Rentenalter (>= 65 Jahre) pro Jahr?

    Als Rückgabe wird ein Pair von float-Zahlen erwartet, welche die beiden Durchschnittswerte der jeweiligen
    Personengruppen angeben:

    (<Durchschnitt-Kinder (float)>, <Durchschnitt-Renter*innen (float)>)

    :return: (<Durchschnitt-Kinder (float)>, <Durchschnitt-Renter*innen (float)>)
    """

    raise NotImplementedError("ToDo: Funktion muss noch implementiert werden!")


def aufgabe_b3() -> str:
    """
    Welche Altersgruppe weist den größten Median hinsichtlich der Anzahl an Verstorbenen pro Jahr aus?

    Als Rückgabe wird die Beschreibung der Altersgruppe als string erwartet (bspw. "15 bis unter 20 Jahre")

    :return: Altersgruppe mit dem größten Median hinsichtlich der Anzahl an Verstorbenen pro Jahr
    """

    raise NotImplementedError("ToDo: Funktion muss noch implementiert werden!")


def aufgabe_b4() -> float:
    """
    In wieviel Prozent der erfassten Jahre sind mehr Frauen als Männer in einem Jahr gestorben?

    Als Rückgabe wird ein float zwischen 0 und 1 erwartet.

    :return: Anteil der Jahre in denen mehr Frauen als Männer verstorben sind (als float)
    """

    raise NotImplementedError("ToDo: Funktion muss noch implementiert werden!")


def aufgabe_b5() -> List[Tuple[str, float]]:
    """
    Welche Todesursachen weisen die größten Unterschiede zwischen Männern und Frauen im Alter von >= 20 Jahren und
    < 30 auf? Berechnen Sie hierzu die absoluten Differenz der Durchschnittswerte pro Jahr und Todesursache und
    geben Sie die drei Todesursachen mit den größten durchschnittlichen Differenzen an.

    Als Rückgabe wird eine drei-elementige Liste erwartet, welche die Todesursachen mit den größten Differenzen
    zwischen Männern und Frauen (absteigend geordnet) enthält. Jedes Element der Liste ist dabei ein Pair (2-Tupel)
    bestehend aus dem Namen der Todesursache und der durchschnittlichen Differenz. Beispiel:

    [
        ("BN des Magens", 245.45),
        ("Diabetes mellitus", 200.87),
        ("Krankheiten der Niere", 196.5)
    ]

    :return: Drei-elementige Liste mit den Todesursachen mit den größten Unterschieden zwischen Männern und Frauen.
    """

    raise NotImplementedError("ToDo: Funktion muss noch implementiert werden!")


def aufgabe_b6() -> List[Tuple[str, float]]:
    """
    Welche Todesursachen weisen die kleinsten Schwankungen hinsichtlich der Anzahl an Verstorbenen pro Jahr auf?
    Berechnen Sie hierzu die Standardabweichungen der einzelnen Todesursachen und setzen Sie diese in Relation
    zu deren jeweiligen Durchschnittswert. Geben Sie die drei Todesursachen mit den kleinsten (relativen)
    Standardabweichungen an.

    Als Rückgabe wird eine drei-elementige Liste erwartet, welche die Todesursachen mit den kleinsten Schwankungen
    (absteigend geordnet) enthält. Jedes Element der Liste ist dabei ein Pair (2-Tupel) bestehend aus dem Namen
    der Todesursache und der (relativen) Standardabweichung. Beispiel:

    [
        ("BN des Magens", 0.123),
        ("Diabetes mellitus", 0.104),
        ("Krankheiten der Niere", 0.0965)
    ]

    :return: Drei-elementige Liste mit den Todesursachen mit den kleinsten Schwankungen.
    """

    raise NotImplementedError("ToDo: Funktion muss noch implementiert werden!")


if __name__ == "__main__":
    #
    # Hier nichts verändern!
    #
    print("Lösungen für a)")

    print("\t1: Anzahl an verschiedenen (“unique”) Todesursachen:")
    print(f"\t\t{aufgabe_a1()}\n")

    print("\t2: Kennzahlen der Verstorbenen pro Jahr:")
    kennzahlen = aufgabe_a2()
    for key in sorted(kennzahlen.keys()):
        print(f"\t\t{key}: {round(kennzahlen[key], 1)}")
    print()

    print("\t3: Anzahl der verstorbenen Kinder bzw. Heranwachsenden (< 15 Jahre) pro Jahr:")
    jahr_zu_todesursache = aufgabe_a3()
    for jahr in sorted(jahr_zu_todesursache.keys()):
        print(f"\t\t{jahr}: {jahr_zu_todesursache[jahr]}")
    print()

    # ----

    print("Lösungen für b)")

    print("\t1: In welchem Jahr sind die meisten Männer durch Stürze ums Leben gekommen?")
    print(f"\t\t{aufgabe_b1()}\n")

    print("\t2: Ertrinken im Durchschnitt mehr Kinder bzw. Heranwachsende (< 15 Jahre) oder mehr "
          "Menschen im Rentenalter (>= 65 Jahre) pro Jahr?")
    ergebnis_b2 = aufgabe_b2()
    print(f"\t\tDurchschnitt Kinder: {round(ergebnis_b2[0], 2)}")
    print(f"\t\tDurchschnitt Rentner:innen: {round(ergebnis_b2[1], 2)}\n")

    print("\t3: Welche Altersgruppe weist den größten Median hinsichtlich der Anzahl an Verstorbenen "
          "pro Jahr aus?")
    print(f"\t\t{aufgabe_b3()}\n")

    print("\t4: In wieviel Prozent der erfassten Jahre sind mehr Frauen als Männer in einem Jahr gestorben?")
    print(f"\t\t{round(aufgabe_b4(), 4) * 100}%\n")

    print("\t5:Welche Todesursachen weisen die größten Unterschiede zwischen Männern und Frauen auf?")
    todesursachen_b5 = aufgabe_b5()
    for i, (todesursache, differenz) in enumerate(todesursachen_b5):
        print(f"\t\t{i}: {todesursache} ({round(differenz, 2)})")
    print()

    print("\t6:Welche Todesursachen weisen die kleinsten Schwankungen hinsichtlich der Anzahl an "
          "Verstorbenen pro Jahr auf?")
    todesursachen_b6 = aufgabe_b6()
    for i, (todesursache, rel_std_abw) in enumerate(todesursachen_b6):
        print(f"\t\t{i}: {todesursache} ({rel_std_abw})")
    print()
