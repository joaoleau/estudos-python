nums = [1,2,3]
n_iterator = iter(nums)

print(next(n_iterator)) #1
print(next(n_iterator)) #2
print(next(n_iterator)) #3
# next(n_iterator) #Retorna uma exceção "StopIteration" pois não tem um proximo

#Laço For
while True:
    try:
        item = next(n_iterator)
        print(item)
    except StopIteration:
        break


class Contagem:
    def __init__(self, max: float = 0) -> None:
        self.max = max
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration


contagens = Contagem(10)
for c in contagens:
    print(c)
