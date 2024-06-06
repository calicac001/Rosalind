with open("datasets/gc.txt", "r") as file:
    data = file.readlines()

name_dna = {}
name = ''

for i in range(len(data)):
    if data[i].startswith(">"):
        name = data[i].strip(">").rstrip()
        name_dna[name] = ''
    else:
        name_dna[name] += data[i].rstrip()

gc_content = {}
for name in name_dna:
    num_c = name_dna[name].count("C")
    num_g = name_dna[name].count("G")
    perc = (num_c + num_g) / len(name_dna[name])

    gc_content[name] = perc*100

highest_perc = max(gc_content.values())
highest_name = [i for i in gc_content if gc_content[i] == highest_perc]

print(highest_name[0] + "\n" + str(highest_perc))

