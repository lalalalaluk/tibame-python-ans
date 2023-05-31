dic ={"HELLO" :"ENGLISH",
"HOLA":"SPANISH",
"HALLO":"GERMAN",
"BONJOUR":"FRENCH",
"CIAO":"ITALIAN",
"ZDRAVSTVUJTE":"RUSSIAN"}

index = 0
while 1:
    a = input()
    index+=1

    if a == "#":
        break
    if a in dic:
        print("Case "+str(index)+": "+dic[a])
    else:
        print("Case "+str(index)+": UNKNOWN")