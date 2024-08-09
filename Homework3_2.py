import re
from typing import Callable



def generator_numbers(text: str):
# регулярний вираз для знаходження дійсних чисел 
    pattern =  r"\b\d+\.\d+\b"
# знаходимо всі числа у тексті    
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)
# використовуємо Callable, щоб вказати що певний параметр є функцією.
def sum_profit(text:str, func: Callable):
    return sum(func(text))
# приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів, а також премії 43.45 "
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід:{total_income}")