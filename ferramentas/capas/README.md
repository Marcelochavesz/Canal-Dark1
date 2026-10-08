# Compor capas

Gera a capa de 1280x720 no estilo "faixa" (ver [template](../../estrategia/capas-template.md)): fundo, faixa colorida inclinada e texto em três linhas, com a fonte Anton (licença SIL Open Font License, em `fontes/Anton-OFL.txt`).

## Instalar

```bash
pip install pillow
```

## Usar

Com arte provisória (símbolos: `teto`, `termostato`, `caderno`, `porta`):

```bash
python3 compor_capa.py --linha1 "SEU" --palavra "TETO" --linha3 "FINANCEIRO" \
  --simbolo teto --paleta padrao --marca "[NOME DO CANAL]" --saida capa_ep01.png
```

Com a imagem final (gerada por você, sem rosto de pessoa real):

```bash
python3 compor_capa.py --linha1 "SEU" --palavra "TETO" --linha3 "FINANCEIRO" \
  --fundo arte_ep01.jpg --paleta propria --lado dir --saida capa_ep01.png
```

| Opção | Para que serve |
| --- | --- |
| `--linha1`, `--palavra`, `--linha3` | As três linhas do texto. A palavra é a grande, sobre a faixa. `--linha1` e `--linha3` são opcionais |
| `--paleta padrao` ou `propria` | Faixa vermelho-laranja com texto branco, ou faixa azul-petróleo com palavra dourada |
| `--lado dir` ou `esq` | Lado em que fica o texto. A arte vai para o lado oposto |
| `--fundo` ou `--simbolo` | Imagem de fundo sua, ou arte provisória |
| `--marca` | Texto pequeno no canto, por exemplo o nome do canal |
| `--saida` | Arquivo de saída. Manter até 2 MB para o YouTube |

As artes provisórias são desenhos simples para testar o layout. A versão final usa uma imagem gerada com o prompt de fundo do template.
