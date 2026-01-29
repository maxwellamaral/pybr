import unittest
import sys
import os
import io
from contextlib import redirect_stdout

# Adiciona o diretório pai ao sys.path para importar o pybr
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pybr import PyBRTranspiler

class TestMultilingualExamples(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.examples_dir = os.path.join(self.base_dir, 'examples')

    def run_example_file(self, filename, lang, expected_fragments):
        """Helper para executar um arquivo de exemplo e verificar a saída."""
        file_path = os.path.join(self.examples_dir, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()

        transpiler = PyBRTranspiler(lang)
        f_out = io.StringIO()
        
        with redirect_stdout(f_out):
            transpiler.executar(code)
        
        output = f_out.getvalue()
        
        for fragment in expected_fragments:
            self.assertIn(fragment, output, f"Fragmento '{fragment}' não encontrado na saída de {filename} ({lang})")

    def test_exemplo_pt(self):
        self.run_example_file('exemplo_pt.pybr', 'pt-br', [
            "0 é par",
            "1 é ímpar",
            "Rex faz um som"
        ])

    def test_ejemplo_es(self):
        self.run_example_file('ejemplo_es.pybr', 'es', [
            "0 es par",
            "1 es impar",
            "Rex hace un sonido"
        ])

    def test_beispiel_de(self):
        self.run_example_file('beispiel_de.pybr', 'de', [
            "0 ist gerade",
            "1 ist ungerade",
            "Rex macht ein Geräusch"
        ])

    def test_esempio_it(self):
        self.run_example_file('esempio_it.pybr', 'it', [
            "0 è pari",
            "1 è dispari",
            "Rex fa un suono"
        ])

    def test_exemple_fr(self):
        self.run_example_file('exemple_fr.pybr', 'fr', [
            "0 est pair",
            "1 est impair",
            "Rex fait un bruit"
        ])

if __name__ == '__main__':
    unittest.main()
