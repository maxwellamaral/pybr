"""
Testes funcionais automatizados para PyBRTranspiler
Autor: Maxwell Anderson Ielpo do Amaral
"""

import unittest
import sys
import os
from io import StringIO

# Adiciona o diretório raiz ao path para importar o módulo pybr
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pybr import PyBRTranspiler


class TestPyBRTranspiler(unittest.TestCase):
    """Testes para o transpilador PyBR"""

    def setUp(self):
        """Configura o transpilador para cada teste"""
        self.transpilador = PyBRTranspiler()
        self.maxDiff = None

    def capturar_saida(self, codigo_pybr):
        """Captura a saída padrão durante a execução do código"""
        saida_capturada = StringIO()
        sys.stdout = saida_capturada
        try:
            self.transpilador.executar(codigo_pybr)
            resultado = saida_capturada.getvalue()
        finally:
            sys.stdout = sys.__stdout__
        return resultado

    # ==================== TESTES DE TRADUÇÃO DE TOKENS ====================

    def test_traducao_palavras_chave_controle_fluxo(self):
        """Testa tradução de palavras-chave de controle de fluxo"""
        import tokenize as tok
        
        testes = [
            ('se', 'if'),
            ('senao', 'else'),
            ('senaose', 'elif'),
            ('para', 'for'),
            ('enquanto', 'while'),
            ('retornar', 'return'),
            ('quebre', 'break'),
            ('continue', 'continue'),
            ('passar', 'pass'),
        ]
        
        for pybr, python in testes:
            resultado = self.transpilador.traduzir_token(tok.NAME, pybr)
            self.assertEqual(resultado, python, 
                           f"Falha ao traduzir '{pybr}' para '{python}'")

    def test_traducao_palavras_chave_definicoes(self):
        """Testa tradução de palavras-chave de definições"""
        import tokenize as tok
        
        testes = [
            ('definir', 'def'),
            ('funcao', 'def'),
            ('classe', 'class'),
            ('importar', 'import'),
            ('de', 'from'),
            ('como', 'as'),
        ]
        
        for pybr, python in testes:
            resultado = self.transpilador.traduzir_token(tok.NAME, pybr)
            self.assertEqual(resultado, python,
                           f"Falha ao traduzir '{pybr}' para '{python}'")

    def test_traducao_operadores_logicos(self):
        """Testa tradução de operadores lógicos"""
        import tokenize as tok
        
        testes = [
            ('e', 'and'),
            ('ou', 'or'),
            ('nao', 'not'),
            ('em', 'in'),
            ('eh', 'is'),
        ]
        
        for pybr, python in testes:
            resultado = self.transpilador.traduzir_token(tok.NAME, pybr)
            self.assertEqual(resultado, python,
                           f"Falha ao traduzir '{pybr}' para '{python}'")

    def test_traducao_constantes(self):
        """Testa tradução de constantes"""
        import tokenize as tok
        
        testes = [
            ('Verdadeiro', 'True'),
            ('Falso', 'False'),
            ('Nulo', 'None'),
        ]
        
        for pybr, python in testes:
            resultado = self.transpilador.traduzir_token(tok.NAME, pybr)
            self.assertEqual(resultado, python,
                           f"Falha ao traduzir '{pybr}' para '{python}'")

    def test_traducao_funcoes_nativas(self):
        """Testa tradução de funções nativas"""
        import tokenize as tok
        
        testes = [
            # Entrada/Saída
            ('imprimir', 'print'),
            ('entrada', 'input'),
            # Conversão de Tipos
            ('inteiro', 'int'),
            ('flutuante', 'float'),
            ('texto', 'str'),
            ('lista', 'list'),
            ('dicionario', 'dict'),
            ('conjunto', 'set'),
            ('tupla', 'tuple'),
            # Manipulação
            ('tamanho', 'len'),
            ('intervalo', 'range'),
            ('tipo', 'type'),
            ('enumerar', 'enumerate'),
            # Matemática
            ('maximo', 'max'),
            ('minimo', 'min'),
            ('abs', 'abs'),
            ('arredondar', 'round'),
            # Ordenação/Iteração
            ('ordenar', 'sorted'),
            ('reverter', 'reversed'),
            ('filtrar', 'filter'),
            ('mapear', 'map'),
            ('qualquer', 'any'),
            ('todos', 'all'),
            # Arquivos
            ('abrir', 'open'),
            # Utilidades
            ('ajuda', 'help'),
            ('dir', 'dir'),
            ('sair', 'exit'),
        ]
        
        for pybr, python in testes:
            resultado = self.transpilador.traduzir_token(tok.NAME, pybr)
            self.assertEqual(resultado, python,
                           f"Falha ao traduzir '{pybr}' para '{python}'")

    def test_nao_traduz_nomes_variaveis(self):
        """Testa que nomes de variáveis não são traduzidos"""
        import tokenize as tok
        
        variaveis = ['nome', 'idade', 'valor', 'resultado', 'contador']
        
        for var in variaveis:
            resultado = self.transpilador.traduzir_token(tok.NAME, var)
            self.assertEqual(resultado, var,
                           f"Variável '{var}' não deveria ser traduzida")

    # ==================== TESTES DE TRANSPILAÇÃO ====================

    def test_transpilacao_funcao_simples(self):
        """Testa transpilação de uma função simples"""
        codigo_pybr = """
definir saudacao():
    imprimir("Olá")
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn('def saudacao', codigo_python)
        self.assertIn('print', codigo_python)

    def test_transpilacao_funcao_alternativa(self):
        """Testa transpilação usando palavra-chave 'funcao'"""
        codigo_pybr = """
funcao saudacao():
    imprimir("Olá")
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn('def saudacao', codigo_python)
        self.assertIn('print', codigo_python)

    def test_transpilacao_classe(self):
        """Testa transpilação de uma classe"""
        codigo_pybr = """
classe Animal:
    definir __init__(proprio, nome):
        proprio.nome = nome
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn('class Animal', codigo_python)
        self.assertIn('def __init__', codigo_python)

    def test_transpilacao_condicional(self):
        """Testa transpilação de estruturas condicionais"""
        codigo_pybr = """
se x > 0:
    imprimir("Positivo")
senaose x < 0:
    imprimir("Negativo")
senao:
    imprimir("Zero")
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn('if x', codigo_python)
        self.assertIn('elif x', codigo_python)
        self.assertIn('else', codigo_python)

    def test_transpilacao_loop_para(self):
        """Testa transpilação de loop para"""
        codigo_pybr = """
para i em intervalo(5):
    imprimir(i)
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn('for i in range', codigo_python)

    def test_transpilacao_loop_enquanto(self):
        """Testa transpilação de loop enquanto"""
        codigo_pybr = """
enquanto x < 10:
    x = x + 1
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn('while x', codigo_python)

    def test_transpilacao_operadores_logicos(self):
        """Testa transpilação de operadores lógicos"""
        codigo_pybr = """
se x > 0 e y > 0:
    passar
se x > 0 ou y > 0:
    passar
se nao x:
    passar
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn(' and ', codigo_python)
        self.assertIn(' or ', codigo_python)
        self.assertIn('not ', codigo_python)

    def test_transpilacao_excecoes(self):
        """Testa transpilação de tratamento de exceções"""
        codigo_pybr = """
tente:
    x = 1 / 0
exceto ZeroDivisionError:
    imprimir("Erro")
finalmente:
    imprimir("Fim")
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn('try', codigo_python)
        self.assertIn('except', codigo_python)
        self.assertIn('finally', codigo_python)

    def test_preserva_strings(self):
        """Testa que strings não são traduzidas"""
        codigo_pybr = 'imprimir("se para enquanto definir")'
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        # As palavras dentro das aspas não devem ser traduzidas
        self.assertIn('"se para enquanto definir"', codigo_python)

    def test_preserva_comentarios(self):
        """Testa que comentários são preservados"""
        codigo_pybr = """
# Este é um comentário com palavras: se para enquanto
imprimir("teste")
"""
        codigo_python = self.transpilador.transpilador(codigo_pybr)
        self.assertIn('# Este é um comentário', codigo_python)

    # ==================== TESTES DE EXECUÇÃO ====================

    def test_execucao_imprimir(self):
        """Testa execução de comando imprimir"""
        codigo = 'imprimir("Olá, Mundo!")'
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "Olá, Mundo!")

    def test_execucao_variavel(self):
        """Testa execução com variáveis"""
        codigo = """
nome = "Python"
imprimir(nome)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "Python")

    def test_execucao_funcao(self):
        """Testa execução de função"""
        codigo = """
definir dobro(x):
    retornar x * 2

resultado = dobro(5)
imprimir(resultado)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "10")

    def test_execucao_funcao_alternativa(self):
        """Testa execução usando palavra-chave 'funcao'"""
        codigo = """
funcao triplo(x):
    retornar x * 3

resultado = triplo(5)
imprimir(resultado)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "15")

    def test_execucao_classe(self):
        """Testa execução de classe"""
        codigo = """
classe Pessoa:
    definir __init__(proprio, nome):
        proprio.nome = nome
    
    definir saudar(proprio):
        imprimir(f"Olá, {proprio.nome}")

p = Pessoa("Maria")
p.saudar()
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "Olá, Maria")

    def test_execucao_condicional(self):
        """Testa execução de condicional"""
        codigo = """
x = 10
se x > 5:
    imprimir("Maior")
senao:
    imprimir("Menor")
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "Maior")

    def test_execucao_loop_para(self):
        """Testa execução de loop para"""
        codigo = """
para i em intervalo(3):
    imprimir(i)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "0\n1\n2")

    def test_execucao_loop_enquanto(self):
        """Testa execução de loop enquanto"""
        codigo = """
contador = 0
enquanto contador < 3:
    imprimir(contador)
    contador = contador + 1
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "0\n1\n2")

    def test_execucao_operadores_logicos(self):
        """Testa execução com operadores lógicos"""
        codigo = """
x = 5
y = 10
se x > 0 e y > 0:
    imprimir("Ambos positivos")
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "Ambos positivos")

    def test_execucao_lista(self):
        """Testa execução com listas"""
        codigo = """
numeros = lista([1, 2, 3])
imprimir(tamanho(numeros))
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "3")

    def test_execucao_dicionario(self):
        """Testa execução com dicionários"""
        codigo = """
dados = dicionario()
dados["nome"] = "Python"
imprimir(dados["nome"])
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "Python")

    def test_execucao_constantes(self):
        """Testa execução com constantes"""
        codigo = """
imprimir(Verdadeiro)
imprimir(Falso)
imprimir(Nulo)
"""
        saida = self.capturar_saida(codigo)
        linhas = saida.strip().split('\n')
        self.assertEqual(linhas[0], "True")
        self.assertEqual(linhas[1], "False")
        self.assertEqual(linhas[2], "None")

    def test_execucao_fstring(self):
        """Testa execução com f-strings"""
        codigo = """
nome = "Python"
versao = 3
imprimir(f"{nome} {versao}")
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "Python 3")

    def test_execucao_recursao(self):
        """Testa execução de função recursiva"""
        codigo = """
definir fatorial(n):
    se n <= 1:
        retornar 1
    senao:
        retornar n * fatorial(n - 1)

resultado = fatorial(5)
imprimir(resultado)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "120")

    def test_execucao_excecao(self):
        """Testa execução com tratamento de exceção"""
        codigo = """
tente:
    x = 10 / 2
    imprimir(inteiro(x))
exceto:
    imprimir("Erro")
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "5")

    def test_execucao_quebre_continue(self):
        """Testa execução com quebre e continue"""
        codigo = """
para i em intervalo(5):
    se i == 2:
        continue
    se i == 4:
        quebre
    imprimir(i)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "0\n1\n3")

    def test_execucao_conversao_tipos(self):
        """Testa execução com conversões de tipos"""
        codigo = """
# Flutuante
x = flutuante("3.14")
imprimir(tipo(x).__name__)

# Conjunto
s = conjunto([1, 2, 2, 3])
imprimir(tamanho(s))

# Tupla
t = tupla([1, 2, 3])
imprimir(tamanho(t))
"""
        saida = self.capturar_saida(codigo)
        linhas = saida.strip().split('\n')
        self.assertEqual(linhas[0], "float")
        self.assertEqual(linhas[1], "3")
        self.assertEqual(linhas[2], "3")

    def test_execucao_funcoes_matematicas(self):
        """Testa execução com funções matemáticas"""
        codigo = """
# Máximo e mínimo
imprimir(maximo(1, 5, 3))
imprimir(minimo(1, 5, 3))

# Arredondar
imprimir(arredondar(3.7))

# Valor absoluto
imprimir(abs(-5))
"""
        saida = self.capturar_saida(codigo)
        linhas = saida.strip().split('\n')
        self.assertEqual(linhas[0], "5")
        self.assertEqual(linhas[1], "1")
        self.assertEqual(linhas[2], "4")
        self.assertEqual(linhas[3], "5")

    def test_execucao_ordenacao_e_reversao(self):
        """Testa execução com ordenação e reversão"""
        codigo = """
numeros = [3, 1, 4, 1, 5]

# Ordenar
ordenados = ordenar(numeros)
imprimir(lista(ordenados))

# Reverter
revertidos = lista(reverter([1, 2, 3]))
imprimir(revertidos)
"""
        saida = self.capturar_saida(codigo)
        linhas = saida.strip().split('\n')
        self.assertIn("[1, 1, 3, 4, 5]", linhas[0])
        self.assertIn("[3, 2, 1]", linhas[1])

    def test_execucao_funcoes_iteracao(self):
        """Testa execução com funções de iteração avançadas"""
        codigo = """
# Enumerar
para i, valor em enumerar(['a', 'b', 'c']):
    se i == 1:
        imprimir(valor)

# Qualquer
imprimir(qualquer([Falso, Verdadeiro, Falso]))

# Todos
imprimir(todos([Verdadeiro, Verdadeiro, Verdadeiro]))
"""
        saida = self.capturar_saida(codigo)
        linhas = saida.strip().split('\n')
        self.assertEqual(linhas[0], "b")
        self.assertEqual(linhas[1], "True")
        self.assertEqual(linhas[2], "True")

    def test_execucao_filtrar_mapear(self):
        """Testa execução com filtrar e mapear"""
        codigo = """
# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = lista(filtrar(lambda x: x % 2 == 0, numeros))
imprimir(tamanho(pares))

# Mapear (dobrar valores)
dobrados = lista(mapear(lambda x: x * 2, [1, 2, 3]))
imprimir(dobrados)
"""
        saida = self.capturar_saida(codigo)
        linhas = saida.strip().split('\n')
        self.assertEqual(linhas[0], "3")
        self.assertIn("[2, 4, 6]", linhas[1])

    # ==================== TESTES DE CÓDIGO COMPLEXO ====================

    def test_codigo_completo_classe_e_metodos(self):
        """Testa código completo com classes e métodos"""
        codigo = """
classe Calculadora:
    definir __init__(proprio):
        proprio.resultado = 0
    
    definir somar(proprio, a, b):
        proprio.resultado = a + b
        retornar proprio.resultado
    
    definir multiplicar(proprio, a, b):
        proprio.resultado = a * b
        retornar proprio.resultado

calc = Calculadora()
imprimir(calc.somar(5, 3))
imprimir(calc.multiplicar(4, 2))
"""
        saida = self.capturar_saida(codigo)
        linhas = saida.strip().split('\n')
        self.assertEqual(linhas[0], "8")
        self.assertEqual(linhas[1], "8")

    def test_codigo_completo_aninhado(self):
        """Testa código com estruturas aninhadas"""
        codigo = """
para i em intervalo(3):
    para j em intervalo(2):
        se i == j:
            imprimir(f"{i},{j}")
"""
        saida = self.capturar_saida(codigo)
        linhas = saida.strip().split('\n')
        self.assertEqual(linhas[0], "0,0")
        self.assertEqual(linhas[1], "1,1")

    def test_codigo_completo_funcoes_multiplas(self):
        """Testa código com múltiplas funções"""
        codigo = """
definir eh_par(n):
    retornar n % 2 == 0

definir eh_impar(n):
    retornar nao eh_par(n)

definir filtrar_pares(numeros):
    resultado = lista()
    para n em numeros:
        se eh_par(n):
            resultado.append(n)
    retornar resultado

nums = [1, 2, 3, 4, 5, 6]
pares = filtrar_pares(nums)
imprimir(tamanho(pares))
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "3")

    # ==================== TESTES DE ERRO ====================

    def test_erro_sintaxe_capturado(self):
        """Testa que erros de sintaxe são capturados"""
        codigo = "definir func("  # Sintaxe inválida
        resultado = self.transpilador.transpilador(codigo)
        self.assertIn("Erro de Sintaxe", resultado)


class TestPyBRExemplosReais(unittest.TestCase):
    """Testes com exemplos reais de código PyBR"""

    def setUp(self):
        """Configura o transpilador para cada teste"""
        self.transpilador = PyBRTranspiler()

    def capturar_saida(self, codigo_pybr):
        """Captura a saída padrão durante a execução do código"""
        saida_capturada = StringIO()
        sys.stdout = saida_capturada
        try:
            self.transpilador.executar(codigo_pybr)
            resultado = saida_capturada.getvalue()
        finally:
            sys.stdout = sys.__stdout__
        return resultado

    def test_exemplo_fibonacci(self):
        """Testa exemplo de Fibonacci"""
        codigo = """
definir fibonacci(n):
    se n <= 1:
        retornar n
    senao:
        retornar fibonacci(n-1) + fibonacci(n-2)

resultado = fibonacci(7)
imprimir(resultado)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "13")

    def test_exemplo_soma_lista(self):
        """Testa exemplo de soma de lista"""
        codigo = """
definir somar_lista(numeros):
    total = 0
    para n em numeros:
        total = total + n
    retornar total

nums = [1, 2, 3, 4, 5]
resultado = somar_lista(nums)
imprimir(resultado)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "15")

    def test_exemplo_busca_binaria(self):
        """Testa exemplo de busca simples"""
        codigo = """
definir buscar(lista_nums, alvo):
    para i em intervalo(tamanho(lista_nums)):
        se lista_nums[i] == alvo:
            retornar i
    retornar -1

nums = [10, 20, 30, 40, 50]
indice = buscar(nums, 30)
imprimir(indice)
"""
        saida = self.capturar_saida(codigo)
        self.assertEqual(saida.strip(), "2")


def executar_testes():
    """Executa todos os testes e mostra relatório"""
    print("="*70)
    print("Executando Testes Funcionais do PyBR")
    print("="*70)
    
    # Cria a suite de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adiciona todos os testes
    suite.addTests(loader.loadTestsFromTestCase(TestPyBRTranspiler))
    suite.addTests(loader.loadTestsFromTestCase(TestPyBRExemplosReais))
    
    # Executa os testes com verbosidade
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Mostra resumo
    print("\n" + "="*70)
    print("RESUMO DOS TESTES")
    print("="*70)
    print(f"Testes executados: {resultado.testsRun}")
    print(f"Sucessos: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}")
    print(f"Falhas: {len(resultado.failures)}")
    print(f"Erros: {len(resultado.errors)}")
    print("="*70)
    
    # Retorna código de saída apropriado
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(executar_testes())
