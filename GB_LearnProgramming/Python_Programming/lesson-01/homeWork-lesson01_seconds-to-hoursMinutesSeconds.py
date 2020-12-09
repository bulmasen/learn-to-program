# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

timeInSeconds = float(input('Введите число секунд: '))

# Переводим секунды в полные минуты
timeInMinutes = timeInSeconds // 60
# Переводим минуты в полные часы
timeInHours = int(timeInMinutes // 60)
# Вычисляем оставшиеся минуты
remainingMinutes = int(timeInMinutes % 60)
# Вычисляем оставшиеся секунды
remainingSeconds = timeInSeconds % 60
# Печатаем результат
# print(f'Получается {timeInHours}:{remainingMinutes:02}:{remainingSeconds:05.2f}')
# Упс, по заданию другой формат:
print(f'Получается {timeInHours}:{remainingMinutes:02}:{round(remainingSeconds):02}')