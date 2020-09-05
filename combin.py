'''

Factorial Function

Returns an integer value representing the factorial of a given positive integer input value. 

'''
def fact(n):
	if (n <= 0 or n % 1 != 0):
		print "Incorrect input value" 
		return -1 
	elif (n == 1):
		return 1
	else:
		return (n * fact(n - 1))

'''

Permutation - ordered, repititions

Returns an integer value representing the total permutations of a set of 'N' elements with 'n' selections

'''
def perm1 (N, n):
	if (N <= 0 or n <= 0 or n % 1 != 0 or N % 1 != 0):
		print "Incorrect input value"
		return -1 
	else: 
		return (N ** n)

'''

Permutation - ordered, no repititions

Returns an integer value representing the total permutations of a set of 'N' element with 'n' selections

	N - integer, cardinality of set
	n - integer, selection of elements
    
'''
def perm2 (N, n):
	if (N <= 0 or n <= 0 or n % 1 != 0 or N % 1 != 0 or n > N):
		print "Incorrect input value"
		return -1 
	else: 
		return (fact(N) / (fact((N - n))))

'''

Multinomial Permutation Function

Return an integer value representing the multinomial permutation of a set of 'N' elements with n1, n2..., nZ selections

    N - integer, cardinality of set
    n - integer list, each elements count

'''
def multi(N, n):
    if (N <= 0 or N % 1 != 0):
        print "Incorrect input value"
        return -1

    check_denom = 0
    denominator = 1

    for i in n:
        if (i <= 0 or i % 1 != 0):
            print "Incorrect input value"
            return -1
        check_denom = check_denom + i
        denominator = denominator * fact(i)

    if (check_denom > N):
            print "Incorrect input value"
            return -1

    return fact(N) / denominator

'''
    
Combination Function - unordered, no repititions

Returns an integer of n selections from N elements

'''
def choose(N, n):
    if (N <= 0 or n <= 0 or n % 1 != 0 or N % 1 != 0 or n > N):
        print "Incorrect input value"
        return -1
    else:
        return (fact(N) / (fact(n)*(fact((N - n)))))





















