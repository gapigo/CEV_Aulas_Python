import interface, textos, arquivos, dados
from time import sleep

arq = "cursoemvideo"

if not arquivos.arquivoExiste(arq):
    arquivos.criarArquivo(arq)

while True:
    opc = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    sleep(0.5)
    if opc == 1:
        # Opção de listar o conteúdo de um arquivo
        textos.título('PESSOAS CADASTRADAS')
        arquivos.lerArquivo(arq)
    if opc == 2:
        textos.título('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = dados.lerInt('Idade: ')
        arquivos.cadastrar(arq, nome, idade)
    if opc == 3:
        break
    sleep(2)
textos.título('Volte até logo!')
