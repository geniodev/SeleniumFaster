

#Tentar Selenium
#Usar Este
#Baixa versão 84 do chrome
#Baixa um chromedriver para usar na maquina do usuário, mais indicado para multiplataforma
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

#Classe Keys para Envio de teclas de atalho
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Classe Select para fazer seleção de Box
from selenium.webdriver.support.ui import Select


#Uso de alguns recursos da da sub biblioteca criada por mim
#import SeleniumSubBiblioteca as Selenium
#from SeleniumSubBiblioteca import EsperarAparecerElemento, EsperarDesaparecerElemento

#Meditor de Tempo
import time

#Requerimentos de online
import requests


from glob import glob

#Teste Mudar opção do navegador
import os
from selenium.webdriver.chrome.options import Options


#Buffer IO
import io

#Sistema
import os

#Operar Area de Transferencia
import clipboard




#Profile é uma pasta do navegador onde estarão os arquivos do chrome, onde você pode copiar o seu navegador e usar nele para ligar plug-ins e ferramentas
def Abrir_navegador(download_dir="", profile="", AutoDownloadFiles=True, Invisivel=False ):
    
    #Diretorio de Download
    if (download_dir  == ""):
        download_dir = os.getcwd()

    #Profile do Navegador
    if (profile==""):
        profile = os.path.join(download_dir, "perfil")  #Define o diretorio do profile do mesmo proejeto
    elif( profile=="dev" ):
        profile = os.path.join("E:\\dev", "perfil")  #Perfil Dev
    else:
        pass
    
    chrome_options = Options()
    chrome_options.add_argument( "user-data-dir={}".format(profile) )
    
    #Aqui Desliga aquelas pergunta de onde quer salvar os arquivos caso baixe, ele salvara na pasta 'download_dir'
    if (AutoDownloadFiles == True):
        chrome_options.add_experimental_option('prefs',  {
                "download.default_directory": download_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": True
                }
            )
    
    if (Invisivel == True):
        chrome_options.headless = True           #Deixa o navegador Invisivel(True) / Visivel(False)-padrao
    else:
        chrome_options.headless = False           #Deixa o navegador Invisivel(True) / Visivel(False)-padrao
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
    #driver.maximize_window()                            #Maximiza a janela do navegador
    driver.implicitly_wait(3)      #Espera Implicita
    driver.set_page_load_timeout(60)                    #Timeout de espera da pagina carregar.
    
    return driver



#Fecha o Navegador
def Fechar_navegador(driver):
        #sair do navegador
        driver.quit()   #Encerra o navegador









## -----------------------------------------------------------       Recursos


#Verifica se esta online
def Online():
    r = requests.get(r"https://www.google.com")
    if r.status_code == requests.codes.ok:
        return True
    else:
        return False


#Copia o que é pra digitar na memoria
def Copiar(text):
    clipboard.copy(text)


def Colar(objeto):
    # objeto.send_keys(Keys.CONTROL+ "v")
    clipboard.paste()



def Digitar(objeto, conteudo, limpar=True):
    try:
        
        #Limpar Campo
        if ( limpar == True ):
            try:
                objeto.clear()
            except Exception:
                pass
            
        
        clipboard.copy(conteudo) #Copia conteudo para a área de Transferencia
        clipboard.paste()
        return True
    except Exception:
        return False




def BaixarCaptcha(Find, NomePng="captchaSimples.png"):
    #Funciona Melhor
    with open(NomePng, 'wb') as file:
        #file.write(driver.find_element_by_css_selector("img#captcha-img").screenshot_as_png) #Exemplo
        file.write(Find.screenshot_as_png)


## -----------------------------------------------------------       Aplicação




## -----------------------------------------------------------       Uso Geral Especifico

# Pagina
driver.page_source   #Retorna o HTML da página
driver.current_url   #Retorna a URL da pagina
driver.title         #Retorna o Título da Página

# Procurar Elementos -- Para Retornar uma Lista de todos encontrado, troque "element" por "elements"
driver.find_element_by_id()
driver.find_element_by_class_name()
driver.find_element_by_css_selector()
driver.find_element_by_xpath()
driver.find_element_by_name()
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()

## Com Espera de tempo máximo de 60 segundos
WebDriverWait(driver, 60).until(visibility_of_element_located( driver.find_element_by_css_selector( "body div[name|='usuario']" ) ))   #Elementos Visiveis

## Baixa os Atributos do Elemento >> Testar Função
driver.find_element_by_css_selector( "body div[name|='usuario']" ).get_attribute(  "disabled"  ) #Pega o Elemento da tag encontrada e imprime o atributo 'value' valor em texto dos botões.

## Operações nos Elementos
driver.find_element_by_css_selector().click()   #Encontra o Elemento e Clica no Elemento
driver.find_element_by_css_selector().clear()   #Encontra o Elemento e Limpa o campo
texto = driver.find_element_by_css_selector().text      #Encontra o Elemento e captura o texto dentro dele

## Não usar para digitar - Acontece Falhas. Usar somente para Enviar combinações de Teclas
driver.find_element_by_css_selector().send_keys(str(Digitar))   #Encontra o Elemento e Digita no campo

campoLogin = driver.find_element_by_css_selector()
Digitar(objeto=campoLogin, conteudo=Digitar, limpar=True) #( Limpar == True) limpa o campo antes de digitar


# Requisição de Um site
site = r"https://servicos.ibama.gov.br/sicafiext/sistema.php"
driver.get(site)


# Rodar Comandos JavaScript
jse3 = driver.execute_script("document.getElementById('p_num_cpf_cnpj').value='{}'".format(DadosCadastrais['cpf'])) #Preenche os Campos cpf
jse4 = driver.execute_script("document.getElementById('btnPesquisar').click()")
jse4 = driver.execute_script("return variavel")  #Retorna uma variável feita com código javascript para interpretar no python. Deve ser guardoado em uma variável


# Seleção de Boxes
selectCity = Select(driver.find_element_by_css_selector("#cad_cod_municipio.formdincampomulti"))    #Cria uma seção de Selecionar Boxes Caixas
selectUF.select_by_index(1)   #Seleciona pelo nome do estado, tudo em maiusculo
selectUF.select_by_visible_text("{}".format(    DadosCadastrais['uf'].upper()    ))   #Seleciona pelo nome do estado, tudo em maiusculo
selectUF = Select(driver.find_element_by_css_selector("#cad_cod_uf.formdincampomulti"))


# Verificar Verdadeiro
assert "estou com sorte" == value_button.lower()    #Verifica se a condição é verdadeira, senão levanta error "AssertionError"

# Printar a tela do Navegador
driver.save_screenshot("screenshot.png")        #Printar a Tela do navegador e salva com nome: screenshot.png

## Version 1.0


# Trocar de Janela (Aba)
# Fechar Aba do navegador e setar na 1ª
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.switch_to.default_content()     #Volta ao Frame Padrão


#Trocar para Alerta Alerta
alert = browser.switch_to.alert
alert.accept()
## Avançado de Alert
try:
    WebDriverWait(browser, 3).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")
#Operando com Alert
alert = Alert(driver)   # Instancia a classe alert
alert.dismiss()     # Clica no Botão Cancelar
alert.accept() # Confirma o alerta
alert.text      # Pega o texto presente na caixa de Alerta
alert.send_keys("Texto a ser enviado para o Alert")
# Login com Alert
driver.switch_to.alert.authenticate('usuario', "senha")
Alert(driver).accept()




#Trocar de Iframe
driver.switch_to.frame("frame3")  #Nome do Iframe
driver.switch_to.default_content()     #Volta ao Frame Padrão
driver.switch_to.frame(2)       #Selecionando o Frame por Número
driver.switch_to.frame(driver.find_element_by_tag_name("iframe")[1]);       #Selecionando Iframe por busca de "Find"


# Limpar Todos os pdfs da pasta atual, Novo dirtorio passe o path completo
files = glob('*.pdf')  #Pega todos os arquivos ".PDF"
#files.extend(glob('*.png')   #Adicionar mais extensões
for atuFile in files:
    os.remove(atuFile)
isExist = os.path.exists(files[0])  #Verifica se o arquivo/pasta existe no disco


# Faz Leitura de um arquivo qualquer e encapsula ele como Binário
ab = open(  arqRen, 'rb'     ).read()
io_buf = io.BytesIO(  ab  )


#Gravar Arquivos
var_file = open( "novo.pdf" , 'wb').write( ArquivoGravar )
try:
    var_file.close()
except Exception:
    pass


#Salvar o JPG para PDF
image1 = Image.open(  os.path.join ( os.getcwd(), "screenshot.png" )    )
im1 = image1.convert('RGB')
im1.save("CND RF {} CPF{}.pdf".format(NomeCapt, cpf ))

os.remove("screenshot.png")


# Opções da classe ActionChains :
actions = ActionChains(driver) # Instaciamos a classe passando o driver.

actions.perform() - Executa todas as ações armazenadas.
actions.click() - Clica em um determinado elemento.
actions.click_and_hold() - Mantém pressionado o botão esquerdo do mouse em um elemento.
actions.context_click() - Executa um contexto-clique (clique com botão direito) em um elemento.
actions.double_click() - Clique duas vezes em um elemento.
actions.drag_and_drop() - Mantém pressionado o botão esquerdo do mouse no elemento de origem e, em seguida, move para o elemento de destino e libera o botão do mouse.
actions.drag_and_drop_by_offset() - Mantém pressionado o botão esquerdo do mouse no elemento de origem e, em seguida, move para o deslocamento de destino e libera o botão do mouse.
actions.key_down() - Envia somente uma tecla pressionada, sem soltá-la. Só deve ser usado com teclas modificadoras (Control, Alt e Shift)
actions.key_up() - Libera uma tecla modificadora
actions.move_by_offset() - Movendo o mouse da atual posição para uma outra posição
actions.move_to_element() - Move o mouse para o meio do elemento
actions.move_to_element_with_offset() - Move o mouse por um deslocamento do elemento especificado Os deslocamentos são relativos ao canto superior esquerdo do elemento
actions.release() - Liberar o botão do mouse sobre o elemento
actions.send_keys() - Envia os caracteres para a atual foco do elemento

#Usando ActionChains (Drag and Drop)
driver.find_element_by_css_selector("#run").click()
driver.switch_to.frame("result")
source = driver.find_element_by_css_selector("#dragThis")   # Elemento que eu desejo arrastar.
target = driver.find_element_by_css_selector("#dropHere")   # Destino do meu elemento.
# Instaciamos a classe passando o driver.
actions = ActionChains(driver)
# Utilizamos a funcao drag_and_drop, passando os elementos.
actions.drag_and_drop(source, target)
# Executamos as acoes.
actions.perform()








#       ----------------------------------------    APLICATIVO -----------------------------------------




# ---- Variáveis




# ---------------------------    Operação

# Exemplo




driver = Abrir_navegador(download_dir="", profile="dev", AutoDownloadFiles=True, Invisivel=False )





#Trocar de Iframe
driver.switch_to.frame("SelectorsHub")  #Nome do Iframe
driver.switch_to.default_content()     #Volta ao Frame Padrão
driver.switch_to.frame(2)       #Selecionando o Frame por Número
driver.switch_to.frame(driver.find_element_by_tag_name("iframe")[1])       #Selecionando Iframe por busca de "Find"


driver.switch_to.frame(0)       #Selecionando o Frame por Número

driver.switch_to.frame(driver.find_element_by_tag_name("SelectorsHub")[0])


Fechar_navegador(driver) #Fecha Navegador



# =============================================================================
# try:
#     cod
#     print(  "Elemento Encontrado: {}".format(   )  )
# except Exception:
#     raise "Falhou ao "
#     # raise "Falhou ao Encontrar: {}".format(   )
# 
# =============================================================================
    
    
    