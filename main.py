"""
Lecture de données depuis un fichier CSV"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as f:
        lignes = f.readlines()
    data = []
    for ligne in lignes:
        # Enlever le retour à la ligne et splitter sur ';'
        data.append([int(x) for x in ligne.strip().split(';')])
    return data

def get_list_k(data, k):
    """retourne la k-ième liste de la liste <data>

    Args:
        data (list): liste de n liste d'entiers

    Returns:
        list: la k-ième liste 
    """
    return data[k]

def get_first(l):
    """retourne le premier élément de la liste <l>

    Args:
        l (list): liste

    Returns:
        entier: le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """retourne le dernier élément de la liste <l>

    Args:
        l (list): liste

    Returns:
        entier: le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """retourne le maximum de la liste <l>

    Args:
        l (list): liste

    Returns:
        entier: le maximum de la liste
    """
    return max(l)

def get_min(l):
    """retourne le minimum de la liste <l>

    Args:
        l (list): liste

    Returns:
        entier: le minimum de la liste
    """
    return min(l)

def get_sum(l):
    """retourne la somme de la liste <l>

    Args:
        l (list): liste

    Returns:
        entier: la somme de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Fonction principale de test des fonctions secondaires
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
