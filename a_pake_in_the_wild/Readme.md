Un ami à vous a conçu un nouveau protocole d'échange de clés authentifié.
Cependant, vous ne possédez pas le secret d'authentification requis.
Prouvez-lui que vous arrivez quand même à compléter ce protocole.
Titre: A PAKE in the wild
Catégorie: Crypto
Difficulté: Moyen/Difficile
Auteur: ElyKar

Description publique
--------------------


Un ami à vous a conçu un nouveau protocole d'échange de clés authentifié.
Cependant, vous ne possédez pas le secret d'authentification requis.
Prouvez-lui que vous arrivez quand même à compléter ce protocole.

Fichiers à donner:
- public/pake-in-the-wild.py

Description privée
------------------

Un protocole d'engagement vulnérable, qui ressemble beaucoup à celui utilisé en Bluetooth Mesh v1.0. La dérivation de clé et les formats de message ont été simplifiés:

A -> B: pubA
B -> A: pubB
A -> B: AES-CMAC(ck, nonceA || AuthValue)
B -> A: AES-CMAC(ck, nonceB || AuthValue)
A -> B: nonceA
B -> A: nonceB

Le problème est lié à l'utilisation d'AES en mode CMAC avec les paramètres choisis dans ce protocole: 
L'AES en mode CMAC est appliqué à chaque fois sur 32 octets: 16 octets de nonce et 16 octets d'AuthValue.
Il est alors possible, à partir d'un tag CMAC et d'un bloc (nonce ou AuthValue) de récupérer le bloc manquant du CMAC.

Solution
--------

Prenons $AES-CMAC(K, B1 || B2) = T$

Concrètement, connaissant le tag T, la clé K et le bloc B1, on peut calculer le block B2 ainsi:

$B2 = AES(K, B1) \oplus AES^{-1}(K, T) \oplus K1$

Connaissant le tag T, la clé K et le bloc B2, on peut calculer le block B1 ainsi:

$B1 = AES^{-1}(K, AES^{-1}(K, T) \oplus K1 \oplus B2)$

La clé K1 est dérivée de la clé K, le procédé est décrit dans la RFC 4493.

Avec ces deux primitives, on peut compléter le protocole d'authentification en une seule passe:

A -> B: pubA
B -> A; pubB
A -> B: AES-CMAC(ck, nonce || AuthValue)
B -> A: 0 # 16 octets nuls
A -> B: nonce

1. A partir de $nonce$, $AES-CMAC(ck, nonce || AuthValue)$ et ck on peut retrouver AuthValue
2. A partir de $AuthValue$, $00000000000000000000000000000000$ et ck on peut retrouver un nonce nonceB qui correspond à la valeur de confirmation envoyée précédemment

B -> A: nonceB

Ainsi, A est persuadé que l'on connait AuthValue depuis le début et nous envoit son secret.

Solution dans src/solve.py, adapter les variables HOST et PORT au déploiement.
