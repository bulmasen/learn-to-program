# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open(r'salaries.txt', 'r') as salaries:
    employees = []
    non_rich = []
    for line in salaries:
        employee = []
        for word in line.split():
            employee.append(word)
        if float(employee[1]) < 20000:
            non_rich.append(employee)
        employees.append(employee)

total_salary = float()
for unit in employees:
    total_salary += float(unit[1])
print(f'Среднеарифметический доход сотрудников в списке: {total_salary / len(employees):,.2f}')
print('Сотрудники с доходом ниже 20,000.00:')
for unit in non_rich:
    print(f'{unit[0]}: {float(unit[1]):,.2f}')
