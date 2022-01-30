from controllers.controller import jogador, jogo, federacao, torneio

jogador(1, "Magnus", "Grande Mestre", "Noruegues", 2900)
jogador(1, "Nakamura", "Grande Mestre", "Japonês", 2450)
jogador(1, "Krikor", "Grande Mestre", "Brasileiro", 2600)
jogador(1, "Fischer", "Grande Mestre", "Estado-unidense", 3000)

jogo(1, 4, "Ruy-Lopez", 61, 0)
jogo(3, 4, "Gambito do rei", 21, 0)
jogo(3, 2, "Gambito da rainha", 21, 1)
jogo(3, 1, "GROB", 7, 0)
jogo(4, 2, "Escandinava", 21, 1)
jogo(1, 2, "Sciliana Aberta", 100, 1)

federacao("FBX", 125)
federacao("FOAP", 500)
federacao("ECC", 125)

torneio(1, 3, 5, 1, 2, "Nenhum")
torneio(2, 2, 6, 2, 3, "Nenhum")
torneio(3, 1, 7, 3, 4, "Nenhum")
torneio(4, 3, 8, 4, 1, "Nenhum")
