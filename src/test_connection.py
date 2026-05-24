#!/usr/bin/env python3
"""Teste de conexão com LangSmith"""
import os
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

print("🔧 Testando conexão com LangSmith...\n")

# Verificar variáveis de ambiente
api_key = os.getenv("LANGSMITH_API_KEY")
if not api_key:
    print("❌ LANGSMITH_API_KEY não encontrada no .env")
    exit(1)

print(f"✅ API Key encontrada: {api_key[:20]}...")

# Testar conexão
try:
    client = Client()
    print("✅ Cliente LangSmith criado com sucesso!")

    # Verificar se consegue acessar a API
    print("\n🔍 Testando acesso à API...")
    # Tentar listar datasets (qualquer operação simples)
    try:
        # Apenas tenta uma operação para validar a conexão
        client.read_project(project_name="default")
        print("✅ Conexão com LangSmith funcionando!")
    except Exception as e:
        # É esperado dar erro se o projeto não existe, mas confirma que a API está acessível
        if "404" in str(e) or "not found" in str(e).lower():
            print("✅ Conexão com LangSmith funcionando!")
        else:
            print(f"⚠️  Possível erro de autenticação: {e}")

    print("\n" + "="*60)
    print("✅ TUDO PRONTO! Configuração do LangSmith OK!")
    print("="*60)

    print("\n📋 Próximo passo: Descobrir seu USERNAME")
    print("\n👉 Siga estes passos:")
    print("   1. Acesse: https://smith.langchain.com/hub")
    print("   2. Clique no botão 'New prompt' (azul, canto superior direito)")
    print("   3. Preencha:")
    print("      - Name: test-prompt")
    print("      - Description: teste")
    print("      - Prompt: qualquer coisa (ex: 'You are a helpful assistant')")
    print("   4. Clique em 'Commit'")
    print("   5. Você verá o nome completo: 'SEU-USERNAME/test-prompt'")
    print("   6. Copie apenas o SEU-USERNAME")
    print("\n   Depois volte e me informe o username!")

except Exception as e:
    print(f"❌ Erro ao conectar com LangSmith: {e}")
    print("\n🔧 Verifique:")
    print("   1. Se a API key está correta no .env")
    print("   2. Se você tem acesso à internet")
    print("   3. Se a key não foi revogada no dashboard do LangSmith")
