import students_functions as sf
import datetime

def main_menu():
    Check = False

    hoje = datetime.datetime.now()

    print("\n__ MENU PRINCIPAL __\n")
    print("1) Cadastrar alunos")
    print("2) Visualizar alunos")
    print("3) Editar aluno")
    print("4) Remover aluno")
    print("5) Sair")

    print(f"\n" + hoje.strftime("%x"))

    while (Check == False):
        try:
            option = int(input("\nSelecione uma das opcoes Acima: "))

            if option == 1:

                nome_aluno = str(input("Informe o nome do aluno: "))

                status_aluno = str(input("Este aluno está tendo aulas? (S/N): ")).upper()
                if status_aluno == "S":
                    status_aluno = "Ativo"
                elif status_aluno == "N":
                    status_aluno = "Deligado"
                else:
                    status_aluno = "UNKNOWN"

                aulas_aluno = int(input("Informe quantas aulas o aluno assistiu: "))
                pagamento_aluno = str(input("Informe a data do pagamento: "))
                nivel_aluno = str(input("Informe o nível do aluno: "))

                novo_Aluno = sf.cadastrar_aluno(nome_aluno, 
                                                status_aluno, 
                                                aulas_aluno,
                                                pagamento_aluno,
                                                nivel_aluno,)

            elif option == 2:
                sf.visualizar_alunos()

            elif option == 3:
                lock = False

                print("\nInformações a serem alteradas:")

                print("1 - Nome")
                print("2 - Status")
                print("3 - Quantidade de aulas")
                print("4 - Dia do pagamento")
                print("5 - Nivel do aluno")
                
                sub_menu = int(input("Selecione uma opcao: "))
                
                while (lock == False):
                    if sub_menu == 1:
                        lock == True
                        new_nome = str(input("Insira o novo nome do aluno: "))

                    elif sub_menu == 2:
                        lock == True
                        new_status = str(input("Insira o novo Status do aluno: "))
                        if new_status == "S":
                            new_status = "Ativo"
                        elif new_status == "N":
                            new_status = "Deligado"
                        else:
                            new_status = "UNKNOWN"


                    elif sub_menu == 3:
                        lock == True
                        new_aulas = str(input("Insira a quantidade de aulas: "))
                        
                    elif sub_menu == 4:
                        lock == True
                        new_pagamento = str(input("Insira o dia de pagamento: "))
                        
                    elif sub_menu == 5:
                        lock == True
                        new_nivel = str(input("Insira o nivel do aluno: "))
                        
                    else:
                        lock == False

                

            elif option == 4:
                nome_aluno = str(input("Informe o nome do aluno: "))
                sf.remover_aluno(nome_aluno)

            elif option == 5:
                print("\nSaindo do programa...")
                break

            else:
                print(f"A Opção '{option}' não exite.")

        except:
            print(f"Este Caractere provavelmente não é inteiro.")
            Check = False
    
main_menu()