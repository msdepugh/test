'''

Factorial Function

Returns an integer value representing the factorial of a given positive integer input value. 

'''
def factorial(n):
	if (n <= 0 or n % 1 != 0):
		print "Incorrect input value" 
		return -1 
	elif (n == 1):
		return 1
	else:
		return (n * factorial(n - 1))

'''

Permutation - ordered, repititions

Returns an integer value representing the total permutations of a set of 'N' elements with 'n' selections

'''
def perm1 (N, n):
	if (N <= 0 or n <= 0 or n % 1 != 0 or N % 1 != 0):):
		print "Incorrect input value"
		return -1 
	else: 
		return (N ** n)
