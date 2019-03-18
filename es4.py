task1 = {"todo": "call John for AmI project organization", "urgent": True}
task2 = {"todo": "buy a new mouse", "urgent": True}
task3 = {"todo": "find a present for Angelina’s birthday", "urgent": False}
task4 = {"todo": "organize mega party (last week of April)", "urgent": False}
task5 = {"todo": "book summer holidays", "urgent": False}
task6 = {"todo": "whatsapp Mary for a coffee", "urgent": False}

list = [task1, task2, task3, task4, task5, task6]
urgents = []

for i in list:
    if i["urgent"]:
        urgents.append(i["todo"])

print(urgents)
