lista = []
sel = 0

while not (sel ==4):
    sel = int(input("\n\n1. insert a new task;\n2. remove a task;\n3. show all the tasks;\n4. close the program\n"))
    if sel == 1:
        activity = input("Scrivi un'attività: ")
        lista.append(activity)
    elif sel == 2:
        activity = input("Scrivi un'attività da rimuovere: ")
        lista.remove(activity)
    elif sel == 3:
        lista=sorted(lista)
        for i in lista:
            print(i)
