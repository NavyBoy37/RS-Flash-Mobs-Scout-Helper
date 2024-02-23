import re

# TODO: Must make the list update as new entries are added because the scouts will not have all the info at once.
# TODO: Update ReadME to be better.]
""" TODO: Sort location groups based off shortest first time_left. Otherwise
1,fh,10
2,wa,15
3,fh,8
4,mta,25
5,fh,20

may be

4, mta, 25
3, fh, 8
1, fh, 10
5, fh, 20
2, wa, 15
"""


big_list = []


class Flash_Mob_Calc:
    def __init__(self, world, location, time_left):
        self.location = location
        self.world = world
        self.time_left = time_left

#   Lists for normalizing user inputs.
#   User will input location values and if matching any phrasing on this list, be converted to standard location names for sorting.
port_phas_names = ['pp', 'port phas','port','phas','phasmatas','portphas'] 
mage_training_names = ['mta','mage training','mage','mage training arena','mage arena']  
uzer_names = ['uzer','uz','uzr','uze']
mena_names = ['mena','menaphos','men','menap','menaph','menapho']
edge_names = ['edge','edgeville','ev','edg','edgevill','edgev']
hills_names = ['fh','hills','feldip','fell','fel','f hills']
west_ardougne_names = ['wa','west','ardougne','west ardougne','ardy','doug']
poison_waste_names = ['pw','poison waste','poison','waste','prif']
seers_village_names = ['seers','sv','village','seer','srs','seers village','vill']

all_names = [
    port_phas_names,
    mage_training_names,
    uzer_names,
    mena_names,
    edge_names,
    hills_names,
    west_ardougne_names,
    poison_waste_names
]
#How to edit the 3rd object of the third variable of big list
#big_list[2].location

#   User input and regex system.  Ensures input will be recognized with commas, weird spaces, and extra letters/numbers
#   utilized regex101.com for the purpose
print("Valid Location Ex: pp, mta, uzer, mena, edge, fh, wa, pw, seers")
print("world, location, time left")

while True:
    try:
        line = input()
        result = re.search("(\d{1,3}\s*),(\s*[\w\s]+),(\s*\d{1,2})", line, re.IGNORECASE)

        if str(result.group(2)).strip() in port_phas_names:
            clean_location = 10001 #pp,  this block of code converts location data to numbers for sorting
    
        if str(result.group(2)).strip() in mage_training_names:
            clean_location = 20002 #mta
    
        if str(result.group(2)).strip() in uzer_names:
            clean_location = 30003 #uzer

        if str(result.group(2)).strip() in mena_names:
            clean_location = 40004 #mena

        if str(result.group(2)).strip() in edge_names:
            clean_location = 50005 #edge
        
        if str(result.group(2)).strip() in hills_names:
            clean_location = 60006 #fh

        if str(result.group(2)).strip() in west_ardougne_names:
            clean_location = 70007 #wa

        if str(result.group(2)).strip() in poison_waste_names:
            clean_location = 80008 #pw

        if str(result.group(2)).strip() in seers_village_names:
            clean_location = 90009 #seers 

    except KeyboardInterrupt:
        break
        
    big_list.append(Flash_Mob_Calc(int(str(result.group(1)).strip()),clean_location,int(str(result.group(3)).strip())))

###


#   takes the list of objects 
#   big_list=[(world1, location1, time_left1),(world2, location2, time_left2),...] 
#   and organized them based on time_left (least to greatest), then location

big_list = sorted(big_list, key=lambda obj: obj.time_left)
big_list = sorted(big_list, key=lambda obj: obj.location)


#the block below returns location from a number to the proper string name.
for obj in big_list:

    if obj.location == 10001:
        obj.location = "pp"

    if obj.location ==20002:
        obj.location = "mta"
    
    if obj.location ==30003:
        obj.location = "uzer"
    
    if obj.location ==40004:
        obj.location="mena"

    if obj.location==50005:
        obj.location="edge"

    if obj.location==60006:
        obj.location="fh"

    if obj.location==70007:
        obj.location="wa"

    if obj.location==80008:
        obj.location="pw"

    if obj.location==90009:
        obj.location="seers"



print("--------------")
for obj in big_list:
    print(f"{obj.world}, {obj.location}, {obj.time_left}")
