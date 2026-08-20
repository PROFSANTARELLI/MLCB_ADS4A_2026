#EXERCÍCIO AULA 01

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. DATASET EXPANDIDO
mensagens_intencao = [
    "Quero a segunda via do meu boleto",
    "Como faço para pagar a fatura?",
    "Minha internet está caindo muito",
    "O sinal da TV não está funcionando",
    "Quero cancelar meu plano imediatamente",
    "Desejo encerrar minha conta",
    "Preciso do código de barras para pagamento",
    "O roteador está com a luz vermelha piscando",
    "Gostaria de solicitar o cancelamento do contrato"
]

rotulos_intencao = [
    "financeiro",
    "financeiro",
    "suporte_tecnico",
    "suporte_tecnico",
    "cancelamento",
    "cancelamento",
    "financeiro",
    "suporte_tecnico",
    "cancelamento"
]

# 2. VETORIZAÇÃO DE TEXTO
vectorizer_intencao = CountVectorizer()
X_intencao = vectorizer_intencao.fit_transform(mensagens_intencao)

# 3. TREINAMENTO DO MODELO
modelo_intencao = MultinomialNB()
modelo_intencao.fit(X_intencao, rotulos_intencao)

# 4. TESTE DE INFERÊNCIA
mensagem_usuario = ["Não recebi minha fatura deste mês"]
X_usuario = vectorizer_intencao.transform(mensagem_usuario)
predicao = modelo_intencao.predict(X_usuario)

print("=== RESULTADO DA CLASSIFICAÇÃO DE INTENÇÃO ===")
print(f"Frase do Usuário: '{mensagem_usuario[0]}'")
print(f"Intenção Identificada pelo Bot: {predicao[0].upper()}")






LAB0313082026
# TODO 1: Separe o dataset em X e y
X = df3['mensagem']
y = df3['intencao']

# TODO 2: Divisão em treino (70%) e teste (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# TODO 3: Vetorização
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# TODO 4: Instanciar e Treinar
modelo_arvore = DecisionTreeClassifier(random_state=42)
modelo_arvore.fit(X_train_vec, y_train)

# TODO 5: Predição e Acurácia
predicoes = modelo_arvore.predict(X_test_vec)
acuracia = accuracy_score(y_test, predicoes)
print(f"Acurácia do Modelo: {acuracia * 100:.2f}%")



LAB0413082026
# ============================================================
# LAB 04 - AULA 02 (MLCB): Motor de NLU para Agência de Viagens
# ============================================================
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ------------------------------------------------------------
# REQUISITO 1: Dataset com no mínimo 12 frases e 3 intenções
# ------------------------------------------------------------
dados_viagem = {
    'mensagem': [
        # Intenção: comprar_passagem (4 frases)
        'Quero comprar uma passagem para Orlando',
        'Gostaria de reservar um voo para Salvador',
        'Qual o preço da passagem de avião para Lisboa?',
        'Preciso comprar bilhete aéreo para o Rio de Janeiro',
        
        # Intenção: cancelar_reserva (4 frases)
        'Como faço para cancelar minha reserva de voo?',
        'Quero pedir o cancelamento da minha viagem',
        'Gostaria de anular minha compra de passagem',
        'Preciso cancelar meu voo marcado para amanhã',
        
        # Intenção: falar_atendente (4 frases)
        'Quero falar com um atendente humano por favor',
        'Pode me transferir para o suporte ao cliente?',
        'Preciso de ajuda com uma pessoa do atendimento',
        'Gostaria de conversar com um operador da agência'
    ],
    'intencao': [
        'comprar_passagem', 'comprar_passagem', 'comprar_passagem', 'comprar_passagem',
        'cancelar_reserva', 'cancelar_reserva', 'cancelar_reserva', 'cancelar_reserva',
        'falar_atendente', 'falar_atendente', 'falar_atendente', 'falar_atendente'
    ]
}

df_viagens = pd.DataFrame(dados_viagem)

# Separação das variáveis X (texto) e y (rótulo/intenção)
X = df_viagens['mensagem']
y = df_viagens['intencao']

# ------------------------------------------------------------
# REQUISITO 2: Divisão em Treino e Teste com train_test_split
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# ------------------------------------------------------------
# REQUISITO 3: Vetorizador de Texto (TfidfVectorizer)
# ------------------------------------------------------------
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ------------------------------------------------------------
# REQUISITO 4: Algoritmo de Classificação (LogisticRegression)
# ------------------------------------------------------------
modelo_nlu = LogisticRegression()
modelo_nlu.fit(X_train_vec, y_train)

# Avaliação rápida de acurácia no conjunto de teste
y_pred_test = modelo_nlu.predict(X_test_vec)
acuracia = accuracy_score(y_test, y_pred_test)

# ------------------------------------------------------------
# REQUISITO 5 & 6: Predição de 3 Frases Inéditas e Exibição
# ------------------------------------------------------------
frases_ineditas = [
    "Gostaria de saber o valor para voar até Paris",   # Esperado: comprar_passagem
    "Quero cancelar o bilhete que comprei ontem",      # Esperado: cancelar_reserva
    "Me transfira para um suporte humano, por favor"    # Esperado: falar_atendente
]

# Vetorização das frases inéditas e predição
frases_ineditas_vec = vectorizer.transform(frases_ineditas)
predicoes_ineditas = modelo_nlu.predict(frases_ineditas_vec)

# Exibição dos Resultados no Console
print("==================================================")
print("--- MOTOR DE NLU: AGÊNCIA DE VIAGENS ---")
print("==================================================")
print(f"Acurácia no conjunto de teste: {acuracia * 100:.2f}%\n")
print("--- PREDIÇÃO DE MENSAGENS INÉDITAS ---")

for frase, intencao in zip(frases_ineditas, predicoes_ineditas):
    print(f"Mensagem: '{frase}'")
    print(f"==> Intenção Predita: [{intencao}]\n")




# ============================================================
# LAB 01 - AULA 03 (MLCB): Pré-processamento e Stopwords
# ============================================================
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Dataset de Atendimento Financeiro
dados = {
    'mensagem': [
        'Como posso emitir a segunda via do meu boleto?',
        'Preciso da 2a via da minha fatura atrasada',
        'Quero negociar o pagamento da minha dívida',
        'Como fazer um acordo para pagar o débito em aberto?',
        'Gostaria de alterar meu endereço de cadastramento',
        'Onde atualizo os meus dados residenciais no app?'
    ],
    'intencao': [
        'segunda_via', 'segunda_via',
        'negociar_divida', 'negociar_divida',
        'atualizar_cadastro', 'atualizar_cadastro'
    ]
}

df1 = pd.DataFrame(dados)

# Criando lista de Stopwords personalizadas em Português
stopwords_pt = [
    'de', 'da', 'do', 'dos', 'das', 'a', 'o', 'as', 'os', 'em', 'para',
    'com', 'por', 'meu', 'minha', 'meus', 'minhas', 'como', 'quero', 'preciso'
]

# Vetorização TF-IDF aplicando stopwords e n-grams
vectorizer = TfidfVectorizer(stop_words=stopwords_pt, ngram_range=(1, 2))
X_vec = vectorizer.fit_transform(df1['mensagem'])
y = df1['intencao']

modelo = LogisticRegression()
modelo.fit(X_vec, y)

# Teste com nova mensagem
frase_teste = ["Preciso urgente da segunda via da fatura"]
frase_vec = vectorizer.transform(frase_teste)
predicao = modelo.predict(frase_vec)[0]

print("--- RESULTADOS DO LAB 01 (AULA 03) ---")
print(f"Mensagem: '{frase_teste[0]}'")
print(f"Intenção Predita: [{predicao}]")
print(f"Vocabulário Filtrado (sem stopwords): {list(vectorizer.get_feature_names_out())}")

#========== PRODUÇÃO DO RELATÓRIO:==============
# 1 - Qual o impacto da remoção de stopwords no tamanho do vocabulário do modelo?
# 2 - O que significa a configuração ngram_range=(1, 2) no TfidfVectorizer?
# 3 - Como a remoção de palavras genéricas ajuda a evitar classificações incorretas?
# Todos os resultados devem ser inseridos no arquivo resultados_aula03.md
#========== FIM ==============



# ============================================================
# LAB 02 - AULA 03 (MLCB): Matriz de Confusão e Métricas
# ============================================================
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Dataset ampliado para avaliação estatística
dados = {
    'mensagem': [
        'Onde fica a loja fisica?', 'Qual o endereço da unidade SP?', 'Como chegar na loja?',
        'Qual o horario de funcionamento?', 'A loja abre aos domingos?', 'Que horas voces fecham?',
        'Quero trocar um produto com defeito', 'Como funciona a troca?', 'Preciso devolver meu pedido'
    ],
    'intencao': [
        'localizacao', 'localizacao', 'localizacao',
        'horario_atendimento', 'horario_atendimento', 'horario_atendimento',
        'troca_devolucao', 'troca_devolucao', 'troca_devolucao'
    ]
}

df2 = pd.DataFrame(dados)

X_train, X_test, y_train, y_test = train_test_split(
    df2['mensagem'], df2['intencao'], test_size=0.33, random_state=42
)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

modelo = MultinomialNB()
modelo.fit(X_train_vec, y_train)

y_pred = modelo.predict(X_test_vec)

print("--- RESULTADOS DO LAB 02 (AULA 03) ---")
print("\n--- Relatório de Classificação ---")
print(classification_report(y_test, y_pred, zero_division=0))

print("--- Matriz de Confusão ---")
print(confusion_matrix(y_test, y_pred))

#========== PRODUÇÃO DO RELATÓRIO:==============
# 1 - O que representam as métricas Precision, Recall e F1-Score no relatório?
# 2 - Como interpretar a diagonal principal da Matriz de Confusão?
# 3 - Por que a acurácia isolada pode ser enganosa quando temos classes desbalanceadas?
# Todos os resultados devem ser inseridos no arquivo resultados_aula03.md
#========== FIM ==============




# ============================================================
# LAB 03 - AULA 03 (MLCB): Scikit-Learn Pipeline (Modo TODO)
# ============================================================
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dados_rh = {
    'mensagem': [
        'Como solicitar minhas ferias?', 'Quero agendar meu periodo de ferias',
        'Onde baixo meu holerite do mes?', 'Preciso do comprovante de rendimentos',
        'Como cadastrar meu atestado medico?', 'Onde envio o atestado de consulta?'
    ],
    'intencao': [
        'solicitar_ferias', 'solicitar_ferias',
        'obter_holerite', 'obter_holerite',
        'enviar_atestado', 'enviar_atestado'
    ]
}

df3 = pd.DataFrame(dados_rh)

# TODO 1: Separe o dataset em X ('mensagem') e y ('intencao')
X = None
y = None

# TODO 2: Realize o train_test_split com test_size=0.33 e random_state=42
# X_train, X_test, y_train, y_test = ...

# TODO 3: Monte o Pipeline encapsulando o TfidfVectorizer e a LogisticRegression
# pipeline = Pipeline([
#     ('vectorizer', TfidfVectorizer(stop_words=['de', 'o', 'meu', 'minhas'])),
#     ('classifier', LogisticRegression())
# ])

# TODO 4: Treine o pipeline completo com .fit() usando os dados de treino brutos
# pipeline.fit(...)

# TODO 5: Faca a predicao nos dados de teste brutos e exiba a acuracia
# predicoes = pipeline.predict(...)
# print(f"Acuracia via Pipeline: {accuracy_score(y_test, predicoes) * 100:.2f}%")

#========== PRODUÇÃO DO RELATÓRIO:==============
# 1 - Cole o código corrigido e a acurácia obtida.
# 2 - Qual é a grande vantagem de utilizar o objeto Pipeline no Scikit-Learn?
# 3 - Por que o Pipeline evita que erros de pré-processamento ocorram entre treino e teste?
# Todos os resultados devem ser inseridos no arquivo resultados_aula03.md
#========== FIM ==============


# ============================================================
# LAB 03 - AULA 03 (MLCB): Scikit-Learn Pipeline (RESOLVIDO)
# ============================================================
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dados_rh = {
    'mensagem': [
        'Como solicitar minhas ferias?', 'Quero agendar meu periodo de ferias',
        'Onde baixo meu holerite do mes?', 'Preciso do comprovante de rendimentos',
        'Como cadastrar meu atestado medico?', 'Onde envio o atestado de consulta?'
    ],
    'intencao': [
        'solicitar_ferias', 'solicitar_ferias',
        'obter_holerite', 'obter_holerite',
        'enviar_atestado', 'enviar_atestado'
    ]
}

df3 = pd.DataFrame(dados_rh)

# TODO 1: Separe o dataset em X ('mensagem') e y ('intencao')
X = df3['mensagem']
y = df3['intencao']

# TODO 2: Realize o train_test_split com test_size=0.33 e random_state=42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# TODO 3: Monte o Pipeline encapsulando o TfidfVectorizer e a LogisticRegression
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=['de', 'o', 'meu', 'minhas', 'como', 'onde'])),
    ('classifier', LogisticRegression())
])

# TODO 4: Treine o pipeline completo com .fit() usando os dados de treino brutos
pipeline.fit(X_train, y_train)

# TODO 5: Faca a predicao nos dados de teste brutos e exiba a acuracia
predicoes = pipeline.predict(X_test)
acuracia = accuracy_score(y_test, predicoes)

print("--- RESULTADOS DO LAB 03 (AULA 03) ---")
print(f"Acuracia via Pipeline: {acuracia * 100:.2f}%")


