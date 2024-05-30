age = 40
new_age = age + 1
category = ['name', 'age', 'new_age', 'is_student', '']
new_category = ((': '.join(category)).title()).split(' ')
data = ['Tania', age, new_age, True]
str_data = list(map(str, data))
transfer = '\n' * len(data)
pre_result = [' '.join(x) for x in zip(new_category, str_data)]
result = [i + j for i, j in zip(pre_result, transfer)]
print(''.join(result))



