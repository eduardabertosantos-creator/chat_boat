def limpar_texto(texto):
    texto = texto.strip().lower()
    substituicoes = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e',
        'í': 'i',
        'ó': 'o', 'õ': 'o', 'ô': 'o',
        'ú': 'u', 'ü': 'u',
        'ç': 'c',
        '?': '', '!': '', '.': '', ',': ''
    }
    for antigo, novo in substituicoes.items():
        texto = texto.replace(antigo, novo)
    return texto

def ensinar():
    pergunta = input("Digite a pergunta: ").strip().lower()
    resposta = input("Digite a resposta: ").strip().lower()
    with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n{pergunta} - {resposta}")
    print("bot: Aprendi!")

def conversar():
    print("\n--- Modo Conversa (digite 'voltar' para sair) ---")
    while True:
        fala = input("Você: ")
        if limpar_texto(fala) == "voltar":
            break
            
        encontrou = False
        try:
            with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    dados = linha.strip().split(" - ")
                    if len(dados) == 2:
                        pergunta_salva = dados[0]
                        resposta_salva = dados[1]
                        if limpar_texto(fala) == limpar_texto(pergunta_salva):
                            print(f"bot: {resposta_salva}")
                            encontrou = True
                            break
            if not encontrou:
                print("bot: Desculpa, não sei a resposta. Digite 'voltar' e use a opção 2 para me ensinar.")
        except FileNotFoundError:
            print("bot: Meu cérebro está vazio! Me ensine algo primeiro.")
            break

def listar_conhecimento():
    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("bot: Meu cérebro está vazio!")
                return
            print("\n--- O que eu já sei ---")
            for linha in linhas:
                dados = linha.strip().split(" - ")
                if len(dados) == 2:
                    print(f"Pergunta: {dados[0]} | Resposta: {dados[1]}")
            print("-----------------------\n")
    except FileNotFoundError:
        print("bot: Meu cérebro está vazio! Me ensine algo primeiro.")

while True:
    print("\n=== MENU DO CHATBOT ===")
    print("1 - Conversar")
    print("2 - Ensinar")
    print("3 - Listar conhecimento")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        conversar()
    elif opcao == "2":
        ensinar()
    elif opcao == "3":
        listar_conhecimento()
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
