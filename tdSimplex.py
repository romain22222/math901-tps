import numpy as np


def simplex(c, A, b):
	m, n = A.shape
	tableau = np.zeros((m + 1, n + m + 1))

	tableau[:-1, :n] = A
	tableau[:-1, -1] = b
	tableau[-1, :n] = -c
	tableau[-1, -1] = 0

	while any(tableau[-1, :n] < 0):
		entering_var = np.argmin(tableau[-1, :n])

		ratios = tableau[:-1, -1] / tableau[:-1, entering_var]
		leaving_var = np.argmin(ratios)

		pivot = tableau[leaving_var, entering_var]
		tableau[leaving_var, :] /= pivot
		for i in range(m + 1):
			if i != leaving_var:
				tableau[i, :] -= tableau[i, entering_var] * \
								 tableau[leaving_var, :]

	solution = tableau[:-1, -1]
	objective_value = -tableau[-1, -1]

	return solution, objective_value


def eqSplitter(eq):
	e = [v.split("-") for v in eq.split("+")]
	ret = []
	for i in e:
		for j, k in enumerate(i):
			if k == "":
				continue
			k = k if k[0] != "x" else "1" + k
			if j == 0:
				ret.append(k)
			else:
				ret.append("-" + k)
	return ret


def parseEquation(eq):
	# Transforme un système de la forme maxZ = a1x1 + a2x2 + ... + anxn; b11x1 + b12x2 + ... + b1nxn + e1 = c1; ...; bm1x1 + bm2x2 + ... + bmnxn + en = cm
	# en 3 tableaux numpy: c, A, b
	# avec c = [a1, a2, ..., an], A = [[b11, b12, ..., b1n], ..., [bm1, bm2, ..., bmn]], b = [c1, ..., cm]
	# Exemple: parseEquation("nbVarX = 2 § maxZ = 30x1 + 50x2; 3x1 + 2x2 + e1 = 1800; x1 + e2 = 400; x2 + e3 = 600") renvoie (array([30, 50, 0]), array([[3, 2, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]]), array([1800, 400, 600]))
	eq = eq.replace(" ", "")
	eq = eq.replace("maxZ=", "")
	eq = eq.split("§")
	nbVarX = int(eq[0].split("=")[1])
	eq = eq[1].split(";")
	cp = eqSplitter(eq[0])
	c = [0 for _ in range(len(eq) + nbVarX - 1)]
	for i in cp:
		c[int(i.split("x")[1]) - 1] = int(i.split("x")[0] if i.split("x")[0] != "" else 1)
	A = []
	b = []
	for i in range(1, len(eq)):
		# For each equation create a new line in A with nbelements in eq + nbequations
		membs = eqSplitter(eq[i].split("=")[0])

		A.append([0] * (len(eq) + nbVarX - 1))
		b.append(int(eq[i].split("=")[1]))
		# For each element in the equation add it to the line in A corresponding to the one written in the equation
		for j in membs[:-1]:
			A[i - 1][int(j.split("x")[1]) - 1] = int(j.split("x")[0] if j.split("x")[0] != "" else 1)
	# In the last len(A) columns of A, add the identity matrix
	for i in range(len(A)):
		A[i][len(cp) + i] = 1
	A = np.array(A)
	b = np.array(b)
	c = np.array(c)
	return c, A, b


if __name__ == '__main__':
	eq = "nbVarX = 2 § maxZ = 30x1 - 50x2; 3x1 - 2x2 + e1 = 1800; -x1 + e2 = 400; x2 + e3 = 600"
	c, A, b = parseEquation(eq)
	print(c)
	print(A)
	print(b)
	exit()
	# Exemple d'utilisation
	A = np.array([[3, 2, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]])
	b = np.array([1800, 400, 600])
	c = np.array([30, 50, 0, 0, 0])

	optimal_solution, optimal_value = simplex(c, A, b)

	print(optimal_solution)
	print(optimal_value)
