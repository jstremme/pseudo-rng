import calendar
import time

def generate_k_random_numbers(x0, m, generated, n, k):

	if n == k:

		return generated

	else:

		a = 675789547
		b = 2453923

		xn = (a*x0 + b) % m
		generated.append(xn)
		print("At n = {}: Xn = {}".format(n, xn))

		n += 1

		return generate_k_random_numbers(x0=xn, m=m, generated=generated, n=n, k=k)

def main():

	k = 5
	m = 101
	generated = []
	current_time = calendar.timegm(time.gmtime())

	print("Current time is {}".format(current_time))
	print("Generating {} random numbers between 0 and {}".format(k, m-1))

	generated = generate_k_random_numbers(x0=current_time, m=m, generated=generated, n=0, k=k)
	print("Generated sequence: \n{}.".format(generated))

if __name__ == '__main__':

	main()