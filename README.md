# skearn-twitter-metrics
A python program that collects data on posts from twitter, then creates a model on the data which can be used for predictions
# How To Use
1. Download the dependancies
2. Remove all the data in Train.csv except the first line if you wish
3. Run the collect.py for however long you want and stop when you have enough data (excel worksheet must be closed)
4. Run the train.py file with your required predicted value and labels
5. Using the best model run the test.py program to test your model and create graphs

# Examples

## collect.py
### Input
- The common names and words in the words.txt file
### Output
- The post data in the Train.csv file

## train.py
### Input
- The post data in the Train.csv file
### Output
- The best SAV model files with the accuracy in the name

## test.py
### Input
- The post data in the Train.csv file
- The chosen model
### Output
- The accuracy and mean error of the model with a range of graphs. Including a comparison between the predicted and actual value
![](https://github.com/James-Charles-Robinson/skearn-twitter-metrics/blob/master/retweet_predictions.png?raw=true)
![](https://github.com/James-Charles-Robinson/skearn-twitter-metrics/blob/master/likestoretweets.png?raw=true)
![](https://github.com/James-Charles-Robinson/skearn-twitter-metrics/blob/master/retweetstofollowers.png?raw=true)

# Limitations
1. Lots of collected data is dirty and doesnt follow the main trend because of different interaction levels depending on the type of post and account, leading to lots of annomlies in the data
2. Unfortunally there is no real trend between a posts interaction levels and the accounts followers
3. Data collection can be slow, taking about 2 hours for 1000 posts
4. Although the accuracy level for a model predicting for example retweets from likes and comments is high (around 95%), the mean error is around 1000, meaning predictions can be lackluster.

# What I Learnt
1. Further advaning my knowledge of webscraping and getting the needed data from the html of a website using selenium
2. Reading and writing from csv files
3. Using pyplot/matplotlib to create scatter graphs
4. Using pandas dataframes to store, manipulate and display data
5. Use sklearn linear regression to create models from data
6. Use sklearn models to make predictions
7. Use sklearn proprocessing to normalize my data
8. Save a model using pickle
9. Use numpy arrays

