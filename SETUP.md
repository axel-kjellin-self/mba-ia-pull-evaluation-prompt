# Guia de Configuração do Ambiente

## ✅ O que já está pronto

- ✅ API Key OpenAI configurada
- ✅ API Key Google Gemini configurada
- ✅ Dockerfile e docker-compose.yml criados
- ✅ .env criado (falta apenas LangSmith)

## 🔧 Passos para configurar LangSmith

### 1. Criar conta no LangSmith

Acesse: https://smith.langchain.com/

- Faça login com Google, GitHub ou email
- É gratuito para uso básico

### 2. Criar API Key do LangSmith

1. Após login, vá em **Settings** (⚙️) no canto superior direito
2. Clique em **API Keys** no menu lateral
3. Clique em **Create API Key**
4. Dê um nome (ex: "prompt-optimization-challenge")
5. Copie a key (ela só aparece uma vez!)

### 3. Descobrir seu username do LangSmith Hub

Seu username é necessário para fazer push dos prompts. Para descobrir:

**Opção 1 - Via interface:**
1. Vá em https://smith.langchain.com/hub
2. Clique em **Create Prompt** (botão azul)
3. Crie um prompt qualquer (só para teste)
4. Após criar, abra o prompt e clique no ícone de cadeado 🔒
5. Você verá algo como: `seu-username/nome-do-prompt`
6. O `seu-username` é o que você precisa!

**Opção 2 - Via Settings:**
1. Vá em Settings → Profile
2. Seu username aparece no campo "Handle" ou "Username"

### 4. Atualizar o arquivo .env

Edite o arquivo `.env` e preencha:

```bash
LANGSMITH_API_KEY=lsv2_pt_xxxxxxxxxxxxx  # A key que você copiou no passo 2
USERNAME_LANGSMITH_HUB=seu-username       # O username do passo 3
```

## 🚀 Testando a configuração

### Opção 1: Com Docker (recomendado)

```bash
# Build da imagem
docker-compose build

# Subir o container
docker-compose up -d

# Entrar no container
docker-compose exec app bash

# Dentro do container, teste se as credenciais funcionam
python -c "from langsmith import Client; client = Client(); print('✅ LangSmith conectado!')"
```

### Opção 2: Sem Docker (usando venv local)

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Testar conexão
python -c "from langsmith import Client; client = Client(); print('✅ LangSmith conectado!')"
```

## 📋 Próximos passos

Após configurar o LangSmith:

1. ✅ Configurar ambiente (você está aqui)
2. 📥 Implementar pull dos prompts (`src/pull_prompts.py`)
3. ✏️ Otimizar prompts (`prompts/bug_to_user_story_v2.yml`)
4. 📤 Implementar push dos prompts (`src/push_prompts.py`)
5. 📊 Avaliar e iterar até atingir >= 0.9
6. 🧪 Implementar testes (`tests/test_prompts.py`)

## 🆘 Troubleshooting

**Erro: "Unauthorized" ao testar LangSmith**
- Verifique se a API key está correta no .env
- Verifique se o arquivo .env está sendo carregado (use `echo $LANGSMITH_API_KEY` dentro do container)

**Erro: "Module not found"**
- Se usando Docker: rode `docker-compose build` novamente
- Se usando venv: rode `pip install -r requirements.txt` novamente

**Erro de rate limit do Gemini**
- Troque para OpenAI no .env: mude `LLM_PROVIDER=openai`
