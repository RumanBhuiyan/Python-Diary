# built-in functions min max
numbers = [1,2,3,4,5,6]

print(min(numbers))
print(max(numbers))

print(min('a','e','b'))
print(max('a','e','b'))

# min max basis on a key
songs = [
    {"name":"dilbara", "view":"80k"},
    {"name":"despasito", "view":"10k"},
    {"name":"slow motion", "view":"50k"}
]

print(max(songs,key = lambda song : song['name']))
print(max(songs,key = lambda song : song['view']))


print(max(songs,key = lambda song : song['name'])['name'])
print(max(songs,key = lambda song : song['view'])['view'])