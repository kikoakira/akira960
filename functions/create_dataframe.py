import pandas as pd
import numpy as np 

def create_dataframe_example(
    size: int = 20, 
    seed: int = 42
) -> pd.DataFrame:
    """
    Gera um DataFrame de exemplo com nomes, notas de duas provas e turnos.

    Parâmetros:
    -----------
    size : int, opcional
        O número de linhas no DataFrame gerado. O padrão é 20.
    
    seed : int, opcional
        Semente para o gerador de números aleatórios para garantir 
        a reprodutibilidade dos resultados. O padrão é 42.

    Retorna:
    --------
    pd.DataFrame
        Um DataFrame contendo colunas com nomes, notas de duas provas e turnos. 
        As colunas geradas são:
        - 'Nome': Um nome aleatório escolhido a partir de uma lista de nomes.
        - 'Nota_1 Prova': Notas aleatórias inteiras entre 50 e 100 para a primeira prova.
        - 'Nota_2 Prova': Notas aleatórias inteiras entre 50 e 100 para a segunda prova.
        - 'Turno': Turnos aleatórios (Manhã, Tarde, Noite).
    
    Exemplo de uso:
    ---------------
    >>> df = create_dataframe_example(size=10, seed=0)
    >>> print(df)
    """
    
    # Gerando dados de exemplo
    np.random.seed(seed)  # Para reprodutibilidade

    nomes = ['Alice', 'Bruno', 'Carla', 'Diego', 'Eva', 'Felipe', 'Gabi', 'Hugo', 'Iara', 'Jorge', 
            'Karen', 'Luis', 'Marina', 'Nina', 'Otávio', 'Paula', 'Quico', 'Rafa', 'Silvia', 'Thiago']
    nomes = nomes[:size]
    
    nomes = np.random.choice(nomes, size=size)
    nota1 = np.random.randint(50, 100, size=size)
    nota2 = np.random.randint(50, 100, size=size)
    turno = np.random.choice(['Manhã', 'Tarde', 'Noite'], size=size)

    # Criando DataFrame
    df = pd.DataFrame({
        'Nome': nomes,
        'Nota_1 Prova': nota1,
        'Nota_2 Prova': nota2,
        'Turno': turno
    })

    return df
