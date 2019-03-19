'''
A thief mat plan to escape from a jail. Mat is a monkey man and is able to jump over a wall. Mat has practiced well and can jump x meter. However because of the wall is slippery, he also slides down Y meter of each jump. To escape from jail, he has to cross N number of walls. 
if the height of each wall is given in an array. write a program to find out total no of jumps he need to escape from jail.

ex:
input1: 10,1,1,{10}
output1: 1 

input2: 5,1,2,{9,10}
output2: 5
'''


def find_no_jumps(x, y, walls):
	jumps = 0
	for w in walls:
		d = w
		while d > 0:
			jumps += 1
			if d == x:
				break
			d = d - (x-y)
	return jumps


if __name__ == '__main__':
	find_no_jumps()