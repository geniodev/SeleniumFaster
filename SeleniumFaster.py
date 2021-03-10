
#Importações de Uso Frequente
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.expected_conditions import visibility_of_element_located, invisibility_of_element_located        #Unico Elemento
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located   #Todos Elementos

from selenium.webdriver.common.by import By

#--------------------------------------------------------------------------------------   CHROME


#Usando o navegador Padrão do seu computador = erros se não for compativel



def BaixarImagem(Find, NomePng="captchaSimples.png"):
    with open(NomePng, 'wb') as file:
        #Exemplo
        #file.write(driver.find_element_by_css_selector("img#captcha-img").screenshot_as_png)
        file.write(Find.screenshot_as_png)




def Navegador( Navegador="chrome", Maximizar=True, Visivel=True, EsperaImplicita=False ):
    
    from selenium import webdriver
    
      
    
    if (Navegador.lower() == "chrome"):
        
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options
        
        option = Options() #Instancia a classe de opções


        if Visivel:
            option.headless = False         #True, desliga a exibição do navegador. False, Exibe o navegador
        else:
            option.headless = True         #True, desliga a exibição do navegador. False, Exibe o navegador
    
        
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)



    
    if (Navegador.lower() == "firefox"):
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.options import Options
        
        option = Options() #Instancia a classe de opções


        if Visivel:
            option.headless = False         #True, desliga a exibição do navegador. False, Exibe o navegador
        else:
            option.headless = True         #True, desliga a exibição do navegador. False, Exibe o navegador
    
 
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)




    if (Navegador.lower() == "edge"):
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from selenium.webdriver.edge.options import Options
        
        option = Options() #Instancia a classe de opções


        if Visivel:
            option.headless = False         #True, desliga a exibição do navegador. False, Exibe o navegador
        else:
            option.headless = True         #True, desliga a exibição do navegador. False, Exibe o navegador

 
        driver = webdriver.Edge(EdgeDriverManager().install(), options=option)




    if (Navegador.lower() == "internet"):
        from webdriver_manager.microsoft import IEDriverManager
        from selenium.webdriver.ie.options import Options
        
        
        option = Options() #Instancia a classe de opções


        if Visivel:
            option.headless = False         #True, desliga a exibição do navegador. False, Exibe o navegador
        else:
            option.headless = True         #True, desliga a exibição do navegador. False, Exibe o navegador

        
        driver = webdriver.Ie(IEDriverManager().install(), options=option)




    if (Navegador.lower() == "internetexplorer"):
        from webdriver_manager.microsoft import IEDriverManager
        from selenium.webdriver.ie.options import Options
        
        
        option = Options() #Instancia a classe de opções


        if Visivel:
            option.headless = False         #True, desliga a exibição do navegador. False, Exibe o navegador
        else:
            option.headless = True         #True, desliga a exibição do navegador. False, Exibe o navegador

        
        driver = webdriver.Ie(IEDriverManager().install(), options=option)

    
    #retorna o Navegador para usos posteriores
    if Maximizar:
        driver.maximize_window()                            #Maximiza a janela do navegador
    
    if EsperaImplicita:
        if (isinstance(EsperaImplicita, (int, float) )):
            driver.implicitly_wait(EsperaImplicita)                          #Determina a Espera um determinado elemento aparecer na pagina, é usado nos find posteriores a ele configurado. Basta aplicar uma vez por seção, quando abre o browser, Vai esperar até '15' segundos no máximo para levantar um error.
        elif ( EsperaImplicita == True ):
            driver.implicitly_wait(65)                                       #Determina a Espera um determinado elemento aparecer na pagina, é usado nos find posteriores a ele configurado. Basta aplicar uma vez por seção, quando abre o browser, Vai esperar até '15' segundos no máximo para levantar um error.
        
        
    #Retorna o Driver
    return driver




#Requisições Web - Construir
def Requisicao(Driver, Site="", Metodo="get", Return_Url=False, TempoCarregamento=0, Return_Html=False, Return_Title=False ):
    if ( TempoCarregamento > 0):
        # Espera o tempo em segundos para carregar a página e levantar um error.
        Driver.set_page_load_timeout(TempoCarregamento)
    
    Driver.get(Site)
    

    #Construir os Return
    if Return_Html:
        return Driver.page_source

    
    if Return_Url:
        return Driver.current_url
    
    if Return_Title:
        return Driver.title
    



#Testar Temporizador Espera...
#Procura Elementos, atualmente somente selenium
def Find(Driver, FindParams= "id",  Find="", TempoMaxEspera=0, All=False, TestFind=False):
    
    if isinstance(FindParams, int):
        ListParams = ["id", "name", "xpath", "class_name", "css_selector", "link_text",  "partial_link_text"]
        atu = ListParams[FindParams]
        del(FindParams)
        FindParams = atu
        del(atu)
    
    
    if (Find == ""):
        return None
    
    if All:
        SearStr= "Driver.find_elements_by_" + str(FindParams) + "('{}')".format(Find)
        print("Sea:", SearStr)
    else:
        SearStr= "Driver.find_element_by_" + str(FindParams) + "('{}')".format(Find)
        print("Sea:", SearStr)
        
    
    
    if (TempoMaxEspera == 0):
        pass
    elif ( TempoMaxEspera > 0 ):
        element = WebDriverWait(Driver, TempoMaxEspera).until(visibility_of_element_located( eval( SearStr ) ))
    elif( (TempoMaxEspera < 0) ):
        pass
    elif ( TempoMaxEspera == None ):
        pass
    elif ( TempoMaxEspera == "None" ):
        pass
    
    
    
    print("Busca:", SearStr)
    #Busca = eval( SearStr )
    return eval( SearStr )
    




#Procura Elementos, atualmente somente selenium
def FindOperation(Driver, FindParams= "id",  Find="", All=False, TestFind=False, Click=False, LimparCampo=False, Digitar=False):
    
    if isinstance(FindParams, int):
        ListParams = ["id", "name", "xpath", "class_name", "css_selector", "link_text",  "partial_link_text"]
        atu = ListParams[FindParams]
        del(FindParams)
        FindParams = atu
        del(atu)
    
    
    if (Find == ""):
        return None
    
    if All:
        SearStr= "Driver.find_elements_by_" + str(FindParame) + "({})".format(Find)
    else:
        SearStr= "Driver.find_element_by_" + str(FindParame) + "({})".format(Find)
        
        
    
    Busca = eval( SearStr )
    
    if (Busca == None):
        return "Error Busca"
    
    #Executa o click
    if Click:
        try:
            Busca.click()
        except Exception:
            return "Error Click"
    
    #Limpa o Campo
    if LimparCampo:
        try:
            Busca.clear()
        except Exception:
            return "Error Clear"
    
    #Digita no campo
    if Digitar:
        try:
            Busca.send_keys(str(Digitar))
        except Exception:
            return "Error Digitar"
    




#Arrumar
#Pesquisa é o elemento retornado de Find
def AtributosFind(Pesquisa, Atributos=""):
    
    if isinstance(Atributos, str):
        valueAtr = element.get_attribute(Atributos) #Pega o Elemento da tag encontrada e imprime o atributo 'value' valor em texto dos botões.
        return valueAtr
    
    if isinstance(Atributos, (list, tuple) ):
        LisRes = []
        for aiu in Atributos:
            valueAtr = element.get_attribute( str(aiu) ) #Pega o Elemento da tag encontrada e imprime o atributo 'value' valor em texto dos botões.
            LisRes.append( valueAtr )
        
        return LisRes



#Espera Elemento Aparecer ou Desaparecer
class EsperarAparecerElemento():
  
    def __init__(self):
        pass

    """
    #Exemplo
    driver = Navegador()
    driver.get(r"https://servicos.ibama.gov.br/sicafiext/sistema.php")
    
    Espera = EsperarAparecerElemento(driver=driver)
    Espera1 = Espera.find(Condicao="id", ElementoEsperar="lnk1", TempoMaxEspera=30)
    """
    
    def find(self, driver, Condicao="id", ElementoEsperar="", TempoMaxEspera=30):
        if ( Condicao.lower() == "id"):
            lineBy = "ID"
            
        elif (   ( Condicao.lower() == "css") or ( Condicao.lower() == "css_selector")   ):
            lineBy =  "CSS_SELECTOR"
                
        elif (   ( Condicao.lower() == "tag") or ( Condicao.lower() == "tag_name")   ):
            lineBy =  "TAG_NAME"
        
        elif (   ( Condicao.lower() == "class") or ( Condicao.lower() == "class_name")  or ( Condicao.lower() == "classe") ):
            lineBy =  "CLASS_NAME"
        
        elif ( Condicao.lower() == "xpath"):
            lineBy =  "XPATH"
            
        elif ( Condicao.lower() == "name"):
            lineBy =  "NAME"
        
        elif ( ( Condicao.lower() == "link") or ( Condicao.lower() == "link_text") ):
            lineBy =  "LINK_TEXT"
        
        
        elif ( ( Condicao.lower() == "partial") or ( Condicao.lower() == "partial_link_text") ):
            lineBy =  "PARTIAL_LINK_TEXT"
        
        funexe = "By." +  str( lineBy )
        Encontrar = ( eval(funexe), ElementoEsperar)
        
        

        
        
        
        try:
            element = WebDriverWait(driver, TempoMaxEspera).until(visibility_of_element_located( Encontrar))
            return True
        except Exception:
            return False
    



#Espera Elemento Aparecer ou Desaparecer
class EsperarDesaparecerElemento():
  
    def __init__(self):
        pass

    """
    #Exemplo
    driver = Navegador()
    driver.get(r"https://servicos.ibama.gov.br/sicafiext/sistema.php")
    
    Espera = EsperarAparecerElemento(driver=driver)
    Espera1 = Espera.find(Condicao="id", ElementoEsperar="lnk1", TempoMaxEspera=30)
    """
    
    def find(self, driver, Condicao="id", ElementoEsperar="", TempoMaxEspera=30):
        if ( Condicao.lower() == "id"):
            lineBy = "ID"
            
        elif (   ( Condicao.lower() == "css") or ( Condicao.lower() == "css_selector")   ):
            lineBy =  "CSS_SELECTOR"
                
        elif (   ( Condicao.lower() == "tag") or ( Condicao.lower() == "tag_name")   ):
            lineBy =  "TAG_NAME"
        
        elif (   ( Condicao.lower() == "class") or ( Condicao.lower() == "class_name")  or ( Condicao.lower() == "classe") ):
            lineBy =  "CLASS_NAME"
        
        elif ( Condicao.lower() == "xpath"):
            lineBy =  "XPATH"
            
        elif ( Condicao.lower() == "name"):
            lineBy =  "NAME"
        
        elif ( ( Condicao.lower() == "link") or ( Condicao.lower() == "link_text") ):
            lineBy =  "LINK_TEXT"
        
        
        elif ( ( Condicao.lower() == "partial") or ( Condicao.lower() == "partial_link_text") ):
            lineBy =  "PARTIAL_LINK_TEXT"
        
        funexe = "By." +  str( lineBy )
        Encontrar = ( eval(funexe), ElementoEsperar)
        

        try:
            element = WebDriverWait(driver, TempoMaxEspera).until(invisibility_of_element_located( Encontrar))
            return True
        except Exception:
            return False
    



#Colocar O restante dos searchs....
def __EscreverBuscas__(dados):
    ListCom = []        #Retorna codigos comum do Selenium, caso dê error olhar o Script
    ListScript = []     #Retorna codigo executado em JavaScript caso o modo normal não funcione
    
    """#Captura os dados sem a variavel tag
    DadosSemTag = dados
    del(DadosSemTag['tag'])"""
    
    
    #Tag
    for aa in dados:
        #SEGUIMENTAÇÃO POR PARAMETROS, O RESTANTE NÃO USAR
        #Fazer um para xpath separado, não tem codigo pelo JavaScript


        if (   str(aa).lower() in ["id", "name"]    ):
            add = "driver.find_element_by_" + str(aa) + "('{}')".format(dados[str(aa)])
            ListCom.append(add)
                
            addscp = 'driver.execute_script("document.getElementBy{}'.format( str(aa).lower().capitalize()  ) + "('{}')".format(   dados[str(aa)]  ) + '")'
            ListScript.append(addscp)
            del(addscp)
            
            
        elif (  str(aa).lower() in ["class", "tag"]  ):
            
            add = 'driver.find_element_by_' + str(aa) + "_name" +"('{}')".format(dados[str(aa)])
            ListCom.append(add) #Normal
            del(add)
            
            addscp = 'driver.execute_script("document.getElementBy{}Name'.format( str(aa).lower().capitalize()  ) + "('{}')".format(   dados[str(aa)]  ) + '")'
            ListScript.append(addscp)
            del(addscp)


        elif (  str(aa).lower() == "link"  ):
            add = "driver.find_element_by_" + str(aa) + "_text" +"('{}')".format(dados[str(aa)])
            ListCom.append(add) #Normal
            del(add)
            
        
            #Achar aplicação do código em JavaScript
            addscp = "pass"
            ListScript.append(addscp)
            del(addscp)
            

            #Meio Furado, ver se precisa Realemnte de por isso aqui
            #Executar Codigo ou expressão em JavaScript quando clicado.
        elif (str(aa).lower() == "onclick"):
            
            #Usar como Try except, ele vai causar erorr aqui e pulará para o proximo passo
            add = str(aa).lower()
            ListCom.append(add) #Normal
            
            
            #jse = driver.execute_script("document.getElementById('mmlink1').click()")
            add = 'driver.execute_script("{}")'.format( dados[str(aa)] )
                
            ListScript.append(add)


                   

    return ListCom, ListScript




#Usado no MontaCodigoSelenium.
#Pega o Dataframe Pandas e roda um por um e escreve codigos em Selenium
def __InterceptaElementos__(PandasDF):
    
    CodPronto = []
    #Roda elementos linhas para pegar os dados e inserir codigos    
    for Ele in PandasDF:
        TagName = str( Ele['tag'] )
        
        #Passar somente 1 Tag por vez
        Busca = __EscreverBuscas__(dados=Ele)   #Cria código de Buscas, [0] Selenium / [1] Código JavaScript
        
        
        
        
        #Codigo Selenium: Busca[0]
        for CSelen in range(len(Busca[0])):
            if ( TagName == "button" ):
                Busca[0][CSelen] = Busca[0][CSelen] + ".click()"
                
            if ( TagName == "input" ):
                Busca[0][CSelen] = Busca[0][CSelen] + ".send_keys('{}').format(vari)"
                
            


        
        #Codigo JavaScript: Busca[1]
        for CJavas in range(len(Busca[1])):
            if ( TagName == "button" ):
                if ( "document." in Busca[1][CJavas] ):
                    Busca[1][CJavas] = Busca[1][CJavas][:-2:] + ".click(" + Busca[1][CJavas][-3:-1:] + Busca[1][CJavas][-1::] 
                else:
                    Busca[1][CJavas] = Busca[1][CJavas]
        
        
            if ( TagName == "input" ):
                Busca[1][CJavas] = Busca[1][CJavas][:-2:]  + ".value = '{}'" + chr(34) + ".format(vari)" + chr(41)



        for Cpronto in range(len(Busca[0])):
            bari = """try:\n    {}\nexcept Exception:\n    {}\n""".format(Busca[0][Cpronto], Busca[1][Cpronto])
            CodPronto.append(  bari    )

    
    #Retorna Codigo Pronto
    return CodPronto





#Monta Codigo Selenium com os elementos tags presente na pagina Atual do Driver
def MontaCodigoSelenium(Driver, OnlySelenium=False, OnlyJScript=False):
    #print(Driver.page_source)                           #Imprime o Código da Pagina em HTML
    #Codigo = driver.page_source                           #Captura Código da Pagina em HTML
    Codigo = Driver.page_source                           #Captura Código da Pagina em HTML
    
    
    #Passar o Código para o WebScrap para pegar os diferenciais
    from DiferHtml import Principal
    PegarDiferencial = Principal(HtmlTxt=Codigo)            #Traz as Tags com Diferenciais para capturar nos searchs. Pandas DF

    NovoPegarDiferencial = []
    
    #Eliminar Tags não Uteis
    EliminTag = ['body', 'head', 'header', 'html', 'br', 'b', 'i', 'abbr', 'bdo', 'blockquote', 'del', 'em', 'param', 'q',
                 'title', 'meta', 'tbody', 'tr', 'td', 'table', 'font']
    
    for aa in range(len(PegarDiferencial)):
        if ( PegarDiferencial[aa]['tag'].lower() in EliminTag ):
            pass
        else:
            NovoPegarDiferencial.append( PegarDiferencial[aa] )
            
    del(PegarDiferencial)
    PegarDiferencial = NovoPegarDiferencial
    del( NovoPegarDiferencial )
    
    
    #Executar uma formula para pegar itens valiosos, passando a tabela PD DF.
    TrazerCodigoPronto = __InterceptaElementos__(PandasDF=PegarDiferencial)




    return TrazerCodigoPronto





def DeixarSomenteColunasDeFind():
    ListaDeixar = ["id", "class", "css_selector", "name", "link_text", "partial_link_text"]
    PegarPosicaoBs4 = ['xpath']


