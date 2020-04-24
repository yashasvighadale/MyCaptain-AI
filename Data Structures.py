#Task1
oddlist = []
evenlist = []

for num in range(0,100):
    if num%2 == 0:
        evenlist.append(num)
    else:
        oddlist.append(num)
        
print("Even :", evenlist)        
print("Odd :", oddlist)

#Task 2
test_tuple = (16,25,36,49,64,81)
for i in range(0,len(test_tuple)):
    print(test_tuple[i])
    
#Task3
test_dict = {'firstName:': 'Yashasvi', 'LastName:' : 'Ghadale', 'Age:' : 19, 'Gender' : 'Female'}
test_dict
