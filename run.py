# -*- coding: utf-8 -*-
import os
import sys

# Adiciona o diretório src ao sys.path para permitir importações de src.*
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src import create_app

app = create_app()

if __name__ == "__main__":
    # Executa a aplicação Flask
    app.run(host="0.0.0.0", port=5000, debug=True)
