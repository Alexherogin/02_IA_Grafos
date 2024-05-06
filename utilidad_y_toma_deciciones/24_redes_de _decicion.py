#programa 24
 
import networkx as nx
G = nx.DiGraph()

G.add_node("inicia",type='decision')
G.add_node("llueve",type='evento')
G.add_node("trafico",type='evento')
G.add_node("tarde",type='evento')
G.add_node("llevar paraguas",type='decicion')

G.add_edge("inicia","llueve")
G.add_edge("llueve","llevar paraguas")
G.add_edge("inicia","trafico")
G.add_edge("trafico","llevar paraguas")
G.add_edge("trafico","tarde")
G.add_edge("tarde","llevar paraguas")

G.add_edge("llueve", "llevar paraguas", probabilidad=0.4)
G.add_edge("trafico", "llevar paraguas", probabilidad=0.4)
G.add_edge("tarde", "llevar paraguas", probabilidad=0.2)
G.add_edge("llevar paraguas", "llevar paraguas", probabilidad=0.5)


def calculo(G):
    valor =1
    for nodo in nx.topological_sort(G):
        if G.nodes[nodo]['type'] == 'decision':
            valor = valor + G.nodes[nodo]['probabilidad']
        else:
            valor = valor * G.nodes[nodo]['probabilidad']
    return valor
valor = calculo(G)
print(valor)

