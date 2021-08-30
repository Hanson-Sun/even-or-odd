n = 100000
f = open("even_or_odd_v3.py", "a")
isodd = "'Even'"
f.write("x = int(input('Check if number is even or odd: ')) \n")
f.write("def EvenOdd(x): \n")
f.write("\t return { \n")
f.write("\t\t 0 : 'Even' ")
for i in range(1,n):
	if i%2 == 0:
		isodd = "'Even'"
	else:
		isodd = "'Odd'"

	f.write(",\n \t\t" + str(i) +" : " + str(isodd))

f.write("\t}.get(x, 'Currently Not Supported')\n")
f.write("print(EvenOdd(x))")
f.close()

