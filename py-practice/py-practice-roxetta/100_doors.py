'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Alternate: As noted in this page's discussion page, the only doors that remain open are whose numbers are perfect squares of integers. Opening only those doors is an optimization that may also be expressed
'''


#unoptimized solution

doors = [False] * 100
for i in range(100):
   for j in range(i, 100, i+1):
       doors[j] = not doors[j]
   print("Door %d:" % (i+1), 'open' if doors[i] else 'close')
 
#optimized solution

for i in range(1, 101):
	if i**0.5 % 1: # Test if i is perfect square or not
		state = 'open'
	else:
		state = 'closed'
	print('Door {} is {}. '.format(i, state), end=' ')

#ultra-optimized solution

for i in range(1,11):
	print("Door %s is open" % i**2)
