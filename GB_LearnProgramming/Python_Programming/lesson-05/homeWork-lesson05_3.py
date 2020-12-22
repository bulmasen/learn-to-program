# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open(r'salaries.txt', 'r', encoding='utf-8') as salaries:
    employees = []
    non_rich = 'Сотрудники с доходом ниже 20,000.00:\n'
    total_salary = float()
    total_employees = 0
    for line in salaries:
        employee = []
        for word in line.split():
            employee.append(word)
        if float(employee[1]) < 20000:
            non_rich += f'{employee[0]}: {float(employee[1]):,.2f}\n'
        total_salary += float(employee[1])
        total_employees += 1

print(f'Среднеарифметический доход сотрудников в списке: {total_salary / total_employees:,.2f}')
print(non_rich)
