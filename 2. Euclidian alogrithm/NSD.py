def nsd(n, m):
	if m == 0:
		return n
	elif n == 0:
		return m
	elif m > n:
		return nsd(n, m % n)
	else:
		return nsd(n % m, m)

print(nsd(int(input("1'st num ")), int(input("2'nd num "))))
