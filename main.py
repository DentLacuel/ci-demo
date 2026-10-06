def est_palindrome(mot):
    """Vérifie si un mot est un palindrome."""
    mot = mot.lower().replace(" ", "")
    return mot == mot[::-1]