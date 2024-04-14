import json

def AdicionarJogador():
    with open("lista.json", "r") as file:
        data = json.load(file)

    clans = [
            "Bichos do Mato", 
            "Vasco", 
            "Inimigos da Moda",
            "Firebirds",
            "Complexo do Corinthians",
            "Strawberry Tea",
            "Aurora",
            "Cruzeiro",
            "Ranked Beasts",
            "Patota da Moneymatch"
            ]
    hierarquia = ["Lider", "Co-Lider", "Membro"]

    print("- Insira as informações requesitadas -\n")
    nome = str(input("Nome: "))

    print("1 - Lider", "\n2 - Co-Lider", "\n3 - Membro")
    hierarquia = hierarquia[int((input("Hierarquia: "))) - 1]

    custo = int(input("Custo (10 até 120): "))

    numberOfClans = 1
    for nClans in clans:
        print(numberOfClans, " - ", nClans)
        numberOfClans += 1

    clan = clans[int((input("Clan: "))) - 1]

    lenda = str(input("Lenda: "))

    data["jogadores"].append({
        "nome": nome,
        "hierarquia": hierarquia,
        "custo": custo,
        "clan": clan,
        "lenda": lenda
    })

    with open("lista.json", "w") as file:
        json.dump(data, file, indent=4)

def ApagarJogador():
    def display_players(players):
        for index, player in enumerate(players):
            print(f"{index + 1}. {player['nome']} - Clan: {player['clan']}")

    def delete_player(players, index):
        del players[index]

    # Read the existing JSON file and load its contents into a Python dictionary
    with open("lista.json", "r") as file:
        data = json.load(file)
        players = data["jogadores"]

    # Display the current list of players
    print("Lista atual de Jogadores:")
    display_players(players)

    # Ask user for the index of the player to delete
    index_to_delete = int(input("Digite o número ao lado do jogador que quer apagar: ")) - 1

    # Check if the index is valid
    if 0 <= index_to_delete < len(players):
        # Delete the player at the specified index
        delete_player(players, index_to_delete)

        # Write the updated dictionary back to the JSON file
        with open("lista.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Jogador deletado com sucesso.")
    else:
        print("Número invalido, nenhum jogador deletado")

loop = True

while(loop):
    try:
        escolha = int(input("1 - Adicionar Jogador ao arquivo JSON\n2 - Apagar Jogador do arquivo JSON\n3 - Sair\nEscolha: "))
        if(escolha==1):
            AdicionarJogador()
        elif(escolha==2):
            ApagarJogador()
        else:
            loop = False
    except:   
        print("Um erro inesperado aconteceu\n")