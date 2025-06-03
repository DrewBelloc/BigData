ruas = [
    ["oscar gomes","1"],
    ["aurino de sa leitao","2"],
    ["heitor mata","3"],
    ["euclides lopes da silva","4"],
    ["isabel ribeiro volp","5"],
    ["professora aida de souza faria","6"],
    ["jockey club 2","7"],
    ["jockey club 5","8"],
    ["antenor rodrigues","9"],
    ["eneida de freitas medeiros","10"],
    ["marina pinheiro de souza","11"],
    ["melquiades peres","12"],
    ["joao froes de abreu","13"],
    ["delfino paulo da costa","14"],
    ["lila de albuquerque","15"],
    ["andre pereira dias","16"],
    ["magestic","17"],
    ["francisco gomes marafone","18"],
    ["claudio de barros","19"],
    ["manoel alves de souza","20"],
    ["cisplatina","21"],
    ["carlota de almeida","22"],
    ["jose melo pires","23"],
    ["laercio xavier de mendonça","24"],
    ["aristide xavier","25"],
    ["cozumel 1","26"],
    ["cozumel 2","27"],
    ["cozumel 3","28"],
    ["gaivotas","29"],
    ["araras","30"],
    ["sabia","31"],
    ["gaivotas","32"],
    ["aruba","33"],
    ["alberto nemer","34"],
    ["orlando jose de araujo","35"],
    ["diamantino gonçalves","36"],
    ["topazio","37"],
    ["maria dos anjos","38"],
    ["alcebiades caldeira","39"],
    ["alberico luciano barbosa","40"],
    ["manoel gomes de abreu","41"],
    ["jose belford filho","42"],
    ["edna leite de queiros","43"],
    ["luis lopes","44"],
    ["clodomiro antunes da costa","45"],
    ["eugenio borges","46"],
    ["village do moinho 1","47"],
    ["village do moinho 2","48"],
    ["village do moinho 3","49"],
    ["monte verde","50"],
    ["caetano fernandes","51"],
    ["avenida do contorno","52"],
    ["elvira das dores","53"],
    ["pedro jose de souza jardim","54"],
    ["leila diniz","55"],
    ["laudelina de almeida","56"],
    ["girassol","57"],
    ["mariana de carvalho","58"],
    ["joao capistrano de abreu","59"],
    ["mamede de souza","60"],
]

def toNumber(nome):
    for rua in ruas:
        if rua[0] in nome:
            novoNome = nome.replace(rua[0],rua[1])
            return novoNome
    print("nome não encontrado")
    return nome

def toName(nome):
    for rua in ruas:
        if rua[1] in nome:
            novoNome = nome.replace(rua[1],rua[0])
            return novoNome
    print("nome não encontrado")
    return False

if __name__=="__main__":
    banco = []
    with open("data.csv","r") as dados:
        banco = dados.readlines()
        novoBanco = []
        for i in banco:
            novoBanco.append(toNumber(i.lower()))
        print(banco)
        print(novoBanco)
        q = input("converter: ")
        if q == "s":
            banco = novoBanco
    with open("data.csv","w") as dados:
        lista = "id,rua,numero,lote,quadra,taxa"
        check = False
        for i in banco:
            if check:
                lista = f"{lista}{i}"
            else:
                lista = f"{lista}\n"
                check = True
        dados.write(lista)
