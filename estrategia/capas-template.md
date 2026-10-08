# Template de capa "Faixa"

Base: o padrão tipográfico do Lewis Howes (faixa vermelho-laranja, texto em itálico condensado com uma palavra enorme) e dos canais da rede do Vibração, como a Excelência, que usam a mesma linguagem em canais sem rosto. Pesquisa em [padrões de títulos e capas](../pesquisa/padroes-titulos-capas.md).

**Mockups:** [`capas/mockups-ep01-ep04.jpg`](capas/mockups-ep01-ep04.jpg), oito capas para o EP01 ao EP04 do [plano](plano-10-videos.md), em duas paletas. A arte desses mockups é provisória, desenhada por código, só para testar o layout. A arte final entra com imagem gerada.

**Ferramenta:** [`ferramentas/capas/compor_capa.py`](../ferramentas/capas/compor_capa.py) compõe a capa a partir de um fundo e de três linhas de texto.

---

## 1. Especificação

| Item | Valor |
| --- | --- |
| Tamanho | 1280 x 720, JPG ou PNG, até 2 MB |
| Texto | 3 a 5 palavras em 3 linhas: linha pequena, **PALAVRA GRANDE** e linha pequena. A linha de cima ou a de baixo pode faltar |
| Fonte | Anton (licença SIL Open Font License), em caixa alta, com contorno preto e sombra |
| Inclinação | 12 graus para a direita, como um itálico |
| Tamanhos | Palavra grande até 230 px. Linhas pequenas até 96 px (a ferramenta reduz se não couber) |
| Faixa | Paralelogramo inclinado atrás da palavra grande, mais larga que o texto |
| Lado do texto | Direita ou esquerda. A arte vai para o lado oposto |
| Canto inferior direito | Deixar livre: é onde o YouTube mostra a duração do vídeo |
| Marca | Nome do canal pequeno, num canto |

**Paletas (a testar):**

| Paleta | Faixa | Palavra grande | Linhas pequenas |
| --- | --- | --- | --- |
| Padrão | Vermelho-laranja (230, 62, 28) | Branco | Branco |
| Própria | Azul-petróleo (14, 90, 102) | Dourado (255, 200, 61) | Branco |

A paleta padrão é muito parecida com a do Lewis Howes. Isso é o que as pesquisas mostram funcionar, mas também pode fazer o espectador achar que é o canal dele ou de alguém ligado a ele. A paleta própria diferencia. O teste de paleta do plano de 10 vídeos serve para decidir.

## 2. O que usamos e o que não usamos

| Usamos | Não usamos |
| --- | --- |
| A estrutura: faixa, itálico condensado, palavra gigante, 3 a 5 palavras | Rosto de pessoa real, incluindo o Proctor, o Dispenza e o Howes |
| Imagem simbólica no lugar do rosto (teto, termostato, caderno, porta de luz) | Logotipo, nome ou marca de outro canal (como "The School of Greatness") |
| Texto que repete a promessa do título em versão curta | Palavrão, promessa de saúde ("CURE E MANIFESTE"), promessa de dinheiro fácil, conspiração ("COMO ELES TE MANTÊM POBRE") |
| Prazo de teste ("TESTE DE 7 DIAS") | Prazo de resultado ("RICO EM 30 DIAS") |
| Citação só se for verificada, com fonte | Citação inventada com o nome de alguém |

## 3. Receita do texto

Três linhas: contexto curto, palavra grande, complemento ou comando.

| Vídeo | Linha 1 | Palavra grande | Linha 3 |
| --- | --- | --- | --- |
| EP01, opção A | SEU | TETO | FINANCEIRO |
| EP01, opção B | O DINHEIRO | SOME? | FAÇA ISTO |
| EP01, opção C | VOCÊ SE | PERMITE? | |
| EP02, opção A | SEU | TERMOSTATO | |
| EP02, opção B | VOLTA AO | MESMO | PONTO? |
| EP02, opção C | REAJUSTE | SEU NORMAL | |
| EP03 (leis), opção A | AS 7 LEIS DO | DINHEIRO | NA PRÁTICA |
| EP03 (leis), opção B | APLIQUE AS | 7 LEIS | ESTA SEMANA |
| EP03 (leis), opção C | LEIS DO | DINHEIRO | COM EXERCÍCIO |
| EP04 (lei da atração), opção A | VISUALIZAR | NÃO | BASTA |
| EP04 (lei da atração), opção B | TESTE DE | 7 DIAS | |
| EP04 (lei da atração), opção C | ONDE | VOCÊ | ERRA |

Cada um com a arte do tema: teto de vidro, porta de luz com moedas, termostato, caderno com sete quadrados. Para o EP03, vale testar dinheiro na capa (moedas ou notas), já que o vídeo de leis do Vibração é o único dos 9 que analisei com dinheiro na mão na capa e é o mais visto.

## 4. Arte final

A ferramenta aceita `--fundo imagem.jpg`. Para gerar a arte, o prompt base é:

> Ilustração cinematográfica de [símbolo: teto de vidro sobre uma silhueta, termostato de parede, porta de luz dourada com moedas, caderno com sete quadrados], luz dourada quente contra azul-petróleo, composição simples com um só assunto, metade da imagem livre para texto, formato 16:9, sem rostos reconhecíveis, sem logotipos, sem texto

Gerar três variações por capa e escolher a mais limpa, porque o texto cobre metade da imagem.

## 5. Processo

1. Escolher o texto (três linhas) a partir da tabela.
2. Gerar a arte (ou usar a provisória para testar).
3. Compor com `compor_capa.py`.
4. Ver a capa em tamanho de celular (168 x 94). O texto grande tem de continuar legível.
5. Exportar em JPG com até 2 MB.
6. Registrar a variação no `metricas/videos.csv` para o teste.

## 6. Limites

- O estilo funciona com rostos no Lewis Howes. Sem rosto, o efeito é hipótese.
- Os mockups têm arte provisória e não representam o resultado final.
- Não há CTR de nenhum desses canais. O teste de paleta e de capa do canal é que vai dizer.
