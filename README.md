<h1>Resumo de estudos para a prova de Processamento Digital de Imagens</h1>
<h4>Mestrado UEM</h4>
<hr />
Processamento digital de imagens é um conjunto de técnicas para capturar, representar e transformar imagens
com o auxílio do computador.

<h5>Etapas do Processamento Digital de Imagens</h5>
<p>Exemplo de dominios que envolvem a utilização de técnicas de processamento de imagens:</p>
<p>medicina, microscopia, astronomia, area militar, artes, arqueologia</p>
<h3>Etapas do processamento digital de imagens:</h3>
<ul>
	<li><p>A etapa de aquisição é responsável pela captura da imagem por meio de um dispositivo ou sensor e pela sua conversão em uma representação adequada para o processamento digital subsequente.</p>
	<p>
		Os principais dispositivos para a aquisição de imagens são câmeras de vídeo, tomógrafos médicos, satélites, scanners.
	</p>
	<p> Dentre os aspectos envolvidos nesta etapa estão a escolha do tipo de sensor, as condições de iluminação da cena, a resolução e o número de níveis de cinza ou cores da imagem digitalizada.</p>
   	</li>
   <li>
   		<p>A imagem digital resultante do processo de aquisição pode apresentar imperfeições ou degradações decorrentes por exemplo, das condições de iluminação ou características dos dispositivos.</p>
   		<p>A etapa de pré-processamento visa melhorar a qualidade da imagem por meio de aplicação de técnicas para atenuação de ruído, correção de contraste ou brilho e suavização de determinadas propriedades da imagem.</p>
   </li>
   <li>
   	<p>A segmentação realiza a extração e identificação de áreas interessantes contidas na imagem</p>
   	<p>Esta etapa é geralmente baseada na detecção de descontinuidades( bordas )ou de similaridades( regiões ) na imagem </p>
   </li>
   <li>
   	<p>A representação é usada para armazenar e manipular os objetos de interesse extraídos na imagem</p>
   	
   </li>
   <li>
   	<p>O processo de descrição visa a extração de características ou propriedades que possam ser utilizadas na descriminação entre classes de objetos. Essas características são em geral descritas por atributos númericos que formam um vetor de características</p>
   </li>
   <li>Reconhecimento ou classificação é o processo que atribui um identificador ou rótulo aos objetos da imagem, baseados nas características provida pelo seus descritores.</li>
   <li>O porcesso de interpretação consiste em atribuir um significado ao conjunto de objetos reconhecidos.</li>




</ul>

<h3>Componentes de um Sistema de Processamento de Imagens</h3>
<h6>Dispositivos de entrada e saída</h6>
	<ul>
		<li><p>Esses dispositivos podem ser utilizados para aquisição, armazenamento, processamento, transmissão e exibição de imagens.</p>
		<p>Os parâmetros de funcionalidade e desempenho dos dispositivos são dependentes, em grande parte das áreas que os utilizam.</p>
		</li>
	</ul>

<h2>Como uma imagem digital é formada?</h2>
<p>Uma imagem é uma função bidimensional f( x,y ) onde x e y são coordenadas espaciais e a amplitude f em qualquer par de coordenadas ( x,y ) é chamada intensidade nesse ponto. Quando x, y e os valores de f são quantidades discretas e finitas a imgem é chamada de digital. Uma imagem digital é composta de um número finito de elementos tendo cada ele mento um valor e uma localização.  </p>
<p>Toda imagem digital é uma matriz. Cada elemento da imagem é chamado de pixel. </p>
<p>No caso de imagens preto e branca a imagem é composta por apenas uma matriz de duas dimensões. Já as imagens coloridas são formadas por três matrizes de duas dimensões cada uma representando neste caso o sistema RGB. Portanto cada pixel é formado de uma tupla de 3 inteiros de 8 bits sem sinal no sistema( R,G,B ) sendo que 0,0,0 representa o preto , ( 255, 255, 255) o branco. As cores mais comuns são:
<ul>
	<li>Branco - RGB( 255,255,255 )</li>
	<li>Azul - RGB( 0,0,255 )</li>
	<li>Vermelho - RGB( 255,0,0 )</li>
	<li>Verde - RGB( 0,255,0 )</li>
	<li>Amarelo - RGB( 255,255,0 )</li>
	<li>Magenta - RGB ( 255,0,255 )</li>
	<li>Ciano - RGB ( 0,255,255 )</li>
	<li>Preto - ( 0,0,0 )</li>
</ul>
 </p>
 <p>As imagens coloridas portanto são compostas de 3 matrizes de inteiros sem sinal de 8 bits, a junção das 3 matrizes produz a imagem colorida com capacidade de reprodução de 16,7 milhões de cores, sendo que os 8 bits tem capacidade para 256 valores e elevando a 3 temos 256 elevado a 3 = 16,7 milhões</p>
 <h5>Sistema de coordenadas e manipulação de pixels</h5>
 <p>No sistema RGB tem-se uma representação de 3 cores, ou seja é possível alterar a cor individualmente para cada pixel, ou seja, manipular individualmente cada pixel da imagem.</p>
 <p>O pixel mais a esquerda e acima da imagem esta na posição ( 0,0 ) esta na linha 0 e na coluna 0.</p>

 <p><strong>Exemplo usando o OpenCV e Python:</strong></p>

 <p>import cv2 #importa a biblioteca OpenCV</p>

 imagem = cv2.imread( "jogador.jpg") #metódo imread retorna matriz e armazena na memória atraves da variavel #imagem

(b, g, r) = imagem[0,0] = armazena na memória valores das tuplas nesta respectiva ordem<br> 

print(b, g, r) #retorna na tela os valores de cada tupla<br>

<hr>
<p><strong>Percorrendo linhas e colunas:</strong></p>
<p>Alterando todos os pixels da imagem</p>

import cv2<br>
imagem = cv2.imread( "jogador.jpg")<br>

for y in range( 0, imagem.shape[0], 1):  #percorre linhas<br>
	for x in range(0, imagem.shape[1], 1):  #percorre colunas<br>
		imagem[y, x] = ( 0, (x*y)%256, 0) <br>
cv2.imshow( 'output', imagem )

<p><strong>Cortando uma imagem:</strong></p>

<p>Para fazer o recorte de uma imagem é selecionado uma area e armazendo em uma varável:</p>

import cv2<br>

imagem = cv2.imread( 'jogador.jpg')<br>
recorte = imagem[220:280, 248:304]<br>

cv2.imshow('output', recorte)<br>

<h2>Cores primárias</h2>
<p>Para que a cor seja vista, é necessário que o olho seja atingido por energia eletromágnetica. Vemos um objeto através da luz refletida por ele. Se ele aparece verde á luz do dia é porque, embora seja banhado pela luz branca so sol, ele reflete somente a parte verde da luz para nossos olhos, o restante do espectro é absorvido. A teoria da percepção cromática pelo olho humano baseia-se em hipótese formulada por Young em 1801, que estabelece que os cones( células fotossensíveis que compõe a retina juntamente com os bastonetes )se subdividem em três classe, com diferentes máximos de sensibilidade situados em torno do vermelho, verde e azul. Desta forma, todas as sensações de cor percebidas pelo olho humanno sã na verdade combinações de intensidades dos estímulos recebidos por cada um destes tipos de cones. Estas três cores são denominadas cores primárias aditivas, pois é possível obter qualquer outra cor a partir de uma combinação aditiva de uma delas, em diferentes proporções.   </p>

<h2>Sistema de cores</h2>
<p><strong>Cor é a propriedade que os corpos tem de absorver e refletir luz.</strong></p>
<p>O sistema RGB possui 3 canais, um para cada cor. Existem funções do OpenCV que permitem separar e visualizar esses canais individualmente.Exemplo:</p>

<h3>O modelo HSI </h3>
<p>O modelo HSI permite separar as componentes de matiz, saturação e intensidade da informação de cor em uma imagem, da forma como o ser humano as percebe. Geometricamente o modelo HSI pode ser visto como um sólido, cujo cortes horizontais produzem triangulos, nos quais os vertices contem as cores primarias e o centro corresponde a combinação destas cores em iguais proporções. Esta combinação estara mais proxima do preto ou do branco, conforme a altura em que o corte tenha sido efetuado. A partir da decompisição da imagem colorida nas compinentes adequadas, diversas técnicas existentes para imagens monocromaticas podem ser aplicadas com sucesso a imagens coloridas, com por exemplo a equalização do histograma.  </p>


import cv2

img = cv2.imread("jogador.jpg")<br>
(canalAzul, canalVerde, canalVermelho) = cv2.split( img )<br>

cv2.imshow( "Vermelho", canalVermelho)<br>
cv2.imshow( "Verde", canalVerde)<br>
cv2.imshow( "Azul", canalAzul)<br>



<h3>Histogramas </h3>
<p>É uma função que mostra a frequencia com que cada nivel de cinza aparece na imagem</p>
<p>Um histograma é um gráfico de colunas e linhas que representa a distribuição dos valores de uma imagem, ou seja, 
a quantidade de pixeis mais claros(próximos de 255) e a quantidade de pixeis mais escuros(próximos de 0)</p>
<p>A região onde a maioria dos valores se encontra é chamada de "gama tonal". </p>
<p>Geralmente o eixo X do gráfico mostra o valor( intensidade ) do pixel que varia de 0 a 255, e no eixo Y é plotada a quantidade de pixels naquela intensidade</p>
<p><strong>Exemplo de código para gerar histograma</strong></p>
<h3>Equalização do histograma</h3>
<p>É a técnica a partir da qual se procura redistribuir os valores de tons de cinza dos pixels de uma imagem. </p>
from matplotlib import pyplot as plt<br>
import cv2<br>

img = cv2.imread("jogador.jpg")<br>
img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)<br>
#Função calcHist para calcular o histograma da imagem
h = cv2.calcHist( [img], [0], None, [256], [0,256])<br>
plt.figure()<br>
plt.title( "Histograma")<br>
plt.xlabel( "Intensidade")<br>
plt.ylabel("Quantidade de pixel")<br>
plt.plot( h )<br>
plt.xlim([0,256])<br>
plt.show()<br>

<h3>Equalização do histograma</h3>
<p>Calculo matemático sobre a distribuição de pixels para aumentar o contraste da imagem.</p>

<h3>Suavização de imagens</h3>
<p>A suavização da imagem, também chamada de blur que traduzida significada "borrão", é um efeito em fotografias fora de foco ou desfocadas onde tudo fica embaçado.</p>
<p>Esse efeito pode ser criado digitalmente, basta alterar a cor de cada pixel misturando a cor com os pixels ao seu redor. </p>
<strong>Suavização por cálculoda média</strong>

<h2>Filtragens Espaciais</h2>
<p>Operam diretamente sobre a matriz de pixels que é a imagem digitalizada, normalmente utilizando operações de convoluções com máscaras. </p>
<p>No processo de filtragem digital utiliza-se uma operação de convolução de uma máscara pela imagem digital. Isso equivale a uma operação que passeia sobre toda a imagem original modificando seus valores de acordo com os valores originais da imagem e os pesos da máscara. </p>
<p>Normalmente utiliza-se vizinhança 8 do pixel de referência. </p>

<h2>Filtros Passa-Baixas ou filtros lineares</h2>
<p>É um filtro de suavização que reduz as variações nos níveis de cinza que dão aparência de serrilhado nos paamares de intensidade. </p>
<p>Eliminam as componnetes de alta frequência, que são as bordas e os detalhes finos da imagem, o efeito da filtragem passa-baixas é a suavização da imagem, provocando um leve borramento na mesma. </p>

<h2></h2>
<p>Os filtros passa-altas atenuam ou elimanam os componentes de baixa frequência e em função disto realçam as bordas e regiões de alto contraste da imagem. </p>

<h2>Filtro da média</h2>
<p>É a máscara de convolução n X n com todos os seus coeficientes iguais a 1 e depois dividindo-se o valor obtido pelo número de pixels da máscara.</p>
<p>Quanto maior a mascára maior o grau de borramento da imagem resultante. </p>

<h2>Filtro da mediana</h2>
<p>Nesta técnica o nível de cinza do pixel central da janela é substituido pela mediana dos pixels situados em sua vizinhança.</p>
<p></p>














































