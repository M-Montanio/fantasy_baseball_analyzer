import pandas as pd
import numpy as np

def fetch_data(position, min_proj_ab, min_proj_starts_sp, min_proj_ip_rp):
    """
    Imports a .csv file that is saved in the repository based on the position
    and minimum at-bats specified.

    Args:
        (str) position - name of position to be evaluated
        (int) min_proj_ab, min_proj_starts_sp, min_proj_ip_rp - number of minimum
                            number of at-bats a player must projected to achieve.

    Returns:
        df - Pandas DataFrame containing all players that meet the
                          minimum projected at-bats at specified position.
        categoties - list of categories used to compute value at position.
    """

    # Load data for specified position
    df = pd.read_csv('FantasyPros_2019_Projections_{}.csv'.format(position))

    # Filter dataframe to only include players and categories that meet requirements
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
    """
    Imports dataframe with players, projected stats at a position, creates a
    player value for each category, and adds up values to create a total value.

    Args:
        (dataframe) df - dataframe containing all players/categories at position.
        (list) categories - list of categories used to calculate value

    Returns:
        df - Pandas DataFrame containing all players that meet the specified
             qualifications at specified position.
    """
    # Create column for total value
    df['total_value'] = 0

    # Loop through each category and create new columns for category values based
    # on projected stats and standard deviations from the mean.
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

    df = df.sort_values(by=['total_value'], ascending=False)

    return df

def main():

    # What position: 1B, 2B, 3B, SS, C, OF, SP, or RP?
    position = '1B'

    # How many players will be drafted at this position?
    num_drafted_at_pos = 50

    # For offensive players, what is the min at-bats required to qualify?
    min_proj_ab = 450

    # For sp's, what is the min starts a pitcher needs to qualify?
    min_proj_starts_sp = 28

    # For rp's, what is the min innings pitched needed to qualify?
    min_proj_ip_rp = 50

    df, categories = fetch_data(position, min_proj_ab, min_proj_starts_sp, min_proj_ip_rp)
    df = calculate_value(df, categories)
    if len(df) > num_drafted_at_pos:
        df = df.head(num_drafted_at_pos)
        df = calculate_value(df, categories)
    df.head()


if __name__ == "__main__":
    main()
