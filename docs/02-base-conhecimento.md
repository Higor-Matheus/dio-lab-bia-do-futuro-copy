# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir respostas adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de acontecimentos historicos |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---
## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Transformei a base de dados para que, em vez de simular perfis de investidores e produtos financeiros, o agente utilize registros históricos e exemplos de acontecimentos marcantes do mercado financeiro mundial. O objetivo é contextualizar eventos passados e ensinar como eles moldaram a evolução da economia.]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[Os arquivos CSV e JSON são carregados no início da sessão e ficam disponíveis no contexto do agente. Eles são lidos e estruturados em memória para que o agente possa consultar dinamicamente conforme a interação avança.]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Os dados não vão diretamente no system prompt. Em vez disso, são consultados dinamicamente: quando o usuário pergunta sobre um período ou evento histórico, o agente busca nos datasets correspondentes e insere trechos relevantes no contexto da resposta. Isso garante que as explicações sejam fundamentadas em registros históricos.]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados Históricos:
- Evento: Crise de 1929
- Local: Estados Unidos
- Impacto: Quebra da Bolsa de Nova York
- Consequências: Grande Depressão, falências em massa, desemprego elevado

Registros adicionais:
- 1971: Fim do padrão-ouro (Nixon Shock)
- 2008: Crise do Subprime

- 03/11: Streaming - R$ 55
...
```
