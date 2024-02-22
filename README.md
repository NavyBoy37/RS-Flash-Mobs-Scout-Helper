# Overview
## Purpose
To give RS Demon Flash Mobs scouts an easy way to sort the bosses by location and time remaining before they despawn.  Info for each boss will be entered and grouped by location, then each group will be sorted by time before despawn.

## What is Runescape's Demon Flash Mobs?
"Demon Flash Mobs" is a <i>Distraction and Diversion</i> that was released in January, 2013.  These bosses spawn in certain locations across Gilenoir and are meant for groups to fight.  Notable drops are title scrolls which can be sold or used to add a title to your in game name.  So long as enough damage is dealt, you are entitled to a drop as if you fought the boss alone.

## Terminology
Below I will explain common terms used in the teams that participate in these events along with sections of the program as appropriate.
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




# Notes on key variables

- The three major lists are as follows
- world_list -> list of worlds
- location_list -> list of locations
- time_left -> list of times left for each demon