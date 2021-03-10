

from bs4 import BeautifulSoup
import pandas as pd
from bs4.element import NavigableString, Tag
import numpy as np


# Pronto
#Parser LXML
#Quebra de Linha (True), com \n.... (False) sem os \n
def __html__(Arquivo=None, String=None, BrowserView=None, QuebraLinhas=None, LetrasMinusculas=None):
    #Fazer requerimento da URL e imprimindo resultado
    
    
    #------------------------------------ String HTML
    if (String == None):
        print("None String")
        pass
    else:
        #with open('arquivo.html', 'r') as ff:
        print("Entrou String HTML")


        if BrowserView:
            if QuebraLinhas:
                if LetrasMinusculas:
                    #soup_string2 = BeautifulSoup(String.lower(), 'html5lib')
                    soup_string2 = BeautifulSoup(String.lower(), 'html5lib', from_encoding=None)
                else:
                    #soup_string2 = BeautifulSoup(String, 'html5lib')
                    soup_string2 = BeautifulSoup(String, 'html5lib', from_encoding=None )
            else:
                boop = f.read()
                bkp = str( boop )
                del(boop)
                bkp = bkp.replace( r"\\n" , "")
                bkp = bkp.replace(chr(10)+chr(10), "")
                bkp = bkp.replace(chr(10), "")
                if LetrasMinusculas:
                    bkp = bkp.lower()
                #soup_string2 = BeautifulSoup(bkp, 'html5lib')
                soup_string2 = BeautifulSoup(bkp, 'html5lib', from_encoding=None )
        else:
            if QuebraLinhas:
                if LetrasMinusculas:
                    #soup_string2 = BeautifulSoup(String.lower(), 'lxml')
                    soup_string2 = BeautifulSoup(String.lower(), 'lxml', from_encoding=None)
                else:
                    #soup_string2 = BeautifulSoup(String, 'lxml')
                    soup_string2 = BeautifulSoup(String, 'lxml', from_encoding=None)
            else:
                boop = String
                bkp = str( boop )
                del(boop)
                if LetrasMinusculas:
                    bkp = bkp.lower()
                #soup_string2 = BeautifulSoup(bkp, 'lxml')
                soup_string2 = BeautifulSoup(bkp, 'lxml', from_encoding=None)
            
            
    
    
    
    
    
    #print("Conteudo:", soup_string2)    
    #------------------------------------ Arquivo HTML
    
    if (Arquivo == None):
        print("None Arquivo")
        pass
    else:
        print("Entrou Arquivo HTML")
        Tipo = None
    
        pp = open(Arquivo, 'r')
        try:
            pp.read()
            Tipo = "string"
        except Exception:
            Tipo = "bytes"

    
        
        if ( Tipo == "string"  ):    #Tente Ler Normal, senão leia Binario
            print("Entrou tipo Texto")
    
            #with open('arquivo.html', 'r') as ff:
            with open(Arquivo, 'r') as ff:
                if BrowserView:
                    if QuebraLinhas:
                        if LetrasMinusculas:
                            #soup_string2 = BeautifulSoup(ff.read().lower(), 'html5lib')
                            soup_string2 = BeautifulSoup(ff.read().lower(), 'html5lib', from_encoding=None)
                        else:
                            #soup_string2 = BeautifulSoup(ff.read(), 'html5lib')
                            soup_string2 = BeautifulSoup(ff.read(), 'html5lib', from_encoding=None )
                    else:
                        boop = f.read()
                        bkp = str( boop )
                        del(boop)
                        bkp = bkp.replace( r"\\n" , "")
                        bkp = bkp.replace(chr(10)+chr(10), "")
                        bkp = bkp.replace(chr(10), "")
                        if LetrasMinusculas:
                            bkp = bkp.lower()
                        #soup_string2 = BeautifulSoup(bkp, 'html5lib')
                        soup_string2 = BeautifulSoup(bkp, 'html5lib', from_encoding=None )
                else:
                    if QuebraLinhas:
                        if LetrasMinusculas:
                            #soup_string2 = BeautifulSoup(ff.read().lower(), 'lxml')
                            soup_string2 = BeautifulSoup(ff.read().lower(), 'lxml', from_encoding=None)
                        else:
                            #soup_string2 = BeautifulSoup(ff.read(), 'lxml')
                            soup_string2 = BeautifulSoup(ff.read(), 'lxml', from_encoding=None)
                    else:
                        boop = ff.read()
                        bkp = str( boop )
                        del(boop)
                        if LetrasMinusculas:
                            bkp = bkp.lower()
                        #soup_string2 = BeautifulSoup(bkp, 'lxml')
                        soup_string2 = BeautifulSoup(bkp, 'lxml', from_encoding=None)
                    
        
        if ( Tipo == "bytes"  ):    #Leia o arquivo como Binário
            print("Lendo Binário")
            with open(Arquivo, 'rb') as ff:
                if BrowserView:
                    if QuebraLinhas:
                        if LetrasMinusculas:
                            #soup_string2 = BeautifulSoup(ff.read().lower(), 'html5lib')
                            soup_string2 = BeautifulSoup(ff.read().lower(), 'html5lib', from_encoding=None)
                        else:
                            #soup_string2 = BeautifulSoup(ff.read(), 'html5lib')
                            soup_string2 = BeautifulSoup(ff.read(), 'html5lib', from_encoding=None )
                    else:
                        boop = ff.read()
                        bkp = str( boop )
                        del(boop)
                        bkp = bkp.replace( r"\\n" , "")
                        bkp = bkp.replace(chr(10)+chr(10), "")
                        bkp = bkp.replace(chr(10), "")
                        if LetrasMinusculas:
                            bkp = bkp.lower()
                        #soup_string2 = BeautifulSoup(bkp, 'html5lib')
                        soup_string2 = BeautifulSoup(bkp, 'html5lib', from_encoding=None )
                else:
                    if QuebraLinhas:
                        if LetrasMinusculas:
                            #soup_string2 = BeautifulSoup(ff.read().lower(), 'lxml')
                            soup_string2 = BeautifulSoup(ff.read().lower(), 'lxml', from_encoding=None)
                        else:
                            #soup_string2 = BeautifulSoup(ff.read(), 'lxml')
                            soup_string2 = BeautifulSoup(ff.read(), 'lxml', from_encoding=None)
                    else:
                        
                        boop = ff.read()
                        bkp = str( boop )
                        del(boop)
                        if LetrasMinusculas:
                            bkp = bkp.lower()
                        #soup_string2 = BeautifulSoup(bkp, 'lxml')
                        soup_string2 = BeautifulSoup(bkp, 'lxml', from_encoding=None)
            
    return soup_string2        
            

        




def __RodarTudo__(Html):
    
    df = pd.DataFrame( columns=['tag', 'id','class', 'string'] )      #Transforma o dado em Dataframe pandas
   
    
    
    Df_index = -1        #Inicia a variavel index
    
    nops = None
    for tag in Html.descendants:
        Df_index += 1   #Index inserir Atual
        
        
        if isinstance(tag, NavigableString):
            #print(tag)#String
            Df_index -= 1
        
        else:
            df.loc[str(Df_index), 'tag'] = str(tag.name)   #TagName

                
            
            QtdAtt = len(tag.attrs)
            
            #Roda Atributo por Atributo e Adiciona na Coluna
            for atb in tag.attrs:
                #print(atb)
                df.loc[str(Df_index), str(atb)] = str ( tag[atb] ) #Passar o valor do atributo
            
            df.loc[str(Df_index), 'string'] = str(tag.string)   #TagName
            

            
                
    df = df.replace("None", np.nan )
    df = df.replace("", np.nan )

    #retornar os dados em Dataframe
    return df


def __DeixarUnico__(RodarTudo):
    
    Subs = RodarTudo   #Usado para limpar valores não unicos para retornar
    
    QtdColunas = len( RodarTudo.columns )       #QTD Colunas
    
    #for acol in range(QtdColunas):
    for acol in RodarTudo.columns[1::]:
        #Ndados = RodarTudo[acol]

        Ndados2 = RodarTudo[acol].astype(str)
        Ndados = Ndados2.to_list()
        del(Ndados2)
        Unic = set(Ndados)
        #del(Ndados)
        Unic = list(Unic)
        
        #Deletar None
        try:
            iddel = Unic.index("nan")
            del(Unic[iddel])            
        except Exception:
            pass

        #Deletar None
        try:
            iddel = Unic.index("None")
            del(Unic[iddel])            
        except Exception:
            pass
        
        
        #Rodar Novamente para somar t
        for aa in Unic:
            Ctt = Ndados.count(aa)
            if (Ctt > 1):
                Subs[acol] = Subs[acol].replace(aa, np.nan)
            else:   #Não tem valores repetidos, é unico
                pass


    
    
    ListaFinal = []
    FullDict = {}
    #Iterar Linha por Linha para Trazer soment o resultado Unico
    for kk in Subs.index:   #Roda a Linha
        
        #Ver = Subs.at[kk, "tag"]
        Ver = str( Subs.at[kk, "tag"]  )
        #print("Tag", Ver)



        
        
        #Condição se a Tag for None, não adicionar na Lista
        if ( Ver == "nan" ):    #Se for Nulo
                pass
        elif ( Ver == "" ):    #Se for Nulo
                pass
            
        elif ( Ver == None ):    #Se for Nulo
                pass
        elif ( Ver == "None" ):    #Se for Nulo
                pass
        
        
        
        else:   #Caso a Tag não Seja Nula
        
                AtualDict = {}
                #AtualDict = Subs.at[kk, 'tag']
                
                #ListaFinal.append([tag])
                #FullDict
                #ListaFinal.append([{"tag":"html"}])
                
                for acol2 in Subs.columns:
                    cod = str ( Subs.at[kk, acol2] )
                    
                    if ( cod == "nan" ):    #Se for Nulo
                        pass
                    elif ( cod == "" ):    #Se for Nulo
                        pass
                    
                    elif ( cod == None ):    #Se for Nulo
                        pass
                    elif ( cod == "None" ):    #Se for Nulo
                        pass
                    else:
                        AtualDict[acol2] = cod    #Vai passar o valor pro dicionario atual
                
                #Antes de Passar pra outra coluna, adicione o diconario na posição
                #ListaFinal.append([AtualDict])  #Passa o dicionario da lista iteira para o valor
                ListaFinal.append(AtualDict)  #Passa o dicionario da lista iteira para o valor
                            
                        

            
        
        
    #return Subs
    return ListaFinal



def Principal(Arquivo=None, HtmlSoup=None, HtmlTxt=None):
    
    if (Arquivo == None and HtmlSoup == None and HtmlTxt == None) :
        return None
    
    #Tipo Arquivo
    if ( Arquivo == None ):
        pass
    else:
        print("Entrou Principal 'Arquivo'")
        #Arquivo = 'correios.html'
        ab = __html__(Arquivo=Arquivo, BrowserView=False, QuebraLinhas=False, LetrasMinusculas=False)
        del(Arquivo)
    
    
    #Tipo Txt
    if ( HtmlTxt == None ):
        pass
    else:
        print("Entrou Principal 'Txt'")
        ab = __html__(String=HtmlTxt, BrowserView=False, QuebraLinhas=False, LetrasMinusculas=False)
        
    
    
    #ab = html(Arquivo, BrowserView=False, QuebraLinhas=False, LetrasMinusculas=False)

    Teste = __RodarTudo__(Html=ab)
    Unin = __DeixarUnico__(RodarTudo=Teste)
    
    return Unin




##############################################     Como Usar




"""
#Uso passe o nome do arquivo salvo em html
Arquivo = 'correios.html'
Codigo = Principal(Arquivo)
#print(Codigo)
"""
