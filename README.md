# Panda Land Safe Box — p1235

Solução para o problema **p1235** do Online Judge, desenvolvido como trabalho avaliativo da disciplina de Grafos, dirigida pelo professor Ricardo Carubbi.

---

## Descrição do Problema

Os cofres da Panda Land usavam um cadeado antigo de **4 dígitos** (cada dígito vai de 0 a 9 e é circular: depois do 9 volta ao 0, e antes do 0 vai pro 9). Como existiam só 10000 combinações possíveis, qualquer um conseguia abrir testando todas — e vários cofres foram roubados.

Para dificultar, foi criado um cadeado novo com **múltiplas chaves**. Agora o cofre só abre quando **todas as N chaves** são destravadas, e da forma mais econômica possível. O funcionamento é:

- O cadeado começa em `0000`.
- Para destravar uma chave, você gira os dígitos até o número dela e aperta **UNLOCK**. Cada giro de um dígito conta como **1 rolagem**.
- Um botão mágico **JUMP** teleporta os dígitos para qualquer chave **já destravada**, sem custo nenhum.
- O cofre só abre se todas as chaves forem destravadas usando o **mínimo total de rolagens** (excluindo os JUMPs).
- Se passar do mínimo, o cadeado reseta tudo e a tentativa falha.

O objetivo do programa é, dadas as chaves, calcular o **número mínimo de rolagens** necessário para destravar o cofre.

### Por que o JUMP muda tudo?

Sem o JUMP, você teria que rolar de uma chave direto para a outra, em sequência. Com ele, depois de destravar algumas chaves, você pode "voltar" de graça para a chave já destravada que estiver mais perto da próxima que você quer abrir. Isso permite escolher sempre o caminho mais curto.

---

## Modelagem

O problema foi modelado como um **grafo completo, não-direcionado e ponderado**:

- **Nós:** as N chaves + o ponto de partida `0000`
- **Arestas:** existem entre todo par de nós, com peso igual à distância de rolagem
- **Distância entre dois números:** soma, dígito a dígito, de `min(|a-b|, 10-|a-b|)` (por ser circular, o dígito pode girar para cima ou para baixo — vale o menor caminho)

Como o JUMP permite mover-se de graça entre chaves já destravadas, cada nova chave paga apenas o custo até a chave mais próxima já disponível. Esse é exatamente o comportamento de uma **Árvore Geradora Mínima (MST)**: conectar todos os nós com o menor custo total, ligando cada novo nó ao vizinho mais barato.

### Detalhe especial: o nó 0000

O `0000` não é uma chave — é só o ponto de partida. Depois que você sai dele, não dá pra voltar via JUMP (ele nunca é "destravado"). Por isso ele entra na árvore como uma **folha**, ligado a exatamente uma chave.

**Fórmula final:**

```
Resposta = MST entre as chaves + menor distância de 0000 até alguma chave
```

---

## Algoritmo de Prim

Para construir a MST foi usado o **algoritmo de Prim**, com complexidade **O(N²)** por caso de teste — eficiente para N ≤ 500.

### Função no código:

```python
def mst_cost(keys):
    n = len(keys)
    if n <= 1:
        return 0
    INF = float('inf')
    in_tree = [False] * n      # controla quem já está na árvore
    min_edge = [INF] * n       # menor custo para conectar cada nó
    min_edge[0] = 0
    total = 0
    for _ in range(n):

        # PASSO 1 — ESCOLHER
        # Acha o nó fora da árvore com menor custo de conexão
        u = -1
        best = INF
        for v in range(n):
            if not in_tree[v] and min_edge[v] < best:
                best = min_edge[v]
                u = v

        # PASSO 2 — ADICIONAR
        # Insere esse nó na árvore e soma o custo ao total
        in_tree[u] = True
        total += best

        # PASSO 3 — ATUALIZAR
        # Verifica se pelo novo nó algum vizinho fica mais barato
        for v in range(n):
            if not in_tree[v]:
                d = dist(keys[u], keys[v])
                if d < min_edge[v]:
                    min_edge[v] = d

    return total
```

### Explicação dos 3 passos:

**Passo 1 — ESCOLHER:** percorre todos os nós que ainda não estão na árvore e escolhe o de menor valor em `min_edge`, ou seja, o mais barato de conectar à árvore atual.

**Passo 2 — ADICIONAR:** marca o nó escolhido como parte da árvore (`in_tree[u] = True`) e soma o custo dessa conexão ao total de rolagens.

**Passo 3 — ATUALIZAR:** para cada nó ainda fora da árvore, calcula a distância até o nó recém-adicionado. Se for menor que o custo já registrado em `min_edge`, atualiza — pois agora existe um caminho mais barato até ele.

Esses 3 passos se repetem N vezes, até que todos os nós estejam na árvore.

---

## Resultados

Entrada de teste com os 4 casos do enunciado (`entrada.txt`):

```
4
2 1155 2211
3 1111 1155 5511
3 1234 5678 9090
4 2145 0213 9113 8113
```

Saída impressa ao executar `python p1235.py < entrada.txt`:

```
16
20
26
17
```

Saída esperada pelo enunciado:

```
16
20
26
17
```

Todos os 4 casos batem com o esperado.

---

## Exemplo Explicado

Chaves: `1111`, `1155`, `5511`

- `0000` -> `1111`: 4 rolagens
- `1111` -> `1155`: 8 rolagens
- JUMP de volta para `1111` (grátis)
- `1111` -> `5511`: 8 rolagens

**Total: 20 rolagens**

---

## Como Executar

Com arquivo de entrada:

```bash
python p1235.py < entrada.txt
```

Ou no PowerShell:

```bash
Get-Content entrada.txt | python p1235.py
```

---

## Tecnologias

- Python 3
- Sem bibliotecas externas (implementação manual do Prim)
