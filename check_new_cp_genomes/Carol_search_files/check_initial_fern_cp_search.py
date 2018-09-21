from __future__ import absolute_import
from __future__ import division
from __future__ import print_function 

# open initial search and make species list
initial_search_results = open('fern_file.csv', 'rU')
initial_species_list = []
line_count = 0
for line in initial_search_results:
    if line_count > 0:
        line = line.split(',')
        species = line[1].strip('chloroplast ')
        species = species.strip('\n')
        initial_species_list.append(species)
    line_count+=1
    
#print(initial_species_list)
print("initial list length: ",len(initial_species_list))


# open current csv file on web page and make species list

current_results = open('fern_plastomes_genbank.csv', 'rU')
current_list = []
line_count = 0
for line in current_results:
    if line_count > 0:
        line = line.split(',')
        current_list.append(line[0])
    line_count+=1

#print(current_list)
print("current list length: ",len(current_list))


# Compare lists
not_in_current = []
for name in initial_species_list:
    if name not in current_list:
        not_in_current.append(name)
print("missing from current list: ",not_in_current)
print(len(not_in_current))

not_in_initial = []
for name in current_list:
    if name not in initial_species_list:
        not_in_initial.append(name)

print("missing from initial list: ",not_in_initial)
print(len(not_in_initial))
