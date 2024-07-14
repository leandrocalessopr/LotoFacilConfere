"""
   PyQt5 é uma biblioteca para criação de interfaces gráficas de usuário em Python, que utiliza a ferramenta de
   desenvolvimento Qt. Com ela, é possível criar aplicações com interfaces ricas e modernas, que podem ser executadas
   em sistemas operacionais Windows, macOS e Linux. A biblioteca oferece um conjunto de widgets e ferramentas para a
   criação de janelas, menus, botões, caixas de texto, tabelas, gráficos, entre outros componentes visuais, além de
   suporte para criação de interfaces responsivas e personalizáveis. PyQt5 também possui suporte a recursos avançados,
   como threads, banco de dados, internacionalização, integração com a web e comunicação com outras aplicações. A
   documentação da biblioteca é extensa e existem diversas comunidades e fóruns de usuários para ajudar na resolução de
   dúvidas e problemas.

   Módulo re -> O módulo re em Python fornece suporte para expressões regulares, que são padrões usados para correspondência de
                sequências de caracteres. As expressões regulares são usadas em muitos contextos, como pesquisa de texto,
                análise de dados, processamento de linguagem natural e extração de informações.

                Algumas das funções mais comuns do módulo re são:
                     match(): verifica se o padrão corresponde ao início da string;
                     search(): procura o padrão na string inteira e retorna o primeiro resultado encontrado;
                     findall(): encontra todas as ocorrências do padrão na string e retorna uma lista com elas;
                     sub(): substitui todas as ocorrências do padrão por uma nova string.

                O módulo re também suporta o uso de metacaracteres para representar classes de caracteres,
                como [a-z] para todas as letras minúsculas, e quantificadores, como * para zero ou mais ocorrências
                de um padrão. É possível também criar grupos de captura, para extrair informações específicas de uma string.

                Em resumo, o módulo re é uma ferramenta poderosa para manipulação e processamento de strings em Python,
                permitindo a busca, extração e manipulação de padrões específicos em textos e dados.

   O módulo sys é uma das bibliotecas padrão do Python e oferece acesso a algumas variáveis e funções do interpretador.
   Algumas das principais funcionalidades incluem:

        sys.argv: lista de argumentos passados na linha de comando.
        sys.path: lista de diretórios onde o interpretador procura por módulos.
        sys.stdin, sys.stdout, sys.stderr: objetos de fluxo de entrada/saída padrão para o interpretador.
        sys.exc_info(): retorna informações sobre a exceção atual.
        sys.platform: string com o nome da plataforma em que o interpretador está sendo executado.

     Essas são apenas algumas das funcionalidades disponíveis no módulo sys. Ele também oferece outras funções e variáveis úteis,
     como sys.exit() para sair do programa com um status de erro, e sys.version para obter a versão do Python sendo executada.
     O módulo sys é amplamente utilizado em scripts e programas Python para realizar tarefas relacionadas ao sistema operacional e
     ao ambiente de execução do Python.O módulo sys é uma das bibliotecas padrão do Python e oferece acesso a algumas variáveis
     e funções do interpretador. Algumas das principais funcionalidades incluem:

     sys.argv: lista de argumentos passados na linha de comando.
     sys.path: lista de diretórios onde o interpretador procura por módulos.
     sys.stdin, sys.stdout, sys.stderr: objetos de fluxo de entrada/saída padrão para o interpretador.
     sys.exc_info(): retorna informações sobre a exceção atual.
     sys.platform: string com o nome da plataforma em que o interpretador está sendo executado.

     Essas são apenas algumas das funcionalidades disponíveis no módulo sys. Ele também oferece outras funções e variáveis úteis,
     como sys.exit() para sair do programa com um status de erro, e sys.version para obter a versão do Python sendo executada. O módulo sys é amplamente utilizado em scripts e programas Python para realizar tarefas relacionadas ao sistema operacional e ao ambiente de execução do Python.

   ------------------------------------------------------------------------------------------------------------------------------
   /O módulo traceback/ do Python é usado para coletar, formatar e imprimir informações de rastreamento (também conhecidas como
   tracebacks) sobre as exceções que ocorrem em um programa Python. É útil para depuração e diagnóstico de erros em programas
   Python. O módulo possui várias funções que podem ser usadas para obter informações sobre o rastreamento da exceção,
   como print_exc() que imprime o rastreamento da exceção para a saída padrão, format_exc() que retorna o rastreamento da
   exceção como uma string e extract_tb() que retorna uma lista de tuplas contendo informações sobre cada quadro (frame) do
   rastreamento da exceção. O módulo também permite personalizar o comportamento padrão de como os tracebacks são impressos,
   usando as classes TracebackException e StackSummary. Além disso, é possível usar a função extract_stack() para obter
   informações sobre a pilha de chamadas atual do programa.

   ------------------------------------------------------------------------------------------------------------------------------
   /O módulo requests/ é uma biblioteca Python utilizada para fazer requisições HTTP/1.1 e HTTP/2 em diversas APIs e websites.
   Com o requests, é possível enviar solicitações HTTP, definir cabeçalhos HTTP, adicionar parâmetros de consulta e cookies,
   além de lidar com redirecionamentos e erros HTTP.

   Algumas das principais características do módulo requests são:

   Fácil de usar: a sintaxe do requests é simples e fácil de entender, permitindo que desenvolvedores iniciantes possam utilizá-lo
   sem dificuldades. Documentação completa: a documentação do requests é completa e detalhada, contendo exemplos e explicações
   detalhadas de todos os recursos disponíveis. Flexibilidade: o requests permite que os desenvolvedores personalizem suas solici-
   tações HTTP com cabeçalhos personalizados, parâmetros de consulta e cookies. Suporte a HTTPS: o requests suporta HTTPS, permi-
   tindo que os desenvolvedores façam solicitações seguras e criptografadas. Em resumo, o módulo requests é uma ferramenta
   essencial para desenvolvedores Python que precisam fazer solicitações HTTP em suas aplicações.

   -----------------------------------------------------------------------------------------------------------------------------
   /A função __init__(self)/ é um método especial em Python que é chamado automaticamente quando um objeto é criado a partir de uma
   classe. É o primeiro método que é chamado após a criação de um objeto, e é usado para inicializar o objeto com valores padrão
   ou atributos. /O parâmetro self/ é usado para se referir ao próprio objeto que está sendo criado.
   ------------------------------------------------------------------------------------------------------------------------------
   /A função map()/ em Python é usada para aplicar uma determinada função a cada elemento de um iterável, como uma lista, e retorna
   um objeto map que contém os resultados dessas aplicações. O objeto map pode ser convertido em uma lista, tupla ou conjunto,
   dependendo da necessidade. A função map() recebe dois argumentos, o primeiro é a função que será aplicada a cada elemento do
   iterável e o segundo é o iterável em si. A função que é passada como primeiro argumento para a map() pode ser uma função predefinida,
   como abs(), str(), int(), etc., ou uma função personalizada que o usuário pode definir. A função personalizada deve ter apenas um
   argumento que representa o elemento a ser aplicado e deve retornar o resultado. O uso da função map() é útil para simplificar a
   sintaxe e tornar o código mais conciso e legível. É uma ferramenta útil para transformar e manipular dados em grandes conjuntos
   de dados.
   -------------------------------------------------------------------------------------------------------------------------------

   /A função filter()/ em Python é uma função de ordem superior que permite filtrar uma sequência de elementos com base em uma determinada
   condição. Ela recebe uma função e um iterável como argumentos, e retorna um iterador contendo apenas os elementos do iterável que sa-
   tisfazem a condição especificada pela função. A função passada como primeiro argumento para filter() deve receber um único argumento
   e retornar um valor booleano indicando se o elemento deve ser mantido na sequência filtrada ou não. Se a função retornar True, o elem-
   ento é incluído no resultado; caso contrário, ele é excluído. O uso da função map() é útil para simplificar a sintaxe e tornar o có-
   digo mais conciso e legível. É uma ferramenta útil para transformar e manipular dados em grandes conjuntos de dados.
     Ex : lista = [1, 2, 3, 4, 5, 6]
          pares = list(filter(lambda x: x % 2 == 0, lista))
          print(pares) # [2, 4, 6]
   -------------------------------------------------------------------------------------------------------------------------------

   /A função reduce()/ está contida no módulo functools do Python e permite aplicar uma função cumulativa aos elementos de uma sequência,
   a fim de reduzi-la a um único valor. A função reduce() é menos utilizada do que map() e filter(), mas ainda pode ser útil em alguns
   casos, especialmente quando se trata de combinar elementos de uma sequência em um único valor.
   -------------------------------------------------------------------------------------------------------------------------------

   /A função zip/ é usada para combinar duas ou mais sequências (como listas, tuplas, dicionários) em um único iterador, produzindo
   tuplas com elementos correspondentes. Essa função cria um objeto iterável que agrega os itens de cada uma das sequências passadas
   como argumento, de tal forma que o primeiro item do primeiro argumento se junta ao primeiro item do segundo argumento e assim por
   diante, até que todos os itens sejam agrupados.

   frutas = ['maçã', 'banana', 'laranja']
   precos = [2.5, 1.5, 3.0]

   for fruta, preco in zip(frutas, precos):
      print(f'{fruta}: R$ {preco:.2f}')
  --------------------------------------------------------------------------------------------------------------------------------

  /A função enumerate/ é uma função embutida do Python que permite iterar simultaneamente sobre os índices e valores de uma sequência
  (por exemplo, uma lista ou uma tupla) de uma maneira mais eficiente do que usando um loop for e indexando a sequência.
  A função enumerate retorna um objeto enumerado, que é uma sequência de pares (índice, valor). O índice começa em 0 por padrão, mas
  isso pode ser alterado passando um segundo argumento opcional para a função.

  nomes = ['Alice', 'Bob', 'Carol', 'Dave']
  for i, nome in enumerate(nomes):
     print(f'O nome da pessoa {i} é {nome}')
  ---------------------------------------------------------------------------------------------------------------------------------
  /As funções any e all/ são funções integradas do Python que podem ser usadas para verificar se uma sequência de valores é considerada
  verdadeira ou falsa. A função any retorna True se pelo menos um elemento da sequência for avaliado como verdadeiro.

  valores = [0, False, None, '', [], {}, 42]
  print(any(valores))  # Saída: True

  /A função any/ retorna True se pelo menos um elemento da sequência for avaliado como verdadeiro. Caso contrário, retorna False.
  valores = [0, False, None, '', [], {}, 42]
  print(any(valores))  # Saída: True
  ---------------------------------------------------------------------------------------------------------------------------------

  As funções lambda, também conhecidas como funções anônimas, são funções que não são definidas com um nome explícito. Em vez disso,
  são criadas usando a palavra-chave lambda, seguida de uma lista de argumentos, separados por vírgulas, e uma expressão. A expressão
  é avaliada e o resultado é retornado como resultado da função.
  Sintaxe básica : lambda argumentos: expressão.
  Por exemplo, para criar uma função que calcule o quadrado de um número, poderíamos escrever:
    1. quadrado = lambda x: x ** 2
    2. Podemos então chamar essa função passando um argumento:
       resultado = quadrado(5)
       print(resultado)  # 25
  As funções lambda são frequentemente usadas em conjunto com outras funções, como map(), filter(), reduce(), entre outras.
  Elas permitem escrever código mais conciso e legível, eliminando a necessidade de definir funções separadas para tarefas simples.
  ----------------------------------------------------------------------------------------------------------------------------------
"""

"""
   Se foi últil para você de alguma forma, então faça uma doação em Crypto.
   
     * Ethereum   : 0xd29b2ff62842f4fd9864caf410155be0ebc2a132
     * Bitcoin    : 15jzC1ynahB187RRxEthgE1Pv1xXZ7EYbW   
     * Zec(Zcash) : tex123as8jgwljy5c3pyx495lyqwm34prywa68tfv2
     * Dash       : XgajTRdHg97VaTwJFrNvqRP8Va1vz6ypd8

"""


import re
import sys
import traceback

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QCheckBox
from PyQt5.QtGui import QIcon

""" Essa linha de código define uma nova classe chamada LotoFacilChecker, que herda da classe QMainWindow do módulo PyQt5. """
class LotoFacilChecker(QMainWindow):

    todos_jogos_global = []

    def __init__(self):
        """chama o método __init__ da classe base da qual a classe atual é derivada, ou seja, a classe base QMainWindow do módulo PyQt5."""
        super().__init__()
        """Esse método é definido na própria classe e é responsável por criar e configurar os widgets (botões, campos de texto, etc) 
           que serão exibidos na janela."""
        self.initUI()
        self.extrai_dados_site()

    def initUI(self):

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('>>>>>>> Analize automatizada - Jogos LOTOFÁCIL <<<<<<<')
        self.setWindowIcon(QIcon('trevo_4folhas'))

        self.label = QLabel('Digite sua aposta (separada por espaço):', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(50, 50)
        self.label.resize(400, 30)

        # Campo para colocar o jogo feito.
        self.textbox_jogo_feito = QLineEdit(self)
        self.textbox_jogo_feito.setAlignment(Qt.AlignCenter)
        self.textbox_jogo_feito.move(50, 90)
        self.textbox_jogo_feito.resize(400, 30)
        self.textbox_jogo_feito.setPlaceholderText("Ex : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")

        # Campo para o sorteio.
        self.textbox_campo_sorteio = QLineEdit(self)
        self.textbox_campo_sorteio.setAlignment(Qt.AlignCenter)
        self.textbox_campo_sorteio.move(170, 135)
        self.textbox_campo_sorteio.resize(150, 30)
        self.textbox_campo_sorteio.setPlaceholderText("Sorteio aqui...")

        # Campo para colocar último jogo manualmente.
        self.textbox_utlimo_jogo_manual = QLineEdit(self)
        self.textbox_utlimo_jogo_manual.setAlignment(Qt.AlignCenter)
        self.textbox_utlimo_jogo_manual.move(50, 180)
        self.textbox_utlimo_jogo_manual.resize(400, 30)
        self.textbox_utlimo_jogo_manual.setPlaceholderText("Último sorteio...")
        self.textbox_utlimo_jogo_manual.setEnabled(False)

        #Botão de checagem.
        self.button = QPushButton('Verificar resultado', self)
        self.button.move(50, 240)
        self.button.resize(400, 30)
        self.button.clicked.connect(self.check_result)

        #Resultado.
        self.result_label = QLabel('', self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.move(50, 280)
        self.result_label.resize(400, 80)

        #------------------ CheckBox ------------------
        checkbox_checagem_direta = QCheckBox('Sorteio Offline', self)
        checkbox_checagem_direta.move(330, 135)
        checkbox_checagem_direta.stateChanged.connect(lambda state: self.onCheckboxStateChanged(state))

        checkbox_ordenar = QCheckBox('Ordenar', self)
        checkbox_ordenar.move(330, 205)
        checkbox_ordenar.stateChanged.connect( lambda state: self.onCheckboxStateChangedOrdenar(state))

        layout = QVBoxLayout()
        layout.addWidget(checkbox_checagem_direta)

        self.setLayout(layout)
        self.show()

    def onCheckboxStateChangedOrdenar(self, state):

        if state == 2:
            lista_sorteio_ultimo = [ int(x) for x in self.textbox_utlimo_jogo_manual.text().split()]
            imprimi_string       = self.convertListaString( lista_sorteio_ultimo )
            self.textbox_utlimo_jogo_manual.clear()
            self.textbox_utlimo_jogo_manual.setText(imprimi_string)

    def onCheckboxStateChanged(self, state):

        if state == 2:
            self.textbox_utlimo_jogo_manual.setEnabled(True)
            self.textbox_campo_sorteio.setEnabled(False)
        else :
            self.textbox_utlimo_jogo_manual.setEnabled(False)
            self.textbox_campo_sorteio.setEnabled(True)

    """ Converte lista em string para imprimir e Ordena."""
    def convertListaString(self, param_lista):

        lista_ordenada = sorted(param_lista)
        string_list = [str(x).zfill(2) for x in lista_ordenada]
        return ' '.join(string_list)

    def extrai_dados_site(self):

        # Obter os números sorteados no último concurso
        url = 'https://asloterias.com.br/lista-de-resultados-da-lotofacil'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }
        response = requests.get(url, verify=False,headers=headers)
        # Obter o conteúdo HTML retornado pela requisição
        html_content = response.text
        padrao_jogo = r'<strong>.*?<div'
        padrao_concurso = r'\d{4}'
        padrao_data = r'\d{2}\/\d{2}\/\d{4}'
        padrao_sequencia = r'\d{2}\s\d{2}.+\d{2}'
        resultado_jogo = re.findall(padrao_jogo, html_content)[1:]
        for linha in resultado_jogo :
            concurso = re.search(padrao_concurso, linha)
            data     = re.search(padrao_data, linha)
            sequencia= re.search(padrao_sequencia, linha)
            sequencia_int = [int(numero) for numero in sequencia.group().split()]
            self.todos_jogos_global.append( [concurso.group(),data.group(),sequencia_int])

    def check_result(self):

        try:

            # Obter os números da aposta do usuário
            aposta = list(map(int, self.textbox_jogo_feito.text().split()))

            if self.textbox_campo_sorteio.isEnabled() and self.textbox_campo_sorteio.text().strip() == '':
                quant_acertos      = len(set(self.todos_jogos_global[0][2]) & set(aposta))
                lista_acertos      = list(set(self.todos_jogos_global[0][2]) & set(aposta))
                concurso_sorteio   = self.todos_jogos_global[0][0]
                data_sorteio       = self.todos_jogos_global[0][1]
                sequencia_sorteada = self.todos_jogos_global[0][2]
            elif self.textbox_campo_sorteio.isEnabled() and self.textbox_campo_sorteio.text().strip() != '' :
                campo_concurso = self.textbox_campo_sorteio.text()
                for lista in self.todos_jogos_global :
                   concurso  = lista[0]
                   result = campo_concurso.find(concurso)
                   if result != -1 :
                       quant_acertos = len(set(lista[2]) & set(aposta))
                       lista_acertos = list(set(lista[2]) & set(aposta))
                       concurso_sorteio   = lista[0]
                       data_sorteio       = lista[1]
                       sequencia_sorteada = lista[2]
            elif self.textbox_campo_sorteio.isEnabled() == False :

                jogo_feito   = list(map(int, self.textbox_jogo_feito.text().split()))
                jogo_sorteio = list(map(int, self.textbox_utlimo_jogo_manual.text().split()))

                quant_acertos      = len(set(jogo_feito) & set(jogo_sorteio))
                lista_acertos      = list(set(jogo_feito) & set(jogo_sorteio))
                concurso_sorteio   = int (self.todos_jogos_global[0][0])+1


            if quant_acertos == 14:
                self.result_label.setText('PARABÉNS !!! ACERTOU 14 NÚMEROS')
            elif quant_acertos == 15:
                self.result_label.setText('PARABÉNS !!! ACERTOU 15 NÚMEROS')
            else:

                if self.textbox_campo_sorteio.isEnabled() :
                   self.result_label.setText(f'Você acertou : {quant_acertos}\n'
                                             f'Acertos : {lista_acertos}\n'
                                             f'Sorteio concurso : {sequencia_sorteada}\n '
                                             f'Concurso : {concurso_sorteio}\n '
                                             f'Data sorteio : {data_sorteio}')
                else :
                    self.result_label.setText(f'Você acertou : {quant_acertos}\n'
                                              f'Acertos : {lista_acertos}\n'
                                              f'Sorteio concurso : {jogo_sorteio}\n '
                                              f'Concurso : {concurso_sorteio}')

        except Exception as e:
            tb = traceback.extract_tb(e.__traceback__)
            filename, line, func, text = tb[-1]
            self.result_label.setText(f"Excessão : {e}\n Na linha : {line} \n Código : {text}")


if __name__ == '__main__':
    """
      /A linha app = QApplication(sys.argv)/ cria uma instância da classe QApplication do módulo PyQt5. A classe QApplication é a classe 
      base para todas as aplicações PyQt e fornece a funcionalidade principal para gerenciar a aplicação, incluindo inicialização, 
      configuração de parâmetros, gerênciamento de janelas, execução do loop de eventos e finalização da aplicação. O parâmetro sys.argv 
      é uma lista de argumentos da linha de comando passados para o programa Python. Quando criamos uma instância da classe 
      QApplication passando sys.argv como argumento, estamos permitindo que a aplicação interaja com a linha de comando, por exemplo, 
      permitindo que a aplicação receba arquivos arrastados e soltos na janela.
      ----------------------------------------------------------------------------------------------------------
    """
    app = QApplication(sys.argv)
    """
      Essa linha cria uma instância da classe LotoFacilChecker e atribui essa instância à variável window. Essa instância representa 
      a janela principal da aplicação.
    """
    window = LotoFacilChecker()
    """
      Essa linha chama o método show() na instância da classe LotoFacilChecker, que faz com que a janela criada seja exibida na tela. 
      Sem essa linha, a janela seria criada, mas não seria exibida.
    """
    window.show()

    """
      Essa linha encerra o programa, retornando um código de saída. A função exec_() é responsável por iniciar o loop de eventos do PyQt, 
      que fica aguardando interações do usuário e executando as ações correspondentes. O valor retornado por essa função indica o motivo
      pelo qual o loop de eventos foi encerrado, como por exemplo se o usuário fechou a janela ou se ocorreu algum erro durante a execução.
      A função sys.exit() é usada para finalizar a execução do programa, passando como argumento o valor de retorno da função exec_().
    """
    sys.exit(app.exec_())
	
