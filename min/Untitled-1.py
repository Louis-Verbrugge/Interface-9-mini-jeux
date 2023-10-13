mouvement_log = [9, 10, 11]
b = [mouvement_log[len(mouvement_log)-1-i] for i in range(min(len(mouvement_log), 5))]
print(b)
