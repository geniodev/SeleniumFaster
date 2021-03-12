# SeleniumFaster
![](https://raw.githubusercontent.com/geniodev/SeleniumFaster/main/selenium%20express.png)</br>
&nbsp;
*SubBiblioteca Selenium facil de usar*</br>


&nbsp;
&nbsp;

*Índices*
&nbsp;
- <a href="https://github.com/geniodev/VozTexto#voztexto" target="_self">Inicio</a>
- <a href='https://github.com/geniodev/VozTexto#bibliotecas-instalar' target='_self'>Bibliotecas Install</a>
- <a href='https://github.com/geniodev/VozTexto#documenta%C3%A7%C3%A3o---f%C3%B3rmulas' target='_self'>Documentação</a>
  - <a href='https://github.com/geniodev/VozTexto#remove-acentos-das-strings-inseridas-no-txt' target='_self'>Remove acentos das strings inseridas no 'txt'</a>
    - <a href='https://github.com/geniodev/VozTexto#remove-acentos-das-strings-inseridas-no-txt' target='_self'>remover_acentos(txt)</a>
  - <a href='https://github.com/geniodev/VozTexto#ouvi-a-fala-de-voz-e-retorna-o-texto-sem-acentos' target='_self'>Ouvi a fala de voz e retorna o texto sem acentos</a>
    - <a href='https://github.com/geniodev/VozTexto#ouvi-a-fala-de-voz-e-retorna-o-texto-sem-acentos' target='_self'>ListenWorkd()</a>
  - <a href='https://github.com/geniodev/VozTexto#fala-a-hora-atual-e-minutos' target='_self'>Fala a hora Atual e minutos</a>
    - <a href='https://github.com/geniodev/VozTexto#fala-a-hora-atual-e-minutos' target='_self'>Falarhora()</a>
  - <a href='https://github.com/geniodev/VozTexto#voz-para-texto' target='_self'>Voz para Texto</a>
    - <a href='https://github.com/geniodev/VozTexto#voz-para-texto' target='_self'>OuvirFala()</a>
  - <a href='https://github.com/geniodev/VozTexto#texto-para-voz' target='_self'>Texto para Voz</a>
    - <a href='https://github.com/geniodev/VozTexto#texto-para-voz' target='_self'>falag(falaragora)</a>





&nbsp;
&nbsp;
<h1 id="install">Bibliotecas Instalar</h1></br>

```bash
pip install *
pip install *
```



&nbsp;
# Documentação - Fórmulas:</br>

#### Faz Download de uma imagem
Exemplo 1:
img = driver.find_element_by_css_selector("img#captcha-img")
SalvarImg = BaixarImagem(Find=img, NomePng="imagem.png" )
Exemplo 2:
SalvarImg = BaixarImagem(Find=driver.find_element_by_css_selector("img#captcha-img"), NomePng="imagem.png" )
> `BaixarImagem(Find, NomePng="imagem.png")`

&nbsp;

#### Inicia uma instancia do navegador
Navegador: "chrome", "firefox", "edge", "internet"/"internetexplorer"
Maximizar: Padrão(True) > Maximiza a tela para preencher a tela inteira do navegador
Visivel: Padrão(True) > Deixa visivel ou invisível o navegador(não aparece no computador)
EsperaImplicita: Padrão(False) > Quando "True" faz com que cada requisição de "Find" seja executado no tempo de espera definido aqui com numero inteiro em segundos.
> `Navegador( Navegador="chrome", Maximizar=True, Visivel=True, EsperaImplicita=False )`

&nbsp;


#### Carrega um site
Site: deve acompanhar conter os HTTP/HTTPS antes "https://wwww.site.com.br"
TempoCarregamento: Padrão(0) Padrão leva o tempo que precisar. Tempo em int que levará até retornar um error.
Return_Html: Padrão(False). "True" Retorna o Codigo HTML da requisição realizada
Return_Title: Padrão(False). "True" Retorna o nome do Titulo da página, util para verificar se acesso foi realizado com sucesso.
> `Requisicao(Driver, Site="", Return_Url=False, TempoCarregamento=0, Return_Html=False, Return_Title=False )`

&nbsp;


#### Busca de Elementos no Driver que estejam visiveis
Driver: driver já iniciado do navegador
FindParams: Padrão(id). Parametros de buscas, sendo ("id", "name", "xpath", "class_name", "css_selector", "link_text", "partial_link_text"), pode ser passado numero de 0 ate 6 a ordem está descrito nesta linha.
Find: O componente que irá pesquisar que estára descrito no html, ex: "search", sera procura um id com nome "search"
TempoMaxEspera: Padrão(0) tempo padrão da biblioteca. Espera o tempo até o valor indicado, podendo terminar antes o valor mencionado em segundos.
All: Padrão(False). "True" > Faz buscas e retorna todos os elementos encontrados em uma lista de elementos selenium.
> `Find(Driver, FindParams= "id", Find="", TempoMaxEspera=0, All=False)`

&nbsp;


#### Busca e Opera nos Elementos
Executa buscas de Elementos no Driver que estejam visiveis e procede com alguns recursos de interação: clicar, limparcampo, digitar
Driver: driver já iniciado do navegador
FindParams: Padrão(id). Parametros de buscas, sendo ("id", "name", "xpath", "class_name", "css_selector", "link_text", "partial_link_text"), pode ser passado numero de 0 ate 6 a ordem está descrito nesta linha.
Find: O componente que irá pesquisar que estára descrito no html, ex: "search", sera procura um id com nome "search"
All: Padrão(False). "True" > Faz buscas e retorna todos os elementos encontrados em uma lista de elementos selenium.
Click: Padrão(False)."True" > Faz um clique no objeto procurado
LimparCampo: Padrão(False)."True" > Limpa o campo de textos, funciona igual o "innterHTML", dentro entre a tag de abertura e fechamento.
Digitar: Padrão(False)."True" > Envia um texto digitado semelhante a um teclado para o elemento procurado
> `FindOperation(Driver, FindParams="id", Find="", All=False, Click=False, LimparCampo=False, Digitar=False)`



&nbsp;


#### Espera Aparecer Elemento
Espera o elemento estar presente na pagina html
Condicao: Padrão(id). Parametros de buscas, sendo ("id", "name", "xpath", "class_name", "css_selector", "link_text", "partial_link_text").
Exemplo de uso:
> `Espera = EsperarAparecerElemento(driver=driver)  #Instancia a classe, basta instanciar uma vez no codigo todo`
> `Espera1 = Espera.find(Condicao="id", ElementoEsperar="lnk1", TempoMaxEspera=30)		#faz a busca de espera do elemento até o tempo indicado`



&nbsp;



#### Espera Desaparecer Elemento
Espera o elemento não existir na pagina html.
Condicao: Padrão(id). Parametros de buscas, sendo ("id", "name", "xpath", "class_name", "css_selector", "link_text", "partial_link_text").
Exemplo de uso:
> `Desaparecer = EsperarDesaparecerElemento(driver=driver) 	#Instancia a classe, basta instanciar uma vez no codigo todo`
> `Desaparecer1 = Desaparecer.find(Condicao="id", ElementoEsperar="lnk1", TempoMaxEspera=30)		#faz a busca se o elemento não existe, caso existe vai esperar até o tempo indicado para levantar um error.`



&nbsp;




#### Monta Códigos para FindElement
recebe o site atual no driver e transforma em uma lista de códigos para usar como buscas find no selenium e também como busca em javascript interagido com selenium.
Driver: driver já iniciado do navegador
OnlySelenium: Padrão(False), "True" traz somente códigos criado somente para interação selenium.
OnlyJScript: Padrão(False), "True" traz somente códigos criados para buscas em javascript interagindo como se executasse um script javascript.
> `MontaCodigoSelenium(Driver, OnlySelenium=False, OnlyJScript=False)`



&nbsp;
<h6 align="center">Desenvolvedor: RA (Ricardo Andrade)</h6>
<h6 align="center">Versão: 5.0.0</h6>
