from colorama import init
from colorama import Fore, Back, Style

adressfile = 'adress.data'

init()

ab = {
		'Дима ЛОХ' : '89898989898',
		'Ваня Красавчик' : '89898989898'
	}

class AKYPOK:
	def __init__(self, name, number):
		self.name = name
		self.number = number
	def ShowNumber(self):
		print(Back.GREEN)
		print(Fore.BLACK)
		print('Контакт {0} с номером {1}'.format(self.name, self.number))
	def AddNumber():
		print(Back.WHITE)
		print(Fore.BLACK)
		Name = input('Введите имя Контакта: ')
		print("Вы ввели {0}.Продолжить?".format(Name))
		answer = input().lower()
		if answer == "да":
			Number = input('Введите номер Контакта: ')
			print('Вы ввели номер {0} для контакта {1}.Вы уверены что хотите добвить этот контакт в AKYPOK?'.format(Number, Name))
			work1 = input().lower()
			if work1 == "да":
				ab[Name] = Number
				if Name in ab:
					print(Back.GREEN)
					print(Fore.BLACK)
					print("Контакт успешно добавлен.")
					Begining()
				else:
					print(Back.RED)
					print(Fore.BLACK)
					print("Ошибка")
					Begining()
			else:
				Begining()
		elif answer == "нет":
			Begining()
		else:
			print('Ошибка!')
			Begining()
	def DelNumber():
		print(Back.WHITE)
		print(Fore.BLACK)
		DelName = input("Введте имя Контакта: ")
		print("Вы ввели {0}.Продолжить?".format(DelName))
		answer1 = input().lower()
		if answer1 == "да":
			if DelName not in ab:
				print(Back.RED)
				print(Fore.BLACK)
				print('Введено неверное имя!')
				Begining()
			elif DelName in ab:
				del ab[DelName]
				if DelName not in ab:
					print(Back.GREEN)
					print(Fore.BLACK)
					print("Успешно!")
					Begining()
				else:
					print(Back.RED)
					print(Fore.BLACK)
					print('Ошибка!')
			else:
				print('Ошибка!')
				Begining()
		else:
			Begining()

def Begining():
	print(Back.WHITE)
	print(Fore.BLACK)
	print("Выберите дейтсвие:	Просмотреть 'АКУРОК' - 1	Добавить контакт - 2	Удалить контакт - 3")
	work = input()
	if work == "1":
		print('Сейчас в "АКУРОК" {0} номеров.\n'.format(len(ab)))
		for name, number in ab.items():
			AKYPOK(name, number).ShowNumber()
	elif work == "2":
		AKYPOK.AddNumber()
	elif work == "3":
		AKYPOK.DelNumber()

print(Back.WHITE)
print(Fore.BLACK)
print("Добро пожаловать в 'АКУРОК'(Адресная Книга Учебная Разработанная Очередным Клешнеруким)")
password = input("Введите пароль: ")
if password != "0000":
		print(Back.RED)
		print(Fore.BLACK)
		print('Доступ запрещен!')
else:
	print('\nУспех!')
	Begining()
