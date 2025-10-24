"""
This file contains the User Interface functions
"""

import datetime

def menu_interface():
    
    hoje = datetime.datetime.now()

    print("\n__ MENU PRINCIPAL __\n")
    print("1) Cadastrar alunos")
    print("2) Visualizar alunos")
    print("3) Editar aluno")
    print("4) Remover aluno")
    print("5) Sair")

    print(f"\n" + hoje.strftime("%x"))