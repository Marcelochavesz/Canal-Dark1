# Capas: a autoridade sempre presente e três padrões para teste A/B

**Decisão de 08/10/2026:** toda capa traz a autoridade (Bob Proctor), com elementos de fundo junto dela, como nas capas virais. O foco é uma capa fácil de ler e chamativa para o público-alvo. Não usamos mais capa só com símbolo e texto.

**Exemplos:** [`capas/ab-padroes-ep01-ep04.jpg`](capas/ab-padroes-ep01-ep04.jpg), 12 capas (4 episódios, 3 padrões). No lugar da autoridade há uma **silhueta** com o aviso "avatar Bob Proctor entra aqui". É o molde. O avatar entra pela ferramenta (seção 6) ou no ChatGPT, com os [prompts](prompts-thumbnail.md).

**Pesquisa de base:** [padrões de títulos e capas](../pesquisa/padroes-titulos-capas.md).

---

## 1. Identidade visual do canal

Vale para os três padrões. Muda o arranjo, não a identidade. O manual completo, com valores e regras, está em [identidade visual](identidade-visual.md) e no documento [`capas/identidade-visual-canal.pdf`](capas/identidade-visual-canal.pdf). Prompts para o ChatGPT: [prompts-thumbnail.md](prompts-thumbnail.md).

| Elemento | Valor |
| --- | --- |
| Fundo | Azul-marinho escuro em degradê, com brilho dourado atrás da cena |
| Palavra de impacto | Dourado (255, 200, 61), com contorno preto |
| Linhas de apoio | Branco, com contorno preto |
| Faixa | Vermelho-laranja (230, 62, 28), decisão de 08/10 (antes era azul-petróleo) |
| Acento | Vermelho-laranja (230, 62, 28), usado em sublinhado e detalhes |
| Fonte do texto | Anton, caixa alta, inclinada 12 graus |
| Fonte da assinatura | Dancing Script (só no padrão retrato) |
| Contorno da autoridade | Dourado, para destacar do fundo |
| Nome | "BOB PROCTOR" em fita dourada ou em assinatura |
| Marca | Sem fita nem texto com o nome do canal na capa (decisão de 08/10). A ferramenta ainda aceita `--marca`, desligado por padrão |
| Tamanho | 1280 x 720, até 2 MB |
| Canto inferior direito | Livre: é onde o YouTube mostra a duração |

A faixa vermelha é parecida com a do Lewis Howes, de propósito: é o padrão que já provou funcionar. O que separa o canal dele é a palavra amarela, o contorno dourado da autoridade e o fundo azul-marinho. A paleta "vermelha" fica na ferramenta como variação de teste, com a palavra branca no lugar da amarela.

## 2. Os três padrões

Cada padrão vem de um grupo de capas virais da [pesquisa](../pesquisa/padroes-titulos-capas.md).

| Padrão | De onde vem | Arranjo | Tipo de headline | Quando usar |
| --- | --- | --- | --- | --- |
| **A. Faixa** | Lewis Howes (de 400 mil a 11 milhões) | Autoridade à esquerda com contorno dourado; símbolo à direita; texto em 3 linhas no centro, com a faixa vermelho-laranja atrás da palavra grande | Curiosidade ou tema ("SEU TETO FINANCEIRO") | Padrão de base. Bom para vídeos de conceito |
| **B. Retrato P&B** | Ensaios com Napoleon Hill (1,2 milhão e 1,1 milhão), "AO ACORDAR OUÇA ISSO" | Autoridade grande em preto e branco à esquerda, que se funde ao fundo; texto em 3 linhas à direita, palavra de impacto dourada com sublinhado vermelho-laranja; assinatura "Bob Proctor" | Comando ("PERMITA-SE GANHAR MAIS") | Vídeos de ação e de hábito. É o mais próximo do estilo dos ensaios narrados |
| **C. Prazo gigante** | Capas com prazo do Howes ("EM 30 DIAS", "9 DAYS") e dos mais vistos com número | Autoridade colorida à direita; número ou prazo enorme com brilho dourado à esquerda; sublinhado vermelho-laranja | Prazo ou número ("TESTE DE 7 DIAS", "7 LEIS") | Vídeos de lista, de teste de 7 dias e de passos |

A mesma ideia vale para os três: **a autoridade e os elementos de fundo aparecem juntos**, o texto ocupa mais da metade da capa e a palavra de impacto é a mais legível a 168 x 94 pixels. Os exemplos foram conferidos nesse tamanho.

## 3. Headlines por episódio

| Episódio | A. Faixa | B. Retrato | C. Prazo |
| --- | --- | --- | --- |
| EP01 | SEU / **TETO** / FINANCEIRO | PERMITA-SE / **GANHAR** / MAIS | TESTE DE / **7 DIAS** / SEU TETO |
| EP02 | SEU / **TERMOSTATO** | REAJUSTE / **SEU NORMAL** | REAJUSTE EM / **3 PASSOS** |
| EP03 (leis) | AS 7 LEIS DO / **DINHEIRO** / NA PRÁTICA | APLIQUE AS / **7 LEIS** / ESTA SEMANA | AS / **7 LEIS** / COM EXERCÍCIO |
| EP04 (lei da atração) | VISUALIZAR / **NÃO** / BASTA | PARE DE / **VISUALIZAR** / ASSIM | TESTE DE / **7 DIAS** |

Fundo simbólico de cada episódio: teto de vidro (EP01), termostato (EP02), porta de luz com moedas (EP03), caderno com sete quadrados (EP04). Na versão final, o fundo é uma imagem gerada com a mesma ideia, atrás da autoridade.

## 4. Como fazer o teste A/B

O recurso "Testar e comparar" do YouTube Studio aceita até três miniaturas por vídeo. Isso casa com os três padrões. Confira se o recurso está disponível no seu canal.

1. **Rodada 1 (primeiros 5 vídeos):** em cada vídeo, as três miniaturas são os três padrões com o **mesmo tema**. Registrar qual vence (CTR e fatia do tempo de exibição) em [`metricas/videos.csv`](../metricas/videos.csv).
2. **Rodada 2:** com o padrão que mais vencer, testar uma variável por vez: a headline, a cor da palavra de impacto (dourado contra branco, com `--paleta vermelha`) e o tamanho da autoridade.
3. **Não parar cedo.** Deixar rodar até o YouTube indicar um vencedor ou até ter visualizações suficientes. Com poucos cliques, a diferença é ruído.
4. **Registrar:** episódio, padrão, headline, CTR, tempo de exibição e data.

## 5. A foto da autoridade

A foto é o elemento mais importante e o que mais pede cuidado.

**Como deve ser:** rosto grande e nítido, olhando para a câmera ou levemente de lado, fundo removido (PNG com transparência), pelo menos 900 pixels de altura (as 7 poses recebidas têm 935), expressão forte. O contorno dourado e o recorte são feitos pela ferramenta.

**Regra da mão:** a mão do avatar fica voltada para o lado do texto, e não cortada pela borda da capa. Autoridade à esquerda (padrões A e B): foto no sentido original. Autoridade à direita (padrão C): foto espelhada (`--espelhar`). Em 08/10 eu apliquei isso ao contrário nas 12 capas de teste e o dono do canal corrigiu; vale a regra desta frase.

**De onde pode vir:**

- Foto com **licença comercial** que cubra o uso de imagem de uma pessoa, ou **autorização por escrito** do detentor dos direitos (por exemplo, o Proctor Gallagher Institute).
- Ilustração encomendada de um artista.

**O que não fazer:**

- Pegar foto de outro canal, de captura de tela de vídeo de terceiros ou de miniatura de outro vídeo.
- Usar imagem gerada por IA de aparência realista dele. Isso exige divulgação de conteúdo sintético na plataforma e agrava o risco acima.
- Escrever uma citação entre aspas com o nome dele que ele não disse. A fita traz só o nome ("BOB PROCTOR"), sem frase escrita no lugar dele.

**Autorização informada:** o dono do canal informou em 08/10 que o direito de imagem do Proctor está liberado para criação de conteúdo. Ele morreu em 2022, então a liberação precisa vir do instituto ou do espólio. O documento e o escopo estão no [registro](autorizacao-imagem.md), ainda pendente. A autorização da imagem não resolve o direito autoral de cada foto.

**Risco, em uma frase:** usar a foto de uma pessoa, viva ou falecida, em capa de vídeo monetizado sem licença ou autorização pode gerar pedido de retirada, perda de monetização ou ação por direito de imagem. No Brasil, o Código Civil (art. 20) permite proibir o uso da imagem para fins comerciais sem autorização, e, no caso de pessoa falecida, o cônjuge, os ascendentes e os descendentes podem pedir. Isto é orientação geral, não parecer jurídico. Vale confirmar com um advogado antes de publicar. Canais concorrentes usam a foto dele, mas não sei se têm licença.

## 6. Ferramenta

[`ferramentas/capas/compor_capa.py`](../ferramentas/capas/compor_capa.py), com instruções em [`ferramentas/capas/README.md`](../ferramentas/capas/README.md). Exemplo:

```bash
python3 compor_capa.py --modelo faixa --autoridade foto_proctor.png \
  --linha1 "SEU" --palavra "TETO" --linha3 "FINANCEIRO" --simbolo teto \
  --saida capa_ep01_a.png
```

Troque `--modelo` por `retrato` ou `prazo` para os outros dois padrões. Sem foto ainda, use `--autoridade placeholder`.

## 7. Limites

- Os exemplos usam uma silhueta. O efeito com o avatar e com uma imagem de fundo gerada vai ser diferente (e, na maioria dos casos, melhor).
- Não há CTR de nenhuma dessas capas. Os padrões vêm do que se repete nos vídeos mais vistos, e o teste do canal é que decide.
- Foto de autoridade em capa é padrão nos nichos, mas a licença de uso ainda precisa ser resolvida.
