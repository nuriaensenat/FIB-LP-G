NB. Composició de funcions.

square =: *:
double =: +:
f =: square @: double
f 3                             NB. Resultat: 36
square @: double 4              NB. Resultat: 64
double @: square 4              NB. Resultat: 32

mod2 =: 2 | ]
eq0 =: 0 = ]
parell1 =: eq0 @: mod2
parell1 i. 6                    NB. Resultat: 1 0 1 0 1 0

parell2 =: 0 = ] @: 2 | ]
parell2 i. 6                    NB. Resultat: 1 0 1 0 1 0

inc =: 1 + ]
test1 =: +/ @: inc @: i.
x =: test1 3                    
x                               NB. Resultat: 6

g =: +/ @: (inc @: square)
g 1 2 3                         NB. Resultat 17

y =: square @: inc @: double
y 2                             NB. Resultat 25

z =: +/ 3 + i. 4               
z                               NB. Resultat: 18

data =: i.10                   
evens =: 0 = 2 | data          
evens # data                    NB. Resultat: 0 2 4 6 8

test2 =: +/ @: +: @: *: @: i.
test2 3                         NB. Resultat: 10