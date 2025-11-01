"""
This file contains the API features
"""

import os
import googleapiclient.discovery # CRIA o SERVICE,  Conexao com a API
import google.auth.transport.requests # Requiscoes http
import google.oauth2.credentials # Gerencia o token de Acesso
import google_auth_oauthlib.flow # controla o fluxo do OAuth (autenticacao via navegador)


# Define o Escopo (O que o programa pode fazer no drive) da API, neste caso apenas leitura
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

caminho_token = os.path.join(os.path.dirname(__file__), "data", "token.json")

def autenticar():
    print("teste")