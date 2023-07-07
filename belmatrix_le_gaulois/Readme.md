Soit une matrice NxN. On définit la "somme maximale" de cette matrice, la somme de N de ses valeurs, de sorte à ce qu'aucune valeur de cette somme ne partage la même ligne ou la même colonne avec une autre.

Par exemple, la matrice 5x5 :
  129 1224  346 1860 1878
 1908  669  932 1940 1843
 1720 1648 1213   60 1786
  253  171  908 1346  118
   49  825 1963 1113 1271

A pour somme maximale 1720 + 1224 + 1963 + 1346 + 1843 = 8096

Quelle est la somme maximale de la matrice 32x32 contenue dans le fichier mat32 ? Le flag est la somme MD5 de la contaténation de tous les nombres utilisés pour faire cette somme, arrangés colonne par colonne.
Le seul fichier à fournir est le fichier mat32
Explications :
La solution est 61152 (1872+1929+1961+1984+1904+1776+1932+1908+1876+1921+1926+1694+1966+1982+1998+1878+1960+1914+1950+1848+1905+1927+1756+1864+1976+1837+1988+1993+1986+1923+1855+1963)
Il est évident pour ce challenge qu'on ne peut pas se contenter de calculer bêtement toutes les sommes possibles. Cela reviendrait à approximativement 32^33 opérations, ce qui est évidement totalement inaccessible.

L'astuce ici est assez complexe. Elle consiste à précalculer la liste MaxS[1..32], pour chaque colonne i, la plus grande valeur que l'on peut obtenir en ajoutenant la plus grande valeur de chaque colonne de i+1 à N (peu importe si ces valeurs sont sur les mêmes lignes ou non).
On va appeler idx[1...32] le numéro de ligne que l'on considère à la colonne 1 ... 32, ainsi qu'une liste de boolean mask[1...32]. Le mask servira à éviter de considérer une valeur dans une ligne où une valeur précédente a été utilisée.
Dans chaque boucle, on va ensuite mettre une condition permettant d'anticiper le fait qu'on ne peut pas atteindre la somme maximale. Il suffit d'ajouter MaxS[colonne de la boucle] à la somme des colonnes précédentes pour savoir si cette valeur est plus grande que la plus grande des sommes calculées (si elle est plus petite, on ne pourra jamais avoir une somme plus élevée en utilisant cette valeur).

L'algorithme est le suivant :
! précalcul de maxS :
maxS[:] = 0
do i = 32, 1, -1
    do j = i + 1, 32
        maxS[i] = maxS[i] + maxval(matrix[:,j])
    enddo
enddo

! calcul principal :
somme = 0
mask = false
maxsomme = 0
do idx[1] = 1 ,32
  si mask[1] == false
    mask[1] = true
    somme = somme + matrix(idx[1],1)
    si somme + maxS[1] > maxsomme

       do idx[2] = 1 ,32
         si mask[2] == false
         mask[2] = true
         somme = somme + matrix(idx[2],2)
         si somme + maxS[2] > maxsomme

            [...]

           do idx[32] = 1 ,32
             si mask[32] == false
               mask[32] = true
               somme = somme + matrix(idx[32],32)
               si somme + maxS[32] > maxsomme
                 si somme > maxsomme
                   écrire idx, somme
                   maxsomme = somme !! mise à jour de maxsomme
               somme = somme - matrix(idx[32],32)
               mask[32] = false

             [...]
         somme = somme - matrix(idx[2],2)
         mask[2] = false
    somme = somme - matrix(idx[1],1)
    mask[1] = false

Un coup d'openMP, et la solution tombe en moins d'une minute sur un processeur i7. Le programme max_matrix (généré par script) est donné en exemple.
