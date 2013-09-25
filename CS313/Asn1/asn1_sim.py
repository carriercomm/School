import subprocess

min_e = 0.001
max_e = 0.002
e_step = 0.0001

for K in range(1, 1001):
	if 8000 % K != 0: continue
	e = min_e
	while e <= max_e:
		#args = "asn1.py 100 " + str(K) + " 8000 " + str(e) + " 8000000 5"
		subprocess.call(["python", "asn1_2.py", "100", str(K), "8000", str(e), "80000000", "5"])
		e += e_step
		print 'finished', K, e

print 'finished sim'
