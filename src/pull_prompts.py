"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    """
    Faz pull de prompts do LangSmith Hub e salva localmente.

    Returns:
        bool: True se sucesso, False caso contrário
    """
    print_section_header("📥 Pull de Prompts do LangSmith Hub")

    # Nome do prompt no Hub (do professor)
    hub_prompt_name = "leonanluppi/bug_to_user_story_v1"
    output_file = "prompts/bug_to_user_story_v1.yml"

    try:
        print(f"🔍 Buscando prompt: {hub_prompt_name}")

        # Faz pull do prompt do Hub
        prompt_obj = hub.pull(hub_prompt_name)

        print(f"✅ Prompt encontrado no Hub!")
        print(f"   Tipo: {type(prompt_obj).__name__}")

        # Extrair informações do prompt
        # O objeto retornado é um ChatPromptTemplate do LangChain
        prompt_dict = prompt_obj.dict() if hasattr(prompt_obj, 'dict') else {}

        # Extrair mensagens do prompt
        messages = []
        system_prompt = ""
        user_prompt = ""

        if hasattr(prompt_obj, 'messages'):
            for msg in prompt_obj.messages:
                # Determinar tipo da mensagem pelo nome da classe
                msg_class = type(msg).__name__

                # Extrair template do prompt
                msg_content = ""
                if hasattr(msg, 'prompt') and hasattr(msg.prompt, 'template'):
                    msg_content = msg.prompt.template

                # Classificar por tipo
                if 'System' in msg_class:
                    system_prompt = msg_content
                    messages.append({'type': 'system', 'content': msg_content})
                elif 'Human' in msg_class or 'User' in msg_class:
                    user_prompt = msg_content
                    messages.append({'type': 'human', 'content': msg_content})
                else:
                    messages.append({'type': 'unknown', 'content': msg_content})

        # Montar estrutura YAML
        yaml_data = {
            'bug_to_user_story_v1': {
                'description': 'Prompt para converter relatos de bugs em User Stories (versão inicial de baixa qualidade)',
                'system_prompt': system_prompt.strip() if system_prompt else "Sistema não definido",
                'user_prompt': user_prompt.strip() if user_prompt else "{bug_report}",
                'version': 'v1',
                'created_at': '2025-01-15',
                'tags': ['bug-analysis', 'user-story', 'product-management'],
                'metadata': {
                    'source': 'langsmith_hub',
                    'original_name': hub_prompt_name,
                    'pulled_at': __import__('datetime').datetime.now().isoformat()
                }
            }
        }

        print(f"\n📝 Estrutura do prompt:")
        print(f"   System Prompt: {len(system_prompt)} caracteres")
        print(f"   User Prompt: {len(user_prompt)} caracteres")
        print(f"   Mensagens: {len(messages)}")

        # Salvar em YAML
        print(f"\n💾 Salvando em: {output_file}")
        if save_yaml(yaml_data, output_file):
            print(f"✅ Prompt salvo com sucesso!")
            return True
        else:
            print(f"❌ Erro ao salvar prompt")
            return False

    except Exception as e:
        print(f"❌ Erro ao fazer pull do prompt: {e}")
        print(f"\n💡 Verifique:")
        print(f"   1. Se o prompt existe no Hub: https://smith.langchain.com/hub/{hub_prompt_name}")
        print(f"   2. Se sua LANGSMITH_API_KEY está correta no .env")
        print(f"   3. Se você tem acesso à internet")
        return False


def main():
    """Função principal"""
    print_section_header("🚀 Pull de Prompts do LangSmith", "=", 60)

    # Verificar variáveis de ambiente necessárias
    required_vars = ['LANGSMITH_API_KEY']
    if not check_env_vars(required_vars):
        return 1

    # Fazer pull dos prompts
    success = pull_prompts_from_langsmith()

    if success:
        print_section_header("✅ Pull concluído com sucesso!", "=", 60)
        print("📂 Próximos passos:")
        print("   1. Analise o prompt em: prompts/bug_to_user_story_v1.yml")
        print("   2. Identifique os problemas de qualidade")
        print("   3. Crie prompts/bug_to_user_story_v2.yml com suas otimizações")
        print("   4. Execute: python src/push_prompts.py")
        return 0
    else:
        print_section_header("❌ Pull falhou", "=", 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
