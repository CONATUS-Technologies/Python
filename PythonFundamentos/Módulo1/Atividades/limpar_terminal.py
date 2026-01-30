import os # Importação do módulo 'os' para interação com o sistema operacional

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_terminal()

'''
    DEFINIÇÃO DA FUNÇÃO limpar_terminal()

    Esta função tem como objetivo limpar a tela do terminal/console,
    funcionando de maneira multiplataforma (Windows, Linux e macOS).

    A lógica implementada detecta automaticamente o sistema operacional
    em execução e seleciona o comando apropriado para limpeza:
    - Windows: utiliza o comando 'cls'
    - Linux/macOS: utiliza o comando 'clear'

    DETALHAMENTO DA IMPLEMENTAÇÃO
    
    os.system(): função do módulo os que permite executar comandos
    diretamente no terminal/shell do sistema operacional.
    
    Expressão condicional ternária:
    'cls' if os.name == 'nt' else 'clear'
    
    Esta expressão verifica:
    1. os.name == 'nt': testa se o sistema é Windows
    ('nt' vem de "New Technology", kernel do Windows)
    2. Se verdadeiro: retorna a string 'cls'
    3. Se falso: retorna a string 'clear'
    
    O comando escolhido é então passado para os.system() para execução.
        os.system('cls' if os.name == 'nt' else 'clear')
'''
