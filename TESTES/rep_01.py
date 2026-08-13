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



