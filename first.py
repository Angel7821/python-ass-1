print('Welcome to python')
# Number 1
numbers = [-4,-3-2,-1,0,2,4,6]
newnumber=[]

for number in numbers:
    if number <= 0:
        newnumber.append(number)
print(newnumber)
# Number 2
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened = []
for sublist in list_of_lists:
    for item in sublist:
        flattened.append(item)
print(flattened)
# Number 3
tuples_list=[
    (n,1,n,n**2,n**3,n**4,n**5)
    for n in range(11)
]
print(tuples_list)
# Number 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = []
for country in countries:
    # country_name, capital = country[0]  unpacking the tuple
    country_name, capital = country[0]
    result.append([country_name.upper(), country_name[:3].upper(), capital.upper()])
print(result)
# number 5
countries_two = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = []
for country_two in countries_two:
    country_two_name, capital_two = country_two[0]
    output.append({'country': country_two_name.upper(), 'city': capital_two.upper()})
print(output)
# Number 6
ames = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output=[]
for name in ames:
    firstname, lastname =name[0]
    output.append(firstname+ " "+ lastname)
print(output)