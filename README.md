# ModulesColles 

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

Un gestionnaire complet à destination des enseignants en CPGE pour les interrogations orales.

## Prérequis

* Une distribution de LaTeX (inclue dans le PATH)
* Python avec les modules `numpy`, `tkinter` et `pickle`.
* Certaines fonctionalités ne sont disponible que sous Windows (en particulier les fichiers `.bat`)

## Module de colles, mode d'emploi


*Ne pas oublier de changer la ligne 86 du fichier `planchedecolle.cls` en conséquence*


### Comment créer une planche de colle?

Pour créer une planche de colle, il faut avoir le fichier `planchedecolle.cls` et les dossier `./images` et `./Exercices` dans le dossier de travail. Il suffit alors de créer un fichier `[Numéro_de_planche]-[Titre_de_la_planche].tex` de la forme:

```latex
\documentclass{planchedecolle}

\title{Thème en cours}
\date{Chapitre(s) de la planche}

\begin{document}

\planche
\cours{definition de cours}{definition de cours}\stopcours
\selectexo{type_exo}{label_exo}  
\selectexo{type_exo}{label_exo}

\planche[nom_de_planche] % On peut indiquer un nom voulu pour la planche

% On peut ajouter autant de planches que voulu

\pageReponses % Pour afficher les réponses  
\end{document}
```

*N.B.*: la macro `\cours` est récursive: on peut ajouter autant de questions de cours que l'on souhaite, mais il faut bien penser a terminer la commande par `\stopcours`.

### Comment faire pour connaître la liste des exercices disponibles?

Dans le dossier `Codes`, le fichier `parse_texfile.py` permet de lire le fichier d'exercices et de produire une liste de labels d'exercices par type de planche.  

### Comment faire pour rajouter un exercice au fichier d'exercice?

Il suffit simplement de rajouter, dans le fichier `exercices_[type_exo].auxtex`, un environnement de la forme:

```latex
\begin{Exercice}  
    [title = titre, type=type_exo, label=label_exo]

% Enoncé de l'exercice

\end{Exercice}
```

Pour rajouter une correction, on fait de même:

```latex
\begin{Answer}  
    [ref = label_exo]

\end{Answer}
```

Notez qu'il n'est pas nécéssaire de se cantonner aux types d'exercices préexistants: libre à vous de créer un nouveau `#type_exo`.

### Comment faire pour visualiser un exercice (seulement sous Windows) ?

*Ne pas oublier de changer la ligne 49 du fichier `exo_view.bat` avec le PATH du visionneur de pdf choisi.*  

On se place dans le dossier `./Codes` et on tape la commande

```bash
exo_view.bat [labels_exos]
```

ou si on veut tous les exercices d'un (ou plusieurs) type

```bash
exo_view.bat -type [type_exo]
```

### Comment faire pour générer un rapport de colle ?

Avant de lancer le programme, il faut:

1) Dans `main.py`, changer la ligne 6 pour inclure toute nouvelle classe à ajouter
2) Dans le dossier `Liste_Eleves`, créer une liste des eleves par classe dans un fichier `[classe]_liste_eleves.csv`
3) Dans le dossier `P-[classe]`, créer les planches données dans l'année sous le nom `[Numéro_de_planche]-[Titre_de_la_planche].tex` dans le format précisé ci-dessus
4) Dans l'invite de commande, utiliser la commande

```bash
cd Codes
python parse_texfile.py
```

5) Lancer le programme avec

```bash
cd ../Rapport
python main.py
```

L'utilisation du programme est assez explicite, il faut bien penser à rafraîchir avec le bouton prévu à cet effet à chaque changement dans les séléctions. A noter que remplir la case `Note` est facultatif. Le rapport est ensuite généré dans le dossier `R-[classe]` sous le nom `Rapport-de-colle-[date]_[Eleve]\_[Numéro_de_planche]-[Titre_de_la_planche].tex`


© Copyright by Ruben Narwa

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
