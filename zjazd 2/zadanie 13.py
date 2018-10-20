liczby = [x/10 for x in range (0, 10) ]
print (liczby)

kwadraty = {(x, x**2, x**3) for x in range (1, 101)}
print (kwadraty)

zbior_napisow = {'abc', 'ala ma kota ', 'aasdllldfsldfsldfl lsll sdfl', 'sd a aer wer das eqryt '}

print ({x: len(x) for x in zbior_napisow})