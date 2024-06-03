# practice in class
number_of_cds = int(input('How many CDs do you have? '))
number_of_lps = int(input('How many LPs do you have? '))
number_of_albums = number_of_cds + number_of_lps

# comma print
print('With', number_of_cds, 'CDs and',
      number_of_lps, 'LPs, the number of albums you have is'
      ,number_of_albums, '.')

# string print
print('With', str(number_of_cds), 'CDs and',
      str(number_of_lps), 'LPs, the number of albums you have is',
      str(number_of_albums)+ '.')

# formatting print
print(f'with {number_of_cds} CDs and {number_of_lps} '
      f'LPs, the number of albums you have is {number_of_albums}.')

word1 = "Dog"
word2 = "Land"

word3 = "Spotted Alligator"
word4 = "Very wet areas"

# Ugly
print(f"{word1} {word2}")
print(f"{word3} {word4}")

# prettier... left justified
print(f"{word1:<25} {word2}")
print(f"{word3:<25} {word4}")

# right justified
print(f"{word1:>25} {word2}")
print(f"{word3:>25} {word4}")

# centered
print(f"{word1:^25} {word2}")
print(f"{word3:^25} {word4}")

# prettier... left justified with dots
print(f"{word1:.<25} {word2}")
print(f"{word3:.<25} {word4}")

print('Coffee'f"{cups_coffee_sold:>22}")

print('Tea'f"{cups_tea_sold:>25} ")

print('Cappuccino'f"{cups_cappuccino_sold:>18} "
      )