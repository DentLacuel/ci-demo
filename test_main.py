from main import est_palindrome

def test_palindrome_simple():
    assert est_palindrome("kayak")
    assert est_palindrome("radar")

def test_palindrome_avec_majuscules():
    assert est_palindrome("Kayak")

def test_non_palindrome():
    assert not est_palindrome("python")