from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Simulação de uma carteira fictícia de ações (dicionário em memória)
carteira = {}

# Token da API
TOKEN = "sm82wqFkZdnKptCiSRkL2b"

# URL base da API
BASE_URL = "https://brapi.dev/api/quote/"

@app.get("/ativos")
def listar_ativos():
    """
    Lista todos os ativos disponíveis na API da bolsa brasileira.
    """
    url = f"https://brapi.dev/api/quote/list?type=stock&token={TOKEN}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    raise HTTPException(status_code=500, detail="Erro ao buscar ativos da bolsa brasileira")

@app.post("/ativos/carteira/adicionar/{codigo_acao}")
def adicionar_acao(codigo_acao: str, quantidade: int):
    """
    Adiciona uma ação à carteira, com base no código da ação.
    """
    url = f"{BASE_URL}{codigo_acao}?token={TOKEN}"

    response = requests.get(url)

    if response.status_code == 200:
        dados_acao = response.json()

        if not dados_acao.get("results"):
            raise HTTPException(status_code=404, detail="Ação não encontrada na API")

        acao_info = dados_acao["results"][0]
        
        carteira[codigo_acao] = {
            "nome": acao_info["longName"],
            "quantidade": quantidade,
            "preco_atual": acao_info["regularMarketPrice"],
            "valor_total": quantidade * acao_info["regularMarketPrice"]
        }
        return {"mensagem": f"Ação {codigo_acao} adicionada à carteira com sucesso!", "detalhes": carteira[codigo_acao]}

    raise HTTPException(status_code=404, detail="Erro ao buscar a ação na API")

@app.get("/ativos/carteira/{codigo_acao}")
def buscar_acao(codigo_acao: str):
    """
    Busca informações de uma ação específica na carteira.
    """
    if codigo_acao in carteira:
        return carteira[codigo_acao]
    
    raise HTTPException(status_code=404, detail="Ação não encontrada na carteira")

@app.get("/ativos/carteira")
def visualizar_carteira():
    """
    Retorna todas as ações da carteira fictícia.
    """
    return carteira

@app.put("/ativos/carteira/atualizar")
def atualizar_carteira():
    """
    Atualiza os preços das ações da carteira fictícia com base nos dados mais recentes da API(Os dados da API são atualizados a cada 30 minutos).
    """
    if not carteira:
        raise HTTPException(status_code=400, detail="A carteira está vazia.")

    for codigo_acao in carteira.keys():
        url = f"{BASE_URL}{codigo_acao}?token={TOKEN}"

        response = requests.get(url)

        if response.status_code == 200:
            dados_acao = response.json()

            if not dados_acao.get("results"):
                continue  # Se a API não encontrar o ativo, ele não será atualizado

            acao_info = dados_acao["results"][0]
            carteira[codigo_acao]["preco_atual"] = acao_info["regularMarketPrice"]
            carteira[codigo_acao]["valor_total"] = carteira[codigo_acao]["quantidade"] * acao_info["regularMarketPrice"]

    return {"mensagem": "Carteira atualizada com sucesso!", "carteira": carteira}

@app.delete("/ativos/carteira/remover/{codigo_acao}")
def remover_acao(codigo_acao: str):
    """
    Remove uma ação da carteira fictícia.
    """
    if codigo_acao in carteira:
        del carteira[codigo_acao]
        return {"mensagem": f"Ação {codigo_acao} removida da carteira."}
    
    raise HTTPException(status_code=404, detail="Ação não encontrada na carteira")

