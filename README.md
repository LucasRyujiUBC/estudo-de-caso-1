#Interpretador de Expressões Aritméticas com IA

## Descrição

Este projeto utiliza um modelo de linguagem baseado em inteligência artificial para interpretar e avaliar expressões aritméticas. Ele emprega o modelo microsoft/phi-2 da biblioteca transformers para processar e calcular expressões matemáticas, mesmo quando escritas de forma não convencional.

A interface gráfica é construída com Gradio, permitindo que os usuários interajam facilmente com o interpretador de expressões.

## Instalação e Configuração

### 1. Instalar Dependências

Certifique-se de ter o Python instalado e, em seguida, instale as bibliotecas necessárias executando:

pip install gradio transformers torch

### 2. Executar o Projeto

Para iniciar o interpretador, basta rodar o seguinte comando:

python programa.py

Isso inicializará a interface gráfica onde você poderá inserir expressões aritméticas para avaliação.

## Como Funciona

O usuário insere uma expressão matemática (exemplo: 2 + (3 * 4) / 2).

O modelo microsoft/phi-2 processa e interpreta a expressão.

O resultado é exibido na interface de Gradio.

A inteligência artificial está configurada para minimizar erros e interpretar expressões que podem estar ligeiramente incorretas ou mal formatadas.

## Dependências

As principais dependências utilizadas no projeto são:

- gradio: Para construção da interface gráfica.
- transformers: Para uso do modelo de linguagem microsoft/phi-2.
- torch: Para suporte à execução do modelo.

## Autores

- Lucas Ryuji Fujimoto
- Britney Brevio dos Santos Lima
- Thiago Viniciys Araújo

## Considerações Finais

Este projeto demonstra o poder dos modelos de linguagem na interpretação de cálculos matemáticos. A interface intuitiva e acessível permite que usuários experimentem a IA para resolver expressões aritméticas de maneira eficiente.
