
customer1 = {'name': 'aa'}
customer2 = {'name': 'bb'}
customer3 = {'name': 'cc'}

customer_list = [customer1, customer2, customer3]

customer_list2 = []
customer_list2.append(customer1)
customer_list2.append(customer2)
print(customer_list2)

for cust in customer_list:
    for key in cust.keys():
        print(f'{key} = {cust[key]}')

for cust in customer_list:
    print(cust.items())
    for k, v in cust.items():
        print(f'{k} <=> {v}')

'''
    zip() : index가 같은 아이템들을 zip해주는 함수
'''

key_list = ['정당', '선거구']
value_list = ['열린민주당', '비례대표']
zip_result = zip(key_list, value_list)
print(zip_result)
for val in zip_result:
    print(val)

dict_result = dict(zip(key_list, value_list))
print(dict_result)
