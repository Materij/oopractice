from catcat import Cat, Wallet

b1 = Cat('Baron', 'Boy', 2)

print("b1.name =", b1.name)
print("b1.sex =", b1.sex)
print("b1.age =", b1.age)
print("b1.getName =", b1.getName())
print("b1.getSex =", b1.getSex())
print("b1.getAge =", b1.getAge())
print("\n")

b2 = Cat('Sam', 'Boy', 2)

print("b2.name =", b2.name)
print("b2.sex =", b2.sex)
print("b2.age =", b2.age)
print("b2.getName =", b2.getName())
print("b2.getSex =", b2.getSex())
print("b2.getAge =", b2.getAge())

client_1 = Wallet("«Ivan Petrov»", 50)

print("Customer:", client_1.client + ". Balance:", client_1.balance, end='')
print(" rub")
