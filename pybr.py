import tokenize
import io
import sys
import os
import json
import argparse

try:
    import readline
except ImportError:
    readline = None

class PyBRTranspiler:
    def __init__(self, lang='pt-br'):
        self.keywords = {}
        self.builtins_map = {}
        self.messages = {}
        self.lang = lang
        self.load_language(lang)

    def load_language(self, lang_code):
        """Carrega o mapeamento de palavras-chave e mensagens de um arquivo JSON."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        lang_file = os.path.join(base_dir, 'languages', f'{lang_code}.json')

        # Fallback messages (Portuguese)
        default_messages = {
            "lang_not_found": "Aviso: Idioma '{}' não encontrado. Usando 'pt-br' como padrão.",
            "lang_load_error": "Erro ao carregar idioma: {}",
            "syntax_error": "Erro de Sintaxe: {}",
            "execution_error": "Erro de Execução: {}",
            "welcome": "Bem-vindo ao PyBR 1.0 (Python Brasileiro)",
            "exit_help": "Digite 'sair()' para encerrar.",
            "interrupted": "Interrompido.",
            "error": "Erro: {}",
            "running_demo": "Executando código de demonstração interno...\n",
            "file_not_found": "Arquivo não encontrado: {}",
            "cli_description": "PyBR - Transpilador de Python em Português (e outras línguas)",
            "cli_help_file": "Arquivo .pybr para executar",
            "cli_help_lang": "Idioma para as palavras-chave (ex: pt-br, es)"
        }

        if not os.path.exists(lang_file):
            print(default_messages["lang_not_found"].format(lang_code))
            lang_file = os.path.join(base_dir, 'languages', 'pt-br.json')

        try:
            with open(lang_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.keywords = data.get('keywords', {})
                self.builtins_map = data.get('builtins', {})
                self.messages = data.get('messages', default_messages)
        except Exception as e:
            if not self.messages:
                print(f"Erro ao carregar idioma: {e}")
                self.messages = default_messages
            # Fallback manual de keywords se falhar
            if not self.keywords:
                self.keywords = {'se': 'if', 'senao': 'else'}

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

    def traduzir_fstrings(self, codigo_python):
        """
        Pós-processa o código para traduzir palavras PyBR dentro de f-strings.
        """
        import re
        for pybr, python in self.builtins_map.items():
            padrao = r'\b' + re.escape(pybr) + r'(?=\s*\()'
            codigo_python = re.sub(padrao, python, codigo_python)
        return codigo_python

    def transpilador(self, codigo_fonte_br):
        """Lê o código em PyBR e retorna código Python válido."""
        tokens = tokenize.tokenize(io.BytesIO(codigo_fonte_br.encode('utf-8')).readline)
        resultado = []
        try:
            for token in tokens:
                tipo = token.type
                string = token.string
                nova_string = self.traduzir_token(tipo, string)
                resultado.append((tipo, nova_string))
            codigo_python = tokenize.untokenize(resultado).decode('utf-8')
            codigo_python = self.traduzir_fstrings(codigo_python)
            return codigo_python
        except tokenize.TokenError as e:
            return self.messages["syntax_error"].format(e)

    def executar(self, codigo_fonte_br):
        """Traduz e executa o código."""
        codigo_python = self.transpilador(codigo_fonte_br)
        import builtins
        ambiente_global = {'__builtins__': builtins}
        try:
            exec(codigo_python, ambiente_global)
        except Exception as e:
            print(self.messages["execution_error"].format(e))

    def repl(self):
        """Inicia um shell interativo (Read-Eval-Print Loop)."""
        print("="*50)
        print(self.messages["welcome"])
        print(self.messages["exit_help"])
        print("="*50)
        
        if readline:
            # Configura o readline para permitir navegação no histórico
            # No Linux/macOS, isso já habilita as setas automaticamente
            pass

        buffer = []
        dentro_de_bloco = False

        while True:
            try:
                prompt = "... " if dentro_de_bloco else ">>> "
                linha = input(prompt)

                # Busca o comando de saída localizado (mapeado para 'exit')
                exit_cmd = next((k for k, v in self.builtins_map.items() if v == 'exit'), 'sair')
                if linha.strip() == f"{exit_cmd}()":
                    break
                
                buffer.append(linha)
                if linha.strip().endswith(':'):
                    dentro_de_bloco = True
                    continue
                
                if dentro_de_bloco and linha.strip() == "":
                    dentro_de_bloco = False
                elif dentro_de_bloco:
                    continue

                codigo_completo = "\n".join(buffer)
                codigo_traduzido = self.transpilador(codigo_completo)
                exec(codigo_traduzido, globals())
                buffer = []

            except KeyboardInterrupt:
                print(f"\n{self.messages['interrupted']}")
                buffer = []
                dentro_de_bloco = False
            except Exception as e:
                print(self.messages["error"].format(e))
                buffer = []
                dentro_de_bloco = False

# Exemplo de Código na nova linguagem
CODIGO_DEMONSTRACAO = """
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
"""

def get_arg_parser(messages):
    parser = argparse.ArgumentParser(description=messages["cli_description"])
    parser.add_argument("arquivo", nargs="?", help=messages["cli_help_file"])
    parser.add_argument("--lang", default="pt-br", help=messages["cli_help_lang"])
    return parser

if __name__ == "__main__":
    # Carregamento inicial apenas para pegar a língua e as mensagens de ajuda do parser
    temp_transpiler = PyBRTranspiler() # Default pt-br
    
    # Precisamos espiar o --lang antes de criar o parser final para que a ajuda seja na língua correta
    # Mas o argparse é melhor para isso. Vamos fazer um parser prévio.
    setup_parser = argparse.ArgumentParser(add_help=False)
    setup_parser.add_argument("--lang", default="pt-br")
    setup_args, _ = setup_parser.parse_known_args()
    
    compilador = PyBRTranspiler(lang=setup_args.lang)
    parser = get_arg_parser(compilador.messages)
    args = parser.parse_args()
    
    if args.arquivo:
        try:
            with open(args.arquivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            compilador.executar(codigo)
        except FileNotFoundError:
            print(compilador.messages["file_not_found"].format(args.arquivo))
    else:
        if args.lang == 'pt-br':
            print(compilador.messages["running_demo"])
            compilador.executar(CODIGO_DEMONSTRACAO)
            print("\n" + "-"*30 + "\n")
        
        compilador.repl()