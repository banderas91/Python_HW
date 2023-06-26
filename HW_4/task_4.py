initial_amount = 0
total_amount = initial_amount
operations = []
operation_count = 0

def calculate_tax(amount):
    if total_amount + amount > 5000000:
        return amount * 0.1
    return 0

def deposit(amount):
    global total_amount, operation_count
    operation_count += 1
    if operation_count % 3 == 0:
        interest = amount * 0.03
        total_amount += amount - interest
        operations.append(f"Пополнение: +{amount} у.е., Списаны проценты: -{interest} у.е.")
    else:
        total_amount += amount
        operations.append(f"Пополнение: +{amount} у.е.")

def withdraw(amount):
    global total_amount, operation_count
    if amount <= total_amount:
        operation_count += 1
        if operation_count % 3 == 0:
            interest = amount * 0.03
            fee = max(30, min(amount * 0.015, 600))
            total_amount -= amount + fee - interest
            operations.append(f"Снятие: -{amount} у.е., комиссия: -{fee} у.е., Списаны проценты: -{interest} у.е.")
        else:
            fee = max(30, min(amount * 0.015, 600))
            total_amount -= amount + fee
            operations.append(f"Снятие: -{amount} у.е., комиссия: -{fee} у.е.")
    else:
        print("Ошибка: недостаточно средств для снятия")

def print_balance():
    print(f"Доступная сумма: {total_amount} у.е.")

def print_operations():
    print("Список операций:")
    for operation in operations:
        print(operation)

while True:
    print("Доступные действия: пополнить, снять, выйти")
    action = input("Введите действие: ")

    if action == "пополнить":
        amount = int(input("Введите сумму для пополнения (кратно 50): "))
        if amount % 50 == 0:
            deposit(amount)
            print_balance()
        else:
            print("Ошибка: сумма пополнения должна быть кратной 50")
    elif action == "снять":
        amount = int(input("Введите сумму для снятия (кратно 50): "))
        if amount % 50 == 0:
            withdraw(amount)
            print_balance()
        else:
            print("Ошибка: сумма снятия должна быть кратной 50")
    elif action == "выйти":
        print_operations()
        break
    else:
        print("Ошибка: недопустимое действие")
