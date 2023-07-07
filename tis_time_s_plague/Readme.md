L'épreuve se nomme "Tis the time's plague when madmen lead the blind"
simplement publier l'image D0Y0U5P34K17.jpg
et le texte:
"Peu avant sa disparition mystérieuse, un ami vous a demandé de l'aide pour analyser ce fichier. "Surement un coup des illuminati" affirmait-il..."


explications: C'est un mix OSINT et décodage binaire/braille un peu tordu

"C'est le malheur du temps que les fous guident les aveugles"
Phrase de William Shakespeare, pour introduire l'indice menant au braille


Le nom du fichier "D0Y0U5P34K17.jpg" est aussi un indice sur le fait qu'on
va parler une autre langue et permettra au gens de lire le flag (meme si le flag doit etre collé en l33t speak pour etre validé)
 
fichier: 
L'image représente John A.Gardner. A travaillé sur le braille et a co-créé le système Gardner-Salinas 8 qui fait passer le braille de 6 à 8 points et introduit les notations mathématiques.
https://en.wikipedia.org/wiki/Gardner%E2%80%93Salinas_braille_codes

Quand on observe le fichier avec strings on retrouve la référence à SALINAS-8

Quand on ouvre le fichier avec un éditeur hexa/binaire et qu'on extrait les datas binaires après SALINAS-8 par groupe de 8, little-endian et qu'on fait correspondre les bits tels que décrits ci-dessous:
https://en.wikipedia.org/wiki/Braille_Patterns

bits		Braille
0 3 		1 4
1 4	<==>	2 5
2 5	<==>	3 6
6 7		7 8

On obtient la correspondance avec les caractères et les chiffres braille en système GS-8 permettant de former le flag

 ⡭⠡⠡⡝⠩⠱⠻⡏
⠡⠗⠩⠹⡧⠩⡥⠫
⠡⠩⡟⡥⠩⡉⠩⠡
⡥⠡⡟⡥⠡⡝⠩⡧
⠩⡥⠻⡏⠹⠱⡧⠬
⠡⠗⠡⠩⡓⠹⡉⡅

"X11N357P1r34V3U613QU3C31U1QU1N3V3U7P45V01r13H4CK"

Le fichier GS8.csv ne doit pas etre inclus au chall: il donne la correspondance bits, braille et lettres/chiffres et n'est là que pour une éventuelle vérification.














