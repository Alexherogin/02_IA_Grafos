#codigo 30red  bayesiana
import matplotlib.pyplot as plt
import networkx as nx
rbd= nx.DiGraph()

t0_nodo = ['CLIMA_0']
T1_nodo = ['clima_1']

clima_t0={'soleado':0.7, 'lluvia':0.3}
clima_t1_y_t0 = {
    'soleado':{'soleado':0.4,'lluvios':0.6},
    'lluvia':{'soleado':0.8,'lluvios':0.2}
}
rbd.add_node('CLIMA_0',valor = ['soleado','lluvios'], proba=clima_t0)
rbd.add_node('clima_1',valor = ['soleado','llivios'], proba=clima_t1_y_t0)
rbd.add_edge('CLIMA_0','clima_1')

import matplotlib.pyplot as plt
proba= nx.spring_layout(rbd, seed=42)
nx.draw(rbd, proba, with_labels=True, node_color='red', node_size=1000, edge_color='black')
labels= nx.get_edge_attributes(rbd,'prob')
nx.draw_networkx_edge_labels(rbd, proba, edge_labels=labels,font_size=10)
plt.title('red de bayesian dinamica (en clima)')