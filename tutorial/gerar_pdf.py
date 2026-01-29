import os
import shutil
import subprocess
import sys

# Configuration for each language
TUTORIALS = [
    {
        "lang": "pt-BR",
        "input": "tutorial-iniciantes.md",
        "output": "tutorial-iniciantes.pdf",
        "title": "PyBR - Python em Português",
        "subtitle": "Tutorial Completo para Iniciantes",
        "description": "Aprenda programação em Python usando português",
        "footer": "PyBR - Python Brasileiro"
    },
    {
        "lang": "es-ES",
        "input": "tutorial-es.md",
        "output": "tutorial-es.pdf",
        "title": "PyBR - Guía para Principiantes",
        "subtitle": "Guía Completa para Principiantes",
        "description": "Aprende a programar en Python usando español",
        "footer": "PyBR - Python Internacional"
    },
    {
        "lang": "de-DE",
        "input": "tutorial-de.md",
        "output": "tutorial-de.pdf",
        "title": "PyBR - Einsteigerhandbuch",
        "subtitle": "Vollständiges Handbuch für Anfänger",
        "description": "Lernen Sie Python-Programmierung auf Deutsch",
        "footer": "PyBR - Python International"
    },
    {
        "lang": "it-IT",
        "input": "tutorial-it.md",
        "output": "tutorial-it.pdf",
        "title": "PyBR - Guida per Principianti",
        "subtitle": "Guida Completa per Principianti",
        "description": "Impara a programmare in Python usando l'italiano",
        "footer": "PyBR - Python Internazionale"
    },
    {
        "lang": "fr-FR",
        "input": "tutorial-fr.md",
        "output": "tutorial-fr.pdf",
        "title": "PyBR - Guide pour Débutants",
        "subtitle": "Guide Complet pour Débutants",
        "description": "Apprendre la programmation Python en français",
        "footer": "PyBR - Python International"
    }
]

def check_dependencies():
    """Checks if pandoc and pdftotext are installed."""
    missing = []
    if not shutil.which("pandoc"):
        missing.append("pandoc")
    if not shutil.which("pdftotext"):
        missing.append("poppler-utils (pdftotext)")
    
    if missing:
        print(f"❌ Error: Missing dependencies: {', '.join(missing)}")
        sys.exit(1)
    print("✓ Dependencies found")

def get_emoji_font():
    """Detects the appropriate emoji font based on the OS."""
    if sys.platform == "darwin":
        return "Apple Color Emoji"
    
    # Check for Noto or DejaVu on Linux
    try:
        fonts = subprocess.check_output(["fc-list", ":", "family"], text=True)
        if "DejaVu Sans" in fonts:
            return "DejaVu Sans"
        elif "Noto Color Emoji" in fonts:
            return "Noto Color Emoji"
    except Exception:
        pass
    
    return "DejaVu Sans" # Fallback

def generate_pdf(config, base_header, emoji_font):
    """Generates a PDF for a specific language configuration."""
    print(f"\nProcessing {config['lang']} ({config['output']})...")
    
    if not os.path.exists(config['input']):
        print(f"  ⚠️  Input file {config['input']} not found. Skipping.")
        return False

    # 1. Prepare localized header
    header_content = base_header.replace("$subtitle$", config['subtitle'])
    header_content = header_content.replace("$description$", config['description'])
    header_content = header_content.replace("$footer_text$", config['footer'])
    header_content = header_content.replace("Segoe UI Emoji", emoji_font)
    
    header_tmp = f"header_{config['lang']}.tex"
    with open(header_tmp, "w", encoding="utf-8") as f:
        f.write(header_content)

    # 2. Run Pandoc
    cmd = [
        "pandoc",
        config['input'],
        "-o", config['output'],
        "--pdf-engine=xelatex",
        "-H", header_tmp,
        "-V", "geometry:margin=1in",
        "-V", "documentclass=article",
        "-V", "papersize=a4",
        "-V", f"title={config['title']}",
        "-V", "author=Maxwell Anderson Ielpo do Amaral",
        "-V", "date=Janeiro/2026",
        "--toc",
        "--toc-depth=2",
        "-V", f"lang={config['lang']}"
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print("  ✓ PDF generated")
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Pandoc failed: {e.stderr.decode()}")
        if os.path.exists(header_tmp): os.remove(header_tmp)
        return False

    # 3. Verify PDF content
    try:
        # Extract first page text
        text = subprocess.check_output(
            ["pdftotext", "-f", "1", "-l", "1", config['output'], "-"], 
            text=True
        )
        
        if config['subtitle'] in text:
            print(f"  ✓ Verification passed: Subtitle found.")
        else:
            print(f"  ❌ VERIFICATION FAILED: Subtitle '{config['subtitle']}' not found in PDF!")
            # Debug: print what was found
            # print(f"Found text: {text[:200]}...") 
            if os.path.exists(header_tmp): os.remove(header_tmp)
            return False

    except Exception as e:
        print(f"  ⚠️  Verification failed (is pdftotext working?): {e}")
    
    # Cleanup
    if os.path.exists(header_tmp):
        os.remove(header_tmp)
    
    return True

def main():
    print("=== PyBR PDF Generator & Verifier ===")
    check_dependencies()
    
    if not os.path.exists("header.tex"):
        print("❌ header.tex not found!")
        sys.exit(1)
        
    with open("header.tex", "r", encoding="utf-8") as f:
        base_header = f.read()
    
    emoji_font = get_emoji_font()
    print(f"✓ Using emoji font: {emoji_font}")
    
    success_count = 0
    for config in TUTORIALS:
        if generate_pdf(config, base_header, emoji_font):
            success_count += 1
            
    print(f"\nFinished! {success_count}/{len(TUTORIALS)} PDFs generated successfully.")

if __name__ == "__main__":
    main()
