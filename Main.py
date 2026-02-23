for i in range(5):
    word = input("Digite uma palavra moderna que você não entende: ")
    palavra = {
                "cringe": "Algo vergonhoso ou constrangedor",
                "stalkear": "Investigar a vida de alguém online",
                "mogar": "humilhar",
                "farmar aura": "uma situação em que se saiu por cima, tipo a expreção: debulhar"
                "absolute cinema": "uma cena imprecionante,impactante ou muito boa "
            }
    if word in palavra.keys():
        print(palavra[word])
    else:
        print("desculpe, não temos essa palavra no nosso dicionario")
