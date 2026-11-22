import json
caminho = "dados/snes_jogos_com_capas.json"
with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
#print(type(dados[0]))
#print(len(dados))
#print(len(dados[0]))
#print(dados[0].keys())
#print(dados[0]["jogo"])
#print(dados[0]["genero"])
generos_escolhidos = []
contador = 0
escolha = int(input("Escolha o gênero de jogo que deseja buscar:"))

if escolha == 1:
    genero_escolhido = "Plataforma"
elif escolha == 2:
    genero_escolhido = "RPG"
elif escolha == 3:
    genero_escolhido = "Ação"
elif escolha == 4:
    genero_escolhido = "Corrida"
else :
    print("Opção inválida")
    exit()


for jogo in dados:
    if jogo["genero"] in generos_escolhidos or jogo["jogadores_max"] == 1:
        print(jogo["jogo"])
        contador += 1

print(f"Total de jogos encontrados: {contador}")