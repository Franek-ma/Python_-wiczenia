l = lambda x,y: x + y

print(l(50,70))

num = [5,9,13,27,45]

lam = lambda x: x / 2
lam2 = lambda x: x % 2

def lambd(lam,nums):
    results = []
    for item in nums:
        new_num = lam(item)
        results.append(new_num)

    return results

print(lambd(lam,num))

#funkcja, która bierze 2 argumenty lambda i lista stringów.Ta funkcja zwraca pierwsze litery

def get_first_letters(lambda_func, string_list):
    return [lambda_func(word) for word in string_list]

string_list = ["Franek","Python","Django"]
lambda_func = lambda x: x[0]
results = get_first_letters(lambda_func, string_list)
print(results)

