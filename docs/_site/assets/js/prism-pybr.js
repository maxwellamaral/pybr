// Definição da linguagem PyBR para Prism.js
// Baseado nas palavras-chave do transpilador PyBR

Prism.languages.pybr = {
    'comment': {
        pattern: /(^|[^\\])#.*/,
        lookbehind: true
    },
    'string': {
        pattern: /("""|'''|"|')(?:\\.|(?!\1)[^\\\r\n])*\1/,
        greedy: true
    },
    'fstring': {
        pattern: /f("|')(?:\\.|(?!\1)[^\\\r\n])*\1/,
        greedy: true,
        inside: {
            'interpolation': {
                pattern: /{[^}]+}/,
                inside: Prism.languages.python
            }
        }
    },
    'keyword': /\b(?:se|senao|senaose|para|enquanto|quebre|continue|retornar|tente|exceto|finalmente|levantar|passar|afirmar|com|definir|funcao|classe|global|importar|de|como|lambda|e|ou|nao|em|eh)\b/,
    'boolean': /\b(?:Verdadeiro|Falso)\b/,
    'constant': /\b(?:Nulo)\b/,
    'builtin': /\b(?:imprimir|entrada|inteiro|flutuante|texto|lista|dicionario|conjunto|tupla|tamanho|intervalo|tipo|enumerar|maximo|minimo|abs|arredondar|ordenar|reverter|filtrar|mapear|qualquer|todos|abrir|ajuda|dir|sair)\b/,
    'number': /\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\b/,
    'operator': /[-+*/%=<>!&|^~]+|\/\/|\*\*/,
    'punctuation': /[{}[\];(),.:]/,
    'function': {
        pattern: /(?:^|\s)definir\s+(\w+)/,
        lookbehind: true
    },
    'class-name': {
        pattern: /(?:^|\s)classe\s+(\w+)/,
        lookbehind: true
    }
};

// Alias para usar 'python' também como PyBR
Prism.languages.python = Prism.languages.pybr;
