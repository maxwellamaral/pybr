import tokenize
import io
import sys

class PyBRTranspiler:
    def __init__(self):
        # Mapeamento de palavras-chave (Português -> Python)
        self.keywords = {
            # Controle de Fluxo
            'se': 'if',
            'senao': 'else',
            'senaose': 'elif',
            'para': 'for',
            'enquanto': 'while',
            'quebre': 'break',
            'continue': 'continue',
            'retornar': 'return',
            'tente': 'try',
            'exceto': 'except',
            'finalmente': 'finally',
            'levantar': 'raise',
            'passar': 'pass',
            'afirmar': 'assert',
            'com': 'with',
            
            # Definições
            'definir': 'def',
            'classe': 'class',
            'global': 'global',
            'importar': 'import',
            'de': 'from',
            'como': 'as',
            'lambda': 'lambda', # Lambda é universal, mas pode ser traduzido se quiser
            
            # Operadores Lógicos e Constantes
            'e': 'and',
            'ou': 'or',
            'nao': 'not',
            'em': 'in',
            'eh': 'is',
            'Verdadeiro': 'True',
            'Falso': 'False',
            'Nulo': 'None',
        }

        # Mapeamento de Funções Nativas Comuns (Opcional, mas útil)
        self.builtins_map = {
            'imprimir': 'print',
            'entrada': 'input',
            'tamanho': 'len',
            'intervalo': 'range',
            'inteiro': 'int',
            'texto': 'str',
            'lista': 'list',
            'dicionario': 'dict',
            'abrir': 'open',
            'ajuda': 'help',
            'sair': 'exit'
        }

    def traduzir_token(self, token_type, token_string):
        """Traduz um único token se for um NOME e estiver no dicionário."""
        if token_type == tokenize.NAME:
            # Verifica keywords
            if token_string in self.keywords:
                return self.keywords[token_string]
            # Verifica built-ins
            if token_string in self.builtins_map:
                return self.builtins_map[token_string]
        return token_string

    def transpilador(self, codigo_fonte_br):
        """
        Lê o código em PyBR e retorna código Python válido.
        Usa o tokenizer para garantir que não traduzimos palavras dentro de strings.
        """
        # O tokenize precisa de bytes
        tokens = tokenize.tokenize(io.BytesIO(codigo_fonte_br.encode('utf-8')).readline)
        resultado = []
        
        try:
            for token in tokens:
                tipo = token.type
                string = token.string
                start = token.start
                end = token.end
                line = token.line
                
                # Traduz apenas identificadores (NOMES)
                nova_string = self.traduzir_token(tipo, string)
                
                # O untokenize é complexo, então vamos reconstruir manualmente de forma simples
                # ou usar o untokenize modificando o stream. A abordagem abaixo reconstrói
                # o token stream modificado.
                resultado.append((tipo, nova_string))
                
            # Reconstrói o código Python a partir dos tokens modificados
            codigo_python = tokenize.untokenize(resultado).decode('utf-8')
            return codigo_python
            
        except tokenize.TokenError as e:
            return f"Erro de Sintaxe: {e}"

    def executar(self, codigo_fonte_br):
        """Traduz e executa o código."""
        codigo_python = self.transpilador(codigo_fonte_br)
        
        # Cria um ambiente isolado para execução
        ambiente_global = {}
        
        try:
            exec(codigo_python, ambiente_global)
        except Exception as e:
            print(f"Erro de Execução: {e}")

    def repl(self):
        """Inicia um shell interativo (Read-Eval-Print Loop)."""
        print("="*50)
        print("Bem-vindo ao PyBR 1.0 (Python Brasileiro)")
        print("Digite 'sair()' para encerrar.")
        print("="*50)
        
        buffer = []
        dentro_de_bloco = False

        while True:
            try:
                # Prompt muda se estivermos dentro de um bloco indentado
                prompt = "... " if dentro_de_bloco else ">>> "
                linha = input(prompt)

                if linha.strip() == "sair()":
                    break
                
                buffer.append(linha)

                # Lógica simples para detectar se o bloco continua
                # Se a linha termina com ':', esperamos mais linhas
                if linha.strip().endswith(':'):
                    dentro_de_bloco = True
                    continue
                
                # Se estamos num bloco e a linha é vazia, executamos
                if dentro_de_bloco and linha.strip() == "":
                    dentro_de_bloco = False
                elif dentro_de_bloco:
                    continue

                # Executar o buffer acumulado
                codigo_completo = "\n".join(buffer)
                codigo_traduzido = self.transpilador(codigo_completo)
                
                # Para debug: descomente a linha abaixo para ver o código Python gerado
                # print(f"--- DEBUG (Python): ---\n{codigo_traduzido}\n-----------------------")
                
                exec(codigo_traduzido, globals())
                buffer = []

            except KeyboardInterrupt:
                print("\nInterrompido.")
                buffer = []
                dentro_de_bloco = False
            except Exception as e:
                print(f"Erro: {e}")
                buffer = []
                dentro_de_bloco = False

# Exemplo de Código na nova linguagem
CODIGO_DEMONSTRACAO = """
# Isto é um comentário
definir calcular_fatorial(n):
    se n <= 1:
        retornar 1
    senao:
        retornar n * calcular_fatorial(n - 1)

imprimir("--- Teste do Compilador PyBR ---")
nome = "Mundo"
imprimir(f"Olá, {nome}! Vamos contar:")

para i em intervalo(5):
    se i % 2 == 0:
        imprimir(f"{i} é par")
    senao:
        imprimir(f"{i} é impar")

resultado = calcular_fatorial(5)
imprimir(f"O fatorial de 5 é: {resultado}")

classe Pessoa:
    definir __init__(proprio, nome, idade):
        proprio.nome = nome
        proprio.idade = idade
    
    definir apresentar(proprio):
        imprimir(f"Meu nome é {proprio.nome} e tenho {proprio.idade} anos.")

p = Pessoa("Maria", 30)
p.apresentar()
"""

if __name__ == "__main__":
    compilador = PyBRTranspiler()
    
    if len(sys.argv) > 1:
        # Se um arquivo for passado como argumento, execute-o
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                codigo = f.read()
            compilador.executar(codigo)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {sys.argv[1]}")
    else:
        # Caso contrário, execute a demonstração e entre no REPL
        print("Executando código de demonstração interno...\n")
        compilador.executar(CODIGO_DEMONSTRACAO)
        print("\n" + "-"*30 + "\n")
        compilador.repl()