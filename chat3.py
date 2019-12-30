chat = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		chat.append(line)

for loop_chat in chat:
	new_chat = loop_chat.strip().split(' ')
	#print(new_chat)
	time = new_chat[0][:5]
	name = new_chat[0][5:]
	chat = new_chat[1]
	print('時間 :', time)
	print(name, ':', chat)
	