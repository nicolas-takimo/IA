# README para o Projeto do Algoritmo A* no Quebra-Cabeça das Oito Peças

## Descrição Geral

Este projeto implementa o algoritmo A* para resolver o quebra-cabeça das oito peças, um jogo popular que envolve deslizar peças em uma grade 3x3 para alcançar uma configuração objetivo. O código é flexível, permitindo o uso de diferentes heurísticas e verificando a solucionabilidade do estado inicial.

## Dependências

- `numpy`: Utilizada para operações com matrizes.
- `PriorityQueue`: Faz parte da biblioteca padrão do Python e é usada para manter os estados na ordem de prioridade.
- `convolve2d`: Da biblioteca SciPy, usada nas funções de movimentação.

## Estrutura do Código

### Classe `Estado`

Representa um estado do quebra-cabeça, incluindo a matriz das peças e o estado pai. Contém métodos para comparações e para exibir o estado.

### Funções Principais

- `acoes_permitidas`: Identifica movimentos possíveis em um estado.
- `movimentar`: Realiza o movimento de uma peça, gerando um novo estado.
- `distancia_manhattan` e `hamming`: Heurísticas para estimar o custo de um estado até o objetivo.
- `a_star`: Implementação do algoritmo A* que encontra o caminho mais eficiente para a solução.
- `reconstruir_caminho`: Reconstrói o caminho da solução a partir do estado final.

### Verificação de Solucionabilidade

- `tem_solucao`: Verifica se o estado inicial pode ser solucionado.

### Execução

Configura o estado inicial e objetivo, verifica a solucionabilidade e, se possível, executa o algoritmo A* e exibe a solução.

## Detalhes Adicionais

- O código é flexível, permitindo a escolha entre diferentes heurísticas.
- A solucionabilidade do estado inicial é verificada antes de tentar encontrar uma solução.
- Cada parte do algoritmo é modular, facilitando a compreensão e a manutenção.

## Como Usar

1. Defina o estado inicial e o estado objetivo do quebra-cabeça.
2. Verifique se o estado inicial é solucionável.
3. Execute o algoritmo A* com a heurística de sua escolha.
4. Visualize o caminho da solução.

## Conclusão

Este projeto fornece uma implementação clara e eficiente do algoritmo A* para resolver o quebra-cabeça das oito peças, com ênfase na flexibilidade, eficiência e facilidade de uso.
