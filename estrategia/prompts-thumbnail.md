# Prompts de thumbnail para o ChatGPT

Mesmos prompts do documento [`capas/identidade-visual-canal.pdf`](capas/identidade-visual-canal.pdf) (página 3), em texto para copiar. A identidade está em [identidade-visual.md](identidade-visual.md). Os campos entre chaves são preenchidos com a ficha do episódio (final desta página).

## Como usar

1. Abra uma conversa nova no ChatGPT e anexe o documento da identidade visual e as fotos do avatar (PNG recortado, as 7 poses).
2. Escreva: "Use o documento anexado como identidade visual do canal. Vou pedir thumbnails."
3. Cole o prompt mestre, preencha as chaves e cole o prompt do layout A, B ou C.
4. Peça as 3 versões (A, B e C) para o teste A/B. Depois use as variações V1 a V7, uma por vez.

## Prompt mestre

```text
Crie UMA thumbnail de YouTube em 1280×720 px (16:9), seguindo à risca a identidade visual do documento anexado.

TEMA: {tema do vídeo em uma frase}
PADRÃO: {A, B ou C}. Use também o prompt de layout do padrão escolhido.
TEXTO DA CAPA, em português, caixa alta. Escreva exatamente assim, com os acentos, e nada além disso:
• linha 1: "{LINHA 1}"
• palavra de impacto: "{PALAVRA}"
• linha 3: "{LINHA 3}"
AVATAR: use a foto anexada do Bob Proctor, recortada. Não redesenhe o rosto, a roupa nem a expressão. Rosto grande e nítido, olhando para a câmera. A mão do avatar fica voltada para o lado do texto, sem sair pela borda da capa.
FUNDO: degradê azul-noite #081222 para azul-aço #16283A, com luz âmbar #FFBE50 atrás do rosto e poeira dourada. Elemento do tema: {ELEMENTO, da página 2}, em ouro e vidro, 3D cinematográfico. Um elemento principal e, no máximo, dois secundários. Sem texto e sem logotipo no fundo.
TIPOGRAFIA: fonte condensada ultrapesada (estilo Anton), caixa alta, inclinada 12°, com contorno preto e sombra. Palavra de impacto em ouro #FFC83D, cerca de 2,4 vezes maior que as linhas de apoio, que são brancas #FFFFFF.
FITA DO NOME: "BOB PROCTOR" em ouro sobre uma fita azul-noite com borda ouro, embaixo, sobre o paletó.
PROIBIDO: texto fora do pedido, nome do canal, logotipo, selo, outras pessoas, cores fora da paleta e qualquer coisa no canto inferior direito.
TESTE: o texto precisa ficar legível numa miniatura de 168 px de largura.
```

## Prompts de layout

```text
LAYOUT A · FAIXA
• Avatar à esquerda, cabeça e ombros, cortado no peito, cerca de 42% da largura, colorido, com contorno dourado #FFC83D de 7 px. Foto no sentido original (a mão fica voltada para o texto).
• Texto à direita, 3 linhas centralizadas por volta de 62% da largura.
• A palavra de impacto fica sobre uma FAIXA vermelho-laranja #E63E1C, inclinada 12°, com sombra. Palavra em ouro.
• Elemento de fundo à direita da faixa (cerca de 85% da largura), com a luz âmbar atrás.
• Fita "BOB PROCTOR" embaixo do avatar.
```

```text
LAYOUT B · RETRATO P&B
• Avatar em PRETO E BRANCO, grande (cerca de 52% da largura), à esquerda, sem contorno, que se funde ao fundo escuro à direita num degradê suave. Foto no sentido original.
• Texto à direita em 3 linhas. Palavra de impacto em ouro com SUBLINHADO vermelho-laranja #E63E1C inclinado. Linhas de apoio brancas.
• No lugar da fita, assinatura "Bob Proctor" em letra manuscrita branca (estilo Dancing Script), embaixo, sob o texto.
• Elemento de fundo discreto (cerca de 30% de opacidade) atrás do texto.
```

```text
LAYOUT C · PRAZO GIGANTE
• Avatar colorido à DIREITA (cerca de 43% da largura), com contorno dourado #FFC83D de 7 px, cortado no peito. Use a foto ESPELHADA, para a mão ficar voltada para o texto (à esquerda).
• À esquerda, o prazo ou número ENORME (ex.: "7 DIAS") em ouro com brilho dourado e sublinhado vermelho-laranja #E63E1C. Linhas de apoio brancas, acima e abaixo.
• Elemento de fundo atrás do número (cerca de 35% de opacidade).
• Fita "BOB PROCTOR" embaixo do avatar.
```

## Variações para o teste A/B

Rodada 1: três miniaturas por vídeo, os padrões A, B e C com o mesmo tema. Rodada 2: com o vencedor, uma variável por vez.

**V1 · Headline**

```text
Refaça a thumbnail anterior mudando SOMENTE o texto da capa: linha 1 "{…}", palavra de impacto "{…}", linha 3 "{…}". (Teste um tipo por vez: curiosidade, comando ou prazo.) Mantenha todo o resto idêntico: avatar, posições, cores e texto. Entregue 1 imagem 1280×720.
```

**V2 · Cor da palavra**

```text
Refaça a thumbnail anterior mudando SOMENTE a cor da palavra de impacto: de ouro #FFC83D para BRANCO #FFFFFF, sobre a faixa vermelho-laranja. Mantenha todo o resto idêntico: avatar, posições, cores e texto. Entregue 1 imagem 1280×720.
```

**V3 · Elemento de fundo**

```text
Refaça a thumbnail anterior mudando SOMENTE o elemento principal do fundo: troque por {outro elemento do mesmo subnicho, página 2}. Mantenha todo o resto idêntico: avatar, posições, cores e texto. Entregue 1 imagem 1280×720.
```

**V4 · Tamanho do avatar**

```text
Refaça a thumbnail anterior mudando SOMENTE o tamanho do avatar: aumente para cerca de 55% da largura (ou reduza para 35%) e ajuste o texto ao espaço. Mantenha todo o resto idêntico: avatar, posições, cores e texto. Entregue 1 imagem 1280×720.
```

**V5 · Pose**

```text
Refaça a thumbnail anterior mudando SOMENTE a pose do avatar: use a foto anexada {pose}. Mantenha todo o resto idêntico: avatar, posições, cores e texto. Entregue 1 imagem 1280×720.
```

**V6 · Faixa**

```text
Refaça a thumbnail anterior mudando SOMENTE a faixa: no padrão A, tire a faixa e use só o sublinhado vermelho-laranja. Nos padrões B e C, ponha a faixa atrás da palavra de impacto. Mantenha todo o resto idêntico: avatar, posições, cores e texto. Entregue 1 imagem 1280×720.
```

**V7 · Luz**

```text
Refaça a thumbnail anterior mudando SOMENTE a luz: aumente a luz âmbar atrás do rosto e o contraste do contorno dourado. Mantenha todo o resto idêntico: avatar, posições, cores e texto. Entregue 1 imagem 1280×720.
```


## Conferir antes de subir

- [ ] O texto está exatamente como pedido, sem erro de português.
- [ ] De 2 a 5 palavras, em até 3 linhas.
- [ ] A palavra de impacto lê numa miniatura de 168 px de largura.
- [ ] O rosto e a roupa são os da foto anexada, sem mudanças.
- [ ] A mão do avatar aponta para o texto e não sai pela borda.
- [ ] Só as cores da paleta (nada de verde, roxo, rosa).
- [ ] Nada no canto inferior direito.
- [ ] Sem logotipo, selo, nome do canal ou texto no fundo.
- [ ] No máximo 1 elemento principal e 2 secundários no fundo.
- [ ] Arquivo 1280×720, JPG ou PNG, até 2 MB.

## Se o ChatGPT errar

- **Texto com erro:** Reescreva o texto da capa exatamente assim: "{…}". Não mude mais nada.
- **Rosto diferente:** Use o rosto da foto anexada, sem alterações. Mantenha a expressão original.
- **Fundo carregado:** Remova tudo do fundo, menos o elemento principal. Mantenha a luz âmbar.
- **Cor fora da paleta:** Use apenas #081222, #16283A, #FFC83D, #FFBE50, #FFFFFF e #E63E1C.
- **Recusou editar a foto:** Gere só o fundo e o texto, deixando a área do avatar vazia (à esquerda no A e no B, à direita no C). Cole o recorte depois, num editor.

## Ficha dos episódios

EP01 a EP04 já foram testados em mockup. EP05 a EP10 são sugestões a testar.

| Ep. | Tema | A · Faixa | B · Retrato P&B | C · Prazo gigante | Elemento de fundo | Poses (A · B · C) |
| --- | --- | --- | --- | --- | --- | --- |
| EP01 | Por que você não se permite ter dinheiro | SEU **TETO** FINANCEIRO | PERMITA-SE **GANHAR** MAIS | TESTE DE **7 DIAS** SEU TETO | Teto de vidro | Aponta · Sério · Dedo para cima |
| EP02 | O paradigma do dinheiro (termostato) | SEU **TERMOSTATO** | REAJUSTE **SEU NORMAL** | REAJUSTE EM **3 PASSOS** | Termostato | Mão aberta · Pensativo · Aponta |
| EP03 | As 7 leis do dinheiro, na prática | AS 7 LEIS DO **DINHEIRO** NA PRÁTICA | APLIQUE AS **7 LEIS** ESTA SEMANA | AS **7 LEIS** COM EXERCÍCIO | Porta de luz | Dedo para cima · Sorrindo · Mão aberta |
| EP04 | A lei da atração não funciona para você? | VISUALIZAR **NÃO** BASTA | PARE DE **VISUALIZAR** ASSIM | TESTE DE **7 DIAS** | Caderno de 7 dias | Na têmpora · Sério · Dedo para cima |
| EP05 | Permissão para prosperar (5 minutos) | SUA **PERMISSÃO** PARA PROSPERAR | DÊ-SE **PERMISSÃO** | 5 MINUTOS **HOJE** | Chave e cadeado | Mão aberta · Sorrindo · Dedo para cima |
| EP06 | Reprogramar a mente para o dinheiro (3 passos) | REPROGRAME **SUA MENTE** SEM ENGANAÇÃO | REPROGRAME **SEM ENGANAÇÃO** | 3 PASSOS **PARA MUDAR** | Cabeça com engrenagens | Na têmpora · Pensativo · Dedo para cima |
| EP07 | Você merece mais? Pare de recusar seu valor | VOCÊ **MERECE** MAIS | PARE DE **RECUSAR** SEU VALOR | CONVERSA DE **1 MINUTO** | Balança | Aponta · Sério · Mão aberta |
| EP08 | Visualiza, agradece e nada muda: o que falta | O QUE **FALTA** VISUALIZAR | COMPLETE A **VISUALIZAÇÃO** | 3 PASSOS **QUE FALTAM** | Ímã | Na têmpora · Aponta · Dedo para cima |
| EP09 | 10 minutos por dia (desafio de 7 dias) | SÓ **10 MINUTOS** POR DIA | DÊ **10 MINUTOS** POR DIA | 7 DIAS **DE 10 MINUTOS** | Ampulheta | Dedo para cima · Sorrindo · Aponta |
| EP10 | O medo aparece quando você chega perto | POR QUE O **MEDO** APARECE AGORA | DÊ UM **PASSO MENOR** | 1 PASSO **MENOR** | Degraus de vidro | Pensativo · Sorrindo · Mão aberta |

## Exemplo preenchido (EP01, padrão A, depois B e C)

```text
Crie UMA thumbnail de YouTube em 1280×720 px (16:9), seguindo à risca a identidade visual do documento anexado.

TEMA: Por que você não se permite ter dinheiro: o teto financeiro que você aprendeu sem perceber
PADRÃO: A (faixa). Use também o prompt de layout do padrão escolhido.
TEXTO DA CAPA, em português, caixa alta. Escreva exatamente assim, com os acentos, e nada além disso:
• linha 1: "SEU"
• palavra de impacto: "TETO"
• linha 3: "FINANCEIRO"
AVATAR: use a foto anexada do Bob Proctor, recortada. Não redesenhe o rosto, a roupa nem a expressão. Rosto grande e nítido, olhando para a câmera. A mão do avatar fica voltada para o lado do texto, sem sair pela borda da capa.
FUNDO: degradê azul-noite #081222 para azul-aço #16283A, com luz âmbar #FFBE50 atrás do rosto e poeira dourada. Elemento do tema: teto de vidro com uma rachadura e luz dourada atravessando, em ouro e vidro, 3D cinematográfico. Um elemento principal e, no máximo, dois secundários. Sem texto e sem logotipo no fundo.
TIPOGRAFIA: fonte condensada ultrapesada (estilo Anton), caixa alta, inclinada 12°, com contorno preto e sombra. Palavra de impacto em ouro #FFC83D, cerca de 2,4 vezes maior que as linhas de apoio, que são brancas #FFFFFF.
FITA DO NOME: "BOB PROCTOR" em ouro sobre uma fita azul-noite com borda ouro, embaixo, sobre o paletó.
PROIBIDO: texto fora do pedido, nome do canal, logotipo, selo, outras pessoas, cores fora da paleta e qualquer coisa no canto inferior direito.
TESTE: o texto precisa ficar legível numa miniatura de 168 px de largura.
```

```text
Agora faça a versão B do mesmo vídeo. Use o prompt do layout B (colado abaixo).
Texto: linha 1 "PERMITA-SE", palavra de impacto "GANHAR", linha 3 "MAIS".
Avatar: pose Sério, foto no sentido original. Mesmo elemento de fundo, mais discreto.
[cole aqui o prompt do layout B]

Agora faça a versão C do mesmo vídeo. Use o prompt do layout C (colado abaixo).
Texto: linha 1 "TESTE DE", palavra de impacto "7 DIAS", linha 3 "SEU TETO".
Avatar: pose Dedo para cima, foto ESPELHADA. Mesmo elemento de fundo, atrás do número.
[cole aqui o prompt do layout C]
```

## Elementos de fundo (frases para o prompt)

### Nicho · mentalidade e prosperidade

Vale para qualquer vídeo do canal.

- **Moedas de ouro**: pilha de moedas de ouro brilhantes, com poeira dourada flutuando
- **Cédulas em voo**: cédulas genéricas voando, sem texto legível e sem rostos
- **Cofre aberto**: cofre de aço aberto, com luz âmbar saindo de dentro
- **Ampulheta** (EP09): ampulheta dourada com a areia caindo (prazo, 7 dias)

### Subnicho 1 · lei da atração sem ilusão

Atrair com ação, plano e prova.

- **Ímã** (EP08): ímã em ferradura dourado, com linhas de campo atraindo moedas
- **Caderno de 7 dias** (EP04): caderno aberto com 7 quadrados, o primeiro marcado em dourado, e uma caneta
- **Bússola**: bússola dourada apontando adiante (foco e direção)
- **Degraus de vidro** (EP10): degraus de vidro subindo, com luz dourada no topo (próximo passo)

### Subnicho 2 · reprogramar a mente para o dinheiro

O nível de normal e o hábito.

- **Cabeça com engrenagens** (EP06): silhueta de cabeça, sem rosto, com engrenagens douradas dentro
- **Termostato** (EP02): termostato de parede redondo, com ponteiro vermelho-laranja
- **Interruptor**: painel com alavanca virando para ligado, com luz âmbar
- **Circuito dourado**: linhas de circuito douradas, como um código, sobre o azul-noite

### Subnicho 3 · merecimento

Permissão, valor e limite.

- **Teto de vidro** (EP01): teto de vidro com uma rachadura e luz dourada atravessando
- **Porta de luz** (EP03): porta entreaberta com luz âmbar saindo e moedas ao redor
- **Balança** (EP07): balança dourada em equilíbrio (valor e culpa)
- **Chave e cadeado** (EP05): chave dourada e cadeado aberto (permissão)

