
disponiveis = {}
doadores = {}
resultados = {}


def filtro1(disponiveis):
    resultados=disponiveis
    print("Inicializando a busca personalizada...\nPara pular o(s) filtro(s) fornecido(s), apenas pressione 'Enter': ")
    while True:
        sexoselecionado=str(input("Qual o sexo desejado? Digite 'm' para macho ou 'f' para fêmea: "))
        if sexoselecionado not in ['m','f','']:
            print("Erro! Por favor, tente novamente.")
        elif sexoselecionado=='':
            print("O filtro de sexo não foi aplicado.")
        else:
            resultados = {nome: detalhes for nome, detalhes in resultados.items() if detalhes['sexo'] == sexoselecionado}
        filtro2(resultados)

def filtro2(resultados):
    while True:
        porteselecionado=str(input("Qual o porte desejado? Digite 'p' para pequeno, 'm' para médio ou 'g' para grande: "))
        if porteselecionado not in ['p','m','g','']:
            print("Erro! Por favor, tente novamente.")
        elif porteselecionado=='':
            print("O filtro de porte não foi aplicado.")
        else:
            resultados = {nome: detalhes for nome, detalhes in resultados.items() if detalhes['porte'] == porteselecionado}
        filtro3(resultados)

def filtro3(resultados):
    while True:
        idadeselecionada=str(input("Qual a idade desejada? Digite 'filhote', 'adulto' ou 'idoso': "))
        if idadeselecionada not in ['filhote','adulto','idoso','']:
            print("Erro. Por favor, tente novamente.")
        elif idadeselecionada=='':
            print("O filtro de idade não foi aplicado.")
        else:
            resultados = {nome: detalhes for nome, detalhes in resultados.items() if detalhes['idade'] == idadeselecionada}
        filtro4(resultados)

def filtro4(resultados):
        tempselecionado=int(input("Qual o temperamento do cão que deseja? Insira um número de 0 a 10 (sendo 0 o mais dócil possível e 10 o mais agressivo possível): ")) #erro: tem que encerrar esse loop
        if tempselecionado not in [0,1,2,3,4,5,6,7,8,9,'']:
            print("Erro. Por favor, tente novamente.")
            filtro4(resultados)
        elif tempselecionado=='':
            print("O filtro de temperamento não foi aplicado.")
        else:
            resultados = {nome: detalhes for nome, detalhes in resultados.items() if detalhes['temperamento'] == tempselecionado}
        resultadopesquisa(resultados):
    
def cadastrodoador(nomedoador):
  while True:
     teldoador = input("Informe o seu número de celular, com DDD, na forma 11987654321: ")
     if len(teldoador) == 10 or len(teldoador) == 11 and teldoador[0] != 0 and teldoador[1] != 0 and teldoador.isnumeric():  # alguns números de regiões do Brasil possuem 8 dígitos e nenhum DDD possui 0 nos seus 2 dígitos.
         emaildoador = str(input("Informe o seu e-mail: "))
         locdoador = input("Você reside em que de algum estado? Se sim, digite '1': ")
         if locdoador == '1':
             localdoador = str(input("Insira a cidade em que você está localizado: "))
         else:
             localdoador = str(input("Qual a capital mais próxima da cidade onde você está localizado? "))  # precisa verificar se o nome da cidade ta no dicionario do Davi (usar if)
         doadores[nomedoador] = {"telefone": teldoador, "e-mail": emaildoador, "localizacao": localdoador}
         print(doadores) 
         print("Seus dados foram cadastrados com sucesso. Prosseguindo com o cadastro do cão...")
         cadastrocao1()
     else:
      print("Número de telefone inválido. Tente novamente.")

def cadastrocao1():
  nome=str(input("Qual o nome do cão? "))
  while True:
    sexo=str(input("Qual o sexo do cão? Digite 'm' para macho ou 'f' para fêmea: "))
    if sexo=="m" or sexo=="f":
      portecao(nome,sexo)
    else:
      print("Dados inválidos. Por favor, tente novamente.")

def portecao(nome,sexo):
  while True:
    porte=str(input("Qual o porte? Digite 'p' para pequeno, 'm' para médio ou 'g' para grande: "))
    if porte=="p" or porte=="m" or porte=="g":
      idadecao(nome,sexo,porte)
    else:
      ajudaporte=str(input("Inválido. Por favor, classifique quanto ao seu porte. Para ajuda, digite 'ajuda': ")) #precisa testar se isso funciona
      if ajudaporte=="ajuda":
        print("Os portes de cães são determinados pelo seu peso.\nPORTE PEQUENO: até 15kg\nPORTE MÉDIO: de 15kg a 25kg\nPORTE GRANDE: acima de 25kg")

def idadecao(nome,sexo,porte):
  while True:
    idade=str(input("Em relação à idade, o cão pode ser classificado como: filhote, adulto, idoso ou indefinido? "))
    if idade == "filhote" or idade == "adulto" or idade == "idoso" or idade == "indefinido":
      raca=str(input("O cão possui raça definida? Se sim, informe o nome da raça. Caso contrário, digite 'indefinido': "))
      pesocao(nome,sexo,porte,idade,raca)
    else:
      ajudaidade=str(input("Inválido. Por favor, classifique o seu cão quanto à idade. Para mais ajuda, digite 'ajuda': ")) #tbm precisa testar esse
      if ajudaidade=="ajuda":
        print("A idade dos cães é determinada pelas seguintes fases da vida:\nPFILHOTE: até 12 meses ou 1 ano de vida\nADULTO: de 1 ano até 7 anos de vida\nIDOSO: acima de 7 anos de vida")

def pesocao(nome,sexo,porte,idade,raca):
  while True:
    peso=float(input("Qual o peso do animal, em kg? "))
    if peso<=0:
      print("Valor incorreto. Por favor, tente novamente.")
    else:
      tempcao(nome,sexo,porte,idade,raca,peso)


def tempcao(nome,sexo,porte,idade,raca,peso): 
  while True:
    temp=int(input("Em uma escala de 0 a 10, sendo 0 completamente dócil e 10 extremamente agressivo, como seria classificado o temperamento do seu cão? "))
    if temp>10 or temp<0:
      print("Valor fora da escala. Por favor, tente novamente.")
    else:
      disponiveis[nome]={"sexo": sexo, "porte": porte, "idade": idade, "raca": raca, "peso": peso, "temperamento": temp}
      print("Suas informações foram cadastradas com sucesso.")
      main()

#MENU INICIAL:
def main():
  while True:
    pergunta=str(input("\nBem-vindo ao iPet! Estamos felizes em ter você aqui! Aqui, conectamos pessoas com cães adoráveis \nque aguardam por um lar cheio de amor, e também ajudamos você a encontrar um novo lar para o seu \nanimal de estimação. Cadastre-se para doar o seu animal ou navegue e conheça nossos amigos de \nquatro patas. Cada um deles está ansioso para encontrar uma nova família. Obrigado por considerar \na adoção e por fazer a diferença na vida desses cães.\n\nVocê deseja: \n1)Doar um cão \n2)Adotar um cão\n\n"))
    if pergunta == "1":
      nomedoador=str(input("Por favor, insira o seu nome completo: "))
      cadastrodoador(nomedoador)
    elif pergunta== "2":
      filtro1(disponiveis)
main()
