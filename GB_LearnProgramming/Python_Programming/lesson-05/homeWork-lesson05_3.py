# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open(r'salaries.txt', 'r') as salaries:
    eof_marker = False
    employees = []
    mendicants = []
    employee = []
    for line in salaries
        for word in line.split():
            employee.append(word)
        if float(employee[1]) < 20000:
            mendicants.append(employee)
        employees.append(employee)

total_salary = float()
for unit in employees:
    total_salary += float(unit[1])
print(f'Среднемесячная зарплата сотрудников в списке: {total_salary / len(employees):.2f}')
print('Сотрудники с зарплатой ниже 20000:')
for unit in mendicants:
    print(f'{unit[0]}: {unit[1]}')
