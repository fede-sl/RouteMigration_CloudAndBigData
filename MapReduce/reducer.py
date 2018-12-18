import sys

f=open("aveX.csv", "w")
for line in sys.stdin:
	f.write(line.replace(" ", ",") + "\n")
	
f.close()
#python mapper.py < "ave.csv" | sort | python reducer.py
	
