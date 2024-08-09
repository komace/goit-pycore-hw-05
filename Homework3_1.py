def caching_fibonacci():
    # створюємо порожній словник для обчислень
    cache = {}  
    # створюємо внутрішню функцію            
    def fibonacci(n):       
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        # рекрусивно обчислюємо і додаємо результати у cache
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result
    return fibonacci
# приклад використання
fib = caching_fibonacci()
print(fib(10))
print(fib(55))