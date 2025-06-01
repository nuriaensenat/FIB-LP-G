NB. Operacions amb variables i funcions.

x =: 10
x                           NB. Resultat: 10
y =: 1 2 3
z =: y , x
z                           NB. Resultat: 1 2 3 10

square =: *:
double =: +:
square 5                    NB. Resultat: 25
double 5                    NB. Resultat: 10
square double 5             NB. Resultat: 100
double square 5             NB. Resultat: 50

vector =: 1 2 3 4 5
negative =: _10 _20 _30
aux =: vector , negative
aux                         NB. Resultat: 1 2 3 4 5 _10 _20 _30

a =: 2
b =: 3
c =: a + b
c * 2                       NB. Resultat: 10
c - 1                       NB. Resultat: 4

res1 =: a + b
res2 =: res1 * 2
res3 =: res2 - 5
res3                        NB. Resultat: 5
res4 =: res2 - 25           NB. Resultat: _15
res4

neg =: -:
neg 1 2 3                   NB. Resultat: 0 0 0

mod2 =: 2 | ]
mod2 i. 4                   NB. Resultat: 0 1 0 1

eq0 =: 0 = ]
eq0 mod2 i. 6               NB. Resultat: 1 0 1 0 1 0