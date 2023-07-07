Un triangle pythagoricien est un triangle rectangle dont les 3 côtés sont des entiers.
Pour un périmètre donné, il peut y avoir plusieurs triangles pythagoriciens ayant ce périmètre.
Par exemple, pour un périmètre de 84, il existe 4 triangles (12,35,37), (21,28,35), (28,21,35), (35,12,37)
Pour quel périmètre, inférieur à 1000000, y-a-t-il le plus grand nombre de triangles pythagoriciens ?

Soluc : 720720

en fait il faut "juste" éviter de tomber dans la solution naive qui consisterait à tester tous les triplets entiers pour voir s'ils sont égaux à un périmètre donné. Il faut regarder la chose à l'envers : pour chaque doublet (a, b), où a et b sont inférieurs à périmètre / 2, sont-ils les cotés d'un triangle rectangle ? Ou : est-ce que int(sqrt(a²+b²))² = a²+b² ? Si oui : c'est un triangle pythagoricien.

Pour chaque triangle, on regarde ainsi son périmètre, et on les compte. Le résultat est 720720, possédant  208 combinaisons.
