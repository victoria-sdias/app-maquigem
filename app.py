import os

maquiagens =  [{'nome':'Batom dior', 'categoria':'Batom','cor':'Rosa',}, 
                {'nome':'Batom oboticario','categoria':'Batom','cor':'Vermelho',}]

def exibir_nome_do_programa():
    print('Ｂｅａｕｔｙ Ｂｌｅｎｄ\n')

def exibir_opcoes():
    print('1. Cadastrar novo item de maquigem')
    print('2. Listar minhas maquiagens')
    print('3. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()  

def cadastrar_nova_maquiagem():
    exibir_subtitulo('Cadastro de novas maquiagens')

    nome_do_item_de_maquiagem = input('Digite o nome do item maquiagem que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do item de maquiagem {nome_do_item_de_maquiagem}: ')
    dados_da_maquiagem = {'nome':nome_do_item_de_maquiagem, 'categoria':categoria }
    maquiagens.append(dados_da_maquiagem)
    print(f'O item de maquiagem {nome_do_item_de_maquiagem} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_maquiagens():
    exibir_subtitulo('Listando maquiagens')

    print(f'{'Nome da maquiagem'.ljust(22)} | {'Categoria'.ljust(20)} | {'Cor'.ljust(20)}')
    for maquiagem in maquiagens:
        nome_maquiagem = maquiagem['nome']
        categoria = maquiagem['categoria']
        cor_maquiagem = maquiagem ['cor']
        print(f'- {nome_maquiagem.ljust(20)} | {categoria.ljust(20)} | {cor_maquiagem.ljust(20)}')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_nova_maquiagem()
        elif opcao_escolhida == 2: 
            listar_maquiagens()
        elif opcao_escolhida == 3: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()