# Quick Start - Guia Rápido

## 🚀 Setup Rápido (5 minutos)

### 1. Configurar Credenciais

```bash
# Copiar template
cp .env.example .env

# Editar .env e preencher:
# - LANGSMITH_API_KEY=lsv2_pt_...
# - USERNAME_LANGSMITH_HUB=axelkjellin
# - OPENAI_API_KEY=sk-proj-...
# - LLM_PROVIDER=openai
# - LLM_MODEL=gpt-4o-mini
# - EVAL_MODEL=gpt-4o
```

### 2. Instalar Dependências

**Opção A: Docker (Recomendado)**
```bash
docker-compose build
docker-compose run --rm app bash
```

**Opção B: Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Executar Avaliação do v5 (Oficial)

```bash
python src/evaluate.py
```

**Resultado esperado:**
```
==================================================
Prompt: axelkjellin/bug_to_user_story_v5
==================================================

Métricas Derivadas:
  - Helpfulness: 0.88 ✗
  - Correctness: 0.86 ✗

Métricas Base:
  - F1-Score: 0.84 ✗
  - Clarity: 0.88 ✗
  - Precision: 0.87 ✗

📊 MÉDIA GERAL: 0.8648
```

---

## 📝 Comandos Principais

### Pull de Prompts
```bash
python src/pull_prompts.py
```

### Push de Prompts
```bash
python src/push_prompts.py
```

### Avaliar Prompts
```bash
python src/evaluate.py
```

### Rodar Testes
```bash
pytest tests/test_prompts.py -v
```

---

## 🔗 Links Rápidos

- **Documentação Completa:** [DOCUMENTACAO.md](./DOCUMENTACAO.md)
- **Resultados:** [RESULTADOS.md](./RESULTADOS.md)
- **Hub v5:** https://smith.langchain.com/hub/axelkjellin/bug_to_user_story_v5
- **Hub v4:** https://smith.langchain.com/hub/axelkjellin/bug_to_user_story_v4

---

## 🧪 Testar com Outro Modelo

### Trocar para GPT-4o (mais potente)

```bash
# Editar .env:
LLM_MODEL=gpt-4o  # Em vez de gpt-4o-mini

# Executar avaliação
python src/evaluate.py
```

### Trocar para Gemini

```bash
# Editar .env:
LLM_PROVIDER=google
LLM_MODEL=gemini-2.5-flash
EVAL_MODEL=gemini-2.5-flash

# Executar avaliação
python src/evaluate.py
```

---

## ❓ Troubleshooting

### Erro: "LANGSMITH_API_KEY não configurada"
```bash
# Verificar se .env existe e tem a key
cat .env | grep LANGSMITH_API_KEY

# Se não, copiar do .env.example e preencher
```

### Erro: "Module not found"
```bash
# Reinstalar dependências
pip install -r requirements.txt
```

### Erro: "Resource not found" ao avaliar
```bash
# Verificar se o prompt existe no Hub
# Fazer push novamente:
python src/push_prompts.py
```

---

## 📊 Estrutura de Arquivos Principais

```
desafio_2/
├── DOCUMENTACAO.md          ← Documentação completa
├── RESULTADOS.md            ← Resumo executivo
├── QUICK_START.md           ← Este arquivo
├── prompts/
│   ├── bug_to_user_story_v5.yml  ← ✅ OFICIAL
│   └── bug_to_user_story_v4.yml  ← 2ª melhor
├── src/
│   ├── pull_prompts.py      ← Pull do Hub
│   ├── push_prompts.py      ← Push ao Hub
│   └── evaluate.py          ← Avaliação (usa v5)
└── tests/
    └── test_prompts.py      ← Testes
```

---

**Pronto para começar!** 🚀

Se tiver dúvidas, consulte [DOCUMENTACAO.md](./DOCUMENTACAO.md)
