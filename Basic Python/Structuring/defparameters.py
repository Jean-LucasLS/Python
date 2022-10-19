def Printer(init='Olá', name='Nome'): # Caso a função não receba parâmetros na sua declaração, ela utilizará os declarados.
    print(f'{init} {name}')
name1 = 'Jonas'
name2 = 'Xi Jinping'
Printer()
Printer('Rei dos Tatchankas', 'Team Dignitas') # Neste caso, foi mandado parâmetros diretamente, sem uso de variáveis na "main".
Printer(name='Rubellus') # Neste caso, está declarado na passagem por parâmetro que "name" equivalerá ao conteúdo entre aspas simples.
Printer(name=name1) # Neste caso, "name" receberá "name1".
Printer(name1, name2) # Neste caso, "init" receberá "name1", e "name" receberá "name2"

""" No caso abaixo, a ordem dos parâmetros passados está invertido em relação à função. Contudo, houve declaração exata das variáveis
(name = '' | init = ''), portanto os parâmetros assumirão a ordem descrita na própria função. Portanto, se a função Printer(init, name)
for chamada no formato "Printer(name = 'X', init = 'Y')", ela receberá "init = Y" e "name = X"."""
Printer(name='Tom Dippler', init='Hello')
