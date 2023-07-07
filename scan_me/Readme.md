voila un petit chall sans pretention aucune
je ne sais pas si ce sera du niveau attendu mais ce n'est pas hyper compliqué (enfin je trouve) mais cela demande tout de même un peu de manips ...

c'est un QR code
une fois scanner il donne :
Ou est le Flag ?
Exclusivement "Au C3nTr3"

la faute sur "où" est volontaire ...
au centre de ce QR code il y a un autre QR-code mais il faut reconstruire les marqueurs (j'ai laissé volontairement ce qu'il faut pour pouvoir les reconstruire facilement avec de simple copier / coller.

une fois les marqueurs reconstruits et le precedent QR code viré car seul celui du centre nous interesse désormais on obtient :

0D 10 00 05 5F 0F 33 52 56 32 01 1A 63 6B 43 1B 20 6C 0D 10 7F 10 5B 0B 26 1B 55 1E 11 45 1C 7F 49 31 01 43 20 16 45 62 12 64

bref une chaine en hexa et si on la passe dans un XOR (un ou exclusif d'où les indices du 1er QR code) avec la clef Au C3nTr3 on obtient

4C 65 20 46 6C 61 67 20 65 73 74 3A 20 58 2D 4F 52 5F 4C 65 5F 53 68 65 72 69 66 5F 64 65 5F 4C 27 65 73 70 61 63 65 21 21 0A

ce qui en ascii donne:
Le Flag est: X-OR_Le_Sherif_de_L'espace!!

j'ai mis le flag en surbrillance ...

Si cela ne fait pas le job aucun souci je ne me vexerai pas mais comme il en faut un peu pour tous les niveaux et que cela ne m'a pas pris trop de temps voilou ...


# --- Solve

zbarimg scan_me.png

$ zbarimg scan_me.png 
QR-Code:Ou est le Flag ?
Exclusivement "Au C3nTr3"
scanned 1 barcode symbols from 1 images in 0.36 seconds

$ str2hex "Au C3nTr3"
41752043336e547233

$ zbarimg scan_me_solved.png 
QR-Code:0D 10 00 05 5F 0F 33 52 56 32 01 1A 63 6B 43 1B 20 6C 0D 10 7F 10 5B 0B 26 1B 55 1E 11 45 1C 7F 49 31 01 43 20 16 45 62 12 64
scanned 1 barcode symbols from 1 images in 0.01 seconds

Faire un xor (https://xor.pw/#) :

0D1000055F0F33525632011A636B431B206C0D107F105B0B261B551E11451C7F49310143201645621264

41752043336e54723341752043336e54723341752043336e54723341752043336e54723341752043336e


# --- Memo

Donner un hint dans l'ennoncé du challenge :
Le premier QR Code contient des "m0ts catqui s3rt de cl3".


