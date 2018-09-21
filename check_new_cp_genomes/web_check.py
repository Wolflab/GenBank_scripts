new = [['1241928872', 'Schizaea pectinata'],
 ['1241931102', 'Matteuccia struthiopteris (ostrich fern)'],
 ['1241922603', 'Diplaziopsis cavaleriana'],
 ['1241922336', 'Austroblechnum melanocaulon'],
 ['1241922691', 'Diplazium dushanense'],
 ['1241930396', 'Diplaziopsis javanica'],
 ['1241930663', 'Diplazium unilobum'],
 ['1241931369', 'Rhachidosorus consimilis'],
 ['1241931635', 'Woodsia polystichoides'],
 ['1241929863', 'Asplenium pekinense'],
 ['1241922780', 'Diplazium striatum'],
 ['1241930485', 'Diplazium bellum'],
 ['1241930307', 'Deparia lancea'],
 ['1241929952', 'Asplenium prolongatum'],
 ['1241931013', 'Macrothelypteris torresiana'],
 ['1241929774', 'Athyrium sheareri'],
 ['1241922514', 'Deparia viridifrons'],
 ['1241931191', 'Onoclea sensibilis'],
 ['1241930574', 'Diplazium dilatatum'],
 ['1241930747', 'Dryopteris decipiens'],
 ['1241922247', 'Athyrium sinense'],
 ['1241922425', 'Deparia pycnosora'],
 ['1241930925', 'Hymenasplenium unilaterale'],
 ['1241930040', 'Athyrium opacum'],
 ['1241929685', 'Ampelopteris elegans'],
 ['1241930129', 'Cyclosorus procerus'],
 ['1241931458', 'Stegnogramma sagittifolia'],
 ['1241930836', 'Homalosorus pycnocarpos'],
 ['1241931546', 'Woodsia macrochlaena'],
 ['1241928788', 'Schizaea elegans'],
 ['1241930218', 'Cystopteris chinensis'],
 ['1241931280', 'Thelypteris aurita'],
 ['1241922869', 'Hypodematium crenatum']]

new_species = [item[1] for item in new]
    
#print new_species
web = open("website.txt", mode='r')

web_list = []
for line in web:
    line = line.split(',')
    web_list.append(line[0])
#print web_list
count = 0
for species in new_species:
    if species in web_list:
        count+=1
    else:
        print "whoops: ", species
print "final count = ", count
web.close()