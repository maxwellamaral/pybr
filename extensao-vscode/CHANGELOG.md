# Changelog

Todas as mudanças notáveis nesta extensão serão documentadas neste arquivo.

## [1.0.0] - 2026-01-04

### Adicionado
- Syntax highlighting completo para PyBR
  - Palavras-chave de controle de fluxo (se, senao, para, enquanto, etc.)
  - Palavras-chave de exceção (tente, exceto, finalmente)
  - Operadores lógicos (e, ou, nao, em, eh)
  - Constantes (Verdadeiro, Falso, Nulo)
  - Funções nativas traduzidas (imprimir, entrada, tamanho, etc.)
- Snippets para estruturas comuns
  - Função (definir)
  - Classe (classe)
  - Condicionais (se, sesenao)
  - Loops (para, enquanto)
  - Tratamento de exceções (tente/exceto)
  - Imprimir e f-strings
- Configuração de linguagem
  - Auto-fechamento de parênteses, colchetes e aspas
  - Indentação automática inteligente
  - Suporte a folding de código
  - Comentários de linha (#) e bloco (''' ou """)
- Suporte para extensões de arquivo .pybr e .pybr.py
- Documentação completa (README.md)
- Changelog para versionamento

### Recursos Principais
- Integração completa com VS Code
- Compatível com temas populares
- Reconhecimento de f-strings para interpolação
- Destaque de definições de funções e classes
- Suporte a métodos especiais do Python (__init__, __str__, etc.)

### Notas
- Primeira versão estável da extensão
- Testado com VS Code 1.75.0+
- Requer transpilador PyBR para execução de código
