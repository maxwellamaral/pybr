import unittest
import sys
import os
import io
from contextlib import redirect_stdout

# Add parent directory to path to import pybr
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
        # Test basic execution
        code = """
si 5 > 2:
    imprimir("Hola")
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        self.assertEqual(f.getvalue().strip(), "Hola")

        # Test advanced features (loops, functions, classes, advanced functions)
        advanced_code = """
# Loops
para i en rango(3):
    imprimir(i)

# Functions
definir duplicar(x):
    retornar x * 2

imprimir(duplicar(4))

# Classes
clase Gato:
    definir __init__(propio, nombre):
        propio.nombre = nombre
    
    definir maullar(propio):
        imprimir(f"{propio.nombre} dice Miau")

michi = Gato("Michi")
michi.maullar()

# Advanced Functions
nums = [1, 2]
dobles = lista(mapear(lambda x: x * 2, nums))
imprimir(dobles)
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(advanced_code)
        
        output = f.getvalue().strip().split('\n')
        expected = ['0', '1', '2', '8', 'Michi dice Miau', '[2, 4]']
        self.assertEqual(output, expected, f"Failed advanced Spanish execution. Got: {output}")

    def test_execution_german(self):
        transpiler = PyBRTranspiler(lang='de')
        # Basic execution
        code = """
wenn 5 > 2:
    drucke("Hallo")
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        self.assertEqual(f.getvalue().strip(), "Hallo")

        # Advanced features
        advanced_code = """
# Loops
fuer i in bereich(3):
    drucke(i)

# Functions
definiere verdoppeln(x):
    rueckgabe x * 2

drucke(verdoppeln(4))

# Classes
klasse Katze:
    definiere __init__(selbst, name):
        selbst.name = name
    
    definiere miauen(selbst):
        drucke(f"{selbst.name} sagt Miau")

gatze = Katze("Gatze")
gatze.miauen()

# Advanced Functions
nums = [1, 2]
doppelt = liste(abbilden(lambda x: x * 2, nums))
drucke(doppelt)
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(advanced_code)
        
        output = f.getvalue().strip().split('\n')
        expected = ['0', '1', '2', '8', 'Gatze sagt Miau', '[2, 4]']
        self.assertEqual(output, expected, f"Failed advanced German execution. Got: {output}")

    def test_execution_italian(self):
        transpiler = PyBRTranspiler(lang='it')
        # Basic execution
        code = """
se 5 > 2:
    stampa("Ciao")
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        self.assertEqual(f.getvalue().strip(), "Ciao")

        # Advanced features
        advanced_code = """
# Loops
per i in intervallo(3):
    stampa(i)

# Functions
definisci raddoppia(x):
    ritorna x * 2

stampa(raddoppia(4))

# Classes
classe Gatto:
    definisci __init__(propio, nome):
        propio.nome = nome
    
    definisci miagolare(propio):
        stampa(f"{propio.nome} dice Miao")

micio = Gatto("Micio")
micio.miagolare()

# Advanced Functions
nums = [1, 2]
doppi = lista(mappa(lambda x: x * 2, nums))
stampa(doppi)
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(advanced_code)
        
        output = f.getvalue().strip().split('\n')
        expected = ['0', '1', '2', '8', 'Micio dice Miao', '[2, 4]']
        self.assertEqual(output, expected, f"Failed advanced Italian execution. Got: {output}")

    def test_execution_french(self):
        transpiler = PyBRTranspiler(lang='fr')
        # Basic execution
        code = """
si 5 > 2:
    imprimer("Bonjour")
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(code)
        self.assertEqual(f.getvalue().strip(), "Bonjour")

        # Advanced features
        advanced_code = """
# Loops
pour i dans intervalle(3):
    imprimer(i)

# Functions
definir doubler(x):
    retourner x * 2

imprimer(doubler(4))

# Classes
classe Chat:
    definir __init__(soi, nom):
        soi.nom = nom
    
    definir miauler(soi):
        imprimer(f"{soi.nom} dit Miaou")

minou = Chat("Minou")
minou.miauler()

# Advanced Functions
nums = [1, 2]
doubles = liste(appliquer(lambda x: x * 2, nums))
imprimer(doubles)
"""
        f = io.StringIO()
        with redirect_stdout(f):
            transpiler.executar(advanced_code)
        
        output = f.getvalue().strip().split('\n')
        expected = ['0', '1', '2', '8', 'Minou dit Miaou', '[2, 4]']
        self.assertEqual(output, expected, f"Failed advanced French execution. Got: {output}")

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
