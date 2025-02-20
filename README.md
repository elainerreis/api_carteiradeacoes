# Documentação da API - Carteira Fictícia de Ações

## Introdução
Esta API permite a gestão de uma carteira fictícia de ações utilizando dados da API **brapi.dev**. A API possibilita a listagem de ativos da bolsa brasileira, adição e remoção de ações na carteira, consulta de uma ação específica, atualização de preços e visualização da carteira completa.

## Endpoints

### 1. **Listar Ativos**
**Rota:** `GET /ativos`

**Descrição:** Retorna a lista de ativos disponíveis na API da bolsa brasileira.

**Resposta de Sucesso:**
```json
{
  "stocks": [
    {"symbol": "PETR4", "longName": "Petrobras PN"},
    {"symbol": "VALE3", "longName": "Vale ON"}
  ]
}
```

**Códigos de Status:**
- `200` - Sucesso
- `500` - Erro ao buscar ativos

---

### 2. **Adicionar Ação na Carteira**
**Rota:** `POST /carteira/adicionar/{codigo_acao}`

**Descrição:** Adiciona uma ação à carteira fictícia informando o **código** da ação e a **quantidade** desejada.

**Parâmetros:**
- `codigo_acao` (string) - Código da ação (ex: "PETR4")
- `quantidade` (int) - Quantidade de ações a serem adicionadas

**Resposta de Sucesso:**
```json
{
  "mensagem": "Ação PETR4 adicionada à carteira com sucesso!",
  "detalhes": {
    "nome": "Petrobras PN",
    "quantidade": 10,
    "preco_atual": 30.5,
    "valor_total": 305.0
  }
}
```

**Códigos de Status:**
- `200` - Sucesso
- `404` - Ação não encontrada

---

### 3. **Buscar uma Ação Específica na Carteira**
**Rota:** `GET /carteira/{codigo_acao}`

**Descrição:** Busca informações de uma ação específica dentro da carteira.

**Resposta de Sucesso:**
```json
{
  "nome": "Petrobras PN",
  "quantidade": 10,
  "preco_atual": 30.5,
  "valor_total": 305.0
}
```

**Códigos de Status:**
- `200` - Sucesso
- `404` - Ação não encontrada na carteira

---

### 4. **Visualizar Toda a Carteira**
**Rota:** `GET /carteira`

**Descrição:** Retorna todas as ações atualmente na carteira.

**Resposta de Sucesso:**
```json
{
  "PETR4": {
    "nome": "Petrobras PN",
    "quantidade": 10,
    "preco_atual": 30.5,
    "valor_total": 305.0
  }
}
```

**Códigos de Status:**
- `200` - Sucesso

---

### 5. **Atualizar Preços das Ações na Carteira**
**Rota:** `PUT /carteira/atualizar`

**Descrição:** Atualiza os preços das ações da carteira com os valores mais recentes da API.

**Resposta de Sucesso:**
```json
{
  "mensagem": "Carteira atualizada com sucesso!",
  "carteira": {
    "PETR4": {
      "nome": "Petrobras PN",
      "quantidade": 10,
      "preco_atual": 31.0,
      "valor_total": 310.0
    }
  }
}
```

**Códigos de Status:**
- `200` - Sucesso
- `400` - Carteira vazia

---

### 6. **Remover Ação da Carteira**
**Rota:** `DELETE /carteira/remover/{codigo_acao}`

**Descrição:** Remove uma ação da carteira fictícia.

**Parâmetros:**
- `codigo_acao` (string) - Código da ação a ser removida

**Resposta de Sucesso:**
```json
{
  "mensagem": "Ação PETR4 removida da carteira."
}
```

**Códigos de Status:**
- `200` - Sucesso
- `404` - Ação não encontrada na carteira

---

## Configuração e Execução
### **Instalação das Dependências**
Para executar a API, instale o **FastAPI** e o **Uvicorn**:
```bash
pip install fastapi uvicorn requests
```

### **Executar a API**
No terminal, rode:
```bash
uvicorn carteira:app --reload
```
(onde `carteira` é o nome do arquivo Python que contém o código.)

### **Acessar a Documentação Interativa**
Após rodar a API, acesse a documentação interativa do **FastAPI**:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


