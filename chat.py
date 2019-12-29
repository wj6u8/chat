def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat_list):
	new = []
	person = None
	for chat_line in chat_list:
		if chat_line == 'Allen':
			person = 'Allen'
			continue
		elif chat_line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + chat_line)
	return new

def write_file(filename, new_chat):
	with open(filename, 'w') as f:
		for new_chat_line in new_chat:
			f.write(new_chat_line + '\n')

def main():
	read_result = read_file('input.txt')
	new = convert(read_result)
	write_file('output.txt', new)

main()