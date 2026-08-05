#Dos encuestas
set1 = ["python","C","java","C++"]
set2 = ["C++", "C","rubi","go"]
s1 = set(set1)
s2 = set(set2)
print("Ambas listas: ", sorted(s1 & s2))
print("Valores unicos: ", sorted((s1-s2)|(s2-s1)))