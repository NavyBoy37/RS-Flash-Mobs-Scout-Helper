# Overview
## Purpose
To give RS Demon Flash Mobs scouts an easy way to sort the bosses by location and time remaining before they despawn.  Info for each boss will be entered and grouped by location, then each group will be sorted by time before despawn.

## What is Runescape's Demon Flash Mobs?
"Demon Flash Mobs" is a <i>Distraction and Diversion</i> that was released in January, 2013.  These bosses spawn in certain locations across Gilenoir and are meant for groups to fight.  Notable drops are title scrolls which can be sold or used to add a title to your in game name.  So long as enough damage is dealt, you are entitled to a drop as if you fought the boss alone.

## Terminology
Below I will explain common terms used in the groups that participate in these events along with sections of the program as appropriate.
### Location Names
This program accounts for 8 locations as of now.  Normalized nomenclature will be as follows.
```
pp -> Port Phasmatys
mta -> Mage Training Arena
uzer -> Uzer
mena -> Menaphos
edge -> Edgeville
fh -> Feldip Hills
wa -> West Ardougne
pw -> Poison Wastes
```
Multiple spellings of each location will be accepted and converted to these abbreviations.

### Scouting
One boss will spawn per world at one of 13 locations every hour (Or one hour after the death of the previous).  After 45 minutes they will despawn.  Therefore some coordination is required in teams to maximize the number of bosses killed in the hour.  Scouts will jump worlds finding locations and times remaining of each boss.  They relay this information to someone making the list like this.  
```
world 21, fh, 15 minutes left
```
Our inputs will be 
```
(world,location,time_left)
Or
1,fh,13
```
The list maker will input this information from the scouts in the format directly above.  The program can account for multiple lines of information at once.  
Ex:
```
input:

1,fh,10
2,wa,15
3,fh,8
4,mta,25
5,fh,20

output:

4, mta, 25
3, fh, 8
1, fh, 10
5, fh, 20
2, wa, 15
```
Time is saved this way because the group can kill all mobs in one location before moving to the next in a prioritized order.  It will later be updated to arrange the location groups by shortest to longest time left like this.
```
output:
3, fh, 8
1, fh, 10
5, fh, 20
2, wa, 15
4, mta, 25
```




## How the code works
1. Established a list of objects that contain a (world, location, time_left)

2. Establishes lists of acceptable names for each location, then nests those lists within the list, "all_names"

3. Takes multiple lines of code at once, and removes stray marks or abnormalities with regex.

4. References each location input with the lists of potential location names via "if" statements, and overwrites the "location" of each object with a number for sorting.  It adds these new cleaned objects to "big_list".  It continues this until the user "ctrl + c"

5. "big_list" is sorted by the "time_left" element of the list's objects.

6. "big_list" is sorted by the number tied to the "location" element of the list's objects.

7. The element "location" of "big_list" objects are converted from numbers to normalized location names as described in the terminology section above.

8. Every object in "big_list" is printed for the user.
