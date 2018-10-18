1 - Resumo rapido sobre o programa:
    O codigo recebe como entrada um arquivo onde cada linha é um comando.
    O comando é interpretado e o metodo calculado, apois isso é mostrado
    ao usuario os pontos calculados via terminal, plot grafico e escrito
    num arquivo de saída. Após fechar a janela do grafico, o programa
    executa a proxima linha do arquivo de entrada, e assim até o seu fim.

2 - Requerimentos:
    É necessário que esteja num ambiente Linux (O ambiente de desenvolvimento e teste foi OpenSUSE Tumbleweed com Kernel 4.18.9-1)
    E python 3 (versão usada: 3.6.5)
    
    Recomendado: ter as bibliotecas de python sympy e matplotlib instaladas em sua maquina e/ou virtualenv instalado.

3 - Executando o programa:
    Caso sua maquina já tenha as bibliotecas sympy e matplotlib, então no diretorio do programa pelo terminal rode o comando:
        python3 main.py
    Caso sua maquina não tenha as bibliotecas, pasta do programa pelo terminal rode:
        source RUNME            (cria um ambiente virtual e instala as bibliotecas)
        python main.py

    A cada metodo calculado o programa mostra no terminal, escreve no arquivo de saida, e faz um grafico. Para ele executar
    o próximo comando o usuario deve fechar a janela do grafico. E dessa forma ele executa até o final do arquivo de entrada.

4 - Especificacao da entrada:
    O arquivo de entrada (entrada.txt) cosiste em comandos por linha dos tipos:
        metodo y0 t0 h n equacao
        metodo y-2 y-1 y0 t0 h n equacao ordem
        metodo y0 t0 h n equacao ordem
    Metodos aceitos pelo programa:
        1) Euler Simples
        2) Euler Inverso
        3) Euler aprimorado
        4) Runge-Kutta
        5) Adam-Bashforth
        6) Adam-Moulton
        7) Formula Inversa de Diferenciacao
    Obs: todos os metodos que envolvem um ponto implicito foram implementados sem o uso de previsao.

    Exemplo de comando no arquivo (vejo o arquivo entrada.txt para mais exemplos):
        euler 1 0 0.1 10 1-t+4*y
        adam_bashforth_by_euler 0 0 0.1 20 1-t+4*y 6

5 - Especificacao da saida:
    A saida consiste num arquivo (saida.txt) onde é gravado informações sobre cada metodo calculado:
        Qual o metodo
        Um ponto inicial dado
        O tamanho do passo
        o passo. e o ponto referente calculado
    Exemplo (para mais exemplos veja o arquivo saida.txt):
        Metodo de Euler Inverso
        y( 0.0 ) = 0.0
        h = 0.1
        1 0.150000000000000
        2 0.383333333333333
        3 0.755555555555556
        4 1.35925925925926
        5 2.34876543209877
