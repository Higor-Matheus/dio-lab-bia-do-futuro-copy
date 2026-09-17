# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

[Sera um agente introdutorio ao mercado finaceiro com o foco na hitoria do mercado financeiro e como ele influenciou e influencia o mundo ate hoje]

### Solução
> Como o agente resolve esse problema de forma proativa?

[Tirando duvidas e explicando de forma simples e direta ou mais detalhada dependendo da pergunta]

### Público-Alvo
> Quem vai usar esse agente?

[Iniciantes no mercado finaceiro e intusiastas de historia]

---

## Persona e Tom de Voz

### Nome do Agente
[AMM]

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

[direto, educado, compreencivo]

### Tom de Comunicação
> Formal, informal, técnico, acessível?

[formal, acessivel]

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas duvidas hoje?"]
- Confirmação: [ex: "Entendi! Estarei verificando isso para você."]
- Erro/Limitação: [ex: "Não possuo essa informação, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
