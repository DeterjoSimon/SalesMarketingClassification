# 2021AI

This is a technical case for my interview at 2021AI.

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
