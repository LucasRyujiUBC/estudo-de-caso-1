# Análise de Logs com IA

## Descrição

Este projeto visa automatizar a análise de logs de sistemas para detectar e classificar eventos, como erros, avisos e falhas críticas, utilizando técnicas de aprendizado de máquina. O objetivo é identificar padrões e anomalias nos logs, gerar alertas automáticos e produzir relatórios detalhados para análise posterior.

## Principais Funcionalidades

- **Carregamento de Logs**: Carrega logs de um arquivo de texto e os estrutura para análise.
- **Pré-processamento de Dados**: Realiza limpeza e transformação das mensagens de log para facilitar a análise.
- **Detecção de Anomalias**: Utiliza o algoritmo de Random Forest para classificar eventos e detectar anomalias nos logs.
- **Classificação dos Logs**: Classifica os eventos como "Normal", "Suspeito" ou "Crítico" com base na análise das mensagens.
- **Geração de Relatórios**: Cria relatórios detalhados em formato `.txt`, indicando o número de eventos processados e a categorização dos logs.
- **Alertas Automáticos**: Gera alertas para eventos críticos detectados nos logs.
- **Visualização**: Exibe gráficos com a distribuição dos eventos classificados.

## Instruções de Instalação / Configuração

### 1. Clone o repositório

Primeiro, clone o repositório para o seu diretório local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
