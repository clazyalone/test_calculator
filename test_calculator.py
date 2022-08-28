#/usr/bin/python3
import requests
import pytest
import random
import platform
import os


max_positive_number = 2147483647	# Максимальное разрешенное положительное число
min_negative_number = -2147483648	# Минимальное разрешенное отрицательное число


hostname = input('Введите хост: ')	# Хост

oc = platform.system()	# Проверка пингов 
if (oc == "Windows"):
    ping_com = "ping -n 1 "
else:
    ping_com = "ping -c 1 "

def scan_Ip(ip):
    comm = ping_com + hostname
    response = os.popen(comm)
    data = response.readlines()
    return data
asd = scan_Ip(hostname)
n = 0
for line in asd:
    if 'ttl' in line:
        n += 1
if n > 0:
    print('ping:', hostname + ':', 'доступен')
else:
	print('ping:', hostname + ':', 'не доступен')


portname = input('Введите порт: ')	
print('Если сервис не доступен, программа выдаст ошибку через 10 секунд')														# Порт
quantity_input = int(input('Введите количество проверок: '))								# Количество проверок
addres_addition = 'http://' + hostname + ':' + portname + '/api/addition'					# Сложение 
addres_multiplication = 'http://' + hostname + ':' + portname + '/api/multiplication'		# Умножение
addres_division = 'http://' + hostname + ':' + portname + '/api/division'					# Деление
addres_remainder = 'http://' + hostname + ':' + portname + '/api/remainder'					# остаток
addres = 'http://' + hostname + ':' + portname + '/api/state'								# Ответ сервера

def test_connection():					# функция для проверки get запроса
	addres_get = requests.get(addres, timeout=10)
	print(addres_get.json())
test_connection()


def test_addition(a, b):	# сложение
	addition_test = requests.post(addres_addition, json={'x':a, 'y':b})
	status_code_addition = addition_test.json()['statusCode']	# Получаем информацию statusCode
	result_addition = addition_test.json()['result'] 			# Получаем информацию результата вычислений калькулятора
	return status_code_addition, result_addition


counter = 0
# сложение отрицательных чисел

for i_min_addition in range(1, quantity_input+1): 		 			
	one_min_number_addition = random.randrange(min_negative_number, 0)
	two_min_number_addition = random.randrange(min_negative_number, 0)
	sum_min_numbers_addition = one_min_number_addition + two_min_number_addition

	stat_negative_addition, res_negative_addition = test_addition(one_min_number_addition, two_min_number_addition)
	if res_negative_addition == sum_min_numbers_addition:
		counter += 1
	else:
		print('Число', one_min_number_addition, '+', 'число', two_min_number_addition, '=', sum_min_numbers_addition, '!= ответу webcalculator', res_negative_addition)
print('Произведено', i_min_addition, 'проверок на сложение отрицательных чисел, из них', counter, 'проверок - OK')


counter = 0
# сложение положительных чисел
for i_max_addition in range(1, quantity_input+1): # 2
	one_max_number_addition = random.randrange(0, max_positive_number)
	two_max_number_addition = random.randrange(0, max_positive_number)
	sum_max_numbers_addition = one_max_number_addition + two_max_number_addition

	stat_positive_addition, res_positive_addition = test_addition(one_max_number_addition, two_max_number_addition)
	if res_positive_addition == sum_max_numbers_addition:
		counter += 1
	else:
		print('Число', one_max_number_addition, '+', 'число', two_max_number_addition, '=', sum_max_numbers_addition, '!= ответу webcalculator', res_positive_addition)
print('Произведено', i_max_addition, 'проверок на сложение положительных чисел, из них', counter, 'проверок - OK')


counter = 0
# сложение положительного и отрицательного числа
for i_max_min_addition in range(1, quantity_input+1): # 3
	one_max_min_number_addition = random.randrange(0, max_positive_number)
	two_min_zero_number_addition = random.randrange(min_negative_number, 0)
	sum_max_min_numbers_addition = one_max_min_number_addition + two_min_zero_number_addition

	stat_positive_negative_addition, res_positive_negative_addition = test_addition(one_max_min_number_addition, two_min_zero_number_addition)
	if res_positive_negative_addition == sum_max_min_numbers_addition:
		counter += 1
	else:
		print('Число', one_max_min_number_addition, '+', 'число', two_min_zero_number_addition, '=', sum_max_min_numbers_addition, '!= ответу webcalculator', res_positive_negative_addition)
print('Произведено', i_max_min_addition, 'проверок на сложение положительного и отрицательного числа, из них', counter, 'проверок - OK')


counter = 0
# отрицательного и положительного числа
for i_min_max_addition in range(1, quantity_input+1): # 4
	one_min_max_number_addition = random.randrange(min_negative_number, 0)
	two_max_min_number_addition = random.randrange(0, max_positive_number)
	sum_min_max_numbers_addition = one_min_max_number_addition + two_max_min_number_addition

	stat_negative_positive_addition, res_negative_positive_addition = test_addition(one_min_max_number_addition, two_max_min_number_addition)
	if res_negative_positive_addition == sum_min_max_numbers_addition:
		counter += 1
	else:
		print('Число', one_min_max_number_addition, '+', 'число', two_max_min_number_addition, '=', sum_min_max_numbers_addition, '!= ответу webcalculator', res_negative_positive_addition)
print('Произведено', i_min_max_addition, 'проверок на сложение отрицательного и положительного числа, из них', counter, 'проверок - OK')


counter = 0
# сложение нуля и положительного числа
for i_zero_max_addition in range(1, quantity_input+1): # 5
	one_zero_with_positive_addition = 0
	two_zero_max_number_addition = random.randrange(0, max_positive_number)
	sum_zero_max_numbers_addition = one_zero_with_positive_addition + two_zero_max_number_addition

	stat_zero_positive_addition, res_zero_positive_addition = test_addition(one_zero_with_positive_addition, two_zero_max_number_addition)
	if res_zero_positive_addition == sum_zero_max_numbers_addition:
		counter += 1
	else:
		print('Число', zero_with_positive_addition, '+', 'число', two_zero_max_number_addition, '=', sum_zero_max_numbers_addition, '!= ответу webcalculator', res_zero_positive_addition)
print('Произведено', i_zero_max_addition, 'проверок на сложение нуля и положительного числа, из них', counter, 'проверок - OK')


counter = 0
# сложение нуля и отрицательного числа
for i_zero_min_addition in range(1, quantity_input+1): # 6
	one_zero_with_negative_addition = 0
	two_zero_min_number_addition = random.randrange(min_negative_number, 0)
	sum_zero_min_numbers_addition = one_zero_with_positive_addition + two_zero_min_number_addition

	stat_zero_positive_addition, res_zero_negative_addition = test_addition(one_zero_with_negative_addition, two_zero_min_number_addition)
	if res_zero_negative_addition == sum_zero_min_numbers_addition:
		counter += 1
	else:
		print('Число', one_zero_with_negative_addition, '+', 'число', two_zero_min_number_addition, '=', sum_zero_min_numbers_addition, '!= ответу webcalculator', res_zero_negative_addition)
print('Произведено', i_zero_min_addition, 'проверок на сложение нуля и отрицательного числа, из них', counter, 'проверок - OK')


counter = 0
# сложение положительного и нуля числа
for i_max_zero_addition in range(1, quantity_input+1): # 7
	one_max_zero_number_addition = random.randrange(0, max_positive_number)
	two_zero_max_number_addition = 0
	sum_zero_max_numbers_addition = one_max_zero_number_addition + two_zero_max_number_addition

	stat_max_zero_positive_addition, res_max_zero_positive_addition = test_addition(one_zero_with_negative_addition, one_max_zero_number_addition)
	if res_max_zero_positive_addition == one_max_zero_number_addition:
		counter += 1
	else:
		print('Число', one_max_zero_number_addition, '+', 'число', two_zero_max_number_addition, '=', sum_zero_max_numbers_addition, '!= ответу webcalculator', res_max_zero_positive_addition)
print('Произведено', i_max_zero_addition, 'проверок на сложение положительного и нуля числа,  из них', counter, 'проверок - OK')


counter = 0
# сложение отрицательного и нуля числа
for i_min_zero_addition in range(1, quantity_input+1): # 8
	one_min_zero_number_addition = random.randrange(min_negative_number, 0)
	two_zero_min_number_addition = 0
	sum_zero_min_numbers_addition = one_min_zero_number_addition + two_zero_min_number_addition

	stat_min_zero_positive_addition, res_min_zero_positive_addition = test_addition(two_zero_min_number_addition, one_min_zero_number_addition)
	if res_min_zero_positive_addition == one_min_zero_number_addition:
		counter += 1
	else:
		print('Число', one_min_zero_number_addition, '+', 'число', two_zero_min_number_addition, '=', sum_zero_min_numbers_addition, '!= ответу webcalculator', res_min_zero_positive_addition)
print('Произведено', i_min_zero_addition, 'проверок на сложение отрицательного и нуля числа,  из них', counter, 'проверок - OK')

print() # перенос строки для читабельности

def test_multiplication(a, b): # умножение
	multiplication_test = requests.post(addres_multiplication, json={'x':a, 'y':b})
	status_code_multiplication = multiplication_test.json()['statusCode']	# Получаем информацию statusCode
	result_multiplication = multiplication_test.json()['result'] 			# Получаем информацию результата вычислений калькулятора
	return status_code_multiplication, result_multiplication


counter = 0
# умножение отрицательных чисел
for i_min_multiplication in range(1, quantity_input+1): # 1
	one_min_number_multiplication = random.randrange(min_negative_number, 0)
	two_min_number_multiplication = random.randrange(min_negative_number, 0)
	min_numbers_multiplication = one_min_number_multiplication * two_min_number_multiplication

	stat_negative_multiplication, res_negative_multiplication = test_multiplication(one_min_number_multiplication, two_min_number_multiplication)
	if res_negative_multiplication == min_numbers_multiplication:
		counter += 1
	else:
		print('Число', one_min_number_multiplication, '*', 'число', two_min_number_multiplication, '=', min_numbers_multiplication, '!= ответу webcalculator', res_negative_multiplication)
print('Произведено', i_min_multiplication, 'проверок на умножение отрицательных чисел, из них', counter, 'проверок - OK')

counter = 0
# умножение положительных чисел
for i_max_multiplication in range(1, quantity_input+1): # 2
	one_max_number_multiplication = random.randrange(0, max_positive_number)
	two_max_number_multiplication = random.randrange(0, max_positive_number)
	max_numbers_multiplication = one_max_number_multiplication * two_max_number_multiplication

	stat_positive_multiplication, res_positive_multiplication = test_multiplication(one_max_number_multiplication, two_max_number_multiplication)
	if res_positive_multiplication == max_numbers_multiplication:
		counter += 1
	else:
		print('Число', one_max_number_multiplication, '*', 'число', two_max_number_multiplication, '=', max_numbers_multiplication, '!= ответу webcalculator', res_positive_multiplication)
print('Произведено', i_max_multiplication, 'проверок на умножение положительных чисел, из них', counter, 'проверок - OK')

counter = 0
# умножение положительного и отрицательного чисел
for i_max_min_multiplication in range(1, quantity_input+1): # 3
	one_max_number_multiplication = random.randrange(0, max_positive_number)
	two_min_number_multiplication = random.randrange(min_negative_number, 0)
	max_min_numbers_multiplication = one_max_number_multiplication * two_min_number_multiplication

	stat_positive_negative_multiplication, res_positive_negative_multiplication = test_multiplication(one_max_number_multiplication, two_min_number_multiplication)
	if res_positive_negative_multiplication == max_min_numbers_multiplication:
		counter += 1
	else:
		print('Число', one_max_number_multiplication, '*', 'число', two_min_number_multiplication, '=', max_min_numbers_multiplication, '!= ответу webcalculator', res_positive_negative_multiplication)
print('Произведено', i_max_min_multiplication, 'проверок на умножение положительного и отрицательного чисел, из них', counter, 'проверок - OK')


counter = 0
# умножение отрицательного и положительного чисел
for i_min_max_multiplication in range(1, quantity_input+1): # 4
	one_min_number_multiplication = random.randrange(min_negative_number, 0)
	two_max_number_multiplication = random.randrange(0, max_positive_number)
	min_max_numbers_multiplication = one_min_number_multiplication * two_max_number_multiplication

	stat_negative_positive_multiplication, res_negative_positive_multiplication = test_multiplication(one_min_number_multiplication, two_max_number_multiplication)
	if res_negative_positive_multiplication == min_max_numbers_multiplication:
		counter += 1
	else:
		print('Число', one_min_number_multiplication, '*', 'число', two_max_number_multiplication, '=', min_max_numbers_multiplication, '!= ответу webcalculator', res_negative_positive_multiplication)
print('Произведено', i_min_max_multiplication, 'проверок на умножение отрицательного и положительного чисел, из них', counter, 'проверок - OK')


counter = 0
# умножение нуля и положительного числа
for i_zero_max_multiplication in range(1, quantity_input+1): # 5
	one_zero_with_positive_multiplication = 0
	two_zero_max_number_multiplication = random.randrange(0, max_positive_number)
	zero_max_numbers_multiplication = one_zero_with_positive_multiplication * two_max_number_multiplication
	
	stat_zero_positive_multiplication, res_zero_positive_multiplication = test_multiplication(one_zero_with_positive_multiplication, two_zero_max_number_multiplication)
	if res_zero_positive_multiplication == zero_max_numbers_multiplication:
		counter += 1
	else:
		print('Число', one_zero_with_positive_multiplication, '*', 'число', two_zero_max_number_multiplication, '=', zero_max_numbers_multiplication, '!= ответу webcalculator', res_zero_positive_multiplication)
print('Произведено', i_zero_max_multiplication, 'проверок на умножение нуля и положительного числа, из них', counter, 'проверок - OK')


counter = 0
# умножение нуля и отрицательного числа
for i_zero_min_multiplication in range(1, quantity_input+1): # 6
	one_zero_with_negative_multiplication = 0
	two_zero_min_number_multiplication = random.randrange(min_negative_number, 0)
	zero_min_numbers_multiplication = one_zero_with_negative_multiplication * two_zero_min_number_multiplication
	
	stat_zero_negative_multiplication, res_zero_negative_multiplication = test_multiplication(one_zero_with_negative_multiplication, two_zero_min_number_multiplication)
	if res_zero_negative_multiplication == zero_min_numbers_multiplication:
		counter += 1
	else:
		print('Число', one_zero_with_negative_multiplication, '*', 'число', two_zero_min_number_multiplication, '=', zero_min_numbers_multiplication, '!= ответу webcalculator', res_zero_negative_multiplication)
print('Произведено', i_zero_min_multiplication, 'проверок на умножение нуля и отрицательного числа, из них', counter, 'проверок - OK')


counter = 0
# умножение положительного и 0 числа
for i_max_zero_multiplication in range(1, quantity_input+1): # 7
	one_positive_zero_number_multiplication = random.randrange(0, max_positive_number)
	two_positive_with_zero_multiplication = 0
	max_zero_numbers_multiplication = one_positive_zero_number_multiplication * two_positive_with_zero_multiplication
	
	stat_posititve_zero_multiplication, res_positive_zero_multiplication = test_multiplication(one_positive_zero_number_multiplication, two_positive_with_zero_multiplication)
	if res_positive_zero_multiplication == max_zero_numbers_multiplication:
		counter += 1
	else:
		print('Число', one_positive_zero_number_multiplication, '*', 'число', two_positive_with_zero_multiplication, '=', max_zero_numbers_multiplication, '!= ответу webcalculator', res_positive_zero_multiplication)
print('Произведено', i_max_zero_multiplication, 'проверок на умножение положительного и 0 числа, из них', counter, 'проверок - OK')


counter = 0
# умножение отрицательного и нуля числа
for i_min_zero_multiplication in range(1, quantity_input+1): # 8
	one_negative_zero_number_multiplication = random.randrange(min_negative_number, 0)
	two_negative_with_zero_multiplication = 0
	min_zero_numbers_multiplication = one_negative_zero_number_multiplication * two_negative_with_zero_multiplication
	
	stat_negative_zero_multiplication, res_negative_zero_multiplication = test_multiplication(one_negative_zero_number_multiplication, two_negative_with_zero_multiplication)
	if res_negative_zero_multiplication == min_zero_numbers_multiplication:
		counter += 1
	else:
		print('Число', one_negative_zero_number_multiplication, '*', 'число', two_negative_with_zero_multiplication, '=', min_zero_numbers_multiplication, '!= ответу webcalculator', res_negative_zero_multiplication)
print('Произведено', i_min_zero_multiplication, 'проверок на умножение отрицательного и нуля числа, из них', counter, 'проверок - OK')

print() # перенос строки для читабельности

def test_division(a, b): # деление
	division_test = requests.post(addres_division, json={'x':a, 'y':b})

	status_code_division = division_test.json()['statusCode']	# Получаем информацию statusCode
	if status_code_division == 0:
		result_division = division_test.json()['result'] 		# Получаем информацию результата вычислений калькулятора
		return status_code_division, result_division
	else:
		statusMessage_division = division_test.json()['statusMessage'] # Информаця в случае ошибки
		return status_code_division, statusMessage_division
	

counter = 0
# деление отрицательных чисел
for i_min_division in range(1, quantity_input+1): # 1 		 			
	one_min_number_division = random.randrange(min_negative_number, 0)
	two_min_number_division = random.randrange(min_negative_number, 0)
	sum_min_numbers_division = one_min_number_division // two_min_number_division

	stat_negative_divison, res_negative_division = test_division(one_min_number_division, two_min_number_division)
	if res_negative_division == sum_min_numbers_division:
		counter += 1
	else:
		print('Число', one_min_number_addition, ':', 'число', two_min_number_addition, '=', sum_min_numbers_division, '!= ответу webcalculator', res_negative_division)
print('Произведено', i_min_division, 'проверок на деление отрицательных чисел, из них', counter, 'проверок - OK')


counter = 0
# деление положительных чисел
for i_max_division in range(1, quantity_input+1): # 2 			
	one_max_number_division = random.randrange(0, max_positive_number)
	two_max_number_division = random.randrange(0, max_positive_number)
	max_numbers_division = one_max_number_division // two_max_number_division

	stat_posititve_divison, res_positive_division = test_division(one_max_number_division, two_max_number_division)
	if res_positive_division == max_numbers_division:
		counter += 1
	else:
		print('Число', one_max_number_addition, ':', 'число', two_max_number_addition, '=', max_numbers_division, '!= ответу webcalculator', res_positive_division)

print('Произведено', i_max_division, 'проверок на деление положительных чисел, из них', counter, 'проверок - OK')


counter = 0
# деление положительного и отрицательного числа
for i_max_min_division in range(1, quantity_input+1): # 3			
	one_max_min_number_division = random.randrange(0, max_positive_number)
	two_min_max_number_division = random.randrange(min_negative_number, 0)
	max_min_numbers_division = one_max_min_number_division // two_min_max_number_division

	stat_posititve_negative_divison, res_positive_negative_division = test_division(one_max_min_number_division, two_min_max_number_division)
	if res_positive_negative_division == max_min_numbers_division:
		counter += 1
	else:
		print('Число', one_max_min_number_division, ':', 'число', two_min_max_number_division, '=', max_min_numbers_division, '!= ответу webcalculator', res_positive_negative_division)
print('Произведено', i_max_min_division, 'проверок на деление положительного и отрицательного числа, из них', counter, 'проверок - OK')


counter = 0
# деление отрицательного и положительного числа
for i_max_min_division in range(1, quantity_input+1): # 4			
	one_min_max_number_division = random.randrange(min_negative_number, 0)
	two_max_min_number_division = random.randrange(0, max_positive_number)
	min_max_numbers_division = one_min_max_number_division // two_max_min_number_division

	stat_negative_positive_divison, res_negative_positive_division = test_division(one_min_max_number_division, two_max_min_number_division)
	if res_negative_positive_division == min_max_numbers_division:
		counter += 1
	else:
		print('Число', one_min_max_number_division, ':', 'число', two_max_min_number_division, '=', min_max_numbers_division, '!= ответу webcalculator', res_negative_positive_division)

print('Произведено', i_max_min_division, 'проверок на деление отрицательного и положительного числа, из них', counter, 'проверок - OK')

counter = 0
# деление нуля и положительного числа
for i_zero_max_division in range(1, quantity_input+1): # 5			
	one_zero_with_positive_division = 0
	two_zero_max_number_division = random.randrange(0, max_positive_number)
	zero_max_numbers_division = one_zero_with_positive_division // two_zero_max_number_division

	stat_zero_max_divison, res_zero_max_division = test_division(one_zero_with_positive_division, two_zero_max_number_division)
	if res_zero_max_division == zero_max_numbers_division:
		counter += 1
	else:
		print(one_zero_with_positive_division, ':', two_zero_max_number_division, '=', zero_max_numbers_division, '!= ответу webcalculator', res_negative_positive_division)
print('Произведено', i_zero_max_division, 'проверок на деление нуля и положительного числа, из них', counter, 'проверок - OK')


counter = 0
# деление нуля и отрицательного числа
for i_zero_min_division in range(1, quantity_input+1): # 6	
	one_zero_with_negative_division = 0	
	two_min_zero_number_division = random.randrange(min_negative_number, 0)
	zero_min_numbers_division = one_zero_with_negative_division // two_min_zero_number_division

	stat_zero_min_division, res_zero_min_division = test_division(one_zero_with_negative_division, two_min_zero_number_division)
	if res_zero_min_division == zero_min_numbers_division:
		counter += 1
	else:
		print(one_zero_with_negative_division, ':', two_min_zero_number_division, '=', zero_min_numbers_division, '!= ответу webcalculator', res_zero_min_division)
print('Произведено', i_zero_min_division, 'проверок на деление нуля и отрицательного числа, из них', counter, 'проверок - OK')


counter = 0
# деление отрицательного и нуля
for i_min_zero_division in range(1, quantity_input+1): # 7
	one_min_zero_number_division = random.randrange(min_negative_number, 0)
	two_zero_with_negative_division = 0

	stat_negative_zero_divison, res_negative_zero_division = test_division(one_min_zero_number_division, two_zero_with_negative_division)
	if stat_negative_zero_divison == 0:
		counter += 1
	else:
		print('Статус', stat_negative_zero_divison, res_negative_zero_division, 'деление на 0')
print('Произведено', i_min_zero_division, 'проверок на деление отрицательного и нуля, из них', counter, 'проверок - OK')


counter = 0
# деление нуля и положительного числа
for i_max_zero_division in range(1, quantity_input+1): # 8
	one_max_zero_number_division = random.randrange(0, max_positive_number)
	two_zero_with_negative_division = 0

	stat_positive_zero_divison, res_posititve_zero_division = test_division(one_max_zero_number_division, two_zero_with_negative_division)
	if stat_positive_zero_divison == 0:
		counter += 1
	else:
		print('Статус', stat_positive_zero_divison, res_posititve_zero_division, ',деление на 0')
print('Произведено', i_max_zero_division, 'проверок на деление нуля и положительного числа, из них', counter, 'проверок - OK')

counter = 0
# деление по модулю числа а и b
for i_abs_1_division in range(1, quantity_input+1): # 9
	one_max_abs_division = abs(random.randrange(0, max_positive_number))
	two_min_abs_division = abs(random.randrange(min_negative_number, 0))
	if one_max_abs_division > two_min_abs_division:
		max_min_abs_numbers_division_1 = abs(one_max_abs_division) // abs(two_min_abs_division)
		stat_negative_zero_divison_1, res_negative_zero_division_1 = test_division(one_max_abs_division, two_min_abs_division)
		if res_negative_zero_division_1 == max_min_abs_numbers_division_1:
			counter += 1
		else:
			print('Число', one_max_abs_division, ':', 'число', two_min_abs_division, '=', max_min_abs_numbers_division_1, '!= ответу webcalculator', res_negative_zero_division_1)
	else:
		max_min_abs_numbers_division_2 = abs(two_min_abs_division) // abs(one_max_abs_division)
		stat_negative_zero_divison_2, res_negative_zero_division_2 = test_division(two_min_abs_division, one_max_abs_division)
		if res_negative_zero_division_2 == max_min_abs_numbers_division_2:
			counter += 1
		else:
			print('Число', one_max_abs_division, ':', 'число', two_min_abs_division, '=', max_min_abs_numbers_division_2, '!= ответу webcalculator', res_negative_zero_division_2)

print('Произведено', i_abs_1_division, 'проверок на деление по модулю числа а и b, из них', counter, 'проверок - OK')


counter = 0
# деление по модулю числа а и b
for i_abs_2_division in range(1, quantity_input+1): # 10
	one_max_abs_division_1 = abs(random.randrange(0, max_positive_number))
	two_min_abs_division_1 = abs(random.randrange(min_negative_number, 0))
	if one_max_abs_division_1 < two_min_abs_division_1:
		max_min_abs_numbers_division_3 = abs(two_min_abs_division_1) // abs(one_max_abs_division_1)
		stat_negative_zero_divison_3, res_negative_zero_division_3 = test_division(two_min_abs_division_1, one_max_abs_division_1)
		if res_negative_zero_division_3 == max_min_abs_numbers_division_3:
			counter += 1
		else:
			print('Число', two_min_abs_division_1, ':', 'число', one_max_abs_division_1, '=', max_min_abs_numbers_division_3, '!= ответу webcalculator', res_negative_zero_division_3)
	else:
		max_min_abs_numbers_division_4 = abs(one_max_abs_division_1) // abs(two_min_abs_division_1)
		stat_negative_zero_divison_4, res_negative_zero_division_4 = test_division(one_max_abs_division_1, two_min_abs_division_1)
		if res_negative_zero_division_4 == max_min_abs_numbers_division_4:
			counter += 1
		else:
			print('Число', one_max_abs_division_1, ':', 'число', two_min_abs_division_1, '=', max_min_abs_numbers_division_4, '!= ответу webcalculator', res_negative_zero_division_4)
		
print('Произведено', i_abs_2_division, 'проверок на наделение по модулю числа а и b, из них', counter, 'проверок - OK')

print() # перенос строки для читабельности

def test_remainder(a, b): # остаток от деления
	remainder_test = requests.post(addres_remainder, json={'x':a, 'y':b})
	status_code_remainder = remainder_test.json()['statusCode']	# Получаем информацию statusCode
	if status_code_remainder == 0:
		result_remainder = remainder_test.json()['result'] 			# Получаем информацию результата вычислений калькулятора
		return status_code_remainder, result_remainder
	else:
		statusMessage_remainder = remainder_test.json()['statusMessage']
		return status_code_remainder, statusMessage_remainder


counter = 0
# остаток минимальных чисел
for i_min_remainder in range(1, quantity_input+1): # 1
	one_min_number_remainder = random.randrange(min_negative_number, 0)
	two_min_number_remainder = random.randrange(min_negative_number, 0)
	min_numbers_remainder = one_min_number_remainder % two_min_number_remainder

	stat_negative_remainder, res_negative_remainder = test_remainder(one_min_number_remainder, two_min_number_remainder)
	if res_negative_remainder == min_numbers_remainder:
		counter += 1
	else:
		print('Число', one_min_number_remainder, ':', 'число', two_min_number_remainder, '=', min_numbers_remainder, '!= ответу webcalculator', res_negative_remainder)
print('Произведено', i_min_remainder, 'проверок на остаток минимальных чисел, из них', counter, 'проверок - OK')


counter = 0
# остаток максимальных чисел
for i_max_remainder in range(1, quantity_input+1): # 2
	one_max_number_remainder = random.randrange(0, max_positive_number)
	two_max_number_remainder = random.randrange(0, max_positive_number)
	max_numbers_remainder = one_max_number_remainder % two_max_number_remainder

	stat_posititve_remainder, res_posititve_remainder = test_remainder(one_max_number_remainder, two_max_number_remainder)
	if res_posititve_remainder == max_numbers_remainder:
		counter += 1
	else:
		print('Число', one_max_number_remainder, ':', 'число', two_max_number_remainder, '=', max_numbers_remainder, '!= ответу webcalculator', res_posititve_remainder)
print('Произведено', i_max_remainder, 'проверок на остаток максимальных чисел, из них', counter, 'проверок - OK')


counter = 0
# остаток максимального и минимального числа
for i_max_min_remainder in range(1, quantity_input+1): # 3
	one_max_min_number_remainder = random.randrange(0, max_positive_number)
	two_min_max_number_remainder = random.randrange(min_negative_number, 0)
	max_min_numbers_remainder = one_max_min_number_remainder % two_min_max_number_remainder

	stat_posititve_negative_remainder, res_posititve_negative_remainder = test_remainder(one_max_min_number_remainder, two_min_max_number_remainder)
	if res_posititve_negative_remainder == max_min_numbers_remainder:
		counter += 1
	else:
		print('Число', one_max_min_number_remainder, ':', 'число', two_min_max_number_remainder, '=', sum_max_min_numbers_remainder, '!= ответу webcalculator', res_posititve_negative_remainder)
print('Произведено', i_max_min_remainder, 'проверок на остаток максимального и минимального числа, из них', counter, 'проверок - OK')


counter = 0
# остаток минимального и максимального числа
for i_min_max_remainder in range(1, quantity_input+1): # 4
	one_min_max_number_remainder = random.randrange(min_negative_number, 0)
	two_max_min_number_remainder = random.randrange(0, max_positive_number)
	min_max_numbers_remainder = one_min_max_number_remainder % two_max_min_number_remainder

	stat_negative_positive_remainder, res_negative_positive_remainder = test_remainder(one_min_max_number_remainder, two_max_min_number_remainder)
	if res_negative_positive_remainder == min_max_numbers_remainder:
		counter += 1
	else:
		print('Число', one_min_max_number_remainder, ':', 'число', two_max_min_number_remainder, '=', min_max_numbers_remainder, '!= ответу webcalculator', res_negative_positive_remainder)
print('Произведено', i_min_max_remainder, 'проверок на остаток минимального и максимального числа, из них', counter, 'проверок - OK')


counter = 0
# остаток нуля и максимального числа
for i_zero_max_remainder in range(1, quantity_input+1): # 5
	one_zero_with_positive_remainder = 0
	two_max_number_remainder = random.randrange(0, max_positive_number)
	zero_max_numbers_remainder = one_zero_with_positive_remainder % two_max_number_remainder

	stat_zero_posititve_remainder, res_zero_posititve_remainder = test_remainder(one_zero_with_positive_remainder, two_max_number_remainder)
	if res_zero_posititve_remainder == zero_max_numbers_remainder:
		counter += 1
	else:
		print('Число', one_zero_with_positive_remainder, ':', 'число', two_max_number_remainder, '=', zero_max_numbers_remainder, '!= ответу webcalculator', res_zero_posititve_remainder)
print('Произведено', i_zero_max_remainder, 'проверок на остаток нуля и максимального числа, из них', counter, 'проверок - OK')


counter = 0
# остаток нуля и минимального числа
for i_zero_min_remainder in range(1, quantity_input+1): # 6
	one_zero_with_negative_remainder = 0
	two_min_number_remainder = random.randrange(min_negative_number, 0)
	zero_min_numbers_remainder = one_zero_with_negative_remainder % two_min_number_remainder

	stat_zero_negative_remainder, res_zero_negative_remainder = test_remainder(one_zero_with_negative_remainder, two_min_number_remainder)
	if res_zero_negative_remainder == zero_min_numbers_remainder:
		counter += 1
	else:
		print('Число', one_zero_with_negative_remainder, ':', 'число', two_min_number_remainder, '=', zero_min_numbers_remainder, '!= ответу webcalculator', res_zero_negative_remainder)
print('Произведено', i_zero_min_remainder, 'проверок на остаток нуля и минимального числа, из них', counter, 'проверок - OK')


counter = 0
# остаток минимального числа и нуля
for i_min_zero_remainder in range(1, quantity_input+1): # 7
	one_min_zero_number_remainder = random.randrange(min_negative_number, 0)
	two_zero_with_negative_remainder = 0

	stat_negative_zero_remainder, res_negative_zero_remainder = test_division(one_min_zero_number_remainder, two_zero_with_negative_remainder)
	if stat_negative_zero_remainder == 0:
		counter += 1
	else:
		print('Статус', stat_negative_zero_remainder, res_negative_zero_remainder, ',остаток от числа  0')
print('Произведено', i_min_zero_remainder, 'проверок на остаток минимального числа и нуля, из них', counter, 'проверок - OK')


counter = 0
# остаток максимального числа и нуля
for i_max_zero_remainder in range(1, quantity_input+1): # 7
	one_max_zero_number_remainder = random.randrange(0, max_positive_number)
	two_zero_with_posititve_remainder = 0

	stat_positive_zero_remainder, res_posititve_zero_remainder = test_division(one_max_zero_number_remainder, two_zero_with_posititve_remainder)
	if stat_negative_zero_remainder == 0:
		counter += 1
	else:
		print('Статус', stat_positive_zero_remainder, res_posititve_zero_remainder, ',остаток от числа  0')
print('Произведено', i_max_zero_remainder, 'проверок на остаток максимального числа и нуля, из них', counter, 'проверок - OK')

# Негативные тесты
print()

print('Проверка кодов ошибок')
print('Проверка 2 статуса')
def test_errors_key(): # не хватает ключей в теле запроса
	addition_test_error_key = requests.post(addres_addition, json={'x':312312})
	status_code_addition_key = addition_test_error_key.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_addition_key = addition_test_error_key.json()['statusMessage']  # Информаця в случае ошибки

	multiplication_test_error_key = requests.post(addres_multiplication, json={'x':312312})
	status_code_multiplication_key = multiplication_test_error_key.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_multiplication_key = multiplication_test_error_key.json()['statusMessage']  # Информаця в случае ошибки

	division_test_error_key = requests.post(addres_division, json={'x':312312})
	status_code_division_key = division_test_error_key.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_division_key = division_test_error_key.json()['statusMessage']  # Информаця в случае ошибки

	remainder_test_error_key = requests.post(addres_remainder, json={'x':312312})
	status_code_remainder_key = remainder_test_error_key.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_remainder_key = remainder_test_error_key.json()['statusMessage']  # Информаця в случае ошибки

	print('Сложение - статус', status_code_addition_key, statusMessage_addition_key)
	print('Умножение - статус', status_code_multiplication_key, statusMessage_status_code_multiplication_key)
	print('Деление - статус', status_code_division_key, statusMessage_status_code_division_key)
	print('Остаток от деления - статус', status_code_remainder_key, statusMessage_status_code_remainder_key)
test_errors_key()

print()

print('Проверка 3 статуса(float)')

def test_errors_float(): # Одно из значений не является целым числом
	addition_test_error_float = requests.post(addres_addition, json={'x':312312, 'y':2.5})
	status_code_addition_float = addition_test_error_float.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_addition_float = addition_test_error_float.json()['statusMessage']  # Информаця в случае ошибки

	multiplication_test_error_float = requests.post(addres_multiplication, json={'x':312312, 'y':2.5})
	status_code_multiplication_float = multiplication_test_error_float.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_multiplication_float = multiplication_test_error_float.json()['statusMessage']  # Информаця в случае ошибки

	division_test_error_float = requests.post(addres_division, json={'x':312312, 'y':2.5})
	status_code_division_float = division_test_error_float.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_division_float = division_test_error_float.json()['statusMessage']  # Информаця в случае ошибки

	remainder_test_error_float = requests.post(addres_remainder, json={'x':312312, 'y':2.5})
	status_code_remainder_float = remainder_test_error_float.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_remainder_float = remainder_test_error_float.json()['statusMessage']  # Информаця в случае ошибки

	print('Сложение - статус(float)', status_code_addition_float, statusMessage_addition_float)
	print('Умножение - статус(float)', status_code_multiplication_float, statusMessage_status_code_multiplication_float)
	print('Деление - статус(float)', status_code_division_float, statusMessage_status_code_division_float)
	print('Остаток от деления - статус(float)', status_code_remainder_float, statusMessage_status_code_remainder_float)
test_errors_float()

print()

print('Проверка 3 статуса(string)')

def test_errors_string(): # Превышен размер одного из значений
	addition_test_error_string = requests.post(addres_addition, json={'x':'dasdas', 'y':'dasdas'})
	status_code_addition_string = addition_test_error_string.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_addition_string = addition_test_error_string.json()['statusMessage']  # Информаця в случае ошибки

	multiplication_test_error_string = requests.post(addres_multiplication, json={'x':'dasdas', 'y':'dasdas'})
	status_code_multiplication_string = multiplication_test_error_string.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_multiplication_string = multiplication_test_error_string.json()['statusMessage']  # Информаця в случае ошибки

	division_test_error_string = requests.post(addres_division, json={'x':'dasdas', 'y':'dasdas'})
	status_code_division_string = division_test_error_string.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_division_string = division_test_error_string.json()['statusMessage']  # Информаця в случае ошибки

	remainder_test_error_string = requests.post(addres_remainder, json={'x':'dasdas', 'y':'dasdas'})
	status_code_remainder_string = remainder_test_error_string.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_remainder_string = remainder_test_error_string.json()['statusMessage']  # Информаця в случае ошибки

	print('Сложение - статус(string)', status_code_addition_string, statusMessage_addition_string)
	print('Умножение - статус(string)', status_code_multiplication_string, statusMessage_status_code_multiplication_string)
	print('Деление - статус(string)', status_code_division_string, statusMessage_status_code_division_string)
	print('Остаток от деления - статус(string)', status_code_remainder_string, statusMessage_status_code_remainder_string)
test_errors_string()

print()

print('Проверка 4 статуса максимального числа')

max_positive_number = 2147483647	# Максимальное разрешенное положительное число
min_negative_number = -2147483648	# Минимальное разрешенное отрицательное число

def test_errors_max(): # Неправильный формат тела запроса
	addition_test_error_max = requests.post(addres_addition, json={'x':2147483647 + 2, 'y':-2147483647})
	status_code_addition_max = addition_test_error_max.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_addition_max = addition_test_error_max.json()['statusMessage']  # Информаця в случае ошибки

	multiplication_test_error_max = requests.post(addres_multiplication, json={'x':2147483647 + 2, 'y':-2147483647})
	status_code_multiplication_max = multiplication_test_error_max.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_multiplication_max = multiplication_test_error_max.json()['statusMessage']  # Информаця в случае ошибки

	division_test_error_max = requests.post(addres_division, json={'x':2147483647 + 2, 'y':-2147483647})
	status_code_division_max = division_test_error_max.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_division_max = division_test_error_max.json()['statusMessage']  # Информаця в случае ошибки

	remainder_test_error_max = requests.post(addres_remainder, json={'x':2147483647 + 2, 'y':-2147483647})
	status_code_remainder_max = remainder_test_error_max.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_remainder_max = remainder_test_error_max.json()['statusMessage']  # Информаця в случае ошибки

	print('Сложение(максимального числа) - статус', status_code_addition_max, statusMessage_addition_max)
	print('Умножение(максимального числа) - статус', status_code_multiplication_max, statusMessage_status_code_multiplication_max)
	print('Деление(максимального числа) - статус', status_code_division_max, statusMessage_status_code_division_max)
	print('Остаток от деления(максимального числа) - статус', status_code_remainder_max, statusMessage_status_code_remainder_max)
test_errors_max()

print()

print('Проверка 4 статуса минимального числа')

def test_errors_min():
	addition_test_error_min = requests.post(addres_addition, json={'x':2147483647, 'y':-2147483647-2})
	status_code_addition_min = addition_test_error_min.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_addition_min = addition_test_error_min.json()['statusMessage']  # Информаця в случае ошибки

	multiplication_test_error_min = requests.post(addres_multiplication, json={'x':2147483647, 'y':-2147483647-2})
	status_code_multiplication_min = multiplication_test_error_min.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_multiplication_min = multiplication_test_error_min.json()['statusMessage']  # Информаця в случае ошибки

	division_test_error_min = requests.post(addres_division, json={'x':2147483647, 'y':-2147483647-2})
	status_code_division_min = division_test_error_min.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_division_min = division_test_error_min.json()['statusMessage']  # Информаця в случае ошибки

	remainder_test_error_min = requests.post(addres_remainder, json={'x':2147483647, 'y':-2147483647-2})
	status_code_remainder_min = remainder_test_error_min.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_remainder_min = remainder_test_error_min.json()['statusMessage']  # Информаця в случае ошибки

	print('Сложение(минимального числа) - статус', status_code_addition_min, statusMessage_addition_min)
	print('Умножение(минимального числа) - статус', status_code_multiplication_min, statusMessage_status_code_multiplication_min)
	print('Деление(минимального числа) - статус', status_code_division_min, statusMessage_status_code_division_min)
	print('Остаток от деления(минимального числа) - статус', status_code_remainder_min, statusMessage_status_code_remainder_min)
test_errors_max()

print()

print('Проверка 5 статуса')

def test_errors_format():
	addition_test_error_format = requests.post(addres_addition)
	status_code_addition_format = addition_test_error_format.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_addition_format = addition_test_error_format.json()['statusMessage']  # Информаця в случае ошибки

	multiplication_test_error_format = requests.post(addres_multiplication)
	status_code_multiplication_format = multiplication_test_error_format.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_multiplication_format = multiplication_test_error_format.json()['statusMessage']  # Информаця в случае ошибки

	division_test_error_format = requests.post(addres_division)
	status_code_division_format = division_test_error_format.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_division_format = division_test_error_format.json()['statusMessage']  # Информаця в случае ошибки

	remainder_test_error_format = requests.post(addres_remainder)
	status_code_remainder_format = remainder_test_error_format.json()['statusCode']	# Получаем информацию statusCode
	statusMessage_status_code_remainder_format = remainder_test_error_format.json()['statusMessage']  # Информаця в случае ошибки

	print('Сложение - статус', status_code_addition_format, statusMessage_addition_format)
	print('Умножение - статус', status_code_multiplication_format, statusMessage_status_code_multiplication_format)
	print('Деление - статус', status_code_division_format, statusMessage_status_code_division_format)
	print('Остаток от деления - статус', status_code_remainder_format, statusMessage_status_code_remainder_format)
test_errors_format()








	






	






