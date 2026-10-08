# Formato: narração com imagens ao fundo

Formato dos vídeos do canal: uma narração contínua, com imagens em sequência por trás. A diferença para o O Caminho da Vibração está no roteiro (protocolo, pausas de ação, dados com fonte), não na aparência. Estrutura de tempo e retenção: [estrutura-retencao.md](estrutura-retencao.md). Exemplo completo: [EP01](ep01-permissao-dinheiro.md).

**O que não analisei:** só vi as capas e li os roteiros do Vibração, não os quadros internos dos vídeos deles. As regras abaixo são minhas, a testar.

---

## 1. Ritmo das imagens

- O roteiro marca **cenas** (`[IMG número · tempo]`). Cada cena dura de 8 a 20 segundos. O EP01 tem 90 cenas em cerca de 20 minutos.
- Cena com mais de 14 segundos pede uma segunda imagem do mesmo motivo, no meio da fala.
- Trechos de lista (os quatro sinais, os três passos) cortam mais rápido. Trechos calmos (exercício guiado) ficam mais tempo na mesma imagem.
- Todas as cenas têm movimento leve (zoom lento) para não parecer imagem parada.

## 2. Motivos recorrentes

O mesmo conjunto de motivos volta ao longo da série, para o espectador reconhecer o canal. Cada cena do roteiro termina com a etiqueta do motivo.

| Etiqueta | O que mostra | Para que serve |
| --- | --- | --- |
| TELA | Celular ou computador com valores genéricos, sem logotipo de banco | Cenas do dia a dia com dinheiro |
| SILHUETA | Pessoa de costas ou em silhueta, sem rosto | Exemplos hipotéticos e identificação |
| TETO | Teto de vidro, muro baixo | O teto financeiro |
| TERMO | Termostato de parede | A imagem do nível de normal |
| CADERNO | Caderno, caneta, lâmpada quente | Exercícios e registros |
| CARTOES | Cartões numerados (sinais, passos, perguntas) | Estrutura do vídeo |
| DADO | Cartão com dado, ano e fonte | Pesquisas e avisos |
| PORTA | Porta entreaberta, degrau, linha no chão | Mudança, medo, primeiro passo |
| RELOGIO / CALEND | Relógio, calendário de 7 dias | Prazos e o teste de 7 dias |
| MAOS | Close de mãos e objetos | Ações pequenas |
| BALANCA | Balança | Culpa e escolha |
| PROGRAMA | Engrenagens atrás de uma tela | A ideia de paradigma |
| REFRAO | Cartão escuro com a frase de refrão | Refrões como "Isso é se permitir." |
| RESPIRO | Círculo que cresce e diminui, fundo escuro | Pausas e respiração |

## 3. Texto na tela

Só em quatro casos, sempre grande e legível no celular, com no máximo 8 palavras:

1. Dado com fonte e ano.
2. Refrão do vídeo.
3. Número do sinal ou do passo.
4. Frase do exercício.

Dado fica na tela por pelo menos 4 segundos.

## 4. Estilo visual

- Ilustração cinematográfica, luz âmbar quente contra azul-petróleo, composição simples com um só assunto, espaço livre para texto, 16:9.
- Nas cenas do vídeo, pessoas só de costas ou em silhueta, sem rosto. A foto da autoridade entra na capa (ver [capas](../estrategia/capas-template.md)). Usá-la também nas cenas depende da mesma licença.
- Nada de logotipo real, aplicativo de banco real, documento verdadeiro ou texto legível dentro da imagem (geradores erram o texto; o texto entra na edição).
- Mãos geradas por IA costumam sair deformadas. Preferir objetos, silhuetas e closes que evitem mãos, ou conferir e refazer.

**Prompt base** (trocar o trecho final pela descrição da cena):

> Ilustração cinematográfica, luz âmbar quente contra azul-petróleo, composição simples com um único assunto, espaço livre para texto, formato 16:9, sem rostos reconhecíveis (pessoas de costas ou em silhueta), sem logotipos, sem texto legível. Cena: {descrição da cena}

## 5. Montagem e áudio

- **Voz:** sintética em português do Brasil, natural, a cerca de 150 palavras por minuto. Ouvir o áudio inteiro à procura de ruídos e erros de pronúncia (números, siglas e nomes como Gollwitzer, Oettingen e Klontz). Um comentário na Excelência ("a tosse foi fantástica!") pode se referir a ruído na narração, mas é só um indício.
- **Pausas:** 3 a 5 segundos de respiro depois de cada bloco. As pausas longas do exercício guiado estão marcadas no roteiro.
- **Música:** instrumental, constante e bem abaixo da voz. No exercício guiado, mais suave.
- **Transições:** fusão curta. Evitar efeitos chamativos.
- **Legendas:** automáticas, revisadas.
- **Capítulos:** gerados do mapa de tempo do roteiro, com nomes pelo benefício.

## 6. Regras legais e éticas

- Nas cenas do vídeo, sem rosto nem imagem de IA de pessoa real. Na capa, só foto licenciada da autoridade.
- Sem citação inventada com o nome dele na imagem.
- Imagens geradas por IA ou ilustradas, declaradas quando a plataforma exigir. Conferir a regra atual do YouTube para conteúdo sintético.
- Sem imagem copiada dos canais concorrentes. Música com licença.
- Sem documento ou captura de tela falsos que pareçam reais.

## 7. Fluxo de produção

1. Fechar o roteiro e conferir as fontes.
2. Gerar a voz e conferir a duração real.
3. Gerar uma imagem por cena com o prompt base. Reaproveitar motivos.
4. Montar: voz, imagens com zoom lento, texto na tela, música, legendas.
5. Revisão (abaixo).
6. Fazer a capa, o título e a descrição com avisos e capítulos.
7. Publicar e registrar em [`metricas/videos.csv`](../metricas/videos.csv).

**Revisão antes de renderizar:**

- Nenhuma cena com rosto de pessoa real, logotipo ou texto errado.
- Cada dado aparece com fonte na tela.
- O gancho entrega a promessa nos primeiros 35 segundos.
- O minuto prometido no roteiro bate com o vídeo.
- Nenhum trecho de mais de 300 palavras sem pergunta ou comando ao espectador.
- O áudio foi ouvido do começo ao fim.
