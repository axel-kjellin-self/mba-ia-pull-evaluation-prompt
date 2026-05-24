"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []

    # Validar campos obrigatórios
    required_fields = ['description', 'system_prompt', 'version']
    for field in required_fields:
        if field not in prompt_data:
            errors.append(f"Campo obrigatório faltando: {field}")

    # Validar conteúdo do system_prompt
    system_prompt = prompt_data.get('system_prompt', '').strip()
    if not system_prompt:
        errors.append("system_prompt está vazio")
    elif len(system_prompt) < 100:
        errors.append(f"system_prompt muito curto ({len(system_prompt)} caracteres). Mínimo recomendado: 100")

    # Validar se há TODOs pendentes
    if 'TODO' in system_prompt or 'TODO' in prompt_data.get('user_prompt', ''):
        errors.append("Prompt ainda contém TODOs - remova antes de fazer push")

    # Validar técnicas aplicadas
    techniques = prompt_data.get('techniques_applied', [])
    if not techniques:
        errors.append("Campo 'techniques_applied' está ausente ou vazio")
    elif len(techniques) < 2:
        errors.append(f"Mínimo de 2 técnicas requeridas, encontradas: {len(techniques)}")

    # Validar se contém exemplos (Few-shot)
    has_examples = 'exemplo' in system_prompt.lower() or 'example' in system_prompt.lower()
    if not has_examples:
        errors.append("Prompt deve conter exemplos (Few-shot Learning é obrigatório)")

    return (len(errors) == 0, errors)


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        username = os.getenv('USERNAME_LANGSMITH_HUB')
        if not username:
            print("❌ USERNAME_LANGSMITH_HUB não configurado no .env")
            print("\n📝 Como descobrir seu username:")
            print("   1. Acesse: https://smith.langchain.com/hub")
            print("   2. Clique em 'New prompt'")
            print("   3. Crie um prompt de teste")
            print("   4. O nome será: 'SEU-USERNAME/nome-do-prompt'")
            print("   5. Adicione USERNAME_LANGSMITH_HUB=seu-username no .env")
            return False

        # Nome completo do prompt no Hub
        full_prompt_name = f"{username}/{prompt_name}"

        print(f"🔍 Preparando prompt: {full_prompt_name}")

        # Extrair dados do prompt
        system_prompt = prompt_data.get('system_prompt', '').strip()
        user_prompt = prompt_data.get('user_prompt', '{bug_report}').strip()

        # Criar ChatPromptTemplate
        from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate

        # Criar templates de mensagem
        system_template = SystemMessagePromptTemplate.from_template(system_prompt)
        human_template = HumanMessagePromptTemplate.from_template(user_prompt)

        # Criar ChatPromptTemplate completo
        chat_prompt = ChatPromptTemplate.from_messages([
            system_template,
            human_template
        ])

        print(f"✅ ChatPromptTemplate criado")
        print(f"   System: {len(system_prompt)} caracteres")
        print(f"   User: {len(user_prompt)} caracteres")

        # Fazer push para o Hub (PÚBLICO por padrão)
        print(f"\n📤 Fazendo push para: {full_prompt_name}")
        print(f"   Modo: PÚBLICO (is_public=True)")

        hub.push(
            repo_full_name=full_prompt_name,
            object=chat_prompt,
            new_repo_is_public=True  # PÚBLICO
        )

        print(f"✅ Push concluído com sucesso!")
        print(f"\n🔗 Links úteis:")
        print(f"   Hub: https://smith.langchain.com/hub/{full_prompt_name}")
        print(f"   Playground: https://smith.langchain.com/playground?promptOwner={username}&promptSlug={prompt_name}")

        # Informações sobre metadados
        techniques = prompt_data.get('techniques_applied', [])
        if techniques:
            print(f"\n🏷️  Técnicas aplicadas ({len(techniques)}):")
            for tech in techniques:
                print(f"   - {tech}")

        return True

    except Exception as e:
        print(f"❌ Erro ao fazer push: {e}")
        print(f"\n💡 Possíveis causas:")
        print(f"   1. USERNAME_LANGSMITH_HUB incorreto no .env")
        print(f"   2. LANGSMITH_API_KEY inválida ou expirada")
        print(f"   3. Permissões insuficientes no LangSmith")
        print(f"   4. Problema de conexão com a internet")
        return False


def main():
    """Função principal"""
    print_section_header("🚀 Push de Prompts para o LangSmith Hub", "=", 60)

    # Verificar variáveis de ambiente
    required_vars = ['LANGSMITH_API_KEY', 'USERNAME_LANGSMITH_HUB']
    if not check_env_vars(required_vars):
        return 1

    # Arquivo de entrada
    input_file = "prompts/bug_to_user_story_v2.yml"

    print(f"📂 Lendo prompt de: {input_file}\n")

    # Carregar prompt
    data = load_yaml(input_file)
    if not data:
        print(f"❌ Erro ao carregar {input_file}")
        return 1

    # Obter dados do prompt
    prompt_key = 'bug_to_user_story_v2'
    if prompt_key not in data:
        print(f"❌ Chave '{prompt_key}' não encontrada no YAML")
        return 1

    prompt_data = data[prompt_key]

    # Validar prompt
    print_section_header("🔍 Validando Prompt", "-", 60)
    is_valid, errors = validate_prompt(prompt_data)

    if not is_valid:
        print("❌ Prompt inválido! Erros encontrados:")
        for error in errors:
            print(f"   - {error}")
        print("\n💡 Corrija os erros em prompts/bug_to_user_story_v2.yml e tente novamente.")
        return 1

    print("✅ Prompt válido! Todas as validações passaram.")

    # Mostrar resumo
    print("\n📊 Resumo do prompt:")
    print(f"   Versão: {prompt_data.get('version', 'N/A')}")
    print(f"   Descrição: {prompt_data.get('description', 'N/A')[:80]}...")
    print(f"   Técnicas: {len(prompt_data.get('techniques_applied', []))}")
    print(f"   Tags: {len(prompt_data.get('tags', []))}")

    # Push para o Hub
    print_section_header("📤 Push para LangSmith Hub", "-", 60)

    # Nome base do prompt (sem username)
    base_name = "bug_to_user_story_v2"

    success = push_prompt_to_langsmith(base_name, prompt_data)

    if success:
        print_section_header("✅ Push concluído com sucesso!", "=", 60)
        print("📂 Próximos passos:")
        print("   1. Verifique o prompt no Hub (link acima)")
        print("   2. Confirme que está PÚBLICO")
        print("   3. Execute: python src/evaluate.py")
        print("   4. Analise as métricas e itere se necessário")
        return 0
    else:
        print_section_header("❌ Push falhou", "=", 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
