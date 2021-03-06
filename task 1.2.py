
"""
Сформувати функцію для обчислення цифрового кореню натурального числа. Цифровий корінь отримується наступним чином:
необхідно скласти всі цифри заданого числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір,
поки сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого числа.

Виконав Іваненко Андрій Вадимович
"""


""" У даному випадку для визначення функції доцільніше використати ітерації ніж рекурсію, оскільки функція визначена 
через рекурсію виконується довше та займає більше пам'яті за функцію визначену через ітерації. """


def digital_root1(digit_root):  # Функція обчислення цифрового кореню заданого числа (через ітерації)
    while len(str(digit_root)) > 1:  # Цикл буде виконуватись поки рядок від заданого числа має більше ніж 1 символ
        digit_sum = 0  # digit_sum - сума цифр заданого числа
        for i in str(digit_root):  # Знаходження суми всіх цифр числа
            digit_sum += int(i)
        digit_root = digit_sum
    return digit_root


def digital_root2(digit_root):  # Функція обчислення цифрового кореню заданого числа (через рекурсію)
    """ Якщо рядок, утворений від заданого числа, має більше ніж 1 символ, то знаходиться значення функції від суми
    першої цифри цього рядка та значення функції від зрізу [1:] рядка. У випадку, коли отримується число, що
    склаадається з одної цифри, то воно повертається. """
    if len(str(digit_root)) > 1:
        return digital_root2(int(str(digit_root)[0]) + int(digital_root2(str(digit_root)[1:])))
    else:
        return digit_root


answer = '1'
while answer == '1':

    while True:  # Введення натурального числа n, цифровий корінь якого буде обчислюватись
        try:
            n = int(input("Введіть натуральне число:"))
            if n > 0:
                break
            else:
                print("Вводьте правильні дані!")
        except ValueError:
            print("Вводьте правильні дані!")

    print(f"Його цифровий корінь (визначений через ітерації) дорівнює: {digital_root1(n)}.\n"
          f"Його цифровий корінь (визначений через рекурсію) дорівнює: {digital_root2(n)}.")

    answer = input("Введіть '1' для повторення:")
