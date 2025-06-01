NB. Operacions amb operadors.

c =: 1 2 3
d =: 4 5 6
c , d                            NB. Resultat: 1 2 3 4 5 6
1 { c                            NB. Resultat: 2
2 { c , d                        NB. Resultat: 3
0 3 5 { c , d                    NB. Resultat: 1 4 6

mask1 =: 1 0 1 1 0
array1 =: 10 20 30 40 50
mask1 # array1                   NB. Resultat: 10 30 40

mask2 =: 1 1 1 0 1 0 1
array2 =: 10 20 30 40 50 60 70
mask2 # array2                   NB. Resultat: 10 20 30 50 70

] 1 2 3                          NB. Resultat: 1 2 3
1 , 2 3                          NB. Resultat: 1 2 3
# 1 2                            NB. Resultat: 2
1 0 1 0 # 1 2 3 4                NB. Resultat: 1 3
0 { 1 2 3                        NB. Resultat: 1
2 { 1 2 3                        NB. Resultat: 3
0 2 { 2 3 4                      NB. Resultat: 2 4
i. 4                             NB. Resultat: 0 1 2 3

+: 1 2 3                         NB. Resultat: 2 4 6
-: 1 2 3                         NB. Resultat 0 0 0
*: 1 2 3                         NB. Resultat 1 4 9

1 2 3 + 4 5                      NB. Resultat: Length error
0 3 5 { 1 2 3                    NB. Resultat: IndexError
1 1 + 1 2 3                      NB. Resultat: Length error