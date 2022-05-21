# Final-project: NBA Predictions

### Why we selected topic:

Interest in sports betting is growing and using machine learning to predict the results of games will help in sports betting. 
Our goal is to achieve an accuracy score of higher than 50%.

### Source of data:

- [nba-games from Kaggle by wyattowalsh](https://www.kaggle.com/wyattowalsh/basketball)
- [nba-games from Kaggle by nathanlauga](https://www.kaggle.com/nathanlauga/nba-games)
- fantasyData
- espn
- cbs sports
- fangraphs

###  Questions we hope to answer with the data:

- Predict outcomes of games
- Analyze why scores are higher than others
- Analyze players and teams comparing different features(injury, weather,home vs away, etc)
- Compare to actual sport betting (fanduel)

## Communication Protocols

- Team slack channel primary text and update communications
- Team Discord Server (Zoom kept kicking us out)
- Meeting at 7 pm Monday-Thursday

## Project Overview: 

- First step was to aquire the data by scraping from kaggle, fantasyData, fangraphs, and sports networks such as espn and cbs.
- The next step was to utilize SQL to create tables with the data to help with the EDA and model building processes

### Exporatory Data Analysis:

- Alex, can you please send me a link to a tableau public version of your graphs so I can use snips of them.

### The Model:

- The model building process began with using the csv files exported by the sql databases.
- The first part was creating a usable dataframe
- [insert picture of before and after of the dataframes to show the seasonalization of the data]
- The use of the loc function was used to breakdown each season into its own dataframe and fed into a list of dataframes.
- Each dataframe was fed through a function tasked with processing them to aquire season averages for features such as 2 or 3 pointer shot averages to average number of rebounds or assists throughout the season.
- A sum of games won was also made from the different frames however this is going to be the target for the linear regression model and the OLS model
- The function split the games into home and away games using the data to accumulate data for everygame throughout the season.
- After getting the dataframes processed they were merged into a unified dataframe broken up by each season.
- A dataframe was made from a csv file containing the seasonal attendance of each season for the teams.
- the 2 frames were organized by team and year so they would align allowing for an easy merge into a unified dataframe.
- The dataframes were fed into a linear regression model and OLS model to predict the number of wins a team would get per season.

![image](https://user-images.githubusercontent.com/71575748/169635542-7759190c-11d1-4faf-b3fa-5ee74017aadf.png)

- The OLS model showed more promise with a higher amount of error it could explain.
- Due to the overlining of metrics such as the average accuracy of 3 pointers and 2 pointers the model has issues with multicolinearity
- This is because a team that can hit 3s consitantly will be able to hit 2s and field goals often.
- However, dropping the 2 column has a strong adverse effect, and doesn't cause an estimator to have a incorrect sign.
- 
