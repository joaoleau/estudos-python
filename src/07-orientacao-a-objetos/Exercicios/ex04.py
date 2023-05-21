
from Pacote.participacao import Participacao
from Pacote.projeto import Projeto

#########################################################################

projeto1 = Projeto("9999","Laboratório de Sistema","Ana")
projeto2 = Projeto("9900","Tecnologia no ensino","Bruno")


participacao1 = Participacao('21','05/05','17/10','Jorge','SI')
participacao3 = Participacao('23','05/05','17/10','Cerol','SI')
participacao2 = Participacao('22','05/06','1/11','Carlos','TI')

projeto1.add_participacao(participacao1)
projeto1.add_participacao(participacao3)
projeto2.add_participacao(participacao2)

print(projeto1)
for part in projeto1.participacao:
    print(part)




