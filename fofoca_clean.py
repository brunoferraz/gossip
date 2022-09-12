import pandas as pd
import encode

normalize = True
# df = pd.read_csv("fofoca_encoded.csv", encoding='utf8')
df = pd.read_csv("new_encoded.csv", encoding='utf8',sep=';')
df.apply(lambda x: pd._lib.infer_dtype(x.values))
nova = ['data_hora',
        'nome',#0
        'idade',#1
        'sexo',#2
        'cidade/estado',#3
        'escolaridade',#4
        'profissao',#5
        'valor_fofoca',#6
        'fofoca_sobre_mim_e',#7
        'fofoca_e',#8
        'viver_sem_fofoca',#9
        'voce_fofoca',#10
        'o_que_e_fofoqueiro',#11
        'se_acha_fofoqueiro',#12
        'moralmente_ser_fofoqueiro',#13
        'quem_fofoca_mais',#14
        'que_idade_fofoca',#15
        'conhece_fofoqueiro',#16
        'fofoca_sempre_negativo',#17
        'temas_frequentes',#18
        'temas_interessam',#19
        'aprendeu_algo',#20
        'caso_interessante',#21
        'nao_e_assunto',#22
        'onde',#23
        'palavras_relacionadas',#24
        'conhece_beneficiado',#25
        'conhece_prejudicado',#26
        'foi_prejudicado',#27
        'prejudicou_alguem',#28
        'sente_quando_conta',#29
        'sente_quando_ouve',#30
        'faz_ou_sente_sobre_conhecido',#31
        'na_internet',#32
        'termo_diferente',#33
        ]
df.columns = nova

# print(df.values)
# 'data_hora',
# 'nome',#0
# 'idade',#1
# 'sexo',#2
#SEXO
df['sexo'].replace(to_replace=['MASCULINO'],value = "0", inplace=True)
df['sexo'].replace(to_replace=['FEMININO'],value = "1", inplace=True)
# df['sexo'].replace(to_replace=['0'],value = "MASCULINO", inplace=True)
# df['sexo'].replace(to_replace=['1'],value = "FEMININO", inplace=True)

# 'cidade/estado',#3 STRING
encode.categories(df['cidade/estado'], normalize=normalize)

# 'escolaridade',#4 (Ensino Fundamental; Ensino Medio; Ensino Superior; Pós-Graduacao – Profissional; Pós-Graduação – Mestrado; Pós-Graduação - Doutorado)
encode.categories(df['escolaridade'], normalize=normalize)
# 'profissao',#5 STRING
# 'valor_fofoca',#6
encode.categories(df['valor_fofoca'], normalize=normalize)
# 'fofoca_sobre_mim_e',#7
encode.categories(df['fofoca_sobre_mim_e'], normalize=normalize)
# 'fofoca_e',#8
# 'viver_sem_fofoca',#9
encode.categories(df['viver_sem_fofoca'], normalize=normalize)
# 'voce_fofoca',#10
encode.categories(df['voce_fofoca'], normalize=normalize)
# 'o_que_e_fofoqueiro',#11
# 'se_acha_fofoqueiro',#12
encode.categories(df['se_acha_fofoqueiro'], normalize=normalize)
# 'moralmente_ser_fofoqueiro',#13
encode.categories(df['moralmente_ser_fofoqueiro'], normalize=normalize)
# 'quem_fofoca_mais',#14
encode.categories(df['quem_fofoca_mais'], normalize=normalize)
# 'que_idade_fofoca',#15
encode.checkbox(df['que_idade_fofoca'],
                        ['CRIANÇAS','ADOLESCENTES','ADULTOS','IDOSOS'])
# 'conhece_fofoqueiro',#16
encode.categories(df['conhece_fofoqueiro'], normalize=normalize)
# 'fofoca_sempre_negativo',#17
encode.categories(df['fofoca_sempre_negativo'], normalize=normalize)
# 'temas_frequentes',#18
encode.clean18(df['temas_frequentes'])
encode.checkbox18(df['temas_frequentes'],
                        ['A VIDA DE SEUS CONHECIDOS E AMIGOS',
                        ' ASSUNTOS DE TRABALHO',
                        ' A VIDA DE SEUS PARENTES',
                        'A VIDA DAS PESSOAS PÚBLICAS; COMO ARTISTAS FAMOSOS E POLÍTICOS',
                        ' JULGAMENTOS MORAIS SOBRE AS PESSOAS',
                        ' NOTÍCIAS VARIADAS',
                        ' BOATOS',
                        ' MENTIRAS',
                        # ' SEXO',
                        # ' RELACIONAMENTO ALHEIO'
                        ])
# 'temas_interessam',#19
# 'aprendeu_algo',#20
# 'caso_interessante',#21
# 'nao_e_assunto',#22
# 'onde',#23
# 'palavras_relacionadas',#24
encode.checkbox24(df['palavras_relacionadas'],
                        ['MENTIRA',
                        'BOATO',
                        'INVEJA',
                        'DISCRIÇÃO',
                        'IMPLICÂNCIA',
                        'VINGANÇA',
                        'SEGREDO',
                        'CONFUSÃO',
                        'IRONIA',
                        'AFRONTA',
                        'INTIMIDADE',
                        'COMPADRIO',
                        'TRAIÇÃO',
                        'CURIOSIDADE',
                        'SUSSURRO',
                        'MALDIÇÃO',
                        'CONSPIRAÇÃO',
                        'DETRAÇÃO',
                        'CUMPLICIDADE',
                        'AMIZADE',
                        'INIMIZADE',
                        'COMPETIÇÃO',
                        'CONTROLE',
                        'ESCONDIDO',
                        'CENSURA',
                        'TAGARELA',
                        'MALÍCIA',
                        'BASTIDORES',
                        'INSINUAÇÃO',
                        'NOVIDADE',
                        'MALDADE',
                        'DIVERSÃO',
                        'INFORMAÇÃO',
                        'FAKE NEWS',
                        'FUXICO',
                        'MANIPULAÇÃO',
                        'CONVERSA',
                        'ZOAÇÃO',
                        'OCULTAÇÃO',
                        'PECADO',
                        'COXIXO'
                        ])
# 'conhece_beneficiado',#25
encode.categories(df['conhece_beneficiado'], normalize=normalize)
# 'conhece_prejudicado',#26
encode.categories(df['conhece_prejudicado'], normalize=normalize)
# 'foi_prejudicado',#27
encode.categories(df['foi_prejudicado'], normalize=normalize)
# 'prejudicou_alguem',#28
encode.categories(df['prejudicou_alguem'], normalize=normalize)
# 'sente_quando_conta',#29
# 'sente_quando_ouve',#30
# 'faz_ou_sente_sobre_conhecido',#31
# 'na_internet',#32
encode.categories(df['na_internet'], normalize=normalize)
# 'termo_diferente',#33

df.to_csv('encoded.csv')


df.drop(columns=['data_hora',
                'nome', #0
                'profissao', #1
                'fofoca_e', #2
                'profissao',#5
                'o_que_e_fofoqueiro', #11
                'temas_interessam',#19
                'aprendeu_algo',#20
                'caso_interessante',#21
                'nao_e_assunto',#22
                'onde',#23
                'sente_quando_conta',#29
                'sente_quando_ouve',#30
                'faz_ou_sente_sobre_conhecido',#31
                'termo_diferente',#33
                ], inplace=True)
                
df.to_csv('encoded_semDiscursivas.csv')