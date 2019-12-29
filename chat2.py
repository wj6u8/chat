def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat


def convert(chat_list):
	new = []
	person = None
	allen_mes_count = 0
	allen_pic_count = 0
	allen_sticker_count = 0
	viki_mes_count = 0
	viki_pic_count = 0
	viki_sticker_count = 0
	for chat_line in chat_list:
		mes = chat_line.split(' ')
		time = mes[0]
		name = mes[1]
		if name == 'Allen':
			if mes[2] == '圖片':
				allen_pic_count += 1
			elif mes[2] == '貼圖':
				allen_sticker_count += 1
			else:
				for count in mes[2:]:
					allen_mes_count += len(count)
		elif name == 'Viki':
			if mes[2] == '圖片':
				viki_pic_count += 1
			elif mes[2] == '貼圖':
				viki_sticker_count += 1
			else:
				for count in mes[2:]:
					viki_mes_count += len(count)

	print('Allen說了', allen_mes_count, '個字')
	print('Allen傳了', allen_pic_count, '張圖片')
	print('Allen傳了', allen_sticker_count, '張貼圖')

	print('Viki說了', viki_mes_count, '個字')
	print('Viki傳了', viki_pic_count, '張圖片')
	print('Viki傳了', viki_sticker_count, '張貼圖')


def write_file(filename, new_chat):
	with open(filename, 'w') as f:
		for new_chat_line in new_chat:
			f.write(new_chat_line + '\n')


def main():
	read_result = read_file('LINE-Viki.txt')
	new = convert(read_result)
	# write_file('output.txt', new)


main()