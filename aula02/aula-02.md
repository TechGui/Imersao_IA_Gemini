# Aula 02: Melhores técnicas em Engenharia de Prompt
## Técnicas de Prompting

### Zero-shot Prompting

Na técnica de Zero-shot prompting, o modelo faz uma tarefa sem ter sido treinado para ela. Ele tem que inferir a resposta só com base no prompt, sem exemplos de treinamento específicos. É útil quando não temos dados de treinamento pra uma tarefa específica.

### Few-shot Prompting

Few-shot prompting consiste em fornecer ao modelo apenas alguns exemplos de treinamento, geralmente poucos, juntamente com um prompt específico. O modelo utiliza esses exemplos para aprender a tarefa e gerar respostas relevantes. Essa abordagem é especialmente eficaz em situações onde há uma quantidade limitada de dados de treinamento disponíveis.

### Few-shot Chain-of-Thought Prompting

Few-shot Chain-of-Thought prompting é tipo uma expansão do Few-shot prompting. Nele, o modelo precisa gerar respostas conectadas usando poucos exemplos de treinamento. Basicamente, encadeia várias tarefas ou perguntas e o modelo tem que responder de forma lógica ao longo do "fluxo de pensamento". É útil quando precisamos de raciocínio complexo e sequencial.

## Desafios

1. Use a técnica de Few-shot Chain-of-Thought

Fiz o Google AI Studio, no seu modelo Gemini 1.5 Pro se passar por um jogador de RPG onde eu instrui para ele uma série de informações. Através das técnicas Few-Shot Prompting misturada com Chain-of-Thought Prompting, para me fornecer um diálogo e conquistar um objetivo de um jogo RPG através da conversa da IA com o NPC (Como se ela estivesse realmente dentro do universo e se deparasse com um NPC, gerando tal diálogo e extraindo do NPC a informação do objetivo, automaticamente).

![IMG RPG](assets/GeminiRPG.gif)

2. Escolha 10 notícias. Mostre título e texto das primeiras 10. Na 11ª, mostre apenas o texto e peça um título. Analise padrões e técnicas.

![IMG Notícias](assets/PadrãoNotícias.gif)