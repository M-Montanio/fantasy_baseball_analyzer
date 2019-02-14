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

def main():
    position = '1B'
    min_proj_ab = 450
    position_df = fetch_data(position, min_proj_ab)
    position_df.head()


if __name__ == "__main__":
    main()
