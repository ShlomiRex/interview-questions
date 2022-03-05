# From amazon interview prep: https://youtu.be/aOu7BaKgnMc?t=786

def nth_fibbo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	i = 0
	j = 1
	for _ in range(n-1):
		i, j = j, i+j
	return j


if __name__ == "__main__":
    for i in range(20):
        res = nth_fibbo(i)
        print("{}th fibbo is {}".format(i, res))
    
    
