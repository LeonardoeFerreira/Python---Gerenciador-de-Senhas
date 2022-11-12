
## Leonardo Ferreira 

def imprimir():
    print('''

    [ 1 ] Incluir Site  
    
    ''')

    print()

#-----------------------------------------------------------------
gerenciador = {}

## Funções

def ler_sites():
    email = input("Digite o email/usuario: ")
    senha = input("Digite a senha: ")
    url = input("Digite a url do site: ")
    return email, senha, url

def editar_sites(sites, email, senha, url):
    gerenciador[sites] = {
        "email": email,
        "senha": senha,
        "url": url
    }
    salvar()
    print()
    print('Site Adicionado...')
    
    


## Salvando dados site   

def salvar():
    exportar_sites("senhas.csv")

def exportar_sites(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for sites in gerenciador:
                email = gerenciador[sites]["email"]
                senha = gerenciador[sites]["senha"]
                url = gerenciador[sites]["url"]
                arquivo.write("{},{},{},{}\n ".format(sites, email, senha, url))
        print("Site exportados com sucesso")
    
    except Exception as erro:
        print("Erro ocorrido...")


## Inicio do programa

while True: 
    opcao = input("Digite uma opção: ")

    if opcao == '1' or opcao == '01':
        sites = input('Digite o nome do site: ')
        if len(sites) <= 2: 
            print("Erro! Nenhum site foi adicionado. ")
        else: 
            try: 
                rr = gerenciador[sites]
                print("Sita já existente......")                 
            except KeyError: 
                email, senha, url = ler_sites()
                editar_sites(sites, email, senha, url)        
   
    
     
