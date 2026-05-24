#!/usr/bin/env python3
"""Debug: visualizar estrutura do prompt do Hub"""
from dotenv import load_dotenv
from langchain import hub
import json

load_dotenv()

hub_prompt_name = "leonanluppi/bug_to_user_story_v1"

print(f"🔍 Fazendo pull de: {hub_prompt_name}\n")

prompt_obj = hub.pull(hub_prompt_name)

print(f"Tipo do objeto: {type(prompt_obj)}")
print(f"Atributos: {dir(prompt_obj)}\n")

# Tentar diferentes formas de acessar o conteúdo
print("="*60)
print("Tentando acessar messages:")
if hasattr(prompt_obj, 'messages'):
    print(f"  Tipo: {type(prompt_obj.messages)}")
    print(f"  Quantidade: {len(prompt_obj.messages)}")
    for i, msg in enumerate(prompt_obj.messages):
        print(f"\n  Mensagem {i}:")
        print(f"    Tipo: {type(msg)}")
        print(f"    Atributos: {dir(msg)}")
        if hasattr(msg, 'content'):
            print(f"    Content: {msg.content[:100]}...")
        if hasattr(msg, 'prompt'):
            print(f"    Prompt: {msg.prompt}")
            if hasattr(msg.prompt, 'template'):
                print(f"    Template: {msg.prompt.template[:100]}...")

print("\n" + "="*60)
print("Tentando format_messages:")
if hasattr(prompt_obj, 'format_messages'):
    try:
        formatted = prompt_obj.format_messages(bug_report="[TESTE]")
        for msg in formatted:
            print(f"\nTipo: {type(msg).__name__}")
            print(f"Content: {msg.content[:200]}...")
    except Exception as e:
        print(f"Erro: {e}")

print("\n" + "="*60)
print("Tentando get_prompts:")
if hasattr(prompt_obj, 'get_prompts'):
    prompts = prompt_obj.get_prompts()
    print(f"Prompts: {prompts}")

print("\n" + "="*60)
print("Tentando acessar via dict/json:")
try:
    if hasattr(prompt_obj, 'dict'):
        data = prompt_obj.dict()
        print(json.dumps(data, indent=2, default=str)[:500])
except Exception as e:
    print(f"Erro: {e}")
