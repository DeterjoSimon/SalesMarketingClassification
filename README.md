# Business Technical Case

This is a technical case project I choose to embark in to test my ML techniques in 7hrs.

A bank has collected a large dataset of marketing data from their users. This dataset contains both continuous and categorical features which need to be considered. My task as a data scientist is to analyse the data and build a relevant model to predict if a customer would be willing to subscribe to additional products from the bank. 

This problem was tackled in a supervised learning manner. I first analysed the data and got a sense of what the feature domain was about. This led me after to start the ML development process. 
I.e. Various pre-processing techniques were tested and implemented, combined with a suitable ML model. Finally the model was trained and then evaluated in order to yield its performance. 

Afterwards, model weights and prediction outcomes were studied to get an idea of how the model interpreted the data and what could be improved upon. Due to time constraints, I did not dwell on hyperparameter fine-tuning - I proceeded to deploy my model as an interactive endpoint. Building a quick and easy FastAPI, I deployed the model and its endpoints to a docker container. This latter was then published and monitored through a simple Heroku server.  

## How to deploy the API

### Develop and save the model

Open the notebook and choose the model you wish to use, either the baseline logistic regression or the gradient boosting:
Access the [notebook](MarketClassifier.ipynb).

### Create Docker Container

```
docker build -t sub-class-app
docker run -p 80:80 sub-class-app
```

Your module is now being deployed on a docker and can be tested through Postman.

### Deploy the project on Heroku

```
heroku login
heroku create sub-class-app
heroku git:remote sub-class-app
heroku stack:set container
git push heroku main #taking into account you have a git repo
```

The server is now deployed on heroku and can be interacted with Postman.

## Results

|   Model   | Logistic Regression | Gradient Boosting | Gradient Boosting PCA |
| :-------: | :-----------------: | :---------------: | :-------------------: |
| F1-score  |         0.5         |     **0.59**      |         0.57          |
|  Recall   |        0.41         |     **0.54**      |         0.51          |
| Precision |        0.66         |     **0.66**      |         0.64          |
