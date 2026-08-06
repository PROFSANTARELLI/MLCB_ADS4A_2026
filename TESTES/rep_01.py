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
