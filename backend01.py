nome = "Renato"
sobrenome = "Rosa"
nome_completo = nome + " " + sobrenome
nome_completo2 = f"(nome) (sobrenome)"
print(nome_completo)

# fatiamento
print("primeira letra", nome[0])
print("primeira letra", nome[1:45])



#Metodos principais

print("Maiuscula", nome.upper())
print("Minuscula", nome.lower())
print(nome_completo)
print("Titulo", nome_completo.title())
print("Titulo", nome_completo.title().replace("Rosa", "Filho"))
print("Split", nome_completo.split(" "))


print("##################################################################")

idade = 34
print("Idade:", idade)
print("Idade x 2:", idade*2)
print("Idade : 2:", idade/2)
print("Potência:", idade**2)
print("Resto da divisão", idade % 5)

print("##################################################################")


#Funções

print("Minimo", min(3,7,1,2,3,5,7,4,2,9))
print("Máximo", max(3,7,1,2,3,5,7,4,2,9))
print("Absoluto", abs(-20))
print("Arredondar", round(20.235645))

print("##################################################################")

#Float

altura = 1.84
#Operações Float
print("Altura", altura)
print("Altura x 2:", altura * 2)
print("Altura : 3", altura /3)

#Operações com float
print("Arredondamento:", round(altura,3))


#Biblioteca

import math

print("Raiz quadrada:", math.sqrt(16))
print("PI:", math.pi)

print("##################################################################")

instrutor = True
ativo = False

# Comparações retornam bool

print("10 > 5?", 10 > 5)
print("10 == 5?", 10 == 5)
print("10 < 5?", 10 < 5)


# Uso em if

if instrutor:
    print("É instrutor")
else:
    print("Não é instrutor")

print("Verdade" if instrutor else "Mentira")


##################Revisão de Lista##########################################
cores = ["vermeljo", "azul", "Verde"]
#Acesso e fatiamento
print("Primeira cor:", cores[1][1])

#Metodos principais
#Adiciona
cores.append("Amarelo")
print("Após append:", cores)

#Remover
cores.remove("Verde")
print("Após remove:", cores)

print("Quantidade:", len(cores))

cores2 = cores
cores.append("Laranja")

print("cores1", cores)
print("cores2", cores2)
cores2[1] = "Cinza"
print("cores2", cores)

print("##################################################################")

cores2 = cores.copy()
cores.append("Laranja")

print("cores1", cores)
print("cores2", cores2)



print("######################Revi~sao Tupla############################################")

par = (1,2,4)
print(par)
print(par)
print("primeiro", par[0])
print("Último", par[-1])



print("Comprimento", len(par))
print("Existe 2?", 3 in par)

######################Revisão Dicionário################################################

config = {"modo": "aula", "nivel": "inicial"}
print(config)

#Acesso
print("nivel", config["nivel"])
print("nivel", config.get("nivel"))

#Adição/alteação
config["Turma"] = "Python 1"
print(config)

#Metodos principais

print("Chaves", config.keys())
print("valores", config.values())
print("Itens", config.items())



#######Exercicios########################


def primeiraFuncao(txt):
    return txt.upper()

print(primeiraFuncao(nome))

print("######################Revi~sao Tupla############################################")

def segundaFuncao 
