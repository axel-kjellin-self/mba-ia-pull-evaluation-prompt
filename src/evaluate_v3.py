#!/usr/bin/env python3
"""Avaliação do prompt v3"""
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Temporariamente mudar para avaliar v3
os.environ['PROMPT_TO_EVALUATE'] = 'axelkjellin/bug_to_user_story_v3'

# Importar e executar avaliação
from evaluate import main

if __name__ == "__main__":
    sys.exit(main())
