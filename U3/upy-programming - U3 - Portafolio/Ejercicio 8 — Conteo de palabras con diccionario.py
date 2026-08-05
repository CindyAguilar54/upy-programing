#Conteo de palabras
sentence = "España es el campeon del mundo y Messi el lloron"
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word,0)+1
print(counts)