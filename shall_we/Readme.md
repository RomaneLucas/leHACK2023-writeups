Shall we play a game? Please download this file and then connect to shallwe.wargame.rocks:1337.
# Description

Title: ShallWe?
Desc: Shall we play a game? Please download this file and then connect to shallwe.wargame.rocks:1337.


# Build du binaire pour les participants

```
cd src/entropid
cargo build --release
mv ./target/release/entropid /where/you/want/wargame
```

# Build du binaire à mettre en prod

```
cd src/entropid
vim src/main.rs #mettre le vrai flag
cargo build --release
```

# Deploy du chall

```
```

# Sploit

Reverser le binaire, voir que c'est du rust et que le generateur de nombre aléatoire est initialisé avec le pid du process.

Sur un système Linux moderne `/proc/sys/kernel/pid_max` peut être à plus que 65k mais au pire, il suffit de tester de manière incrémentale pour avoir le meme seed que le process.

```
nc shallwe.wargame.rocks 1337
Greetings Professor Falken
Shall we play a game?
What's your number?
1
Giving you another try.
My number was: 938106121
What's your number?
444728686
lh_FLAG
```

Mettre un nombre au hasard la première fois, ensuite on récupère le nombre et on utilise le sploit pour trouver le bon deuxième nombre.

```
cd src/sploit
cargo build
./target/debug/sploit | grep "^938106121"
```
