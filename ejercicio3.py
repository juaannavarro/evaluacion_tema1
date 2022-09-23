def lista_1(valor_inicio,valor_fin,incremento):
    if valor_inicio >= valor_fin:
        print()
        return
    print(list(range(valor_inicio,valor_inicio+incremento,incremento)), end=' ')
    nuevo_valor = valor_inicio + incremento
    lista_1(nuevo_valor, valor_fin, incremento)
