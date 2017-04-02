# Ophelia's Algorithm
# may be used to create "super" random choice from a dice.

'''
# main code...
nums = [1, 2, 3, 4, 5, 6]

a = random.choice(nums)
b = random.randint(1, 6)
c = (((random.choice(nums) * random.randint(1, 6)) * (a * b)) % 5) + 1
d = (((a + b + c) ** random.choice(nums) ) % 5) + 1

lis1 = [a, b, d, c]

lis2 =  []
random.shuffle(lis1)

for i in range(random.choice(lis1) * (a+b+c+d)):
	y = random.randint(0, 666)
	w = ((math.sqrt((a + b + c + d)) ** math.sqrt((random.randint(y, y * (a+ b + c + d)))) * random.randint(1, 8))  % 5) + 1
	lis2.append(w)

for w in lis2:
	w = ((w**w) % 6) + 1
	lis1.append(w)
	random.shuffle(lis1)

t = (math.sqrt((a + b + c + d) ** random.choice(lis1) * random.choice(lis2)) % 5)
p = random.choice(lis1) ** math.sqrt(t * (a + b + c + d))
q = (((t**a) * (len(lis1) + len(lis2)) * p) % 5) + 1
ret = lis1[int((t**q) % len(lis1))]

return int(ret)
'''


# ------------------------------------


'''
# function version.


def rndzer():
	nums = [1, 2, 3, 4, 5, 6]

	a = random.choice(nums)
	b = random.randint(1, 6)
	c = (((random.choice(nums) * random.randint(1, 6)) * (a * b)) % 5) + 1
	d = (((a + b + c) ** random.choice(nums) ) % 5) + 1

	lis1 = [a, b, d, c]

	lis2 =  []
	random.shuffle(lis1)

	for i in range(random.choice(lis1) * (a+b+c+d)):
		y = random.randint(0, 666)
		w = ((math.sqrt((a + b + c + d)) ** math.sqrt((random.randint(y, y * (a+ b + c + d)))) * random.randint(1, 8))  % 5) + 1
		lis2.append(w)

	for w in lis2:
		w = ((w**w) % 6) + 1
		lis1.append(w)
		random.shuffle(lis1)
	
	t = (math.sqrt((a + b + c + d) ** random.choice(lis1) * random.choice(lis2)) % 5)
	p = random.choice(lis1) ** math.sqrt(t * (a + b + c + d))
	q = (((t**a) * (len(lis1) + len(lis2)) * p) % 5) + 1
	ret = lis1[int((t**q) % len(lis1))]

	return int(ret)

'''
