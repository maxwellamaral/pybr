"""
Testes Funcionais para os Exercícios PyBR
==========================================

Este script testa todos os arquivos de exemplo na pasta exercicios/
para garantir que estão funcionando corretamente.
"""

import unittest
import subprocess
import sys
import os
from io import StringIO
from pathlib import Path


class TestExercicios(unittest.TestCase):
    """Testa a execução de todos os arquivos de exercícios"""
    
    @classmethod
    def setUpClass(cls):
        """Configuração inicial dos testes"""
        cls.exercicios_dir = Path("exercicios")
        cls.pybr_script = Path("pybr.py")
        
        # Verifica se os diretórios existem
        if not cls.exercicios_dir.exists():
            raise FileNotFoundError(f"Diretório {cls.exercicios_dir} não encontrado")
        if not cls.pybr_script.exists():
            raise FileNotFoundError(f"Script {cls.pybr_script} não encontrado")
    
    def executar_pybr(self, arquivo, entrada=None, timeout=5):
        """
        Executa um arquivo .pybr e retorna o resultado
        
        Args:
            arquivo: Path do arquivo .pybr
            entrada: String com entradas simuladas (separadas por \n)
            timeout: Timeout em segundos
            
        Returns:
            tuple: (codigo_saida, stdout, stderr)
        """
        cmd = [sys.executable, str(self.pybr_script), str(arquivo)]
        
        try:
            resultado = subprocess.run(
                cmd,
                input=entrada,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=timeout
            )
            return resultado.returncode, resultado.stdout, resultado.stderr
        except subprocess.TimeoutExpired:
            return -1, "", "Timeout excedido"
    
    def test_01_ola_mundo(self):
        """Teste: 01-ola-mundo.pybr"""
        arquivo = self.exercicios_dir / "01-ola-mundo.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Olá, Mundo!", stdout)
        self.assertIn("PyBR é demais!", stdout)
    
    def test_02_variaveis(self):
        """Teste: 02-variaveis.pybr"""
        arquivo = self.exercicios_dir / "02-variaveis.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Maria", stdout)
        self.assertIn("25", stdout)
        # Aceita 19.9 ou 19.90
        self.assertTrue("19.9" in stdout or "19.90" in stdout)
    
    def test_03_calculos(self):
        """Teste: 03-calculos.pybr"""
        arquivo = self.exercicios_dir / "03-calculos.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("15", stdout)  # 10 + 5
        self.assertIn("42", stdout)  # 6 * 7
        self.assertIn("CALCULADORA DE COMPRAS", stdout)
    
    def test_04_entrada_saida(self):
        """Teste: 04-entrada-saida.pybr"""
        arquivo = self.exercicios_dir / "04-entrada-saida.pybr"
        entrada = "João\n25\nSão Paulo\n"
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Olá, João", stdout)
        self.assertIn("25", stdout)
    
    def test_05_calculadora_imc(self):
        """Teste: 05-calculadora-imc.pybr"""
        arquivo = self.exercicios_dir / "05-calculadora-imc.pybr"
        entrada = "Maria\n70\n1.70\n"
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("IMC", stdout)
        self.assertIn("Maria", stdout)
    
    def test_06_condicionais(self):
        """Teste: 06-condicionais.pybr"""
        arquivo = self.exercicios_dir / "06-condicionais.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("maior de idade", stdout)
        self.assertIn("Pode dirigir", stdout)
    
    def test_07_sistema_login(self):
        """Teste: 07-sistema-login.pybr"""
        arquivo = self.exercicios_dir / "07-sistema-login.pybr"
        
        # Teste com login correto
        entrada = "admin\n1234\n"
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Login realizado", stdout)
        
        # Teste com login incorreto
        entrada = "usuario\nsenha\n"
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("incorretos", stdout)
    
    def test_08_lacos_para(self):
        """Teste: 08-lacos-para.pybr"""
        arquivo = self.exercicios_dir / "08-lacos-para.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("0", stdout)
        self.assertIn("1", stdout)
        self.assertIn("Lancamento", stdout)
    
    def test_09_tabuada(self):
        """Teste: 09-tabuada.pybr"""
        arquivo = self.exercicios_dir / "09-tabuada.pybr"
        entrada = "5\n"
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Tabuada do 5", stdout)
        self.assertIn("5 x 1 = 5", stdout)
        self.assertIn("5 x 10 = 50", stdout)
    
    def test_10_enquanto(self):
        """Teste: 10-enquanto.pybr"""
        arquivo = self.exercicios_dir / "10-enquanto.pybr"
        entrada = "5\n3\n0\n"
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Contador", stdout)
        self.assertIn("Soma total", stdout)
    
    def test_11_jogo_adivinhacao(self):
        """Teste: 11-jogo-adivinhacao.pybr"""
        arquivo = self.exercicios_dir / "11-jogo-adivinhacao.pybr"
        entrada = "50\n42\n"  # Tenta 50, depois acerta com 42
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Parabens", stdout)
        self.assertIn("tentativas", stdout)
    
    def test_12_listas(self):
        """Teste: 12-listas.pybr"""
        arquivo = self.exercicios_dir / "12-listas.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("maçã", stdout)
        self.assertIn("banana", stdout)
        self.assertIn("morango", stdout)
    
    def test_13_funcoes_simples(self):
        """Teste: 13-funcoes-simples.pybr"""
        arquivo = self.exercicios_dir / "13-funcoes-simples.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("bem-vindo", stdout)
        self.assertIn("Maria", stdout)
        self.assertIn("média", stdout)
    
    def test_14_funcoes_retorno(self):
        """Teste: 14-funcoes-retorno.pybr"""
        arquivo = self.exercicios_dir / "14-funcoes-retorno.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("15", stdout)  # 10 + 5
        self.assertIn("42", stdout)  # 6 * 7
        self.assertIn("Erro", stdout)  # Divisão por zero
    
    def test_15_calculadora_funcoes(self):
        """Teste: 15-calculadora-funcoes.pybr"""
        arquivo = self.exercicios_dir / "15-calculadora-funcoes.pybr"
        entrada = "1\n10\n5\n"  # Opção 1 (somar), 10 + 5
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("15", stdout)
    
    def test_16_classe_cachorro(self):
        """Teste: 16-classe-cachorro.pybr"""
        arquivo = self.exercicios_dir / "16-classe-cachorro.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Rex", stdout)
        self.assertIn("Au au", stdout)
        self.assertIn("Labrador", stdout)
    
    def test_17_classe_conta_bancaria(self):
        """Teste: 17-classe-conta-bancaria.pybr"""
        arquivo = self.exercicios_dir / "17-classe-conta-bancaria.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("João", stdout)
        self.assertIn("Maria", stdout)
        self.assertIn("Saldo", stdout)
        self.assertIn("insuficiente", stdout)
    
    def test_18_classe_retangulo(self):
        """Teste: 18-classe-retangulo.pybr"""
        arquivo = self.exercicios_dir / "18-classe-retangulo.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Retângulo", stdout)
        self.assertIn("Área", stdout)
        self.assertIn("Perímetro", stdout)
    
    def test_19_classe_aluno(self):
        """Teste: 19-classe-aluno.pybr"""
        arquivo = self.exercicios_dir / "19-classe-aluno.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Carlos Silva", stdout)
        self.assertIn("APROVADO", stdout)
        self.assertIn("Boletim", stdout)
    
    def test_20_projeto_lista_tarefas(self):
        """Teste: 20-projeto-lista-tarefas.pybr"""
        arquivo = self.exercicios_dir / "20-projeto-lista-tarefas.pybr"
        entrada = "1\nEstudar PyBR\n2\n4\n"  # Adiciona tarefa, lista, sai
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("Estudar PyBR", stdout)
        self.assertIn("adicionada", stdout)
    
    def test_21_projeto_quiz(self):
        """Teste: 21-projeto-quiz.pybr"""
        arquivo = self.exercicios_dir / "21-projeto-quiz.pybr"
        entrada = "3\n3\n2\n3\n4\n"  # Respostas para as 5 perguntas
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("QUIZ", stdout)
        self.assertIn("RESULTADO FINAL", stdout)
    
    def test_22_projeto_conversor_temperatura(self):
        """Teste: 22-projeto-conversor-temperatura.pybr"""
        arquivo = self.exercicios_dir / "22-projeto-conversor-temperatura.pybr"
        entrada = "1\n100\n5\n"  # Opção 1 (C->F), temperatura 100, depois sai
        codigo, stdout, stderr = self.executar_pybr(arquivo, entrada)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("212", stdout)  # 100°C = 212°F
    
    def test_23_funcoes_avancadas(self):
        """Teste: 23-funcoes-avancadas.pybr"""
        arquivo = self.exercicios_dir / "23-funcoes-avancadas.pybr"
        codigo, stdout, stderr = self.executar_pybr(arquivo)
        
        self.assertEqual(codigo, 0, f"Erro na execução: {stderr}")
        self.assertIn("FUNÇÕES LAMBDA", stdout)
        self.assertIn("MAPEAR", stdout)
        self.assertIn("FILTRAR", stdout)
        self.assertIn("Dobro de 5: 10", stdout)
        self.assertIn("Apenas pares:", stdout)
        self.assertIn("QUALQUER e TODOS", stdout)


class TestTranspilacaoExercicios(unittest.TestCase):
    """Testa se todos os arquivos podem ser transpilados sem erros"""
    
    def test_todos_arquivos_transpilam(self):
        """Verifica se todos os .pybr podem ser transpilados"""
        # Importa as funções do pybr
        sys.path.insert(0, '.')
        from pybr import PyBRTranspiler
        
        transpiler = PyBRTranspiler()
        exercicios_dir = Path("exercicios")
        arquivos_pybr = sorted(exercicios_dir.glob("*.pybr"))
        
        self.assertGreater(len(arquivos_pybr), 0, "Nenhum arquivo .pybr encontrado")
        
        sucessos = 0
        for arquivo in arquivos_pybr:
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    codigo_pybr = f.read()
                
                # Tenta transpilar
                codigo_python = transpiler.transpilador(codigo_pybr)
                
                # Verifica se retornou algo
                self.assertIsNotNone(codigo_python, f"Transpilação retornou None para {arquivo.name}")
                self.assertGreater(len(codigo_python), 0, f"Transpilação retornou string vazia para {arquivo.name}")
                # Verifica que não há erro de sintaxe
                self.assertNotIn("Erro de Sintaxe", codigo_python, f"Erro de sintaxe em {arquivo.name}")
                
                sucessos += 1
                
            except Exception as e:
                self.fail(f"Erro ao transpilar {arquivo.name}: {str(e)}")
        
        print(f"\nTranspilação bem-sucedida: {sucessos}/{len(arquivos_pybr)} arquivos")


def main():
    """Função principal para executar os testes"""
    print("=" * 70)
    print("TESTES FUNCIONAIS DOS EXERCÍCIOS PYBR")
    print("=" * 70)
    print()
    
    # Configura o test runner
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adiciona os testes
    suite.addTests(loader.loadTestsFromTestCase(TestExercicios))
    suite.addTests(loader.loadTestsFromTestCase(TestTranspilacaoExercicios))
    
    # Executa os testes
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Resumo
    print()
    print("=" * 70)
    print("RESUMO DOS TESTES")
    print("=" * 70)
    print(f"Testes executados: {resultado.testsRun}")
    print(f"Sucessos: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}")
    print(f"Falhas: {len(resultado.failures)}")
    print(f"Erros: {len(resultado.errors)}")
    print("=" * 70)
    
    # Retorna código de saída apropriado
    return 0 if resultado.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())
