# Panda Land Safe Box — p1235

Solução para o problema **p1235** do Online Judge, desenvolvido como trabalho avaliativo da disciplina de CANA.

---

## Descrição do Problema

Um cadeado de 4 dígitos (cada um de 0 a 9, circular) começa em `0000`. Existem **N chaves** que precisam ser destravadas. Para destravar uma chave, rolam-se os dígitos até o valor dela — cada rolagem custa 1. Um botão **JUMP** permite teleportar de graça para qualquer chave já destravada.

O objetivo é desbloquear todas as chaves com o **mínimo total de rolagens**.

---

## Modelagem

O problema foi modelado como um **grafo completo não-direcionado ponderado**:

- **Nós:** as N chaves + o ponto de partida `0000`
- **Arestas:** entre todo par de nós, com peso = distância de rolagem
- **Distância entre dois números:** soma dígito a dígito de `min(|a-b|, 10-|a-b|)` (distância circular)

Como o JUMP permite mover-se de graça entre chaves já destravadas, cada nova chave paga apenas o custo até a mais próxima já disponível — comportamento exato de uma **Árvore Geradora Mínima (MST)**.

### Detalhe especial: o nó 0000

O `0000` não é uma chave — é só o ponto de partida. Após sair dele, não é possível voltar via JUMP. Por isso ele entra na árvore como **folha**, ligado a exatamente uma chave.

**Fórmula final:**
```
Resposta = MST entre as chaves + menor distância de 0000 até alguma chave
```

---

## Algoritmo

Foi utilizado o **algoritmo de Prim** para construir a MST, com complexidade **O(N²)** por caso de teste — eficiente para N ≤ 500.

### Os 3 passos do Prim:

1. **Escolher** — o nó fora da árvore com menor custo de conexão
2. **Adicionar** — insere esse nó na árvore e soma o custo
3. **Atualizar** — verifica se pelo novo nó algum vizinho fica mais barato

---

## Exemplo

Entrada:
```
3
1111 1155 5511
```

- `0000` → `1111`: 4 rolagens
- `1111` → `1155`: 8 rolagens
- JUMP de volta para `1111` (grátis)
- `1111` → `5511`: 8 rolagens

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

##  Prova da submissão

}<img width="832" height="300" alt="image" src="https://github.com/user-attachments/assets/fd1f120a-9970-4ab4-a3a2-2c197d5235b8" />

