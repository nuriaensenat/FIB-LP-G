# Pràctica LP: MiniJ
Projecte de l'assignatura de Llenguatges de Programació (FIB) - 2024-2025 Q2

Autora: Nuria Enseñat

## Índex
- [Descripció del projecte](#descripció-del-projecte)
- [Estructura del projecte](#estructura-del-projecte)
- [Característiques de l'intèrpret](#característiques-de-lintèrpret)
- [Gestió d'errors](#gestió-derrors)
- [Què es necessita?](#què-es-necessita)
- [Instal·lació](#instal·lació)
- [Ús](#ús)
- [Observacions](#observacions)

## Descripció del projecte
J és un llenguatge derivat d'APL que utilitza només caràcters ASCII. En aquest projecte trobaràs un subconjunt d'aquest llenguatge J. G (o MiniJ) és un intèrpret reduït del llenguatge J que suporta diferents operacions explicades en les següents seccions d'aquest arxiu. 

Aquesta projecte és la pràctica de l'assignatura de llenguatges de programació del quadrimestre de primavera del curs 2024-2025. Se pot trobar l'enunciat complet en [lp-mini-j](https://github.com/gebakx/lp-mini-j).


## Estructura del projecte
En aquest projecte pots trobar els següents fitxers/directoris:

- `g.g4` gramàtica del llenguatge en ANTLR4.
- `g.py` programa principal de l'intèrpret.
- `gVisitorImpl.py` implementació de l’intèrpret.
- `Makefile` per executar el projecte automàticament.
- `jocs_proves/` directori amb els jocs de prova (.j) organitzats en diferents categories per comprovat el funcionament de l'intèrpret.
- `outputs/` directori amb els fitxers de sortida (.out).


## Característiques de l'intèrpret
- Utilitza functools.reduce i numpy per interpretar el codi al visitor.
- Operacions amb arrays i escalars.
- Suporta operacions amb verbs, adverbis i operadors (`+`, `-`, `%`, `|`, `^`, `>`, `<`, `>=`, `<=`, `=`, `<>`, `]`, `,`, `#` unari, `#` binari, `{`, `i.`, `:`, `/`, `~`)
- Suporta composició i aplicació de funcions a més de definicions de variables i funcions.

## Gestió d'errors
El projecte compta amb gestió d'errors en els següents casos:
- Intent d'accedir a un índex inexistent d'una llista (mitjançant un `try-except`).
- Intent de fer una operació de dos llistes que tenen diferent tamany.
- Operacions amb operands nul·ls (none).
- Ús de verbs/adverbs/operadors no reconeguts.
- Crida a variables/funcions no definides.
- Excepcions a l'hora de composar funcions.


A més, com diu l'enunciat, suposarem que no es dónen errors semàntics, de tipus ni d'execució; si se contemplen alguns d'aquests casos, l'efecte del programa és indefinit.

## Què es necessita?

### Prerequisits

- Python 3
- Comanda `make`
- Paquet de Python [numpy](https://numpy.org)
- [ANTLR4](https://www.antlr.org/)

### Instal·lació

Instal·la Python i les eines `pip` i `make` en el teu sistema. Comandes a seguir en Linux:

    sudo apt update
    sudo apt install python3 python3-pip
    sudo apt install make

Ara ja pots utilitzar `pip` per instal·lar les dependències requerides per aquest projecte.

    pip install numpy 
    pip install antlr4-tools
    pip install antlr4-python3-runtime
    

## Ús

Ara que ja tens tot lo necessari ja pots provar el projecte! Si vols executar l’intèrpret amb un fitxer `.j` propi fes servir la següent comanda:

```sh
python3 g.py <fitxer>
```
També pots utilizar la comanda make per executar les proves predefinides:

```sh
make
```
Si fas servir la comanda make, pots trobar els resultats al directori `outputs/`, on cada prova té el seu nom d'arxiu corresponent.

## Observacions
- S'utilitza functools.reduce (funció de la llibreria estàndard de Python per a aplicar una funció de manera acumulativa per a reduïr una llista o un array a un únic valor) a l'hora de fer els folds quan numpy no suporta la operació.
- L'operador `:` quan s'utilitza amb alguns verbs, com per exemple `-` (és a dir, `-:`), tenen un altre significat a J (en el cas de `-:` és  dividir a la meitat l'operand). En aquest projecte qualsevol operador binari que se li apliqui `:` aplicarà l'operador utilitzant dues vegades l'operand. Per comoditat, se consideraràn els casos amb l'operador `:` com adverbis (ja que passen a ser operadors unaris).