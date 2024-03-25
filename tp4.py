# TP4
import math
import random

import numpy as np
from matplotlib import pyplot as plt

# datas

pos = """1 7810 6053
2 7798 5709
3 7264 5575
4 7324 5560
5 7547 5503
6 7744 5476
7 7821 5457
8 7883 5408
9 7874 5405
10 7927 5365
11 7848 5358
12 7802 5317
13 7962 5287
14 7913 5280
15 7724 5210
16 7503 5191
17 7759 5143
18 7890 5130
19 7254 5129
20 7790 5038
21 7142 5032
22 7606 5009
23 7772 4989
24 7744 4933
25 7846 4923
26 7622 4917
27 6937 4917
28 7576 4915
29 7783 4912
30 7716 4909
31 7295 4887
32 7777 4869
33 7700 4854
34 7726 4833
35 7702 4815
36 7583 4813
37 7654 4795
38 7417 4788
39 7267 4779
40 6806 4755
41 5259 4751
42 7698 4745
43 7570 4741
44 7617 4724
45 7752 4721
46 7673 4718
47 7692 4666
48 7547 4664
49 7259 4630
50 5387 4623
51 7679 4581
52 7674 4579
53 7631 4573
54 7520 4572
55 7848 4546
56 5685 4546
57 7832 4542
58 6735 4509
59 7647 4504
60 7338 4481
61 4602 4478
62 4606 4468
63 7399 4467
64 7037 4446
65 7458 4428
66 7364 4427
67 6058 4426
68 6868 4418
69 3832 4410
70 6670 4401
71 7443 4375
72 7160 4370
73 6139 4369
74 7333 4335
75 6237 4332
76 5385 4318
77 6911 4296
78 6304 4294
79 7111 4288
80 6740 4282
81 7698 4279
82 7613 4275
83 7360 4275
84 6779 4273
85 7207 4270
86 6241 4268
87 7432 4265
88 4354 4262
89 6589 4256
90 7817 4252
91 6051 4246
92 5356 4241
93 7554 4236
94 7534 4227
95 4217 4224
96 7349 4219
97 7128 4215
98 3950 4215
99 6947 4209
100 7549 4208
101 5168 4208
102 6524 4207
103 5871 4202
104 7542 4198
105 6660 4193
106 7216 4180
107 6607 4173
108 7601 4171
109 6123 4167
110 6450 4160
111 6713 4154
112 7355 4151
113 7604 4146
114 7541 4141
115 7506 4138
116 4871 4132
117 2906 4131
118 6488 4128
119 6312 4126
120 6008 4117
121 4427 4109
122 4679 4084
123 5955 4081
124 6891 4075
125 7705 4065
126 7562 4058
127 4634 4054
128 4607 4049
129 6557 4047
130 7344 4046
131 5543 4042
132 7124 4039
133 7466 4037
134 6259 4030
135 6366 4002
136 5597 3993
137 4655 3992
138 7805 3991
139 3396 3990
140 6603 3982
141 6537 3982
142 4342 3966
143 7037 3965
144 7345 3951
145 7271 3948
146 5336 3943
147 5964 3935
148 7660 3924
149 7872 3922
150 6567 3922
151 6602 3920
152 4806 3914
153 7909 3912
154 5926 3912
155 7449 3911
156 6333 3909
157 3108 3908
158 7844 3902
159 5427 3894
160 6862 3892
161 6621 3891
162 6150 3888
163 7388 3879
164 7351 3877
165 4694 3877
166 6340 3870
167 6425 3867
168 6577 3858
169 6864 3854
170 5706 3844
171 4496 3844
172 4574 3843
173 3824 3838
174 5803 3824
175 5720 3823
176 6454 3821
177 6120 3821
178 7988 3820
179 6376 3819
180 7841 3818
181 5778 3813
182 5457 3808
183 5671 3807
184 4293 3788
185 7423 3776
186 7342 3775
187 5541 3769
188 5621 3768
189 7750 3760
190 6327 3745
191 7879 3743
192 199 3743
193 6652 3742
194 5678 3742
195 5207 3742
196 7429 3737
197 7262 3725
198 6427 3717
199 1851 3710
200 6207 3700
201 6069 3695
202 4780 3694
203 7603 3690
204 5751 3681
205 6365 3679
206 6958 3678
207 6317 3673
208 5417 3673
209 6426 3656
210 7922 3655
211 7331 3634
212 5965 3624
213 4965 3622
214 6833 3618
215 6798 3610
216 7667 3608
217 1047 3602
218 7803 3598
219 7370 3588
220 952 3583
221 7906 3580
222 250 3578
223 5111 3569
224 6453 3567
225 7492 3560
226 6140 3558
227 5315 3557
228 5316 3554
229 4232 3551
230 7408 3534
231 8013 3523
232 5160 3517
233 7141 3514
234 5887 3508
235 4694 3502
236 7633 3499
237 7919 3496
238 1784 3494
239 1482 3494
240 236 3494
241 6713 3488
242 7696 3486
243 536 3481
244 317 3476
245 5649 3472
246 6235 3471
247 7199 3469
248 5540 3468
249 5400 3461
250 5796 3459
251 2342 3439
252 7494 3430
253 7321 3429
254 6265 3426
255 8001 3418
256 226 3415
257 6148 3413
258 5987 3402
259 7582 3396
260 7422 3390
261 6623 3389
262 7475 3388
263 7654 3377
264 7838 3375
265 6570 3371
266 4364 3362
267 7316 3360
268 4857 3359
269 7533 3358
270 5719 3352
271 7452 3339
272 7747 3329
273 5841 3328
274 3229 3312
275 7076 3302
276 7657 3301
277 6360 3301
278 525 3297
279 5619 3291
280 7989 3271
281 5697 3269
282 6050 3242
283 7082 3235
284 5539 3235
285 741 3235
286 6731 3234
287 7453 3229
288 7695 3220
289 7299 3219
290 863 3219
291 7861 3216
292 5960 3207
293 4252 3206
294 6402 3190
295 5342 3188
296 6656 3181
297 7532 3175
298 7434 3173
299 5679 3171
300 6518 3165
301 4537 3143
302 806 3123
303 6113 3101
304 7440 3100
305 6204 3099
306 7715 3086
307 7503 3086
308 5821 3086
309 7131 3081
310 7909 3080
311 920 3065
312 6468 3050
313 5677 3049
314 218 3031
315 6881 3029
316 5650 3023
317 197 3021
318 5531 3011
319 6387 3008
320 4458 3007
321 6190 2985
322 7055 2981
323 7238 2957
324 5930 2948
325 7543 2929
326 5291 2929
327 4196 2929
328 6617 2928
329 4831 2917
330 2835 2912
331 174 2901
332 5350 2867
333 7346 2858
334 6044 2848
335 4898 2840
336 3307 2833
337 1918 2832
338 7125 2823
339 6422 2820
340 5881 2817
341 141 2814
342 7851 2809
343 4929 2803
344 5963 2789
345 5470 2774
346 7458 2741
347 1263 2734
348 6766 2732
349 4763 2720
350 3461 2718
351 7309 2717
352 6848 2712
353 178 2702
354 1882 2684
355 4584 2643
356 3174 2627
357 7049 2570
358 7753 2564
359 6597 2563
360 4476 2555
361 1575 2555
362 7304 2550
363 10 2537
364 6800 2532
365 5296 2520
366 7104 2510
367 6547 2506
368 7267 2466
369 3189 2411
370 5117 2409
371 4973 2406
372 4488 2378
373 7351 2376
374 6007 2359
375 4612 2341
376 7015 2333
377 3233 2329
378 240 2327
379 6686 2312
380 6307 2295
381 7448 2291
382 7087 2274
383 2067 2254
384 5260 2230
385 4174 2190
386 36 2185
387 7856 2181
388 7315 2181
389 3319 2151
390 2126 2150
391 7418 2139
392 6885 2138
393 4959 2123
394 4996 2115
395 5681 2109
396 5277 2078
397 7643 2048
398 3390 2043
399 8080 2039
400 6139 2032
401 2694 2026
402 7152 2000
403 7822 1992
404 7416 1953
405 7352 1952
406 354 1950
407 6493 1931
408 7905 1921
409 8229 1905
410 6803 1886
411 4012 1886
412 4759 1883
413 8101 1876
414 7989 1876
415 8063 1860
416 8080 1835
417 7004 1805
418 6252 1795
419 6826 1774
420 7218 1773
421 464 1773
422 809 1766
423 7240 1762
424 7046 1757
425 8098 1746
426 7314 1739
427 7035 1733
428 5506 1719
429 8184 1685
430 6932 1683
431 5914 1682
432 2908 1681
433 6496 1678
434 8525 1664
435 6765 1663
436 7985 1657
437 6854 1640
438 7926 1627
439 7973 1606
440 5060 1577
441 4056 1564
442 5637 1558
443 2011 1558
444 8038 1535
445 6651 1534
446 552 1526
447 6621 1513
448 8594 1510
449 4719 1504
450 5472 1482
451 8605 1479
452 345 1476
453 8228 1471
454 5005 1458
455 5114 1430
456 5964 1421
457 602 1395
458 5098 1394
459 5068 1390
460 8292 1383
461 6258 1354
462 5010 1351
463 6494 1347
464 437 1344
465 413 1338
466 659 1331
467 5840 1325
468 6378 1314
469 6379 1302
470 6359 1298
471 3245 1281
472 450 1274
473 478 1256
474 5571 1255
475 489 1254
476 513 1247
477 6136 1243
478 4170 1232
479 1721 1165
480 893 1161
481 5930 1151
482 4619 1132
483 4125 1125
484 5139 1124
485 572 1108
486 4500 1093
487 2372 1084
488 993 1084
489 527 1077
490 5788 1053
491 3719 1043
492 4805 1033
493 5140 1018
494 5344 1003
495 5532 998
496 5069 998
497 1595 942
498 5666 914
499 2260 913
500 4244 896
501 5596 892
502 4569 886
503 1072 883
504 3499 863
505 5136 825
506 783 825
507 834 757
508 1406 750
509 3390 698
510 2384 695
511 982 659
512 1422 658
513 1361 637
514 1926 636
515 1213 633
516 1415 628
517 1082 625
518 1254 617
519 5070 605
520 1212 603
521 1249 600
522 3477 599
523 1322 580
524 1253 580
525 1276 559
526 2647 485
527 1443 459
528 1961 445
529 1790 429
530 1503 362
531 5393 355
532 5469 10"""

pos = np.array([np.array([float(x) for x in line.split()[1:]]) for line in pos.splitlines()])

dists = np.array([[np.linalg.norm(pos[i] - pos[j]) for j in range(len(pos))] for i in range(len(pos))])

# Q1

"""Faire tourner votre algorithme du recuit simulé sur la matrice des distances (par la route) entre les 128 villes.

Donner votre optimum pour le cas d’un camion avec 128 villes.

Visualiser le parcours."""


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


def calcPerm(graph, perm):
	return sum([graph[perm[i]][perm[i + 1]] for i in range(perm.__len__() - 1)]) + graph[perm[perm.__len__() - 1]][
		perm[0]]


def recuitSimule(distances, x0, T0, L, alpha, K):
	T = T0
	xBest = x0
	FBest = calcPerm(distances, xBest)
	xN = xBest
	k = 0
	n = 0
	while k < K:
		xTmp = randomVoisinChooseV(xN, 3)
		FTmp = calcPerm(distances, xTmp)
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


def surface(dists, initialPerm, alphaTarget, kTarget, LTarget):
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
	vect_alpha = np.linspace(max(alphaTarget - 0.05, 0), min(0.999, alphaTarget + 0.05), 10)
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
				Fc = recuitSimule(dists, initialPerm, T_0, LTarget, vect_alpha[i_alpha], vect_k[i_k])
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


def getClosest(distances, i, l):
	m = l[0]
	for j in l:
		if distances[i][j] < distances[i][m]:
			m = j
	return m


def calcGluttonPerm(distances, start):
	perm = [start]
	for i in range(distances.__len__() - 1):
		perm.append(getClosest(distances, perm[i], [j for j in range(distances.__len__()) if j not in perm]))
	return perm


def bestGlouton(distances):
	bestPerm = []
	bestDist = 100000000000
	for i in range(distances.__len__()):
		perm = calcGluttonPerm(distances, i)
		dist = calcPerm(distances, perm)
		if dist < bestDist:
			bestDist = dist
			bestPerm = perm
	return bestPerm


# bestG = [228, 265, 292, 326, 319, 300, 328, 334, 342, 348, 354, 359, 371, 374, 370, 369, 364, 383, 395, 393, 392, 411, 448, 453, 458, 457, 454, 461, 439, 449, 441, 427, 430, 455, 466, 480, 489, 497, 500, 494, 493, 492, 483, 495, 504, 518, 530, 531, 491, 481, 485, 501, 499, 482, 477, 440, 410, 384, 397, 388, 376, 368, 355, 335, 349, 273, 329, 250, 237, 198, 238, 216, 219, 289, 301, 310, 284, 277, 242, 243, 239, 255, 221, 191, 313, 316, 330, 340, 352, 362, 377, 385, 405, 420, 445, 456, 465, 475, 474, 472, 471, 463, 464, 451, 484, 488, 505, 506, 510, 516, 514, 519, 520, 517, 523, 524, 522, 512, 515, 511, 507, 496, 478, 442, 486, 498, 509, 525, 527, 528, 513, 529, 526, 502, 487, 479, 421, 346, 360, 353, 336, 382, 389, 400, 431, 470, 503, 508, 521, 490, 473, 476, 460, 469, 468, 467, 462, 446, 444, 434, 436, 429, 426, 423, 416, 418, 409, 391, 375, 381, 365, 356, 367, 361, 350, 332, 322, 308, 321, 337, 351, 347, 363, 358, 366, 378, 379, 373, 399, 417, 432, 406, 401, 404, 403, 390, 387, 380, 372, 345, 324, 306, 303, 297, 286, 296, 287, 275, 262, 258, 268, 261, 251, 259, 270, 266, 252, 246, 232, 274, 282, 288, 229, 218, 210, 196, 185, 184, 195, 162, 163, 143, 144, 129, 111, 95, 82, 73, 65, 62, 59, 64, 70, 86, 93, 92, 99, 103, 113, 114, 125, 112, 107, 81, 80, 89, 124, 137, 148, 157, 152, 179, 190, 209, 220, 236, 230, 254, 279, 290, 309, 305, 271, 263, 241, 235, 215, 202, 188, 217, 177, 147, 154, 132, 105, 84, 96, 78, 71, 63, 67, 76, 98, 123, 142, 131, 159, 168, 205, 213, 214, 240, 260, 264, 295, 285, 299, 293, 276, 253, 245, 256, 225, 200, 211, 233, 249, 269, 280, 278, 283, 298, 312, 315, 317, 331, 325, 344, 339, 343, 333, 323, 307, 291, 281, 302, 304, 320, 318, 311, 327, 338, 314, 223, 208, 197, 204, 206, 189, 178, 165, 155, 134, 133, 118, 109, 117, 101, 88, 106, 104, 110, 79, 83, 69, 57, 39, 26, 20, 18, 30, 38, 48, 37, 42, 43, 45, 41, 44, 46, 50, 51, 52, 58, 53, 47, 35, 36, 34, 33, 32, 29, 23, 28, 31, 24, 22, 19, 16, 14, 11, 10, 8, 7, 9, 12, 13, 17, 21, 25, 27, 15, 4, 5, 6, 1, 0, 3, 2, 56, 54, 224, 341, 357, 386, 402, 407, 413, 414, 415, 412, 424, 428, 435, 438, 437, 443, 452, 459, 450, 447, 433, 408, 398, 396, 425, 422, 419, 394, 294, 248, 227, 226, 207, 181, 158, 145, 130, 135, 169, 174, 182, 187, 193, 203, 180, 173, 153, 146, 122, 119, 108, 90, 72, 66, 74, 85, 77, 128, 140, 139, 150, 160, 167, 149, 175, 166, 192, 199, 176, 161, 102, 55, 49, 40, 75, 91, 100, 115, 121, 126, 127, 136, 164, 151, 201, 212, 222, 231, 194, 186, 247, 244, 272, 257, 267, 234, 171, 170, 141, 120, 87, 94, 97, 68, 172, 138, 156, 116, 183, 61, 60]
# alphaTarget = 0.85
# kTarget = 95
# LTarget = 5
# best = bestG
# while True:
# 	alphaTarget, kTarget, _, LTarget, best = surface(dists, best, alphaTarget, kTarget, LTarget)
# 	print(calcPerm(dists, best))
# 	print(best)
# 	plt.plot(pos[:, 0], pos[:, 1], 'ro')
# 	plt.plot(pos[best, 0], pos[best, 1])
# 	plt.show()


# Now I want to find the center in x and y of the pos
def center(pos):
	# calculate the median of all pos
	# return the pos closest to the median
	v = np.median(pos, axis=0)[0]
	return min(pos, key=lambda x: abs(x[0] - v))


def findClosestPos(pos, center):
	minDist = 100000000
	minPos = 0
	for i in range(len(pos)):
		dist = np.linalg.norm(pos[i] - center)
		if dist < minDist:
			minDist = dist
			minPos = i
	return minPos


def splitAlong(pos, nbAxis2or4=4):
	# Split the pos along the center
	# Return the 4 lists of pos
	# 1: x < center[0] and y < center[1]
	# 2: x < center[0] and y > center[1]
	# 3: x > center[0] and y < center[1]
	# 4: x > center[0] and y > center[1]
	lists = [[] for _ in range(nbAxis2or4)]
	c = findClosestPos(pos, center(pos))
	for i, x in enumerate(pos):
		if x[0] == pos[c][0] or x[1] == pos[c][1]:
			for l in lists:
				l.append(i)
		if x[0] < pos[c][0] and x[1] < pos[c][1]:
			lists[0 % nbAxis2or4].append(i)
		elif x[0] < pos[c][0] and x[1] > pos[c][1]:
			lists[2 % nbAxis2or4].append(i)
		elif x[0] > pos[c][0] and x[1] < pos[c][1]:
			lists[1 % nbAxis2or4].append(i)
		elif x[0] > pos[c][0] and x[1] > pos[c][1]:
			lists[3 % nbAxis2or4].append(i)
	return lists


# Now find the closest path for each list
posSplitting = splitAlong(pos, 2)

# Get the distances between the points in each list
distsSplitting = []
for l in posSplitting:
	distsSplitting.append(dists[l][:, l])

paths = []
pathsInternalIndexes = []
for i, dist in enumerate(distsSplitting):
	start = bestGlouton(dist)

	pathsInternalIndexes.append(bestGlouton(dist))
	tmp = list(map(lambda x: posSplitting[i][x], pathsInternalIndexes[i]))
	paths.append(tmp)

plt.plot(pos[:, 0], pos[:, 1], 'ro')
colors = ['b', 'g', 'y', 'c']
for i, v in enumerate(pathsInternalIndexes):
	print(calcPerm(distsSplitting[i], v))
	print(paths[i])
	cc = colors.pop()
	plt.plot(pos[paths[i], 0], pos[paths[i], 1], cc)
	# add a link between the last and the first
	plt.plot([pos[paths[i][0], 0], pos[paths[i][-1], 0]], [pos[paths[i][0], 1], pos[paths[i][-1], 1]], cc)
# Print the sum of the distances
print(sum(map(lambda x: calcPerm(distsSplitting[x], pathsInternalIndexes[x]), range(len(paths)))))
plt.show()
