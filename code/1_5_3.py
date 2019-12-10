#百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
#鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
#百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
#翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只

#暴力求解

for m_chicken in range(0,21):
	for f_chicken in range(0,34):
		for c_chicken in range(0,301,3):
			if m_chicken*5 + f_chicken *3 + c_chicken/3 == 100:
				print('%d m_chicken,%d f_chicken,%d,c_chicken'%(m_chicken,f_chicken,c_chicken))
				continue

