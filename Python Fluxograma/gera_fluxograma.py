from graphviz import Digraph

# Criando o fluxograma
fluxo = Digraph(format='png')
fluxo.attr(rankdir='TB')

# Nós do fluxograma
fluxo.node('inicio', 'Início', shape='oval')
fluxo.node('n1', 'Digite a primeira nota', shape='parallelogram')
fluxo.node('n2', 'Digite a segunda nota', shape='parallelogram')
fluxo.node('calc', 'Calcular média = (nota1 + nota2) / 2', shape='rectangle')
fluxo.node('cond', 'A média é >= 7?', shape='diamond')
fluxo.node('aprovado', 'Aprovado', shape='rectangle',
           style='filled', color='lightgreen')
fluxo.node('reprovado', 'Reprovado', shape='rectangle',
           style='filled', color='lightcoral')
fluxo.node('fim', 'Fim', shape='oval')

# Conectando os nós
fluxo.edge('inicio', 'n1')
fluxo.edge('n1', 'n2')
fluxo.edge('n2', 'calc')
fluxo.edge('calc', 'cond')
fluxo.edge('cond', 'aprovado', label='Sim')
fluxo.edge('cond', 'reprovado', label='Não')
fluxo.edge('aprovado', 'fim')
fluxo.edge('reprovado', 'fim')

# Gerar imagem
fluxo.render('fluxograma_media', view=True)
