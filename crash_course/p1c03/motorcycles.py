motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(f'The last motorcycle I owned was a {popped_motorcycle.title()}!')
first_owned_motorcycle = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned_motorcycle.title()}!')
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(f'\n\n\n\n The {too_expensive.title()} motorcycle was to expensive!')




