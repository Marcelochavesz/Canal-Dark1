# Identidade visual do canal (versão 1, 08/10/2026)

Documento em PDF, com 4 páginas: [`capas/identidade-visual-canal.pdf`](capas/identidade-visual-canal.pdf). Ele traz o manual, os moldes sem o personagem, os elementos de fundo e os prompts para o ChatGPT. Esta página é a mesma informação em texto. Os prompts para copiar estão em [prompts-thumbnail.md](prompts-thumbnail.md). As decisões vêm dos pedidos do dono do canal e da [pesquisa de capas](../pesquisa/padroes-titulos-capas.md). Os padrões e os testes A/B estão em [capas e testes A/B](capas-template.md). A ferramenta que aplica tudo isso está em [`ferramentas/capas`](../ferramentas/capas/README.md).

O documento usa uma silhueta com o aviso "avatar Bob Proctor entra aqui" no lugar da foto. As fotos do Proctor e as capas finais ficam fora do repositório, que é público.

## 1. Paleta

| Nome | Hex | RGB | Uso |
| --- | --- | --- | --- |
| Azul-noite | `#081222` | 8, 18, 34 | Fundo e sombras, topo do degradê |
| Azul-aço | `#16283A` | 22, 40, 58 | Base do degradê, meio-tom do fundo |
| Ouro | `#FFC83D` | 255, 200, 61 | Palavra de impacto, contorno da foto, fita do nome, brilho do prazo |
| Âmbar | `#FFBE50` | 255, 190, 80 | Só a luz dourada atrás da cena |
| Branco | `#FFFFFF` | 255, 255, 255 | Linhas de apoio e assinatura, sempre com contorno preto |
| Brasa | `#E63E1C` | 230, 62, 28 | A faixa e o sublinhado, nada mais |
| Preto | `#000000` | 0, 0, 0 | Só o contorno e a sombra das letras |

**Proporção medida nas 12 capas de EP01 a EP04:** 55% azul-noite, 30% autoridade e luz, 7% ouro, 5% branco, 3% brasa.

**Proibido:** azul-petróleo (era a cor da faixa até 08/10), verde, roxo, rosa e degradê colorido.

## 2. Hierarquia

Ordem de leitura: **rosto, palavra de impacto, linhas de apoio, símbolo**.

1. **Palavra de impacto:** Anton, até 230 px (280 px no prazo), ouro, contorno preto de 10 px, sobre a faixa brasa.
2. **Linhas de apoio:** Anton, até 96 px, branco, contorno preto de 6 px, 1 a 2 linhas.
3. **Autoridade:** olhando para a câmera, contorno ouro de 7 px, cerca de 43% da largura (52% no retrato P&B).
4. **Fita do nome:** "BOB PROCTOR", Anton 36 px, ouro sobre azul-noite com borda ouro. Padrões A e C. No padrão B entra a assinatura.
5. **Símbolo e luz:** um só por capa, com a luz âmbar do canal.

## 3. Tipografia

- **Anton** (licença OFL): toda a headline e a fita. Caixa alta, inclinada 12 graus, contorno preto e sombra. Foi escolhida por ser grossa e estreita, e por ler bem a 168 px de largura.
- **Dancing Script Bold** (licença OFL): só a assinatura "Bob Proctor" do padrão B, 58 px.
- Uma fonte só na headline. A palavra de impacto tem cerca de 2,4 vezes o tamanho das linhas de apoio.
- Os arquivos estão em [`ferramentas/capas/fontes`](../ferramentas/capas/fontes).

## 4. Cor de cada tipo de palavra

| Tipo | Cor | Observação |
| --- | --- | --- |
| Palavra de impacto | Ouro | Uma por capa. Ex.: TETO, GANHAR, NÃO |
| Linhas de apoio | Branco | Completam a frase |
| Número ou prazo | Ouro com brilho | Padrão C. O prazo é a imagem da capa |
| Faixa de destaque | Brasa | Padrão A, inclinada 12 graus. Nos padrões B e C vira um sublinhado |
| Fita do nome | Ouro sobre azul-noite | Padrões A e C |
| Assinatura | Branco | Padrão B |

**Proibido:** logo, selo, nome do canal e qualquer texto fora da headline, da fita e da assinatura. Nenhuma citação entre aspas com o nome do Proctor.

Variação de teste: palavra branca sobre a faixa brasa (`--paleta vermelha`). A faixa vermelha é parecida com a do Lewis Howes, de propósito. O que separa o canal dele é a palavra amarela, o contorno dourado da autoridade e o fundo azul-marinho.

## 5. Layout e ângulos

| Padrão | Autoridade | Texto | Símbolo |
| --- | --- | --- | --- |
| A. Faixa | Esquerda, 42% da largura, colorida com contorno ouro | Centro-direita, 3 linhas, palavra sobre a faixa | À direita |
| B. Retrato P&B | Esquerda, 52%, em preto e branco, funde-se à direita | À direita, 3 linhas, sublinhado brasa, assinatura embaixo | Atrás da foto, discreto |
| C. Prazo gigante | Direita, 43%, colorida com contorno ouro | À esquerda, prazo ou número enorme com brilho | Atrás do número |

- **Enquadramento:** plano médio, cabeça e ombros, cortado no peito.
- **Olhar:** direto para a câmera. **Rosto:** no terço superior.
- **Regra da mão:** a mão do avatar fica sempre voltada para o lado do texto e nunca cortada pela borda da capa. Avatar à esquerda (padrões A e B): foto no sentido original. Avatar à direita (padrão C): foto **espelhada** (`--espelhar` na ferramenta).
- **Mãos:** apontam para o texto ou para o espectador.
- **Foto:** recorte limpo, com no mínimo 900 px de altura. As 7 poses recebidas têm 935 px.
- **Canto livre:** nada no canto inferior direito, onde o YouTube mostra a duração do vídeo.

## 6. Poses e cenários

As 7 poses recebidas em 08/10 e onde cada uma funciona melhor. A pose acompanha a mensagem e sempre olha para a câmera.

| Pose | Quando usar | Padrão |
| --- | --- | --- |
| Sério (mão no queixo) | Alerta, conflito, "pare" | B |
| Apontando | Fala com "você", comando, teste | A, C |
| Dedo para cima | Número, prazo, "um só" | C |
| Mão aberta | Apresenta o conceito | A, C |
| Pensativo (queixo) | Reflexão, reajuste | B |
| Sorrindo (queixo) | Convite, acolhimento | B |
| Dedo na têmpora | Mente, crença, visualização | A |

| Cenário | Para quê | Episódio |
| --- | --- | --- |
| Teto de vidro | Limite, "seu teto" | EP01 |
| Termostato | O "normal", o padrão | EP02 |
| Porta de luz | Leis, abertura, dinheiro | EP03 |
| Caderno com sete quadrados | Teste de 7 dias, exercício | EP04 |

Um cenário por capa, desfocado atrás do texto, com a mesma luz âmbar. Próximos a criar: balança (merecimento), engrenagens (reprogramar), relógio (10 minutos) e degrau (medo).

## 7. Elementos de fundo do nicho e do subnicho

É o que dá identidade própria às capas. A assinatura do canal é a **luz âmbar atrás do assunto, a poeira dourada e objetos em ouro e vidro** sobre o azul-noite. Regras: um elemento principal e, no máximo, dois secundários; atrás ou ao lado do texto, nunca na frente do rosto; sem texto, número, logotipo ou rosto dentro do elemento; estilo 3D cinematográfico semirrealista, sem cartoon, emoji ou neon colorido. As mesmas ideias aparecem nas cenas dos vídeos, para o espectador reconhecer o canal.

| Grupo | Elementos (episódio planejado) |
| --- | --- |
| Nicho: mentalidade e prosperidade | Moedas de ouro, cédulas em voo, cofre aberto, ampulheta (EP09) |
| Subnicho 1: lei da atração sem ilusão | Ímã (EP08), caderno de 7 dias (EP04), bússola, degraus de vidro (EP10) |
| Subnicho 2: reprogramar a mente para o dinheiro | Cabeça com engrenagens (EP06), termostato (EP02), interruptor, circuito dourado |
| Subnicho 3: merecimento | Teto de vidro (EP01), porta de luz (EP03), balança (EP07), chave e cadeado (EP05) |

A frase pronta de cada elemento para usar no prompt está em [prompts-thumbnail.md](prompts-thumbnail.md).

## 8. Cinco regras de bolso

1. **2 a 5 palavras.** Máximo de 5, em até 3 linhas.
2. **1 palavra em ouro.** O resto em branco.
3. **Autoridade sempre.** Rosto grande, olhando para a câmera, com contorno ouro.
4. **Canto livre.** Nada no canto inferior direito.
5. **Teste a 168 px.** Se não lê na miniatura pequena, corte palavras.

## 9. O que ainda falta

- **Nome do canal** e, depois dele, o logo, o avatar e o banner do canal. A capa não leva nome nem logo, mas o canal precisa deles. Sugestão: partir das mesmas cores, com o ouro sobre o azul-noite.
- **Estilo do texto dentro do vídeo** (dados, refrões, número do sinal e do passo): usar Anton, branco com contorno preto e ouro para o destaque, como na capa. Ainda não foi desenhado.
- **Medir:** esta identidade vem de padrões de vídeos de outros canais. O CTR real vem do teste A/B dos primeiros vídeos ([plano](plano-10-videos.md)).
