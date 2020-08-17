# NLProject
This repo contains some coding to test Natural Language Processing in the communications released by Banco Central do Brasil.
The purpose is to detect sentiment from the Copom's minutes, in order to check if the BCB is trying to express negative or positive feeling regarding the brazilian economy.

# Data
All PDF files from Copom meetings, since 2016.

# Predictions
I have used a labeled database from data.world, with economic news classified according to the text sentiment.Then I used a logistic regression to build the machine learning algorithm, and updated the weights and added vocabulary to make the algorithm more specific for BCB communications.

