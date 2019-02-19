# fantasy_baseball_analyzer

I created this program to analyze fantasy baseball players for an upcoming draft. I am using projections from <https://www.fantasypros.com/>. It is meant to analyze player value at each position only against other players that will be drafted.
The user can adjust several variables, including minumum number of projected at bats/innings pitched/quality starts and the number of players that are anticipated to be drafted at each position for the entire draft. Based on this information, it will return a the standard deviation from the mean for each scoring category for eligible drafted players. I also included a column that adds all of the standard deviations to give an overall player value.  

In addition to the variables stated, you can easily change the scoring categories and the website where you can get the projections in the 'fetch_data' function.
