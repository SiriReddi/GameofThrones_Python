from pprint import pprint
from characters import characters


numofA = []
for character in characters:
    if character['name'][0] == 'A':
        numofA.append(character['name'])
print("Total number : ", len(numofA))   
    #if character['name'].startswith('A') == True:
       # pprint(character['name'])

# print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))
def numofZ(z):
    numofz = []
    for character in characters:
        if character['name'].startswith('Z') == True:
            numofz.append(character['name'])
    print("Total number of Z: " , len(numofz))

numofZ('Z')

def chardead():
    dead = []
    for character in characters:
        if character['died'] != '':
            dead.append(character['died'])
    print("total number of characters died :" ,len(dead))

chardead()

def mosttitles():
    moretitle = 0
    for character in characters:
        numoftitles = len(character['titles'])
        if numoftitles > moretitle:
            moretitle = numoftitles
            print(character['name'], ":", moretitle)
            
mosttitles()

def valyrian():
    valy = []
    for valyrian in characters:
        if valyrian['culture'] == 'Valyrian':
            valy.append(valyrian['culture'])
    print("total Valyrians : ", len(valy))

valyrian()

def nottv():
    nottvs = []
    for character in characters:
        if character['tvSeries'] != '':
            nottvs.append(character['tvSeries'])
    print("How many characters are not in tvshows: ",len(nottvs))
    
nottv()

def hotpie():
    for character in characters:
        if character['name'] == 'Hot Pie':
            print("the actors played as Hot Pie: ",character['name'])

hotpie()

def targaryen():
    lastname = []
    for lastname in characters:
        #if lastname['name'][1] == 'Targaryen':
           # lastname.append(lastname['name'])
    #print(lastname)

            
        lasnam = lastname['name'].split()
     
     # print(lasnam)
        if lasnam == 'Targaryen':
           lastname.append(lastname['name'])
    print("the last name: ",lastname)

targaryen()
