# Message ambassade Cryptanga

Type de l’epreuve : Stéganographie
Auteur : M0N5T3R
Texte d’introduction : Vous interceptez un message de l’ambassade du pays
Cryptanga.

Texte d'introduction 2 : Vous interceptez un message de l’ambassade du pays Cryptanga. Trouvez quelle transformation a été utilisée pour encoder ce message, décodez-le et récupérez y le code secret du ministère cryptangais. Le flag est au format LeHack{lecodesecretduministere}

Niveau de difficulté : medium
Le flag : qwvmegh

## Le challenge chiffré :

I KYIAA T I IKNNZYH ANZZIZN I W LY/A FKHKKN HFFIFAHHZ AMNFN LFYNHYH I NYXKN IHZ I/I AFIHF X I
KZHZIYZ KAYIFYH I M VA YZZNHZA HNNHYY/MKZKYAK YT FYYNFZN ZNZ FKKH YYKY TK TFHKYKNFK/ZHWHF
HANYHH VY ZALAK E FZFFYK VY/K AYHKH AXZNF YKNZNXY I Y ZNKHKFL/I YMNKNHY TN A/NAHIZ FHKFA
FNYKL KIANZFH AAA ZV AZFNKAK KYHZNN/ZEH AAHZA NXN FVNFK/ANIZAFK HHIKA KNA AAKHXHK NFT/I A
KAKNVFZ HKFZFYZ LZ ZNHN FNFA FV AIZAF YV HHZXH NHLKNAY/Z ZHA YHHHXNH ZKHFY YKIKAFAAZ XK
FKNZV/I ZKLHF AZZYFNF YNKIH KV YKYAAY ZZH Y I ZHY FFYVY/NAKZNWN NL KKKKYZY ZHN FFNZ YKKH XK
TKNZHFFFN/KT INN I YHKY AX HYAIN AL FHALK HAZXHAZ/NZAK FHHAAKH ZKK/KFYAAN YL IANZH XZ
FYKFFKT ZHYFFLY ZFAFFK YL/AZYFNYK XHAKF/EZFZY I IZHYHYY HHYIHYY KT NFMAY FKKHZ AZAZNA
NZFVZNF/I ZYHNHEY TH Y/AYKZ YV/F AZNHK W LA/YAAYIAF HX A AKYFKN KV KFYHAZT/LNZZNH AAYKXZZH
MHZAHFZ HNINF LY YKI HXH/HWHKF KAAHZ FKYAYFY ZFNYHZ/ZZKHHA FL HFTKF NNFHHVZ FNFFNA LK
NHKYFY/W I KHVFK AYAYKIN/HKFZ YV/AAKKYIZ YKN LZKNZNN AT/AYNIK ZKA FHZVN AZZ XH NAHNKK/F
YZKAYZ KNHKNIFAZ ANYAM ZANZZVY I AAVHY NZI I FYH KNFFFYI/KWF HL/AKYTZ NL/M AZZYF NYKZYNN
ZKFFLKK LY/YZKEH I ZKIHHHF/KKTHFY KKAFZFK LZ/YWNZYHA NNKFY ZYNANHH HHAIZYN/LY NNNYXAK XA
FNAAHIF/Y KFHKA LZYHA YAKYIAY Y FFA TF XKKHN FKAKVYA/E NX/FFNF/AAA ZZIYF WAZZF HHHYY ZZNAHA
TYYYFHA I KXKHA K VZ/E/FT AFFNAAL YHANNF ZT/E ZHF KNAYAKI N HZZHFN AT ZVKZHYA/KFKIKAZ NNHFZKA
FANAAY/K VY XNHHZYA/ZL Z YXZ I AHXAK IHK LY/TN FZHNXAF/E KL/ZAZA/ZNY ZZZIA KKMKF AYFYN HZANFY
KZNNLNA I YHAXF Y LZ/Z HNAAHF FZH YAKHLYA HHY KYYYFV KHKHKAN VA/M/I F AZTZAH HHAZAFA LA
KYNHYN HYA AHZHZY/Y XA FFYZFHT ANNZFVZ LA/NKAKKVF VF A FHT YYKXH KAHNN FKYK KAYYZ IHK AZF
LF/I HZ FZK YLFHK/W LY/ZKZHKH I ZNLAZYZ ZXYYZYN NYKYNN I HYWNA VN ZANFHF/ZNYH YL/KFFANK FX
ZAHHZFT I ZFAZFZ M/M VF/LKNNF KAFHZ HHFNXFK FAHHKZ HL/YHH AKXAH E AKAYNNF HYAYNNI ZNYKAHX
ANFAKF FKA NT/HIAAYYY HAYHZYH HHYAKK/ZYKA I/ANHTYHF KL A TKN KXAAN YAKHN AKKY FFYHF NKI YNH
TZ/M/XZ KAYANKKA K I HEYYKZY I HYKHNXY HKZ AFKYN TYHZF/HFIAK AL Z I FFYXA ZAZ HKHLZH HYFYHYY
TK/IKZZK ZFF HNHFL KFF NIZANYZ KHLNANF KHFNAZ LY/M ZX IYNNKNK/AHFHXHA HL A VZK TZFHZ HKKHH
NHNK YHKKY KNI YHH VZ KAHYINA/T TH KHFKHN AVZKY I ANHHZK M/E W KFNKY AINFZHZ

## Le challenge déchiffré :

> Ambassade Cryptanga,
> Ambassadeur,
> Veuillez prendre contact avec monsieur john smith, actuellement citoyen anumericain. Veuillez egalement lui remettre un
> passeport avec le code secret qwvmegh pour rentrer dans le site minier Cryptangais.
> Je ne doute pas que vous etes conscient de l'importance d'etre discret sur cet echange et de l'importance critique
> d'acquerir cette technologie afin de rattraper le retard de notre industrie sur la technologie d'excavation mecanique.
> Ministre des Technologies,
> Bernard Ddos

# LES INDICES :

Indice1 : Il y a que des traits.

## Réponse/Write UP :

On constate que les lettres du message chiffrée sont composées uniquement de caractères avec des traits
rectilignes et les lettres I,L,T,V,X,A,F,H,K,N,Y,Z,E,M,W sont les plus courantes.
Le principe du chiffrement est de relier à un nombre, une lettre ou groupe de lettres comportant autant de
lignes distinctes nécessaires à leur écriture.
La lettre A est composée de 3 traits et la lettre I est composé d’1 seul trait. La position de la lettre A est 1
dans l’alphabet. Donc la lettre A sera chiffrée en I. La lettre B a la position 2 dans l’alphabet donc elle sera
chiffrée en T ou en L ou en V.
Nous utilisons Dcode pour déchiffrer tout le message : https://www.dcode.fr/chiffre-traits-lettre
