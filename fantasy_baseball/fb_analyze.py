import pandas as pd
import numpy as np

def fetch_data(position, min_proj_ab):
    """
    Imports a .csv file that is saved in the repository based on the position
    and minimum at-bats specified.

    Args:
        (str) position - name of position to be evaluated
        (int) min_proj_ab - number of minimum number of at-bats a player must
                             projected to achieve.

    Returns:
        df - Pandas DataFrame containing all players that meet the
                          minimum projected at-bats at specified position.
    """

    # Load data for specified position
    df = pd.read_csv('FantasyPros_2019_Projections_{}.csv'.format(position))

    # Filter dataframe to only include players that meet at-bat requirement
    df = df[df['AB'] >= min_proj_ab]

    return df

def calculate_value(df, categories):
    df['total_value'] = 0
    for category in categories:
        mean = np.mean(df['{}'.format(category)])
        stand_dev = np.std(df['{}'.format(category)])
        df['{}_value'.format(category)] = (df['{}'.format(category)] - mean) / stand_dev
        df['total_value'] += df['{}_value'.format(category)]
    return df

def main():
    position = '1B'
    min_proj_ab = 450

    # category options are AB,R,HR,RBI,SB,AVG,OBP,H,2B,3B,BB,SO,SLG,OPS 
    categories = ['R','HR','RBI','SB','OBP','SLG']
    df = fetch_data(position, min_proj_ab)
    df.head()


if __name__ == "__main__":
    main()
