# Series d'exercices - Section 1 

- Chapitre abordé dans cette section :
    - Les variables
    - Les Conditions if - else 
    - Les Boucles FOR 
    - Les Fonctions

## Exercice 1 
- Dites si c'est les  propositions sont True ou False ou ERROR 

```python 
>>> 5 == 5
True

>>> 6 > 7
False

>>> 2+3 >= 7 
False

>>> "5" == "5"
True

>>> "56" == 56 
False

>>> "5"*2 == "55"
True

>>> "6"+3 < 10 
ERROR

>>> 7 != 23
True

>>> "6" != 6 
True

>>> 6 - "2" == "4" 
ERROR

```
## Exercie 2 

- Donner le type des variables suivantes (int / float / bool / str ) ? 

```python 
x = 5 

y = 2.5 

z = "3" 

var1 = str(3)

var2 = int("5")

var3 = str(int("6"))

var4 = "6" 

var5 = var2+x 

var4 = int(var4)


>>> type(x) ??
int

>>> type(y) ??
float

>>> type(z) ??
str

>>> type(var1) ??
str

>>> type(var2) ??
int

>>> type(var3) ??
str

>>> type(var4) ?? # faire bien attention a var4 !!
int

>>> type(var5) ??
int
```

## Exercice 3 

- Decouvrer quelle est la fonctionnalité du code suivant et remplacer les "xxxxx" par le mot qui correspond 

```python 

x=5

if ( x%2 == 0 ):
    print("x est un nombre xxxxx ") => paire
else: 
    print("x est un nombre xxxxx ") => impaire 

```

## Exercice 4 
- Écris un programme qui utilise une boucle for pour afficher les nombres pairs de 0 à 10 inclus.

```python 
rappel: range(0,10) -> [0,9]
afficher signifie print()
```
```python 
#correction
for i in range(0,11):
    if (i%2 == 0):
        print(i)


## Exercice 5
- Écris un programme qui prend un mot en entrée et utilise une boucle for pour afficher le mot à l'envers.

```python
# exemple:
## avion -> noiva 
## bateau -> uaetab
```

## Exercice 6 
- Ecrire une fonction nommé "aire" qui prend 2 arguments et retourne l'aire d'un carré . 

```python
def aire(x,y):
    return x*y
```