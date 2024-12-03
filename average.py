def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager


if __name__ == '__main__':
    # Closure
    avg = make_averager()

    # com closures é possivel extender o limite da existencia de uma variavel para além
    # do escopo local como pode ser observado no resulta abaixo
    # a variavel series continua existindo e registrando dados
    # mesmo após a chamada da função avg
    print(avg(10))
    print(avg(11))
    print(avg(15))

    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__)
    print(avg.__closure__[0].cell_contents)

