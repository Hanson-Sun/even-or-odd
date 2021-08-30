n = 1000;
f = open("even_or_odd.py", "a")
isodd = "'Even'"
f.write("x = int(input('Check if number is even or odd: ')) \n")
f.write("def EvenOdd(x): \n")
f.write("\tif x == 0: \n \t\t return "+ isodd +"\n")
for i in range(1,n):
	if i%2 == 0:
		isodd = "'Even'"
	else:
		isodd = "'Odd'"

	f.write("\telif x == " + str(i) +": \n \t\t return " + str(isodd)+"\n")

f.write("\telse: \n \t\t return 'Currently Not Supported' \n")
f.write("print(EvenOdd(x))")
f.close()

