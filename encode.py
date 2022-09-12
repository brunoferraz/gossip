def categories(serie, normalize = True):
    l = []
    # pega lista
    # tira elementos repetidos
    for i in serie:
        if(i not in l):
            l.append(i)
    # cria hash table
    dic = {}
    undic = {}
    for i in range(len(l)):
        key = i
        if(normalize):
            key = i/len(l)
        dic[l[i]] = key
        undic[key] = l[i]
    # altera valores
    for i in range(len(serie.values)):
        serie[i] = dic[serie[i]]
    return dic, undic

def checkbox(serie, options= None, binary = False):
    if options is not None:
        for i in range(len(serie)):
            cod = []
            if(type(serie[i]) == str):
                for j in options:
                    # print(serie[i].split(','))
                    escolhas = serie[i].split(',')
                    if j not in escolhas:
                        cod.append(0)
                    else:
                        cod.append(1)
                serie[i] = cod
            else:
                serie[i] = [0, 0, 0, 0]
def clean18(serie):
    for i in range(len(serie)):
        serie[i] = serie[i].upper()
        serie[i] = serie[i].replace('PÚBLICAS,', 'PÚBLICAS;')
    pass
def checkbox18(serie, options= None, binary = False):
    if options is not None:
        for i in range(len(serie)):
            cod = []
            if(type(serie[i]) == str):
                escolhas = serie[i].split(',')
                # print(len(options))
                if((len(escolhas)) > (len(options))):
                    pass
                    # print(serie[i])
                    # print(escolhas)
                else:
                    for j in options:
                        if j not in escolhas:
                            cod.append(0)
                        else:
                            cod.append(1)
                    serie[i] = cod
            else:
                serie[i] = [0, 0, 0, 0, 0, 0, 0, 0]

def checkbox24(serie, options = None, binary = False):
    count = 0
    if options is not None:
        for i in range(len(serie)):
            cod = []
            if(type(serie[i]) == str):
                escolhas = serie[i].split(',')
                if((len(escolhas)) > (len(options))):
                    pass
                else:
                    for j in options:
                        if j not in escolhas:
                            cod.append(0)
                        else:
                            cod.append(1)
                    serie[i] = cod
            else:
                count = count + 1
                for i in range(len(options)):
                    cod.append(0)
                serie[i] = cod
    # print('>>>>>>>>>>', count)
