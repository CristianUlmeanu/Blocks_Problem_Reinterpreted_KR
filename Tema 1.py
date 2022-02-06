import copy
import time
from os import listdir
from os.path import isfile, join
from math import factorial

# informatii despre un nod din arborele de parcurgere (nu din graful initial)
class NodParcurgere:
    def __init__(self, info, parinte, cost=0, h=0):
        self.info = info
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g = cost  # consider cost=1 pentru o mutare
        self.h = h
        self.f = self.g + self.h

    def obtineDrum(self):
        l = [self];
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte)
            nod = nod.parinte
        return l

    def afisDrum(self, afisCost=False, afisLung=False):  # returneaza si lungimea drumului
        l = self.obtineDrum()
        idx=0
        for nod in l:
            idx+=1
            g.write(f"\nNumarul de ordine al nodului este: {idx}\n")
            g.write(str(nod))
        if afisCost:
            g.write(f"\nCost: {self.g}\n")
        if afisCost:
            g.write(f"Lungime: {len(l)}\n")
        return len(l)

    def contineInDrum(self, infoNodNou):
        nodDrum = self
        while nodDrum is not None:
            if (infoNodNou == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False

    def __repr__(self):
        sir = ""
        sir += str(self.info)
        return (sir)

    # euristica banală: daca nu e stare scop, returnez 1, altfel 0

    def __str__(self):
        sir = ""
        lista_identificatori=[]
        listaChar=[]
        maxChar=0
        for stiva in self.info:
            for elem in stiva:
                lista_identificatori.append(elem[0])
        for elem in lista_identificatori:
            listaChar.append(len(elem))
        maxChar=max(listaChar)
        maxInalt = max([len(stiva) for stiva in self.info])
        for inalt in range(maxInalt, 0, -1):
            for stiva in self.info:
                if len(stiva) < inalt:
                    sir += "       "
                    for i in range(1,maxChar):
                        sir=sir+" "
                else:
                    #nr_stiv=nr_stiv+1
                    k = len(stiva[inalt - 1][0])
                    if stiva[inalt-1][1]=="s":
                        sir += "[ "+stiva[inalt - 1][1]+":"
                        while k<maxChar:
                            sir=sir+" "
                            k=k+1
                        sir=sir+stiva[inalt - 1][0] + "] "
                    else:
                        sir += "[" + stiva[inalt - 1][1] + ":"
                        while k<maxChar:
                            sir=sir+" "
                            k=k+1
                        sir=sir+stiva[inalt - 1][0] + "] "
            sir += "\n"
        sir += "----" * (2 * len(self.info))
        return sir

    """
    def __str__(self):
        sir=""
        for stiva in self.info:
            sir+=(str(stiva))+"\n"
        sir+="--------------\n"
        return sir
    """


class Graph:  # graful problemei
    def __init__(self, nume_fisier):

        def obtineStive(sir):
            stiveSiruri = sir.strip().split("\n")  # ["a","c b","d"]
            #print(stiveSiruri)
            #print("________________")
            listaStive = [sirStiva.strip().split("#") if sirStiva != "=" else [[]] for sirStiva in stiveSiruri]
            #print(listaStive)
            #print("________________")
            listaInfoBloc=[]
            for listaBlocuri in listaStive:
                listaAux=[]
                for Bloc in listaBlocuri:
                    #print(f"Blocul este {Bloc}")
                    if Bloc==[]:
                        listaAux.append(Bloc)
                    else:
                        listaAux.append(Bloc.split(":"))
                    #print(listaInfoBloc)
                listaInfoBloc.append(listaAux)
            #print(listaBlocuri)
            #print(listaInfoBloc)
            return listaInfoBloc

        f = open(nume_fisier, 'r')

        continutFisier = f.read()  # citesc tot continutul fisierului
        siruriStari = continutFisier.split("stari_finale")
        self.start = obtineStive(siruriStari[0])  # [["a"], ["c","b"],["d"]]
        # self.scopuri = []
        # siruriStariFinale = siruriStari[1].strip().split("---")
        # for scop in siruriStariFinale:
        #     self.scopuri.append(obtineStive(scop))
        #print("Stare Initiala:", self.start)
        # print("Stari finale posibile:", self.scopuri)
        # input()

    def testeaza_scop(self, nodCurent):
        ok=1
        for lista in nodCurent.info:
            for idx_bloc in lista:
                if(idx_bloc[1]=="pf"):
                    ok=0
                    break
        #print(nodCurent.info, ok)
        if(ok==0):
            return False
        else:
            return True
        # print(f"Nodul curent este{nodCurent.info} si Scopul este{self.scopuri}, asadar in urma verificarii daca nodul este scop avem: {nodCurent.info in self.scopuri}")
        # return nodCurent.info in self.scopuri;

    # va genera succesorii sub forma de noduri in arborele de parcurgere

    def genereazaSuccesori(self, nodCurent, tip_euristica="euristica banala"):
        global cnt_list_succesori
        listaSuccesori = []
        stive_c = nodCurent.info  # stivele din nodul curent
        nr_stive = len(stive_c)
        #print(f"\n Numarul de stive este:{nr_stive} si acestea sunt: {stive_c}")
        for idx in range(nr_stive):  # idx= indicele stivei de pe care iau bloc
            #print(f"Stiva cu indexul: {idx}   este: {stive_c[idx]}")
            if len(stive_c[idx]) == 0:
                continue
            copie_interm = copy.deepcopy(stive_c)
            bloc = copie_interm[idx].pop()  # iau varful stivei
            #print(f"Blocul este: {bloc}")
            for j in range(nr_stive):  # j = indicele stivei pe care pun blocul
                if idx == j:  # nu punem blocul de unde l-am luat
                    continue
                stive_n = copy.deepcopy(copie_interm)  # lista noua de stive
                copie_bloc_satul = copy.deepcopy(bloc)
                #print(f"Lista noua de stive este: {stive_n}")
                if (len(stive_n[j]) > 0):
                    if bloc[1]=="pf" and stive_n[j][-1][1]=="pf":
                        #print(f"Blocul este {bloc[1]}, si elementul pe care vrem sa punem blocul este: {stive_n[j][-1][1]}")
                        continue
                    else:
                        for elem in reversed(stive_n[j]):#range(stive_n[j][-1], stive_n[j][0], -1):
                            #print(elem[1])
                            if (elem[1] == "s" and bloc[1] == "pf"):
                                stive_n[j].remove(elem)
                                copie_bloc_satul[1]="ps"
                            else:
                                break
                stive_n[j].append(copie_bloc_satul)  # pun blocul
                time_rulare=time.time()
                if(time_rulare-timout_start>timout):
                    raise Exception("\n###############\nTIMEOUT!\n###############\nRularea cautarii a depasit timpul maxim")
                #print(f"Lista noua de stive este: {stive_n}")
                if bloc[1]=="ps":
                    costMutareBloc =3
                elif bloc[1]=="pf":
                    costMutareBloc=2
                elif bloc[1]=="s":
                    costMutareBloc=1
                if not nodCurent.contineInDrum(stive_n):
                    nod_nou = NodParcurgere(stive_n, nodCurent, cost=nodCurent.g + costMutareBloc,
                                            h=self.calculeaza_h(stive_n, tip_euristica))
                    listaSuccesori.append(nod_nou)
                    cnt_list_succesori=cnt_list_succesori+1
        return listaSuccesori

    # euristica banala
    def calculeaza_h(self, infoNod, tip_euristica="euristica banala"):
        if tip_euristica == "euristica banala":
            # if infoNod not in self.scopuri:
            ok = 1
            for lista in infoNod:
                for idx_bloc in lista:
                    if (idx_bloc[1] == "pf"):
                        ok = 0
                        break
            # print(nodCurent.info, ok)
            if (ok == 0):
                return 1
            else:
                return 0
        elif tip_euristica == "euristica admisibila 1":
            # calculam numarul de de pisici flamande care au ramas de hranit
            h=0
            euristici = []
            for stiva in infoNod:
                for elem in stiva:
                    if elem[1]=="pf":
                        h+=2
                euristici.append(h)
            return min(euristici)
        elif tip_euristica == "euristica admisibila 2":
            # calculez cate blocuri se afla peste pisica flamanda, deoarece ca sa hranim pisica va trebui sa mutam ce e deasupra si pe ea ulterior
            h=0
            euristici = []
            for stiva in infoNod:
                for elem in reversed(stiva):
                    if elem[1]=="s":
                        h+=1
                    elif elem[1]=="ps":
                        h+=3
                    elif elem[1]=="pf":
                        h+=2
                euristici.append(h)
            return min(euristici)
        else:  # tip_euristica=="euristica neadmisibila"
            h = 0
            euristici = []
            for stiva in infoNod:
                for elem in reversed(stiva):
                    if elem[1] == "s":
                        h += 1
                    elif elem[1] == "ps":
                        h += 3
                    elif elem[1] == "pf":
                        h += 2
                h=h*2
                euristici.append(h)
            return max(euristici)

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return (sir)


def breadth_first(gr, nrSolutiiCautate, tip_euristica="euristica banala"):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None)]
    max_solutii=nrSolutiiCautate+1
    global nr_max_nod

    while len(c) > 0:
        if(len(c)>nr_max_nod):
            nr_max_nod = len(c)
        # print("Coada actuala: " + str(c))
        # input()
        nodCurent = c.pop(0)
        if gr.testeaza_scop(nodCurent):
            g.write(f"Aceasta este solutia {max_solutii - nrSolutiiCautate}:\n")
            nodCurent.afisDrum(afisCost=True, afisLung=True)
            g.write("----" * (2 * len(nodCurent.info)))
            g.write("\n")
            end_time = time.time()
            g.write(f"Timpul de gasire al solutiei de mai sus este: {round(end_time - init_time,4)} secunde\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent,tip_euristica=tip_euristica)
        c.extend(lSuccesori)


def a_star(gr, nrSolutiiCautate, tip_euristica):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start))]
    max_solutii=nrSolutiiCautate+1
    time_now=time.time()
    global nr_max_nod
    while len(c) > 0:
        if(len(c)>nr_max_nod):
            nr_max_nod = len(c)
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            g.write(f"Aceasta este solutia {max_solutii - nrSolutiiCautate}:\n")
            nodCurent.afisDrum(afisCost=True, afisLung=True)
            g.write("----" * (2 * len(nodCurent.info)))
            g.write("\n")
            end_time = time.time()
            g.write(f"Timpul de gasire al solutiei de mai sus este: {round(end_time - init_time,3)} secunde\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent, tip_euristica=tip_euristica)
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(c)):
                # diferenta fata de UCS e ca ordonez dupa f
                if c[i].f >= s.f:
                    gasit_loc = True
                    break;
            if gasit_loc:
                c.insert(i, s)
            else:
                c.append(s)


def greedy(gr, nrSolutiiCautate, tip_euristica):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start))]
    max_solutii=nrSolutiiCautate
    global nr_max_nod
    while len(c) > 0:
        if(len(c)>nr_max_nod):
            nr_max_nod = len(c)
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            g.write(f"Aceasta este solutia {max_solutii - nrSolutiiCautate}:\n")
            nodCurent.afisDrum(afisCost=True, afisLung=True)
            g.write("----" * (2 * len(nodCurent.info)))
            g.write("\n")
            end_time = time.time()
            g.write(f"Timpul de gasire al solutiei de mai sus este: {round(end_time - init_time,3)} secunde\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent, tip_euristica=tip_euristica)
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(c)):
                # diferenta fata de A* e ca ordonez dupa h
                if c[i].h >= s.h:
                    gasit_loc = True
                    break;
            if gasit_loc:
                c.insert(i, s)
            else:
                c.append(s)


def df(nodCurent, nrSolutiiCautate,tip_euristica="euristica banala"):
    max_solutii=nrSolutiiCautate+1
    global nr_max_nod
    if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
        return nrSolutiiCautate
    #print("Stiva actuala: " + "->",nodCurent.info)
    # input()
    if gr.testeaza_scop(nodCurent):
        g.write(f"Aceasta este solutia {max_solutii - nrSolutiiCautate}:\n")
        nodCurent.afisDrum(afisCost=True,afisLung=True)
        g.write("----" * (2 * len(nodCurent.info)))
        g.write("\n")
        # input()
        end_time = time.time()
        g.write(f"Timpul de gasire al solutiei de mai sus este: {round(end_time - init_time, 3)} secunde\n")
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return nrSolutiiCautate
    lSuccesori = gr.genereazaSuccesori(nodCurent,tip_euristica=tip_euristica)
    if len(lSuccesori)>nr_max_nod:
        nr_max_nod=len(lSuccesori)
    for sc in lSuccesori:
        if nrSolutiiCautate != 0:
            nrSolutiiCautate = df(sc, nrSolutiiCautate)
    return nrSolutiiCautate


# df(a)->df(b)->df(c)
#############################################


def dfi(nodCurent, adancime, nrSolutiiCautate, tip_euristica="euristica banala"):
    #print(nodCurent.info)
    #print("Stiva actuala: " + "->",nodCurent.info)
    max_solutii=nrSolutiiCautate+1
    global nr_max_nod
    if adancime == 1 and gr.testeaza_scop(nodCurent)==True:
        g.write(f"Aceasta este solutia {max_solutii-nrSolutiiCautate}:\n")
        nodCurent.afisDrum(afisCost=True, afisLung=True)
        g.write("----" * (2 * len(nodCurent.info)))
        g.write("\n")
        end_time = time.time()
        g.write(f"Timpul de gasire al solutiei de mai sus este: {round(end_time - init_time, 3)} secunde\n")
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return nrSolutiiCautate
    if adancime > 1:
        lSuccesori = gr.genereazaSuccesori(nodCurent,tip_euristica=tip_euristica)
        if len(lSuccesori) > nr_max_nod:
            nr_max_nod = len(lSuccesori)
        for sc in lSuccesori:
            if nrSolutiiCautate != 0:
                nrSolutiiCautate = dfi(sc, adancime - 1, nrSolutiiCautate)
    return nrSolutiiCautate


def depth_first_iterativ(gr, nrSolutiiCautate, tip_euristica="euristica banala"):
    creare_nod=[NodParcurgere(gr.start, None)]
    #print(creare_nod)
    nod_c=creare_nod.pop()
    #print(f"Nod C este: {nod_c.info}")
    #print(f"Lungimea nodului este {len(nod_c.info)}")
    nr_maxNoduri=factorial(len(nod_c.info))
    #print(f"Nr max noduri{nr_maxNoduri}")
    for i in range(1, nr_maxNoduri + 1):
        if nrSolutiiCautate == 0:
            return
        #print("**************\nAdancime maxima: ", i)
        nrSolutiiCautate = dfi(NodParcurgere(gr.start, None), i, nrSolutiiCautate,tip_euristica=tip_euristica)


def uniform_cost(gr, nrSolutiiCautate=1, tip_euristica="euristica banala"):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start,None)]
    max_solutii=nrSolutiiCautate+1
    global nr_max_nod

    while len(c) > 0:
        if len(c)>nr_max_nod:
            nr_max_nod=len(c)
        #print("Coada actuala: " + str(c))
        # input()
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            g.write(f"Aceasta este solutia {max_solutii - nrSolutiiCautate}:\n")
            nodCurent.afisDrum(afisCost=True,afisLung=True)
            g.write("----" * (2 * len(nodCurent.info)))
            g.write("\n")
            end_time = time.time()
            g.write(f"Timpul de gasire al solutiei de mai sus este: {round(end_time - init_time,3)} secunde\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent, tip_euristica=tip_euristica)
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(c)):
                # ordonez dupa cost(notat cu g aici și în desenele de pe site)
                if c[i].g > s.g:
                    gasit_loc = True
                    break
            if gasit_loc:
                c.insert(i, s)
            else:
                c.append(s)



print("Scrieti pathul de unde vrei sa preiei fisierul de input. \n Inputurile se pot gasi in 'InputuriTema\\' si acestea sunt:")
fisiereInput=[fisier for fisier in listdir("InputuriTema") if isfile(join("InputuriTema",fisier))]
i=1
for idx in fisiereInput:
    print(str(i)+") "+str(idx)+";")
    i=i+1
path=input()

gr = Graph(path)
# gr2 = Graph("input2.txt")
# gr3 = Graph("input3.txt")
# gr4 = Graph("input4.txt")

g = open("OutputuriTema\output.txt", 'w')

print("Alegeti tipul de cautare. Acestea sunt: \n1) BF;\n2) DF;\n3) DFI;\n4) UCS;\n5) A*;\n6) Greedy;")
tip=input()
g.write("\nObservatie: stivele sunt afisate pe orizontala, cu baza la stanga si varful la dreapta.")
print("__________________________\n Se ruleaza\n__________________________")
timout=300
timout_start=time.time()
cnt_list_succesori=0#counter la numar succesori
nr_max_nod=1#max nr de noduri
init_time=time.time()
### Se Alege tipul cautarii pentru rulare
if tip=="BF":

    g.write("\n##################\nSolutii obtinute cu breadth first:")
    breadth_first(gr, nrSolutiiCautate=1, tip_euristica="euristica admisibila 2")
    g.write(f"Numarul total de sucesori generati pana in acest moment este: {cnt_list_succesori}\n")
    g.write(f"Numarul maxim de noduri existente este: {nr_max_nod}\n")
    g.close()
elif tip=="DF":

    creare_nod=[NodParcurgere(gr.start, None)]
    #print(creare_nod)
    nod_c=creare_nod.pop()
    g.write("\n##################\nSolutii obtinute cu depth first:")
    df(nod_c, nrSolutiiCautate=1, tip_euristica="euristica banala")
    g.write(f"Numarul total de sucesori generati pana in acest moment este: {cnt_list_succesori}\n")
    g.write(f"Numarul maxim de noduri existente este: {nr_max_nod}\n")
    g.close()
elif tip=="DFI":

    g.write("\n##################\nSolutii obtinute cu depth first iterativ:")
    depth_first_iterativ(gr, nrSolutiiCautate=1, tip_euristica="euristica neadmisibila")
    g.write(f"Numarul total de sucesori generati pana in acest moment este: {cnt_list_succesori}\n")
    g.write(f"Numarul maxim de noduri existente este: {nr_max_nod}\n")
    g.close()
elif tip=="UCS":

    g.write("\n##################\nSolutii obtinute cu uniform cost search:")
    uniform_cost(gr, nrSolutiiCautate=1, tip_euristica="euristica banala")
    g.write(f"Numarul total de sucesori generati pana in acest moment este: {cnt_list_succesori}\n")
    g.write(f"Numarul maxim de noduri existente este: {nr_max_nod}\n")
    g.close()
elif tip=="A*":

    g.write("\n##################\nSolutii obtinute cu A*:")
    a_star(gr, nrSolutiiCautate=1, tip_euristica="euristica banala")
    g.write(f"Numarul total de sucesori generati pana in acest moment este: {cnt_list_succesori}\n")
    g.write(f"Numarul maxim de noduri existente este: {nr_max_nod}\n")
    g.close()
elif tip=="Greedy":

    g.write("\n##################\nSolutii obtinute cu Greedy:")
    greedy(gr, nrSolutiiCautate=1, tip_euristica="euristica banala")
    g.write(f"Numarul total de sucesori generati pana in acest moment este: {cnt_list_succesori}\n")
    g.write(f"Numarul maxim de noduri existente este: {nr_max_nod}\n")
    g.close()

#_______________________________________________________________#

# print("\n##################\nSolutii obtinute cu breadth first:")
# breadth_first(gr, nrSolutiiCautate=1)
# creare_nod=[NodParcurgere(gr.start, None)]
# #print(creare_nod)
# nod_c=creare_nod.pop()
# print("\n##################\nSolutii obtinute cu depth first:")
# df(nod_c, nrSolutiiCautate=1)
# print("\n##################\nSolutii obtinute cu depth first iterativ:")
# depth_first_iterativ(gr, nrSolutiiCautate=1)
# print("\n##################\nSolutii obtinute cu uniform cost search:")
# uniform_cost(gr, nrSolutiiCautate=1, tip_euristica="euristica admisibila 2")
# print("\n##################\nSolutii obtinute cu A*:")
# a_star(gr, nrSolutiiCautate=5, tip_euristica="euristica banala")
# print("\n##################\nSolutii obtinute cu Greedy:")
# greedy(gr, nrSolutiiCautate=1, tip_euristica="euristica banala")



#
#

#


"""
a b c
d e
g


g e c
d a b
|

"""