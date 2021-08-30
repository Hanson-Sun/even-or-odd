n = 1000
f = open("even_or_odd_v2.py", "a")
isodd = "'Even'"
f.write("x = int(input('Check if number is even or odd: ')) \n")
f.write("def EvenOdd(x): \n")
f.write("\tmatch x:\n")
f.write("\t\t case 0: \n \t\t\t return "+ isodd +"\n")
for i in range(1,n):
	if i%2 == 0:
		isodd = "'Even'"
	else:
		isodd = "'Odd'"

	f.write("\t\t case " + str(i) +": \n \t\t\t return " + str(isodd)+"\n")

f.write("\treturn 'Currently Not Supported' \n")
f.write("print(EvenOdd(x))")
f.close()
