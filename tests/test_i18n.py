import unittest
import io
import sys
from contextlib import redirect_stdout
from pybr import PyBRTranspiler

class TestI18n(unittest.TestCase):
    def test_transpilation_all_langs(self):
        langs = {
            'es': ("si Verdadero: pasar", "if True :pass"),
            'de': ("wenn Wahr: pass", "if True :pass"),
            'it': ("se Vero: passa", "if True :pass"),
            'fr': ("si Vrai: passer", "if True :pass")
        }
        for lang, (br, py) in langs.items():
            transpiler = PyBRTranspiler(lang=lang)
            self.assertEqual(transpiler.transpilador(br).strip(), py, f"Failed transpilation for {lang}")

    def test_execution_spanish(self):
        transpiler = PyBRTranspiler(lang='es')
        code = """
si 5 > 2:
    imprimir("Hola")
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        self.assertEqual(f.getvalue().strip(), "Hola")

    def test_execution_german(self):
        transpiler = PyBRTranspiler(lang='de')
        code = """
wenn 5 > 2:
    drucke("Hallo")
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        self.assertEqual(f.getvalue().strip(), "Hallo")

    def test_execution_italian(self):
        transpiler = PyBRTranspiler(lang='it')
        code = """
se 5 > 2:
    stampa("Ciao")
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        self.assertEqual(f.getvalue().strip(), "Ciao")

    def test_execution_french(self):
        transpiler = PyBRTranspiler(lang='fr')
        code = """
si 5 > 2:
    imprimer("Bonjour")
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        self.assertEqual(f.getvalue().strip(), "Bonjour")

    def test_messages_i18n(self):
        msg_checks = {
            'es': "Archivo no encontrado",
            'de': "Datei nicht gefunden",
            'it': "File non trovato",
            'fr': "Fichier non trouvé"
        }
        for lang, expected in msg_checks.items():
            transpiler = PyBRTranspiler(lang=lang)
            self.assertIn(expected, transpiler.messages["file_not_found"])

if __name__ == "__main__":
    unittest.main()
