from sys import argv
script, namefile = argv

lista = []

file = open(namefile)
for i in file:
    lista.append(i.rstrip())
print("Ho importato " + str(len(lista)) + " task")
file.close()

file = open(namefile, 'w')

sel = "0"

while not (sel =="4"):
    sel = input("\n\n1. insert a new task;\n2. remove a task;\n3. show all the tasks;\n4. close the program and export\n")
    if sel == "1":
        activity = input("Scrivi un'attività: ")
        lista.append(activity)
    elif sel == "2":
        activity = input("Scrivi un'attività da rimuovere: ")
        lista.remove(activity)
    elif sel == "3":
        lista=sorted(lista)
        for i in lista:
            print(i)
    elif sel == "4":
        for i in lista:
            file.write(i+"\n")

file.close()