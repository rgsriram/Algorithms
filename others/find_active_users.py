'''
Find active users in chat
'''

def get_users_msg_map(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	users_msg_map = dict()
	
	for line in lines:
		user = line.split(':')[0]
		if user not in users_msg_map:
			users_msg_map[user] = 0
		users_msg_map[user] += 1

	return users_msg_map

def get_top_active_users(users_msg_map, show_top=3):
	reversed_users_msg_map = {}
	
	for k,v in users_msg_map.iteritems()

		if v not in reversed_users_msg_map:
			reversed_users_msg_map[v] = []

		reversed_users_msg_map[v].append(k)

	top_active_messages_count = reversed_users_msg_map.keys()
	top_active_messages_count.sort(reverse=True)

	index = 0
	
	for user in reversed_users_msg_map[top_active_messages_count[index]]:
		print user
		index += 1

		if index > show_top:
			break





