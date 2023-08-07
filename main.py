## Abrindo Imagem ##
with open("imagem.ppm", "r") as image:
  ppm_info = (image.readlines())
print(ppm_info)
image = []
aux = []
controle = False

## Criando Matrix com a Imagem ##
for i in range(len(ppm_info)):
  if str(ppm_info[i]) == "255\n":
    dimensoes = ppm_info[i - 1]
    largura = int(dimensoes.split()[0])
    altura = int(dimensoes.split()[1])
    controle = True

  elif controle:
    pixel = []
    for j in ppm_info[i].split():
      pixel.append(j)

      if len(pixel) == 3:
        aux.append(pixel)
        pixel = []
    image.append(aux)
    aux = []
    
## Editando imagem ##
image[2][1] = ['105','32','175']

## Convertendo Matrix para Imagem ##
cabecalho = ("P3\n%s255\n" % dimensoes)
ppm = ""
for i in image:
  for j in i:
    ppm += ' '.join(j) + "    "
  ppm += "\n"

ppm_info = cabecalho + ppm

## Salvando Imagem Editada ##
file = open("imagem_editada.ppm", "w")
file.write(ppm_info)
file.close()

print(ppm_info)