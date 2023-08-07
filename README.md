# Manipulação de Imagem PPM

Este projeto é um exemplo de manipulação de uma imagem no formato PPM (Portable Pixmap), que é um formato de arquivo de imagem de mapa de bits, comumente utilizado para representar imagens em formato RGB.

## Funcionamento do Script

1. O Script abre o arquivo "imagem.ppm" no modo de leitura ("r") e armazena as linhas do arquivo na variável `ppm_info`.
2. Em seguida, ele inicializa uma lista vazia chamada `image`, que será usada para armazenar os pixels da imagem em forma de matriz.
3. Percorre as linhas do arquivo `ppm_info` e, quando encontra a linha que contém "255" (o valor máximo de cor para o formato PPM), ele identifica as dimensões da imagem a partir da linha anterior e define as variáveis `largura` e `altura`.
4. A partir desse ponto, o código começa a criar a matriz `image` contendo os pixels da imagem. Ele percorre cada linha da `ppm_info`, dividindo-a em valores RGB de cada pixel e armazenando-os na lista `aux`. Quando atinge o comprimento de 3 (representando os três componentes de cor RGB), ele adiciona a lista `aux` à matriz `image` e reinicializa a lista `aux` para o próximo conjunto de pixels.
5. Após construir a matriz `image`, o código altera o valor do pixel na posição `[2][1]` (terceira linha, segunda coluna) para `[105, 32, 175]`, o que corresponde a uma cor RGB específica (105 para vermelho, 32 para verde e 175 para azul). Essa alteração é um exemplo e pode ser customizada de acordo com a necessidade.
6. A seguir, o código constrói uma nova string `ppm_info`, que contém o cabeçalho PPM, seguido dos pixels RGB da imagem. Cada linha da imagem é concatenada na string `ppm`, separada por espaços, para formar o conteúdo final da imagem editada.
7. O programa salva a imagem editada em um novo arquivo chamado "imagem_editada.ppm".


## Execução

`python main.py`

** Certifique-se que o arquivo de imagem desejado, "imagem.ppm", está na mesma pasta na qual iremos executar o Script.
