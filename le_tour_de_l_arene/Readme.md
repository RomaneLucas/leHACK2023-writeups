Challenge : hardcore

## Description
Pour résoudre ce challenge, il ne faut être ni trop con, ni trop pressé...

## Writeup
Dans le PDF se trouvent 3 chaines de caractère camouflées en noir/noir dans la bordure de l'échiquier. Il faut faire un string sur le pdf pour les obtenir. Parmis ces 3 chaines, seulement une a le flag : "eJxzzs9LL0osKc1JLMnMzytWUFQIyUhVSMtJTFfILFawUijOTczJSS1S0CjJLy1ROLw8UaEgv7QIxNDT09MEAMRyFmM="
Ces chaines sont des B64, qu'il sagira de convertir en binaire, avant de faire appel à la bib système libz ('uncompress') pour avoir son contenu (ce ne sont pas des fichiers). Le contenu de ces 3 chaines sont :

1° : Hmmm, not so far, but its not here...
2° : Hmmm, not so far, but its not here too...
3° : Congratulations ! The flag is : smaller (tout ça pour ça...)

Du coup, le flag est évidement "smaller (tout ça pour ça...)"


## Test
selectionner le texte dans le pdf, copier coller, 
```
python3
import zlib
import base64
zlib.decompress(base64.b64decode("eJxzzs9LL0osKc1JLMnMzytWUFQIyUhVSMtJTFfILFawUijOTczJSS1S0CjJLy1ROLw8UaEgv7QIxNDT09MEAMRyFmM=").decode('utf-8')
```
