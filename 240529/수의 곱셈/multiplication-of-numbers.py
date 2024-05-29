import itertools

def find_highest_priority_number(a, b, c):

    numbers = [a, b, c]
    products = set()
    
    for r in range(1, 4):  
        for combo in itertools.combinations(numbers, r):
            product = 1
            for num in combo:
                product *= num
            products.add(product)
    

    odd_numbers = []
    even_numbers = []
    
    for num in products:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
            
    if odd_numbers:
        return max(odd_numbers)
    else:
        return max(even_numbers)

a, b, c = map(int, input().split())

print(find_highest_priority_number(a, b, c))