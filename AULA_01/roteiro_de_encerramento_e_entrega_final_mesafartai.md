# 🚀 ROTEIRO DE ENCERRAMENTO E ENTREGA FINAL — PROJETO MESAFARTAI
## **Machine Learning & Chatbots — FASE 2 (Etapa Final & Ponto Bônus)**
**Ambiente de Desenvolvimento:** 100% VS Code Local  
**Diretório de Assets:** `assets/` (Logotipo já criado pelo grupo)  
**Versionamento:** Git & GitHub (`main`)

---

## 🎯 OBJETIVO DA AULA DE ENCERRAMENTO
Consolidar todas as camadas do **MESAFARTAI** (NLU com Random Forest, Extração com Regex, Matchmaking com KNN, Persistência em SQLite3 e Interface Reativa em Streamlit), aplicando **5 melhorias finais** (3 de interface/layout e 2 de regras de negócio), executando o **teste integrado ponta a ponta** e realizando o commit final no GitHub.

---

## 🛠️ PARTE 1: AS 5 MELHORIAS OBRIGATÓRIAS NO VS CODE

### 🖥️ A. Melhorias de Layout e Experiência do Usuário (3 Melhorias)

1. **Integração do Logotipo (`assets/`) e Barra Lateral (`st.sidebar`):**
   * Carregar a imagem já salva na pasta `assets/` no topo da barra lateral:
     ```python
     st.sidebar.image("assets/logo.png", width=180)
     st.sidebar.title("MESAFARTAI")
     st.sidebar.info("ODS 2 — Fome Zero e Agricultura Sustentável")
     ```
   * Incluir na barra lateral os **nomes dos integrantes do grupo** e um botão funcional para resetar a conversa:
     ```python
     if st.sidebar.button("🗑️ Limpar Conversa"):
         st.session_state.historico = []
         st.rerun()
     ```

2. **Mapa Geográfico das ONGs Parceiras (`st.map`):**
   * Na aba do **Dashboard**, utilizar o DataFrame `df_ongs` (que já possui as colunas `latitude` e `longitude`) para plotar a localização das entidades:
     ```python
     st.subheader("🗺️ Distribuição Geográfica das ONGs")
     st.map(df_ongs)
     ```

3. **Indicador Visual de Confiança da IA (`st.progress` e `st.toast`):**
   * Ao processar uma mensagem no chatbot, exibir visualmente a confiança da classificação NLU e disparar uma notificação rápida na tela:
     ```python
     st.progress(float(confianca), text=f"Confiança da IA (NLU): {confianca * 100:.1f}%")
     st.toast("✅ Doação processada e registrada no banco!", icon="🍲")
     ```

---

### ⚙️ B. Melhorias de Regras de Negócio (2 Melhorias)

4. **Persistência Real das Doações no SQLite3 (Dashboard Dinâmico):**
   * Criar a tabela `doacoes` no banco `mesafartai.db` caso não exista:
     ```sql
     CREATE TABLE IF NOT EXISTS doacoes (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         alimento TEXT NOT NULL,
         quantidade_kg REAL NOT NULL,
         validade TEXT NOT NULL,
         urgencia TEXT NOT NULL,
         ong_destino TEXT NOT NULL
     )
     ```
   * Sempre que o chatbot validar uma doação, executar um `INSERT` parametrizado (`?`) com `conn.commit()`.
   * No **Dashboard**, substituir os números estáticos por consultas reais (`SELECT COALESCE(SUM(quantidade_kg), 0) FROM doacoes` e `SELECT * FROM doacoes`).

5. **Classificação Automática de Urgência Logística (Perecibilidade):**
   * Implementar no extrator (`src/entities.py`) ou no fluxo principal (`src/app.py`) a regra de prioridade baseada na validade identificada:
     * Validade para **hoje** (`0 dias`) $\rightarrow$ `"🚨 ALTA (Coleta Imediata)"`
     * Validade para **amanhã** (`1 dia`) $\rightarrow$ `"⚠️ MÉDIA (Prioridade 24h)"`
     * Demais prazos $\rightarrow$ `"🟢 NORMAL"`
   * Exibir o nível de urgência tanto na resposta do chatbot quanto na tabela de registros do Dashboard.

---

## 🧪 PARTE 2: ROTEIRO DE TESTE COMPLETO DO SISTEMA (END-TO-END)

Antes de finalizar o repositório, o grupo deve rodar `streamlit run src/app.py` no terminal do VS Code e validar **todos os 5 cenários abaixo** em sequência:

| Passo | Ação no Sistema | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Abrir a aplicação no navegador | Logotipo da pasta `assets/` visível na barra lateral e abas funcionando sem erros. |
| **2** | Enviar no chat: `"Quero doar 15,5 kg de tomate que vencem hoje"` | NLU reconhece intenção; Regex extrai `15.5 kg` e `Tomate`; Urgência marcada como **ALTA**; KNN aponta a ONG mais próxima; barra de confiança exibida. |
| **3** | Enviar no chat: `"Tenho 40 quilos de arroz para doar amanhã"` | Registro gravado no SQLite com Urgência **MÉDIA**. |
| **4** | Enviar no chat: `"Qual a previsão do tempo hoje?"` | Trava de *Threshold* aciona o *fallback* sem gravar lixo no banco de dados. |
| **5** | Acessar a aba **Dashboard de Impacto Social** | KPIs atualizados automaticamente somando `55.5 kg` arrecadados, tabela exibindo as 2 doações reais e mapa plotando as ONGs. |

---

## 📦 PARTE 3: ENTREGA OFICIAL NO GITHUB (VS CODE)

Com os testes validados e o banco `mesafartai.db` populado com os testes do grupo, execute no terminal do VS Code:

```bash
git status
git add .
git commit -m "feat(final): conclui projeto mesafartai com melhorias de layout, regras de negocio e testes"
git push origin main
```

---

## 🌟 ATIVIDADE BÔNUS (+0,25 PONTO): VITRINE TÉCNICA NO LINKEDIN

Para conquistar **+0,25 ponto extra** na média final, o grupo (ou cada integrante) deve publicar uma demonstração prática do projeto funcionando:

1. **Gravação de Tela (30s a 60s):**
   * Grave a tela do computador mostrando a interface do **MESAFARTAI** rodando localmente, realizando **pelo menos duas doações reais pelo chatbot** (testando a extração de texto e o match logístico) e abrindo a aba do **Dashboard** para mostrar os indicadores e o mapa atualizados em tempo real.
2. **Publicação no LinkedIn:**
   * Poste o vídeo no LinkedIn explicando brevemente a arquitetura utilizada (**Python, Machine Learning com Random Forest & KNN, Regex, SQLite3 e Streamlit**) e o alinhamento com a **ODS 2 da ONU (Fome Zero)**.
   * Marque o professor na publicação e inclua o link do repositório GitHub do grupo.