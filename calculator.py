
def main():
	#write your code here
	pass
	n1=input("Enter the first number: ")
	n2=input("Enter the second number: ")
	op=input("Choose the operation (+, -, /, *): ")
	if n1.isdigit():
		if n2.isdigit():
			if op == '+':
				an = int(n1) + int(n2)
				print ("The answer is " + str(an))
			elif op == '-':
				an = int(n1) - int(n2)
				print ("The answer is " + str(an))
			elif op == '*':
				an = int(n1) * int(n2)
				print ("The answer is " + str(an))
			elif op == '/':
				an = int(n1) / int(n2)
				print ("The answer is " + str(an))
			else :
				print (" invalid operation ")


		else :
			print (" invalid second number")
	else :
		print ("invalid first number")






if __name__ == '__main__':
	main()
