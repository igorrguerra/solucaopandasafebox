def dist(a, b):
    # distancia entre dois numeros de 4 digitos
    # para cada digito, o menor giro: subindo ou descendo (lock circular 0-9)
    total = 0
    for i in range(4):
        d = abs(int(a[i]) - int(b[i]))
        total += min(d, 10 - d)
    return total

def mst_cost(keys):
    # Arvore Geradora Minima entre as chaves usando Prim
    n = len(keys)
    if n <= 1:
        return 0
    INF = float('inf')
    in_tree = [False] * n      # se o no ja entrou na arvore
    min_edge = [INF] * n       # menor custo para conectar cada no
    min_edge[0] = 0
    total = 0
    for _ in range(n):
        # escolhe o no fora da arvore com menor custo de conexao
        u = -1
        best = INF
        for v in range(n):
            if not in_tree[v] and min_edge[v] < best:
                best = min_edge[v]
                u = v
        in_tree[u] = True
        total += best
        # atualiza os custos com base no novo no adicionado
        for v in range(n):
            if not in_tree[v]:
                d = dist(keys[u], keys[v])
                if d < min_edge[v]:
                    min_edge[v] = d
    return total

def main():
    # le a entrada e separa em pedaços
    tokens = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        tokens.extend(line.split())

    pos = 0
    T = int(tokens[pos]); pos += 1
    saida = []
    for _ in range(T):
        N = int(tokens[pos]); pos += 1
        keys = []
        for _ in range(N):
            keys.append(tokens[pos].zfill(4)); pos += 1  # garante 4 digitos com zeros a esquerda
        custo = mst_cost(keys)
        ligacao_inicial = min(dist("0000", k) for k in keys)  # 0000 entra como folha
        saida.append(str(custo + ligacao_inicial))
    print("\n".join(saida))

main()