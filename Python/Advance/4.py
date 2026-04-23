""" 
! Comprehension:
	- It is a process of creating a new mutable collection by using an existing iterable in a single line of expression.
	- It is of 4 types:
		- List
		- set
		- Dictionary
		- Generator iterable

	! List Comprehension:
		- It is a process of creating a list collection by using an existing iterable.
		- Syntax:
			* var = [i for i in iterable]
			* var = [i for i in iterable if condition]
			* var = [TBS if condition else FBS for i in iterable]
			* var = [(i,j) for i in iterable1 for j in iterable2]
"""

def list_comp():
	natural = [i for i in range(1, 11)]
	print(natural)

	reverse = [i for i in range(10,0,-1)]
	print(reverse)

	print([i for i in range(1, int(input("Enter a number: "))+1)])

	even = [i for i in range(1, 11) if i%2 == 0]
	print(even)

	odd = [i for i in range(1, 11) if i%2 != 0]
	print(odd)

	nums = [i**2 if i%2 == 0 else i**3 for i in range(1,11)]
	print(nums)

	palindrome = [i for i in range(1,int(input("Enter a number: "))+1)  if str(i) == str(i)[::-1]]
	print(palindrome)

	vowel = [i for i in input("Enter a String: ") if i in "aeiouAEIOU"]
	print(vowel)

	collection = ["odd" if i%2 != 0 else i for i in range(1,6)]
	print(collection)

	digits = [int(i) for i in input("Enter a number: ")]
	print(digits)

	nested = [(i,j) for i in "Hai" for j in range(3)]
	print(nested)

	list1 = [[1,2],[3,4],[5,6]]
	out = [j for i in list1 for j in i]
	print(out)
# list_comp()

"""
! Set Comprehension:
		- It is a process of creating a set collection by using an existing iterable.
		- Syntax:
			* var = {i for i in iterable}
			* var = {i for i in iterable if condition}
			* var = {TBS if condition else FBS for i in iterable}
			* var = {(i,j) for i in iterable1 for j in iterable2}
"""		

"""
!Dictionary Comprehension:
"""

l1 = [1,2,3]
l2 = [456,789,890]

dic = {i:j for i, j in zip(l1,l2)}
print(dic)


"""+
! Generator iterable:
	- Comprehension way of creating a generator.
"""

n = int(input("Enter a number: "))
var = (i for i in range(1, n+1))

for i in var:
	print(i)

