import random
intents=0
llista_de_paraules=[
    "aigua", "arbre", "cotxe", "feina", "llamp", 
    "pedra", "plata", "pluja", "poble", "porta", 
    "taula", "temps", "terra", "canta", "creia", 
    "mirar", "parla", "pensa", "picar", "podia", 
    "venir", "veure", "volar", "volia", "blanc", 
    "clara", "curta", "fosca", "llarg", "negre", 
    "petit", "verda"
]
paraula_escollida=(random.choice(llista_de_paraules))
paraula_escollida=list(paraula_escollida)
paraula_enigma=[]
#creo la paraula que sortirá a la consola
for lletra in paraula_escollida:
    paraula_enigma.append("X")
print(paraula_enigma)
#faig uns intents
while intents !=6:
    paraules_encertades=0 #poso aqui la variable comptalletres perque així es reinicia a 0 per cada iteració
    for i in range(5): #abanç de demanar la paraula, creo aquests bucle perque neteigi les O de l'ultim intent, prque de lo contrari, el jugador no sabra a on hi han les X i es perdra
        if paraula_enigma[i] == "O": 
            #no borro totes les lletres per poder donar una pista(com en un ahorcado)
            paraula_enigma[i] = "X"  

    escullir=input(f"Intent numero: {intents+1}") #l'usuari posa una paraula
    escullir=list(escullir) #la converteixo en llista
    numero_de_lletres=len(escullir)
    
    if numero_de_lletres !=5:
        print("La paraula ha de tenir 5 lletres")
        continue #faig servir continue perque aixi no compti com a intent
    else:
        intents+=1
        for i in range(5):
            if escullir[i]==paraula_escollida[i]:
                paraula_enigma[i]=escullir[i]
                paraules_encertades+=1
            elif escullir[i] in paraula_escollida and paraula_enigma[i]=="X": #si hi ha una lletra en la paraula que hem posat que estigui en la paraula que hem de adivinar, pero no coincideix la posicio i la lletra encara no a sigut adivinada, afageix una O
                paraula_enigma[i]="O"
    print(paraula_enigma)
    print(f"Tens {paraules_encertades} lletres encertades")
    if paraules_encertades==5:
        print("Enhorabona!, has guanyat")
        break
if paraules_encertades !=5:
    print("Game over")
    print(f"la paraula era: {paraula_escollida}")
       
print("joc finalitzat")
    


