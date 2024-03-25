# 1)
import csv
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot

Goriente = [
	[0, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 1],
	[0, 0, 0, 1, 0, 0, 0],
	[0, 1, 1, 0, 0, 0, 0],
	[0, 0, 1, 0, 1, 1, 0],
	[0, 1, 0, 0, 1, 0, 1],
	[0, 0, 0, 0, 0, 0, 0],
]
Gnon_oriente = [
	[0, 1, 1, 0, 0, 0, 0],
	[1, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 1, 1, 0, 0],
	[0, 1, 1, 0, 0, 0, 0],
	[0, 1, 1, 0, 1, 1, 0],
	[0, 0, 0, 0, 1, 0, 1],
	[0, 1, 0, 0, 0, 1, 0],
]


# 2)

def degre(graph, sommet):
	return sum(graph[sommet])


for s in range(Gnon_oriente.__len__()):
	...
# print("degre de", s + 1, "sur non orienté :", degre(Gnon_oriente, s))


# print()


def degre_entrant(graph, sommet):
	return sum([graph[i][sommet] for i in range(graph.__len__())])


for s in range(Goriente.__len__()):
	...
# print("degre sortant de", s + 1, "sur orienté:", degre(Goriente, s))
# print("degre entrant de", s + 1, "sur orienté:", degre_entrant(Goriente, s))


# print()


# 3)

# classic matrix multiplication with bitwise OR
def produit_matriciel(A, B):
	return [[int(any(([A[i][k] & B[k][j] for k in range(A.__len__())]))) for j in range(B.__len__())] for i in
			range(A.__len__())]


def identity(matrice):
	return [[1 if i == j else 0 for j in range(matrice)] for i in range(matrice)]


def matrice_sum(m1, m2):
	return [[m1[i][j] | m2[i][j] for j in range(m1.__len__())] for i in range(m1.__len__())]


def print_matrice(matrice):
	for i in range(matrice.__len__()):
		...
	# print(matrice[i])


# print()


def A_n(graph):
	A = matrice_sum(graph, identity(graph.__len__()))
	Ai = A[:]
	while A != produit_matriciel(A, Ai):
		A = produit_matriciel(A, Ai)
	return A


def distance(graph, sommet, n):
	A = graph
	for i in range(n - 1):
		A = produit_matriciel(A, graph)
	return [(i if A[sommet][i] > 0 else -1) for i in range(A.__len__())]


def sommets_a_distance(graph, sommet, n):
	tab = distance(graph, sommet, n)
	return [i for i in range(graph.__len__()) if tab[i] > 0]


for s in range(Gnon_oriente.__len__()):
	...
# print("sommets à distance 2 de", s + 1, "sur le non orienté :", sommets_a_distance(Gnon_oriente, s, 2))
# print()
for s in range(Gnon_oriente.__len__()):
	...
# print("sommets à distance 3 de", s + 1, "sur le non orienté :", sommets_a_distance(Gnon_oriente, s, 3))
# print()
for s in range(Goriente.__len__()):
	...
# print("sommets à distance 2 de", s + 1, "sur l'orienté :", sommets_a_distance(Goriente, s, 2))
# print()
for s in range(Goriente.__len__()):
	...
# print("sommets à distance 3 de", s + 1, "sur l'orienté :", sommets_a_distance(Goriente, s, 3))


# print()


# 4)

def distance_min(graph, sommet1, sommet2):
	if sommet1 == sommet2:
		return 0
	A = matrice_sum(graph, identity(graph.__len__()))
	Ai = A[:]
	An = A_n(A)
	n = 1
	while A[sommet1][sommet2] == 0 and A != An:
		A = produit_matriciel(A, Ai)
		n += 1
	return n if A[sommet1][sommet2] > 0 else -1


for s1 in range(Gnon_oriente.__len__()):
	for s2 in range(Gnon_oriente.__len__()):
		...
	# print("distance minimale entre", s1 + 1, "et", s2 + 1, "sur le non orienté :",
	# 	  distance_min(Gnon_oriente, s1, s2))
# print()
# print()

for s1 in range(Goriente.__len__()):
	for s2 in range(Goriente.__len__()):
		...
	# print("distance minimale entre", s1 + 1, "et", s2 + 1, "sur l'orienté :", distance_min(Goriente, s1, s2))
# print()


# print()


# 5)

def composantes_connexes(graph):
	A = A_n(graph)
	cc_count = 1
	cPos = 0
	for i in range(A.__len__()):
		if A[i][cPos] == 0:
			cc_count += 1
			while A[i][cPos] == 0:
				cPos += 1
	return cc_count


# print("nombre de composantes connexes du graphe non orienté :", composantes_connexes(Gnon_oriente))
# print("nombre de composantes fortement connexes du graphe orienté :", composantes_connexes(Goriente))
# print()


# 6)

def rang(graph):
	treated = [i for i in range(graph.__len__()) if degre_entrant(graph, i) == 0]
	if not treated:
		return -1
	toTreat = [i for i in range(graph.__len__()) if i not in treated]
	r = [0 if i in treated else -1 for i in range(graph.__len__())]
	k = 1
	while toTreat:
		newTreated = treated[:]
		for i in toTreat:
			if sum([graph[j][i] for j in toTreat]) == 0:
				r[i] = k
				treated.append(i)
		toTreat = [i for i in toTreat if r[i] == -1]
		if set(treated) == set(newTreated):
			return -1
		k += 1
	return r


# print("rang sur le non orienté :", rang(Gnon_oriente))
# print("rang sur l'orienté :", rang(Goriente))

Goriente2 = [
	[0, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 1, 1, 1, 1],
	[0, 0, 0, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 1, 0, 1],
	[0, 0, 0, 0, 0, 0, 0]
]

# print("rang sur l'orienté 2 :", rang(Goriente2))
# print()

# TP 2

I = float("inf")

# 1)

Gorientep = [
	[0, 8, 2, I, I, I, I],
	[I, 0, I, I, 3, I, 10],
	[I, I, 0, 3, I, I, I],
	[I, 2, 4, 0, I, I, I],
	[I, I, 5, I, 0, 4, I],
	[I, 5, I, I, 2, 0, 2],
	[I, I, I, I, I, I, 0]
]


def dijkstra(graph, sommet):
	l = [graph[sommet][i] for i in range(graph.__len__())]
	p = [sommet if l[i] != I else -1 for i in range(graph.__len__())]
	D = [sommet]
	while len(D) != graph.__len__():
		lMin = min([l[i] for i in range(graph.__len__()) if i not in D])
		iMin = l.index(lMin)
		D.append(iMin)
		for j in range(graph.__len__()):
			if j not in D:
				l[j] = min(l[j], l[iMin] + graph[iMin][j])
				if l[j] == l[iMin] + graph[iMin][j]:
					p[j] = iMin
	return l, [p[i] + 1 if l[i] != I else -1 for i in range(graph.__len__())]


# print("dijkstra sur le graphe proposé en partant de 1 :", dijkstra(Gorientep, 0))
# print()

# print("dijkstra sur le graphe proposé en partant de 2 :", dijkstra(Gorientep, 1))
# print()


# 2)

def floyd(graph):
	W = [[graph[i][j] for j in range(graph.__len__())] for i in range(graph.__len__())]
	P = [[i + 1 if graph[i][j] != I else -1 for j in range(graph.__len__())] for i in range(graph.__len__())]
	for k in range(graph.__len__()):
		for i in range(graph.__len__()):
			for j in range(graph.__len__()):
				if W[i][j] > W[i][k] + W[k][j]:
					W[i][j] = W[i][k] + W[k][j]
					P[i][j] = P[k][j]
	return W, P


floydGop = floyd(Gorientep)

# print("floyd sur le graphe proposé :")
# print_matrice(floydGop[0])
# print_matrice(floydGop[1])
# print()

GorientepNeg = [
	[0, 8, 2, I, I, I, I],
	[I, 0, I, I, -3, I, 10],
	[I, I, 0, -3, I, I, I],
	[I, 2, 4, 0, I, I, I],
	[I, I, 5, I, 0, 4, I],
	[I, 5, I, I, -2, 0, -2],
	[I, I, I, I, I, I, 0]
]

floydGopNeg = floyd(GorientepNeg)


# print("floyd sur le graphe proposé avec des poids négatifs :")
# print_matrice(floydGopNeg[0])
# print_matrice(floydGopNeg[1])
# print()


def pathFromFloyd(P, i, j):
	if P[i][j] == -1:
		return []
	return ([] if i == j else pathFromFloyd(P, i, P[i][j] - 1)) + [j + 1]


for x in range(Gorientep.__len__()):
	for y in range(Gorientep.__len__()):
		...
# 	print("chemin de", x + 1, "à", y + 1, " pour le graphe de base :", pathFromFloyd(floydGop[1], x, y))
# print()

for x in range(GorientepNeg.__len__()):
	for y in range(GorientepNeg.__len__()):
		...
# 	print("chemin de", x + 1, "à", y + 1, " pour le graphe à poids négatifs :", pathFromFloyd(floydGopNeg[1], x, y))
# print()


def floyd2(graph):
	W = [[graph[i][j] for j in range(graph.__len__())] for i in range(graph.__len__())]
	P = [[j + 1 if graph[i][j] != I else 0 for j in range(graph.__len__())] for i in range(graph.__len__())]
	for k in range(graph.__len__()):
		for i in range(graph.__len__()):
			for j in range(graph.__len__()):
				if W[i][j] > W[i][k] + W[k][j]:
					W[i][j] = W[i][k] + W[k][j]
					P[i][j] = k + 1
	return W, P


def pathFromFloyd2(P, i, j):
	return [] if (P[i][j] == 0) else ([i + 1, j + 1] if i != j else [j + 1]) if (P[i][j] == j + 1) else (
			pathFromFloyd2(P, i, P[i][j] - 1) + pathFromFloyd2(P, P[i][j] - 1, j)[1:])


floydGop2 = floyd2(GorientepNeg)
print_matrice(floydGop2[0])
print_matrice(floydGop2[1])

for x in range(GorientepNeg.__len__()):
	for y in range(GorientepNeg.__len__()):
		...
# 	print("chemin de", x + 1, "à", y + 1, " pour le graphe à poids négatifs :", pathFromFloyd2(floydGop2[1], x, y))
# print()

# TP 3

# 1)

pos = []

with open('defi250.csv', 'r') as f:
	reader = csv.reader(f, delimiter=';')
	l = list(reader)[1:]
	for x in range(l.__len__()):
		pos.append((float(l[x][0]), float(l[x][1])))

distEucl = [[math.sqrt((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2) for j in range(pos.__len__())] for i
			in range(pos.__len__())]
for x in range(distEucl.__len__()):
	distEucl[x][x] = I


def calcPerm(graph, perm):
	return sum([graph[perm[i]][perm[i + 1]] for i in range(perm.__len__() - 1)]) + graph[perm[perm.__len__() - 1]][
		perm[0]]


# print("permutation de base (0, 1, ..., 249) :", calcPerm(distEucl, [i for i in range(distEucl.__len__())]))


def permute(perm, i, j):
	pc = perm.copy()
	pc[i], pc[j] = perm[j], perm[i]
	return pc


def permuteConsec(perm, i):
	return permute(perm, i % len(perm), (i + 1) % len(perm))


def insert(perm, i, j):
	pc = perm.copy()
	pc.insert(j, pc.pop(i))
	return pc


def opt2(perm, i, j):
	pc = perm.copy()
	for k in range(abs(j - i) // 2 + 1):
		pc = permute(pc, (i + k) % len(pc), (j - k) % len(pc))
	return pc


test = [i for i in range(10)]


# print("TESTS")
# print("Base", test)
# print("2-Opt(du 2e au 7e)", opt2(test, 2, 7))
# print("Permute(2e et 7e)", permute(test, 2, 7))
# print("PermuteConsec(2e et 3e)", permuteConsec(test, 2))
# print("PermuteConsec(7e et 8e)", permuteConsec(test, 7))
# print("Insert(2e en 7e)", insert(test, 2, 7))


def randomVoisinChooseV(perm, choice):
	a = random.randint(0, len(perm) - 1)
	b = random.randint(0, len(perm) - 1)
	if choice == 0:
		return permute(perm, a, b)
	elif choice == 1:
		return permuteConsec(perm, a)
	elif choice == 2:
		return insert(perm, a, b)
	else:
		return opt2(perm, a, b)


def randomVoisin(perm):
	return randomVoisinChooseV(perm, random.randint(0, 3))


"""
8) On pourra faire une visualisation du circuit hamiltonien avec mathplotlib
Pour représenter les villes par des points on peut utiliser pyplot.scatter(M[ :,0],M[ :,1])
"""


def showPerm(perm):
	plt.scatter([pos[i][0] for i in perm], [pos[i][1] for i in perm])
	pyplot.plot([pos[perm[i]][0] for i in range(perm.__len__())] + [pos[perm[0]][0]],
				[pos[perm[i]][1] for i in range(perm.__len__())] + [pos[perm[0]][1]])
	plt.show()


# randomPerm = [i for i in range(250)]
# for i in range(100):
# 	randomPerm = randomVoisin(randomPerm)
#
# showPerm(randomPerm)
# print("random :", calcPerm(distEucl, randomPerm))


def getClosest(i, l):
	m = l[0]
	for j in l:
		if distEucl[i][j] < distEucl[i][m]:
			m = j
	return m


def calcGluttonPerm(dists, start):
	perm = [start]
	for i in range(dists.__len__() - 1):
		perm.append(getClosest(perm[i], [j for j in range(dists.__len__()) if j not in perm]))
	return perm


# gluttonPerm = [i for i in range(250)]
# for i in range(len(gluttonPerm) - 1):
# 	closest = getClosest(gluttonPerm[i], gluttonPerm[i + 1:])
# 	gluttonPerm = insert(gluttonPerm, gluttonPerm.index(closest), i + 1)

# showPerm(gluttonPerm)
# print("glouton ville 0 :", calcPerm(distEucl, gluttonPerm))

# best = gluttonPerm
# bestDist = calcPerm(distEucl, best)
# bestI = 0
# for i in range(250):
# 	gluttonPerm = calcGluttonPerm(distEucl, i)
# 	newDist = calcPerm(distEucl, gluttonPerm)
# 	if newDist < bestDist:
# 		best = gluttonPerm
# 		bestDist = newDist
# 		bestI = i
# 	showPerm(gluttonPerm)
# 	print("glouton ville", i, ":", newDist)
#
# print("best glouton ville", bestI, ":", bestDist)

def recuitSimule(dists, x0, T0, L, alpha, K):
	T = T0
	xBest = x0
	FBest = calcPerm(dists, xBest)
	xN = xBest
	k = 0
	n = 0
	while k < K:
		xTmp = randomVoisinChooseV(xN, 3)
		FTmp = calcPerm(dists, xTmp)
		deltaF = FTmp - FBest
		if deltaF <= 0:
			xN = xTmp
			if FTmp < FBest:
				xBest = xTmp
				FBest = FTmp
				k = 0
			else:
				k += 1
		else:
			if random.random() < math.exp(-deltaF / T):
				xN = xTmp
			k += 1
		n += 1
		if n % L == 0:
			T = T * alpha
	return xBest, FBest


def surface(initialPerm, alphaTarget, kTarget, LTarget):
	"""
	Cette fonction permet de tracer une surface avec les valeurs de k, de
	alpha en abscisse et ordonnee et la valeur du chemin en axe z. Cela
	permet de trouver pour quelles valeurs de k et de alpha , la fonction
	recuit simule optimise le mieux . Cela permet de faire un choix sur les
	parametres afin de mieux optimiser
	"""
	# bp = [calcGluttonPerm(distEucl, i) for i in range(250)]
	T_0 = 10000
	# vect_L = np.linspace(max(1, LTarget-1), min(30, LTarget+1), 3)
	# Vecteur des valeurs de alpha et de k
	vect_alpha = np.linspace(max(alphaTarget - 0.05, 0), min(0.999, alphaTarget + 0.05, 10))
	vect_k = np.linspace(max(5, kTarget - 5), kTarget + 5, 10)
	# Initialisation du vecteur qui contient la longueur des chemins
	vect_F = np.zeros((len(vect_alpha), len(vect_k)))
	alphaMin = 0
	kMin = 0
	LMin = 0
	FMin = 1000000000
	permMin = []
	# Double boucle sur les 2 parametres a optimiser
	for i_alpha in range(len(vect_alpha)):
		for i_k in range(len(vect_k)):
			list_F = []
			# On applique le recuit simule
			for i in range(20):
				Fc = recuitSimule(distEucl, initialPerm, T_0, LTarget, vect_alpha[i_alpha], vect_k[i_k])
				list_F.append(Fc[1])
				if Fc[1] < FMin:
					FMin = Fc[1]
					alphaMin = vect_alpha[i_alpha]
					kMin = vect_k[i_k]
					permMin = Fc[0]
					LMin = LTarget
			# On garde le minimum du recuit
			F = min(list_F)
			vect_F[i_alpha, i_k] = F
	# Graphe en 3D
	fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
	vect_k, vect_alpha = np.meshgrid(vect_k, vect_alpha)
	S = ax.plot_surface(vect_alpha, vect_k, vect_F, cmap="plasma")
	# Vue du dessous
	ax.view_init(-90, 90, 0)
	fig.colorbar(S)
	print("alpha min :", alphaMin, "; k min :", kMin, "; F min :", FMin, "; L min :", LMin, "; perm min :", permMin)
	plt.show()
	# showPerm(permMin)
	return alphaMin, kMin, FMin, LMin, permMin


# currentBest = [151, 89, 221, 204, 28, 208, 231, 123, 98, 108, 241, 23, 87, 34, 38, 177, 210, 173, 223, 41, 67, 159, 16, 79, 179, 198, 42, 144, 72, 64, 132, 137, 237, 187, 229, 84, 239, 190, 219, 60, 154, 136, 143, 181, 214, 14, 59, 180, 127, 246, 145, 20, 117, 9, 90, 83, 27, 157, 176, 21, 57, 209, 104, 220, 99, 45, 53, 71, 226, 186, 172, 65, 35, 211, 224, 7, 140, 228, 50, 183, 131, 192, 230, 164, 49, 166, 3, 156, 17, 215, 91, 163, 69, 101, 200, 182, 95, 167, 146, 109, 233, 0, 85, 24, 202, 199, 80, 240, 206, 234, 76, 232, 112, 125, 160, 171, 88, 5, 51, 61, 92, 37, 6, 153, 32, 242, 58, 155, 203, 193, 213, 249, 134, 94, 39, 150, 227, 113, 126, 110, 44, 8, 124, 118, 243, 73, 19, 86, 139, 100, 29, 236, 222, 218, 188, 106, 248, 68, 205, 147, 216, 225, 33, 115, 56, 162, 43, 244, 96, 129, 195, 22, 116, 148, 105, 70, 169, 235, 66, 201, 121, 130, 184, 189, 238, 152, 138, 175, 40, 128, 247, 18, 11, 48, 15, 197, 25, 245, 13, 77, 93, 119, 4, 30, 82, 114, 178, 191, 174, 158, 74, 103, 78, 135, 142, 26, 149, 36, 170, 62, 194, 54, 75, 63, 141, 168, 185, 31, 217, 52, 196, 107, 212, 10, 97, 165, 120, 207, 102, 2, 122, 161, 46, 55, 1, 12, 47, 111, 81, 133]
# showPerm(currentBest)
# print(currentBest)
# print(calcPerm(distEucl, currentBest))
# best = calcGluttonPerm(distEucl, 0)
# alphaTarget = 0.85
# kTarget = 95
# LTarget = 5
# while True:
# 	alphaTarget, kTarget, _, LTarget, best = surface(best, alphaTarget, kTarget, LTarget)
