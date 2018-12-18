import sys

for line in sys.stdin:
    word = line.split(',')
    latitud = word[4]#recibe la latitud
    longitud = word[3]#recibe la altitud
    date = word[2]
    print(date + " " + longitud + " " + latitud)
#python mapper.py < "ave.csv"
