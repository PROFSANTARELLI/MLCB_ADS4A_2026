import pandas as pd

# Dataset Sintético de Mensagens do SAC da MóveisDesign S.A.
data_raw = [
    # trocas_devolucoes
    ("Quero devolver este sofa que chegou com rasgo", "trocas_devolucoes"),
    ("Gostaria de trocar minha mesa veio arranhada", "trocas_devolucoes"),
    ("Como faco para solicitar a devolucao do meu estofado?", "trocas_devolucoes"),
    ("O rack veio com defeito e quero trocar", "trocas_devolucoes"),
    ("Preciso devolver a cadeira de escritorio com defeito", "trocas_devolucoes"),
    ("Quero cancelar a compra e pedir extorno do sofá", "trocas_devolucoes"),
    ("Viu meu painel de tv veio quebrado quero troca", "trocas_devolucoes"),
    ("Gostaria de devolver o armário por defeito", "trocas_devolucoes"),
    
    # logistica_entregas
    ("Qual o status da entrega da minha estante?", "logistica_entregas"),
    ("Onde esta meu pedido de poltrona?", "logistica_entregas"),
    ("Qual o prazo de entrega do sofa que comprei?", "logistica_entregas"),
    ("Meu armario de cozinha ainda nao chegou", "logistica_entregas"),
    ("Quero rastrear o transporte da minha mesa de jantar", "logistica_entregas"),
    ("A entrega do guarda roupa esta atrasada", "logistica_entregas"),
    ("Quando chega minha cadeira presidente?", "logistica_entregas"),
    ("Saber dia que chegam meus moveis", "logistica_entregas"),

    # suporte_tecnico
    ("Como montar o painel de tv da sala?", "suporte_tecnico"),
    ("Nao consigo entender o manual de montagem do rack", "suporte_tecnico"),
    ("Faltaram parafusos no kit do meu guarda roupa", "suporte_tecnico"),
    ("Preciso de ajuda para ajustar a porta do armario", "suporte_tecnico"),
    ("A peca B da mesa nao encaixa na peca C", "suporte_tecnico"),
    ("Como regulo a altura da minha cadeira ergonomica?", "suporte_tecnico"),
    ("Voces enviam montador para a estante?", "suporte_tecnico"),
    ("Manual da cama de casal veio em branco", "suporte_tecnico"),

    # vendas_orcamento
    ("Qual o valor da mesa de jantar 6 lugares?", "vendas_orcamento"),
    ("Gostaria de um orcamento de sofa retratil", "vendas_orcamento"),
    ("Voces tem desconto para pagamento via pix na poltrona?", "vendas_orcamento"),
    ("Quanto custa o frete para o guarda roupa de casal?", "vendas_orcamento"),
    ("Tem promocao de comoda este mes?", "vendas_orcamento"),
    ("Qual o preço do armario de cozinha planejado?", "vendas_orcamento"),
    ("Gostaria de comprar um beliche de madeira", "vendas_orcamento"),
    ("Quais as formas de parcelamento do rack?", "vendas_orcamento")
]

# Criar DataFrame e salvar em arquivo CSV
df = pd.DataFrame(data_raw, columns=["mensagem", "intencao"])
df.to_csv("sac_moveis_ac2.csv", index=False)
print(" Dataset 'sac_moveis_ac2.csv' gerado com sucesso!")
