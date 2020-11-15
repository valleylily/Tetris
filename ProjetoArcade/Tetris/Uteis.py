def intersecao(conjuntoA, conjuntoB):
    inter = []
    for x in conjuntoA:
        for y in conjuntoB:
            if x == y:
                inter.append(x)
    return inter