# ---------------------------------------------------------------------------------------
# Abgabegruppe: 64
# Personen: Tom Aßmann, Leon Grant, Mathis Siebert
#
# -------------------------------------------------------------------------------------
import sys
import time

from pathlib import Path
from typing import Tuple, List

USAGE_TEXT = """
Das Skript wurde mit der falschen Anzahl an Parametern aufgerufen.
Die korrekte Aufrufsyntax ist:

    python permutationtest.py <sample-datei1> <sample-datei2> <alpha> <modus>
        <sample-datei1> - Eingabedatei mit den Werten der ersten Stichprobe
        <sample-datei2> - Eingabedatei mit den Werten der zweiten Stichprobe
        <alpha>         - Signifikanzniveau (im Bereich (0,1))
        <modus>         - Modus der Berechnung, exakt (exact) oder approximativ (approx)

Beispiel:

    python permutationtest.py sample1.txt sample2.txt 0.05 exact
        
        oder
    
    python permutationtest.py sample1.txt sample2.txt 0.05 approx 10000
                        
"""


def read_values(input_file: Path) -> List[float]:
    with input_file.open("r") as in_stream:
        values = [float(line.strip()) for line in in_stream.readlines() if line.strip()]

    return values


def run_exact_permutationtest(samples1: List[float], samples2: List[float]) -> Tuple[float, float]:
    """
    Diese Funktion testet, ob sich die Erwartungswerte der beiden Stichproben samples1 und samples2
    signifikant unterscheiden durch Prüfung aller möglichen Permutationen. Die (alternative) Hypothese
    nimmt an, dass sich die Erwartungswerte der beiden Populationen unterscheiden ((E(samples1) != E(samples2)).
    Die Null-Hypothese nimmt hingegen an, dass die Samples aus Populationen mit dem gleichen Erwartungswert stammen
    (E(samples1) = E(samples2)).

    Die Funktion gibt die Differenz der Erwartungswerte der Stichproben und den p-Wert des Tests zurück. Der p-Wert
    quantifiziert die Wahrscheinlichkeit, den gleichen oder einen noch größeren (absoluten) Unterschied der
    Erwartungswerte zu beobachten, wenn die Nullhypothese, dass die Stichproben aus Populationen mit demselben
    Erwartungswert gezogen wurden, wahr ist.

    :param samples1: Liste der beobachteten Werte aus der ersten Stichprobe
    :param samples2: Liste der beobachteten Werte aus der zweiten Stichprobe
    :return: Tuple bestehend aus der Differenz der Mittelwerte und dem p-Wert des Tests: (mean-diff,p)
    """

    complete_list = []
    complete_list.extend(samples1)
    complete_list.extend(samples2)

    print(len(complete_list))
    all_permutations = recursive_permutations(0, complete_list, [[complete_list[1]]])
    mean = 0

    for i, permutation in enumerate(all_permutations):
        mean_temp = 0
        for j, entry in enumerate(permutation):
            mean_temp += entry
        mean += mean_temp / len(permutation)

    mean = mean / len(all_permutations)

    return mean, 0

def recursive_permutations(index: int, sample_list: List[float], permutations: List[List[float]]) -> List[List[float]]:
    new_permutations = []
    for i, permutation in enumerate(permutations):
        insert_index = 0
        while insert_index <= len(permutation):
            #print(" --- INSERT INDEX: " + str(insert_index))
            #print(" --- LEN(X): " + str(len(permutation)))
            new_permutation = permutation.copy()
            new_permutation.insert(insert_index, sample_list[index])
            new_permutations.append(new_permutation)
            insert_index += 1

    if index + 3 == len(sample_list):
        return new_permutations
    return recursive_permutations(index + 1, sample_list, new_permutations)


def run_approx_permutationtest(samples1: List[float], samples2: List[float], n: int) -> Tuple[float, float]:
    """
    Diese Funktion testet, ob sich die Erwartungswerte der beiden Stichproben samples1 und samples2
    signifikant unterscheiden durch Prüfung von n zufälligen, duplikatfreien Permutationen. Die (alternative)
    Hypothese nimmt an, dass sich die Erwartungswerte der beiden Populationen unterscheiden
    ((E(samples1) != E(samples2)). Die Null-Hypothese nimmt hingegen an, dass die Samples aus Populationen
    mit dem gleichen Erwartungswert stammen (E(samples1) = E(samples2)).

    Die Funktion gibt die Differenz der Erwartungswerte der Stichproben und den p-Wert des Tests zurück. Der p-Wert
    quantifiziert die Wahrscheinlichkeit, den gleichen oder einen noch größeren (absoluten) Unterschied der
    Erwartungswerte zu beobachten, wenn die Nullhypothese, dass die Stichproben aus Populationen mit demselben
    Erwartungswert gezogen wurden, wahr ist.

    :param samples1: Liste der beobachteten Werte aus der ersten Stichprobe
    :param samples2: Liste der beobachteten Werte aus der zweiten Stichprobe
    :param n: Anzahl der zu bildenden zufälligen, duplikatfreien Permutationen
    :return: Tuple bestehend aus der Differenz der Mittelwerte und dem p-Wert des Tests: (mean-diff,p)
    """
    raise NotImplementedError("ToDo: Funktion muss implementiert werden.")


if __name__ == "__main__":
    if len(sys.argv) < 5 or len(sys.argv) > 6:
        print(USAGE_TEXT)
        exit(-1)

    input_file1 = Path(sys.argv[1])
    if not input_file1.exists() or input_file1.is_dir():
        print(f"Eingabedatei {input_file1} ist nicht vorhanden")
        exit(-1)

    input_file2 = Path(sys.argv[2])
    if not input_file2.exists() or input_file2.is_dir():
        print(f"Eingabedatei {input_file2} ist nicht vorhanden")
        exit(-1)

    alpha = float(sys.argv[3])
    if not alpha > 0 and alpha < 1.0:
        print("Der Parameter alpha muss im Bereich (0, 1) liegen!")
        exit(-1)

    modus = sys.argv[4].lower()
    if modus not in ["exact", "approx"]:
        print("Der Parameter muss entweder 'exact' oder 'approx' sein")
        exit(-1)

    samples1 = read_values(input_file1)
    samples2 = read_values(input_file2)

    if modus == "exact":
        mean_diff, p_value = run_exact_permutationtest(samples1, samples2)
    elif modus == "approx":
        num_permutations = int(sys.argv[5])
        if num_permutations <= 0:
            print("Anzahl der zu generierenden Permutationen muss größer als 0 sein")
            exit(0)

        mean_diff, p_value = run_approx_permutationtest(samples1, samples2, num_permutations)
    else:
        raise AssertionError()

    print(f"Differenz zwischen den Mittelwerten: {mean_diff}")
    print(f"P-Wert (p={p_value})")
