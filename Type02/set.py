# Set items are unchangeable but you can remove items and new items 
# basically sets are used to store multiple items in a single variable 
# Set {} suplicates value not allowed 
set2={'saruar','he','saruar'}
# here output will be saruar and he  sets ignore same value also its unchangeable
# Once a set is created ,you cannot change its itmes , but you can add new itmes


# add an item to a set , using the add()
t={'s','r','d'}
print(t.add('tdl'))


# Add element from tropical into thisset :
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# remove something
# set is unchangeable we can add but can't remove 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)#loop sets
  
#   union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# output wil be {a,1,b2,b,3}
# its tipically union and update both wil exclude any duplicate itmes 

# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the 
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others