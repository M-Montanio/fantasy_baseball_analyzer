import pandas as pd
import numpy as np

def fetch_data(position, min_proj_ab, min_proj_starts_sp, min_proj_ip_rp):
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

    # Filter dataframe to only include players that meet requirements
    if position == 'SP':
        df = df[df['GS'] >= min_proj_starts_sp]
        df['K/BB'] = df['K']/df['BB']
        categories = ['ERA', 'WHIP', 'K', 'QS', 'K/BB']
    elif position == 'RP':
        df = df[df['IP'] >= min_proj_ip_rp]
        df['K/BB'] = df['K']/df['BB']
        categories = ['ERA', 'WHIP', 'K', 'K/BB', 'SV']
    else:
        df = df[df['AB'] >= min_proj_ab]
        categories = ['R','HR','RBI','SB','OBP','SLG']

    return df, categories

def calculate_value(df, categories):
    df['total_value'] = 0
    for category in categories:
        if category == 'ERA' or category == 'WHIP':
            mean = np.mean(df['{}'.format(category)])
            stand_dev = np.std(df['{}'.format(category)])
            df['{}_value'.format(category)] = ((mean - df['{}'.format(category)]) / stand_dev)
            df['total_value'] += df['{}_value'.format(category)]
        else:
            mean = np.mean(df['{}'.format(category)])
            stand_dev = np.std(df['{}'.format(category)])
            df['{}_value'.format(category)] = (df['{}'.format(category)] - mean) / stand_dev
            df['total_value'] += df['{}_value'.format(category)]

    return df

def main():
    position = '1B'
    min_proj_ab = 450
    min_proj_starts_sp = 28
    min_proj_ip_rp = 50

    df, categories = fetch_data(position, min_proj_ab, min_proj_starts_sp, min_proj_ip_rp)
    df = calculate_value(df, categories)
    df.head()


if __name__ == "__main__":
    main()
