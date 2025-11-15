def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    broj_samoglasnika = sum(1 for c in tekst if c in vowels)
    broj_suglasnika = sum(1 for c in tekst if c in consonants)
    
    return {'vowels': broj_samoglasnika, 'consonants': broj_suglasnika}

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))

