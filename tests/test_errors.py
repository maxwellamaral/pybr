import unittest
import sys
import os
import io
from contextlib import redirect_stdout

# Adiciona o diretório pai ao sys.path para importar o pybr
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pybr import PyBRTranspiler

class TestErrorTranslation(unittest.TestCase):
    def setUp(self):
        # Configura o transpilador para português
        self.transpiler_pt = PyBRTranspiler('pt-br')

    def assertErrorOutput(self, code, expected_fragment, lang='pt-br'):
        """Helper para executar código e verificar se a saída de erro contém o fragmento esperado."""
        transpiler = PyBRTranspiler(lang)
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        output = f.getvalue()
        self.assertIn(expected_fragment, output)

    def test_name_error(self):
        code = "imprimir(variavel_inexistente)"
        self.assertErrorOutput(code, "Nome 'variavel_inexistente' não definido")

    def test_type_error_concatenation(self):
        code = "imprimir('texto' + 5)"
        self.assertErrorOutput(code, "Só é possível concatenar texto com texto (não 'int')")

    def test_type_error_function_call(self):
        # Tentar chamar um inteiro como função
        code = "x = 5\nx()"
        self.assertErrorOutput(code, "O objeto 'int' não pode ser chamado como uma função")

    def test_index_error_list(self):
        code = "lista = [1, 2, 3]\nimprimir(lista[5])"
        self.assertErrorOutput(code, "Índice da lista fora do intervalo")

    def test_key_error(self):
        code = "dic = {'a': 1}\nimprimir(dic['b'])"
        self.assertErrorOutput(code, "Chave 'b' não encontrada no dicionário")

    def test_value_error_int(self):
        code = "a = inteiro('abc')"
        self.assertErrorOutput(code, "Valor inválido para a função int(): 'abc'")

    def test_zero_division_error(self):
        code = "imprimir(10 / 0)"
        self.assertErrorOutput(code, "Divisão por zero não permitida")

    def test_attribute_error(self):
        code = "t = 'texto'\nt.atributo_inexistente"
        # O fragmento deve corresponder ao padrão substituído
        self.assertErrorOutput(code, "Objeto 'str' não possui o atributo 'atributo_inexistente'")

    def test_file_not_found_error(self):
        # Este teste depende de tentar abrir um arquivo que não existe
        # open() não é traduzido diretamente, mas é um builtin do Python
        # Se o usuário usar 'abrir' (se estivesse mapeado) ou uma função que chame open
        # Vamos assumir que 'open' funciona como builtin python padrão se não mapeado ou se mapeado como 'open'
        # Verificando se 'open' está no builtins do pt-br.json...
        # Se não estiver, o pybr deixa passar. Se estiver mapeado como 'abrir', testamos 'abrir'.
        # Vou usar um código que gera FileNotFoundError garantido.
        code = "importar modelo_inexistente_123"
        # ImportError vs ModuleNotFoundError. Vamos testar ModuleNotFoundError especificamente
        # Ou abrir arquivo:
        # Se 'open' não for traduzido, ele é chamado diretamente?
        # O transpilador traduz tokens. Se 'open' não está no mapa, fica 'open'.
        pass 
        # Vou testar ModuleNotFoundError que é mais garantido no ambiente de teste
        code_mod = "importar modulo_que_nao_existe_xyz"
        self.assertErrorOutput(code_mod, "Módulo 'modulo_que_nao_existe_xyz' não encontrado")

    def test_real_file_not_found_error(self):
        # Teste específico para FileNotFoundError usando open() (função nativa do Python)
        # O PyBR permite chamar funções nativas se não houver tradução, ou se a tradução mapear para ela.
        # Vamos assumir que 'open' pode ser chamado.
        code = "open('arquivo_fantasma_123.txt')"
        self.assertErrorOutput(code, "Arquivo ou diretório não encontrado: 'arquivo_fantasma_123.txt'")

    def test_import_from_error(self):
        # Tentar importar algo que não existe de um módulo que existe
        code = "de math importar funcao_inexistente"
        self.assertErrorOutput(code, "Não foi possível importar 'funcao_inexistente' de 'math'")

    # --- Testes Básicos em Espanhol para garantir que o regex funciona em outros idiomas ---
    def test_name_error_es(self):
        code = "imprimir(variable_inexistente)"
        self.assertErrorOutput(code, "Nombre 'variable_inexistente' no definido", lang='es')

    def test_zero_division_es(self):
        code = "imprimir(1 / 0)"
        self.assertErrorOutput(code, "División por cero no permitida", lang='es')

if __name__ == '__main__':
    unittest.main()
