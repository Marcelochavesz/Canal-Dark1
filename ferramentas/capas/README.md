# Compor capas

Gera a capa de 1280x720 com a **autoridade em destaque** e a identidade visual do canal, em três modelos para teste A/B (ver [capas e testes A/B](../../estrategia/capas-template.md)). Fontes Anton e Dancing Script, ambas SIL Open Font License (em `fontes/`).

## Instalar

```bash
pip install pillow
```

## Usar

```bash
python3 compor_capa.py --modelo faixa --autoridade foto_proctor.png \
  --linha1 "SEU" --palavra "TETO" --linha3 "FINANCEIRO" --simbolo teto \
  --marca "NOME DO CANAL" --saida capa_ep01_faixa.png
```

Os três modelos usam as mesmas opções. Troque `--modelo`:

| `--modelo` | Arranjo |
| --- | --- |
| `faixa` | Autoridade à esquerda, símbolo à direita, texto em 3 linhas com faixa azul-petróleo |
| `retrato` | Autoridade grande em preto e branco, texto em comando com sublinhado e assinatura |
| `prazo` | Autoridade à direita, número ou prazo gigante com brilho à esquerda |

| Opção | Para que serve |
| --- | --- |
| `--autoridade` | Foto da autoridade (PNG com fundo transparente é o ideal) ou `placeholder` para testar o layout |
| `--linha1`, `--palavra`, `--linha3` | As três linhas do texto. A palavra é a grande. As outras duas são opcionais |
| `--nome` | Texto da fita ou da assinatura. Padrão: `SEGUNDO BOB PROCTOR` |
| `--simbolo` | Arte provisória de fundo: `teto`, `termostato`, `caderno`, `porta` |
| `--fundo` | Imagem de fundo própria (gerada), no lugar da arte provisória |
| `--paleta` | `marca` (padrão do canal) ou `vermelha` (variação de teste da faixa) |
| `--pb` | Autoridade em preto e branco (o modelo `retrato` já usa) |
| `--marca` | Nome do canal, pequeno, no canto |
| `--sem-rotulo` | Tira o rótulo "foto licenciada entra aqui" do placeholder |
| `--saida` | Arquivo de saída. Manter até 2 MB para o YouTube |

## Sobre a foto

- Use uma foto **com licença comercial ou autorização por escrito**. Não use captura de tela de vídeo ou miniatura de terceiros, nem imagem de IA realista da pessoa.
- Remova o fundo antes (PNG com transparência). Se mandar um JPG, a ferramenta só esmaece as bordas.
- O `placeholder` é um busto genérico de teste. Não é retrato de ninguém.
