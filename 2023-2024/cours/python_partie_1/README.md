# Resumé de cours - Introduction à python 

## Prérequis 
- Intaller un IDE , à savoir Thonny ou vscode (avec l'extension python)

## Les variables

### Types

- Nous avons vu 4 types de variables en python:
    - int   -> Nombre entier
    - float -> Nombre flottant , nombre à virgule
    - str   -> chaine de caractère, element entre guillemets 
    - bool  -> True ou False 

```python
La fonction  type() permet de connaitre le type d une variable
>>> type(5)
int 
>>> type(5.5)
float
>>> type('a')
str
>>> type('5')
str
>>> type(True)
bool
>>> type(False)
bool 
```

### Les operations 

- il y'a plusieurs operations possible en python: 
    - "+" -> l'addition 
    ```python 
    int + int -> OK 
    float + float -> OK 
    float + int -> OK 
    str + int -> ERROR
    str + str -> OK 
        >>> "ab" + "cd" 
        "abcd"
        >>> "5"+"3"
        "53"
    ```
    - "-" -> soustraction 
    ```python 
    int - int -> OK 
    float - float -> OK 
    float - int -> OK 
    str - str -> ERROR  
    ```
    - "*" -> multiplication 
    ```python 
    int * int -> OK 
    float * float -> OK 
    float * int -> OK 
    str * str -> ERROR
    str * int -> OK 
        >>> "ab"*3
        "ababab"
    ```
    - "/" -> division avec resultat à virgule 
    ```python 
    int / int -> OK 
    float / float -> OK 
    float / int -> OK 
    str / str -> ERROR
    str / int -> ERROR 
    ```
    - "//" -> division euclidienne 
    ```python 
    int // int -> OK 
    float // float -> OK 
    float // int -> OK 
    str // str -> ERROR
    str // int -> ERROR 
    ```
    - "%" -> reste de la division euclidienne 
    ```python 
    >>> 5%2
    1
    >>> 4%2
    0

    NB: Pour savoir si un nombre est paire ou impaire , on cherche le reste de sa division euclidienne par 2
    si le reste de la division est égale à 0 -> alors le nombre est paire 
    si le reste de la division est égale à 1 -> alors le nombre est impaire 
     >>> 5%2
    1  -> Donc 5 est impaire
    ```

    ### Operateurs de comparaisons 

    - les operateurs de comparaisons permettent de comparer 2 elements entre eux et renvoie toujours un bool , à savoir la comprraison est vrai (True) ou fausse (False).
        - "==" -> comprare si 2 elements sont egaux 
        - "!=" -> comprare si 2 elements sont differents 
        - ">" -> comprare si un element est superieur à l'autre 
        - "<" -> comprare si un element est inferieur à l'autre 
        - ">=" -> comprare si un element est superieur ou egale à l'autre 
        - "<=" -> comprare si un element est inferieur ou egale  à l'autre

    ```python 
    >>> 5 == 5 
    True
    >>> "5" == 5
    False
    >>> 5 > 3 
    True
    >>> 5 >= (6-1)
    True
    >>> 6 < 3
    False 
    >>> "bonjour" != " bonjour" # l'espace est consideré comme un caractère 
    True 
    ```
## La Condition IF - ELSE 
- il existe un moyen de créer des conditions en python grace au element "if" , "elif" et "else"
    - "if" -> signifie si ( si la condition est respecté)
    -> "else" -> signifie sinon ( si la conidition n'est pas respecté , sinon je fais ça )
```python 
<Condition> -> represente la condition que doit verifier le "if" , celle ci doit renvoyer True ou False
< Code du si > -> partie de code qui est executé seulement si la condtion est respecté est donc renvoie True
< Code du sinon > -> partie de code executer seulement si la condition n est pas respecté est donc renvoie False

if (<Condition>):
    < Code du si >
else:
    < Code du sinon >
```

Exemple: 
```python 
x=5 

if (x == 5 ): 
    print("x est egale à 5")         # Code Si
else: 
    print ("x est different de 5")   # Code Sinon

# Dans cette exemple seul le "code du Si" qui sera executé car x est bien egale à 5 . 

```

## Les Boucles 

### Boucles FOR 
- La boucle for permet de parcourir un ensemble d'element que ce soit un ensemble de nombre ou autre et d'attribuer à chaque tour de boucle une valeur de l'element à une variable

- la fonction range() permet de definir un intervalle de nombre
```python 
range(0,5) -> va creer un ensemble de nombre entier allant de 0 jusqu a le dernier element -1 , ici 5 -1 donc 4 -> [0,1,2,3,4]
range(0,3) -> [0,1,2]
```

```python 
<variable> -> nom de la variable dont la valeur changera à chaque tour de boucle pour prendre comme valeur chaque element de l ensemble 

<ensemble> -> ensenble que va parcourir la boucle 

<code boucle> -> le meme code sera executé à chaque nouveau tour de boucle

for <variable> in <ensemble>:
    <code boucle>

```

Exemple: 

```python 

res=0

for i in range(0,5):
    res=res+i

print("res est egale à " + res) # -> "res est egale à 12"

```

## Les fonctions

- Comme en maths , en python une fonction prend des arguments et effectue une operation pour renvoyer un resulat 

```python 

En Maths: 
f(x) = 2x+3
f(1) = 2*1 +3 = 5 

En python la meme fonction peut s ecrire 

def f(x): 
    return 2*x +3 

>>> f(1)
5 
```

- Pour creer une nouvelle fonction en python il faut la definir avec le mot clé "def" 

```python 
def <nom de la fonction>(<argument>):
    <Code de la focntion>
``` 

Exemple 

```python 
# fonction qui additionne 2 nombres
def add(x,y):
    return x+y

# une fois que la fonction est definie on peut l'utiliser , on l'appelant simplement 

>>> add(5,6)
11 
```
- Le mot clé "return" permet de renvoyer le resultat d'une fonction, pour que ce resultat nous soit pas supprimer à la fin de l'execution de la fonction 

```python 
def add(x,y):
    return x+y

def add2(x,y):
    print (x+y)

>>> res= add(5,6) 
# res = 12 -> la variable res a pu recuperer le resultat de la fonction add , car elle a un return

>>> res2 = add2(5,6)
# res2 = None -> la variable res2 n'a rien pu recuperer de la fonction add2 ,car elle ne return rien (il ny'a pas de return)
```