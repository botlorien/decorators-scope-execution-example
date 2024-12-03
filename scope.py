
def f1(a):
    print(a)
    print(b)


def f2(a):
    print(a)
    print(b)
    b = 9


def f3(a):
    global b
    print(a)
    print(b)
    b = 9

# variavel b não definida
try:
    f1(3)
except NameError as e:
    print(e)


# definindo b global
b = 6

# variavel b global
f1(3)

# tentar atribuir valor a b sem especificar que estamos nos referindo ao b global
# faz com que o interpretador entenda que b pertence ao escopo local da função
# como o print vem antes da atribuição local provoca erro de referencia
try:
    f2(3)
except UnboundLocalError as e:
    print(e)

# especificando que b é global, possibilidando referencia antes da atribuição
# já que b já existe no escopo global
f3(3)

from dis import dis

# inspecionando os bytecodes
print(dis(f1))
print(dis(f2))