def input_data():
    num1 = input("Введіть перше число: ").strip()
    try:
        float(num1)
    except ValueError:
        print("Некоректний ввід числа")
        return None, None, None

    operat = input("Введіть оператор (+, -, :, *): ").strip()
    if operat.isalnum():
        print("Некоректний ввід оператора")

    num2 = input("Введіть друге число: ").strip()
    try:
        float(num2)
    except ValueError:
        print("Некоректний ввід числа")
        return None, None, None

    verification = input(f"Ви хочете обчислити {num1} {operat} {num2}?"
                         " (так/ні) ").strip().lower()
    if verification == "так":
        return num1, num2, operat
    elif verification == "ні":
        num1, num2, operat = input_data()
    else:
        print("Некоректний ввід")
        return None, None, None

num1, num2, operat = input_data()
if num1:
    if operat == "+":
        print(f"{num1} {operat} {num2} = {float(num1) + float(num2)}")
    elif operat == "-":
        print(f"{num1} {operat} {num2} = {float(num1) - float(num2)}")
    elif operat == ":":
        if int(num2) == 0:
            print("Не можна ділити на 0")
        else:
            print(f"{num1} {operat} {num2} = {float(num1) / float(num2)}")
    elif operat == "*":
        print(f"{num1} {operat} {num2} = {float(num1) * float(num2)}")
    else:
        print("Невідома операція")
