#!/usr/bin/env python3
"""Push do prompt v3"""
import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from utils import load_yaml

load_dotenv()

# Carregar v3
data = load_yaml('prompts/bug_to_user_story_v3.yml')
if not data:
    print("❌ Erro ao carregar v3.yml")
    sys.exit(1)

prompt_data = data['bug_to_user_story_v3']

# Criar ChatPromptTemplate
system_template = SystemMessagePromptTemplate.from_template(prompt_data['system_prompt'])
human_template = HumanMessagePromptTemplate.from_template(prompt_data['user_prompt'])
chat_prompt = ChatPromptTemplate.from_messages([system_template, human_template])

# Push
username = os.getenv('USERNAME_LANGSMITH_HUB')
full_name = f'{username}/bug_to_user_story_v3'

print(f"📤 Fazendo push: {full_name}")
hub.push(full_name, chat_prompt, new_repo_is_public=True)

print(f'✅ Push concluído!')
print(f'🔗 Hub: https://smith.langchain.com/hub/{full_name}')
