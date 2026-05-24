# Documentação do Processo de Otimização de Prompts

## 📋 Visão Geral do Desafio

### Objetivo
Otimizar prompts de conversão de bugs em User Stories até atingir **≥ 0.9 (90%)** em **TODAS** as 5 métricas de avaliação:
- Helpfulness
- Correctness
- F1-Score
- Clarity
- Precision

### Requisitos Técnicos
- **Linguagem:** Python 3.9+
- **Framework:** LangChain
- **Plataforma:** LangSmith
- **LLM para responder:** gpt-4o-mini
- **LLM para avaliar:** gpt-4o
- **Dataset:** 15 exemplos de bugs (5 simples, 7 médios, 3 complexos)

### Técnicas Obrigatórias
- ✅ **Few-shot Learning** (obrigatório)
- ✅ **Chain of Thought** (aplicado)
- ✅ **Role Prompting** (aplicado)
- Outras técnicas adicionais conforme necessário

---

## 🔄 Processo de Otimização Realizado

### Resumo das Iterações

Foram realizadas **9 iterações** de otimização do prompt, partindo de um prompt inicial ruim (v1) até chegar ao melhor resultado (v5).

| Versão | F1-Score | Clarity | Precision | Helpfulness | Correctness | **MÉDIA** | Δ vs Anterior | Status |
|--------|----------|---------|-----------|-------------|-------------|-----------|---------------|--------|
| **v1** | - | - | - | - | - | - | - | Baseline ruim |
| **v2** | 0.73 | 0.89 | **0.90** ✓ | 0.89 | 0.81 | 0.8447 | - | Primeira versão testada |
| v3 | 0.68 | 0.85 | 0.82 | 0.84 | 0.75 | 0.7880 | -0.0567 | ❌ Piorou |
| **v4** | **0.82** | 0.87 | 0.88 | 0.87 | 0.85 | **0.8558** | +0.0678 | ⬆️ 2º Melhor |
| **v5** | **0.84** | **0.88** | **0.87** | **0.88** | **0.86** | **0.8648** | +0.0090 | ✅ **MELHOR** |
| v6 | 0.78 | 0.86 | 0.79 | 0.82 | 0.79 | 0.8079 | -0.0569 | ❌ Piorou |
| v7 | 0.77 | **0.90** ✓ | 0.84 | 0.87 | 0.81 | 0.8374 | +0.0295 | 1ª métrica passou |
| v8 | 0.82 | 0.87 | 0.86 | 0.87 | 0.84 | 0.8520 | +0.0146 | ⬆️ Melhorou |
| v9 | 0.79 | 0.87 | 0.86 | 0.87 | 0.83 | 0.8440 | -0.0080 | ❌ Piorou |

### Destaques
- ✅ **Melhor média geral:** v5 (0.8648)
- ✅ **Segunda melhor média:** v4 (0.8558)
- ✅ **Única métrica ≥ 0.9:** Clarity no v7 (0.90)
- ✅ **Melhor Precision:** v2 (0.90)
- ⚠️ **Distância da meta:** 0.0352 (3.52%)

---

## 🏆 Melhores Prompts

### v5 - Prompt Oficial (Média: 0.8648)

**Arquivo:** `prompts/bug_to_user_story_v5.yml`

**Pontos Fortes:**
- Melhor equilíbrio entre todas as métricas
- F1-Score mais alto (0.84)
- Estrutura clara e adaptativa por complexidade
- Exemplos bem alinhados com o dataset

**Técnicas Aplicadas:**
1. Few-shot Learning com 3 exemplos (simples, médio, complexo)
2. Chain of Thought com 4 etapas de análise
3. Role Prompting (Product Manager sênior)
4. Adaptive Complexity (formato específico por nível)
5. Self-Validation (checklist de validação)
6. Clear Guidelines (regras do que fazer e não fazer)

**Características Principais:**
- Formato BDD completo: "Dado que... Quando... Então... E..."
- Tudo em português
- Critérios específicos e testáveis
- Limites claros para bugs complexos

### v4 - Segunda Melhor Opção (Média: 0.8558)

**Arquivo:** `prompts/bug_to_user_story_v4.yml`

**Pontos Fortes:**
- Segundo melhor F1-Score (0.82)
- Bom equilíbrio geral
- Estrutura sólida

**Diferenças vs v5:**
- v5 tem instruções mais refinadas
- v5 tem validação mais robusta
- v5 tem F1-Score ligeiramente superior (+0.02)

---

## 📊 Análise Detalhada

### Problemas Identificados

**1. Bugs SIMPLES (itens 1-5, 10):**
- F1-Score consistentemente em 0.75
- Hipótese: Falta de especificidade nos critérios
- Solução tentada: Enfatizar detalhes concretos (não melhorou significativamente)

**2. Bugs COMPLEXOS (item 15):**
- Precision baixo (0.67)
- Hipótese: Excesso de verbosidade
- Solução tentada: Limites mais restritivos (melhorou parcialmente)

**3. Trade-offs Observados:**
- Melhorar F1-Score tende a reduzir Precision
- Melhorar Clarity tende a reduzir F1-Score
- Não foi possível otimizar todas as métricas simultaneamente

### Itens com Performance Perfeita (v5)

**Item 9:** F1:1.00, Clarity:0.90, Precision:0.90 (bug médio)
**Item 12:** F1:1.00, Clarity:1.00, Precision:1.00 (bug complexo)
**Item 13:** F1:1.00, Clarity:0.95, Precision:1.00 (bug complexo)

**Conclusão:** O prompt v5 performa MUITO BEM em bugs médios e complexos, mas tem dificuldade consistente com bugs simples.

---

## 🔧 Técnicas de Prompt Engineering Aplicadas

### 1. Few-shot Learning (Obrigatório)
- 3 exemplos de entrada/saída
- Cobrindo bugs simples, médios e complexos
- Formato alinhado com o dataset esperado

### 2. Chain of Thought
- Processo de 4 etapas antes de gerar resposta:
  1. Analisar complexidade
  2. Identificar elementos
  3. Escrever User Story
  4. Validar

### 3. Role Prompting
- Persona: "Product Manager sênior com 10+ anos de experiência em metodologias ágeis"
- Contexto e especialidade bem definidos

### 4. Adaptive Complexity
- Formato de saída varia conforme complexidade do bug
- Bugs simples: formato básico (5 critérios)
- Bugs médios: formato + contexto técnico
- Bugs complexos: formato com seções detalhadas

### 5. Self-Validation
- Checklist de validação antes de finalizar
- Verifica: idioma, formato BDD, especificidade, verbosidade

### 6. Clear Guidelines
- Regras explícitas: ✅ SEMPRE vs ❌ NUNCA
- Exemplos do que fazer e não fazer

---

## 🎯 Resultados Finais

### Métricas Alcançadas (v5)

```
Helpfulness:   0.88 / 0.90 (97.8% da meta)
Correctness:   0.86 / 0.90 (95.6% da meta)
F1-Score:      0.84 / 0.90 (93.3% da meta)
Clarity:       0.88 / 0.90 (97.8% da meta)
Precision:     0.87 / 0.90 (96.7% da meta)

MÉDIA GERAL:   0.8648 / 0.9000 (96.1% da meta)
```

### Distância da Meta
- **Falta:** 0.0352 pontos (3.52%)
- **Progresso:** Partimos de 0.8447 (v2) → 0.8648 (v5)
- **Melhoria:** +0.0201 pontos (+2.38%)

---

## 💡 Insights e Aprendizados

### 1. Limitações do gpt-4o-mini
- Após 9 iterações, atingimos um platô em ~0.86
- Trade-offs entre métricas impedem otimização simultânea
- O modelo tem dificuldade consistente com bugs simples (F1=0.75)

### 2. Padrões Observados
- **Bugs simples:** Sempre F1=0.75 (problema sistemático)
- **Bugs médios/complexos:** Performance excelente (até 1.00)
- **Verbosidade:** Difícil balancear completude vs concisão

### 3. Iteração 5 foi o Pico
- v5 alcançou a melhor média (0.8648)
- Iterações posteriores (v6-v9) não conseguiram superar
- Cada mudança causava trade-offs que não melhoravam a média geral

### 4. Técnicas que Funcionaram
- ✅ Few-shot Learning bem alinhado com dataset
- ✅ Formato adaptativo por complexidade
- ✅ BDD em português
- ✅ Validação robusta

### 5. Técnicas que NÃO Funcionaram
- ❌ Adicionar mais exemplos (v6 piorou)
- ❌ Skeleton of Thought adicional (sem impacto significativo)
- ❌ Limites muito restritivos (v7-v9 não melhoraram média)

---

## 🚀 Como Executar

### 1. Configuração do Ambiente

```bash
# Clonar repositório
cd /home/axel/pos/desafio_2

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar .env
cp .env.example .env
# Editar .env com suas credenciais:
# - LANGSMITH_API_KEY
# - USERNAME_LANGSMITH_HUB
# - OPENAI_API_KEY (ou GOOGLE_API_KEY)
```

### 2. Pull do Prompt v1 (baseline ruim)

```bash
python src/pull_prompts.py
```

### 3. Push do Prompt v5 (melhor versão)

O prompt v5 já está otimizado em `prompts/bug_to_user_story_v5.yml`

```bash
# Modificar push_prompts.py para ler v5 em vez de v2
python src/push_prompts.py
```

### 4. Avaliar o Prompt

```bash
# Avalia o prompt configurado no evaluate.py (atualmente v5)
python src/evaluate.py
```

### 5. Rodar Testes

```bash
pytest tests/test_prompts.py -v
```

---

## 📁 Estrutura do Projeto

```
desafio_2/
├── .env                          # Credenciais (não versionado)
├── .env.example                  # Template de credenciais
├── requirements.txt              # Dependências Python
├── README.md                     # README original do desafio
├── DOCUMENTACAO.md              # Esta documentação
│
├── prompts/
│   ├── bug_to_user_story_v1.yml  # Prompt inicial (ruim)
│   ├── bug_to_user_story_v2.yml  # Primeira versão testada
│   ├── bug_to_user_story_v3.yml  # Iteração 3
│   ├── bug_to_user_story_v4.yml  # 2ª melhor (0.8558)
│   ├── bug_to_user_story_v5.yml  # ✅ MELHOR (0.8648) - OFICIAL
│   ├── bug_to_user_story_v6.yml  # Iteração 6
│   ├── bug_to_user_story_v7.yml  # Iteração 7 (Clarity 0.90)
│   ├── bug_to_user_story_v8.yml  # Iteração 8
│   └── bug_to_user_story_v9.yml  # Iteração 9
│
├── datasets/
│   └── bug_to_user_story.jsonl   # 15 exemplos de bugs
│
├── src/
│   ├── pull_prompts.py           # Pull do LangSmith Hub
│   ├── push_prompts.py           # Push ao LangSmith Hub
│   ├── evaluate.py               # Avaliação (usa v5)
│   ├── metrics.py                # 5 métricas implementadas
│   └── utils.py                  # Funções auxiliares
│
├── tests/
│   └── test_prompts.py           # Testes de validação
│
├── Dockerfile                    # Container Python
├── docker-compose.yml            # Orquestração
└── .gitignore                    # Arquivos ignorados
```

---

## 🔬 Próximos Passos Sugeridos

### 1. Testar com Outros Modelos

**Para explorar se é possível ultrapassar 0.9:**

```python
# No .env, testar com:
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o  # Modelo mais potente (mais caro)
EVAL_MODEL=gpt-4o

# Ou testar com outros providers:
# - Claude Opus/Sonnet (via Anthropic)
# - Gemini Pro/Ultra (via Google)
```

**Expectativa:** Modelos mais potentes podem:
- Melhorar F1-Score em bugs simples (atual: 0.75)
- Reduzir verbosidade em bugs complexos
- Atingir a meta de 0.9 em todas as métricas

### 2. Análise Manual de Exemplos Falhados

**Próximo passo de debugging:**
- Executar v5 manualmente em cada um dos 15 exemplos
- Comparar resposta gerada vs resposta esperada
- Identificar padrões específicos de falha
- Ajustar prompt baseado em falhas reais

### 3. Tentar Abordagens Alternadas

**Opção A - Exemplos Dinâmicos:**
- Incluir exemplo EXATO do dataset nos prompts
- Few-shot com exemplos mais próximos ao bug sendo processado

**Opção B - Prompts Especializados:**
- Criar 3 prompts separados (simples/médio/complexo)
- Classificar bug primeiro, depois usar prompt especializado

**Opção C - Hybrid Approach:**
- Combinar output de múltiplos prompts
- Usar votação ou ensemble

### 4. Fine-tuning (Avançado)

Se o objetivo é alcançar 0.9+ de forma consistente:
- Coletar mais exemplos (50-100)
- Fine-tunar gpt-4o-mini especificamente para esta tarefa
- Custo mais alto mas resultado mais consistente

---

## 📈 Comparação: v4 vs v5

| Aspecto | v4 | v5 | Vencedor |
|---------|----|----|----------|
| **Média Geral** | 0.8558 | **0.8648** | v5 ✅ |
| **F1-Score** | 0.82 | **0.84** | v5 ✅ |
| **Clarity** | 0.87 | **0.88** | v5 ✅ |
| **Precision** | **0.88** | 0.87 | v4 |
| **Helpfulness** | 0.87 | **0.88** | v5 ✅ |
| **Correctness** | 0.85 | **0.86** | v5 ✅ |
| **Complexidade** | Médio | Médio | Empate |
| **Manutenibilidade** | Alta | **Muito Alta** | v5 ✅ |

**Recomendação:** Usar **v5 como oficial** para produção.

---

## 🎓 Conclusão

Após **9 iterações** de otimização sistemática, alcançamos:
- ✅ **96.1% da meta** com o prompt v5
- ✅ Identificamos limitações do gpt-4o-mini para esta tarefa
- ✅ Documentamos todo o processo de otimização
- ✅ Criamos base sólida para testes com modelos mais potentes

**Resultado Final:** Prompt v5 está **APROVADO** para uso, com ressalva de que ultrapassa 86% da meta estabelecida. Para atingir 90%+, recomenda-se testar com modelos mais potentes (gpt-4o, Claude Opus, etc).

---

## 📞 Links Úteis

- **Prompt v5 no LangSmith Hub:** https://smith.langchain.com/hub/axelkjellin/bug_to_user_story_v5
- **Prompt v4 no LangSmith Hub:** https://smith.langchain.com/hub/axelkjellin/bug_to_user_story_v4
- **Projeto LangSmith:** prompt-optimization-challenge
- **Dataset de Avaliação:** prompt-optimization-challenge-eval

---

**Documentação criada em:** 2026-05-24
**Autor:** Axel Kjellin
**Versão Oficial:** v5 (média: 0.8648)
**Status:** Pronto para avaliação / Testes adicionais com outros modelos
