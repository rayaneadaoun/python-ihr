# Resumé de cours - Introduction à python 

## Prérequis 
- Intaller un IDE , à savoir Thonny ou vscode (avec l'extension python)

## Les Listes

### Definition d'une liste

- une liste en python; est une structure de donnée qui permet de stocker des valeurs de type differents ( int, str ...)

```python
Definir une liste vide

var=[]
# ou 
var=list()
```

```python
Ajouter un element a la fin d une liste 

l=[3,4,5,6]

# si on veut ajouter le chiffre 7 à la fin on peut faire: 
l=l+[7]

# ou 

l.append(7)
```
### Les indices d'une liste 

- Dans une liste les elements se suivent les uns les autres, ainsi definir un element en particulier , on introduit la notions d'indices qui permettent d'identifier chaque element de la liste.
- On debutant du premier element de la liste qui aura l'indice 0, puis le suivant l'indice 1 etc ...

```python 
l= ["a","b","c","d"]
#   0    1   2    3   => indices de la liste l 

On comprend dans cette exemple que l element "a" de la liste l est à l indice 0, si on veut à la position 0 de la liste.  
```

### Operations sur les listes

- On peut additionner 2 listes

```python
l1=["a","b"]
l2=[1,2]

l1+l2 => ["a","b",1,2]

```

- On peut mutiplier une liste par un nombre entier , car cela revient à l'additionner par elle meme plusieurs fois 

```python
l1=["a","b"]


l1 * 2 => l1 + l1 => ["a","b","a","b"]

```
### Fonctions et methodes utiles sur les listes

- DEL 
```python
l=[1,8,9]
>>> del l[0] # va supprimer l'element a l'indice 0 de la liste l
>>>l
[8,9]

```
- INSERT

```python 
list.insert(i, x)
Insère un élément  x à la position  i de la liste 

l=[1,2,3]
l.insert(1,5) => [1,5,2,3]

```

- POP 

```python
list.pop(i)

Retire et affiche element à la position i de la liste 

l=[1,2,3]
l.pop(1) => [1,3]

```

### Pacrourir une liste

- Parcourir une liste pour afficher un element

```python 

l=["a","b","c"]

for i in l: 
    print i 

Resultat: 
"a"
"b"
"c"

```

- Parcourir une liste pour modifier un element 
- Dans ce cas de figure nous devons plutot parcourir les indices de la liste et non pas les elements de la liste directement 

```python
l=["a" , "d" , "c"]

#modifier la lettre d par b 

for i in range(0, len(l)):
    if (l[i] == "d" ):
        l[i]="b"

Resultat:
["a","b","c"]
```