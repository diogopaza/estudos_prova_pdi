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
<p>Toda imagem digital é uma matriz.</p>
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




