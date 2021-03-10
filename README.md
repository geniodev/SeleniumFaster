# SeleniumFaster
 SubBiblioteca Selenium facil de usar


#Fun��o
BaixarImagem(Find, NomePng="imagem.png")
#Exemplo 1:
img = driver.find_element_by_css_selector("img#captcha-img")
SalvarImg = BaixarImagem(Find=img, NomePng="imagem.png" )
#Exemplo 2:
SalvarImg = BaixarImagem(Find=driver.find_element_by_css_selector("img#captcha-img"), NomePng="imagem.png" )


#Inicia uma instancia do navegador("chrome") mas pode escolher("chrome", "firefox", "edge", "internet"/"internetexplorer")
#Maximizar: Padr�o(True) > Maximiza a tela para preencher a tela inteira do navegador
#Visivel: Padr�o(True) > Deixa visivel ou invis�vel o navegador(n�o aparece no computador)
#EsperaImplicita: Padr�o(False) > Quando "True" faz com que cada requisi��o de "Find" seja executado no tempo de espera definido aqui com numero inteiro em segundos.
#Fun��o
Navegador( Navegador="chrome", Maximizar=True, Visivel=True, EsperaImplicita=False )

#Faz uma requisi��o de Get em um site / Carrega/Entra um site
#Site: deve acompanhar conter os HTTP/HTTPS antes "https://wwww.site.com.br"
#TempoCarregamento: Padr�o(0) Padr�o leva o tempo que precisar. Tempo em int que levar� at� retornar um error.
#Return_Html: Padr�o(False). "True" Retorna o Codigo HTML da requisi��o realizada
#Return_Title: Padr�o(False). "True" Retorna o nome do Titulo da p�gina, util para verificar se acesso foi realizado com sucesso.
#Fun��o
def Requisicao(Driver, Site="", Return_Url=False, TempoCarregamento=0, Return_Html=False, Return_Title=False )


#Executa buscas de Elementos no Driver que estejam visiveis
#Driver: driver j� iniciado do navegador
#FindParams: Padr�o(id). Parametros de buscas, sendo ("id", "name", "xpath", "class_name", "css_selector", "link_text", "partial_link_text"), pode ser passado numero de 0 ate 6 a ordem est� descrito nesta linha.
#Find: O componente que ir� pesquisar que est�ra descrito no html, ex: "search", sera procura um id com nome "search"
#TempoMaxEspera: Padr�o(0) tempo padr�o da biblioteca. Espera o tempo at� o valor indicado, podendo terminar antes o valor mencionado em segundos.
#All: Padr�o(False). "True" > Faz buscas e retorna todos os elementos encontrados em uma lista de elementos selenium.
#Fun��o
Find(Driver, FindParams= "id", Find="", TempoMaxEspera=0, All=False)




#Executa buscas de Elementos no Driver que estejam visiveis e procede com alguns recursos de intera��o: clicar, limparcampo, digitar
#Driver: driver j� iniciado do navegador
#FindParams: Padr�o(id). Parametros de buscas, sendo ("id", "name", "xpath", "class_name", "css_selector", "link_text", "partial_link_text"), pode ser passado numero de 0 ate 6 a ordem est� descrito nesta linha.
#Find: O componente que ir� pesquisar que est�ra descrito no html, ex: "search", sera procura um id com nome "search"
#All: Padr�o(False). "True" > Faz buscas e retorna todos os elementos encontrados em uma lista de elementos selenium.
#Click: Padr�o(False)."True" > Faz um clique no objeto procurado
#LimparCampo: Padr�o(False)."True" > Limpa o campo de textos, funciona igual o "innterHTML", dentro entre a tag de abertura e fechamento.
#Digitar: Padr�o(False)."True" > Envia um texto digitado semelhante a um teclado para o elemento procurado
#Fun��o
FindOperation(Driver, FindParams="id", Find="", All=False, Click=False, LimparCampo=False, Digitar=False)




#Espera o elemento estar presente na pagina html
#Condicao: Padr�o(id). Parametros de buscas, sendo ("id", "name", "xpath", "class_name", "css_selector", "link_text", "partial_link_text").
#Exemplo de uso:
Espera = EsperarAparecerElemento(driver=driver)  #Instancia a classe, basta instanciar uma vez no codigo todo
Espera1 = Espera.find(Condicao="id", ElementoEsperar="lnk1", TempoMaxEspera=30)		#faz a busca de espera do elemento at� o tempo indicado




#Espera o elemento n�o existir na pagina html
#Condicao: Padr�o(id). Parametros de buscas, sendo ("id", "name", "xpath", "class_name", "css_selector", "link_text", "partial_link_text").
#Exemplo de uso:
Desaparecer = EsperarDesaparecerElemento(driver=driver) 	#Instancia a classe, basta instanciar uma vez no codigo todo
Desaparecer1 = Desaparecer.find(Condicao="id", ElementoEsperar="lnk1", TempoMaxEspera=30)		#faz a busca se o elemento n�o existe, caso existe vai esperar at� o tempo indicado para levantar um error.




#recebe o site atual no driver e transforma em uma lista de c�digos para usar como buscas find no selenium e tamb�m como busca em javascript interagido com selenium.
#Driver: driver j� iniciado do navegador
#OnlySelenium: Padr�o(False), "True" traz somente c�digos criado somente para intera��o selenium.
#OnlyJScript: Padr�o(False), "True" traz somente c�digos criados para buscas em javascript interagindo como se executasse um script javascript.
#Fun��o
MontaCodigoSelenium(Driver, OnlySelenium=False, OnlyJScript=False)