## Project 2-2 : Email Spam Classification with Sentiment Analysis

# Description:
Email classification remains a critical challenge in modern information systems, particularly in managing the influx of spam emails that inundate user inboxes on a daily basis. While traditional approaches to spam detection have proven effective to some extent, they often struggle to adapt to the evolving tactics employed by spammers. The current spam detection algorithms are effective, but they could be further improved by integrating sentiment analysis to assess its influence on existing email spam detection techniques. Sentiment analysis, which involves evaluating the emotional tone and subjective information within text, is generally used to gauge public opinion, monitor brand reputation, and analyze customer feedback.

Therefore, this project is about the task of classifying an email of classifying an email as either spam or not spam, using Support Vector Machines and Naive Bayes as our main classifiers. On top of these, we'll employ Sentiment Analysis to check wether this improves or not the overall detection.

The dataset used for this project is the 'Spambase' dataset from the UCI Machine Learning Repository. The dataset contains a total of 4601 emails, of which 1813 are spam emails and the rest are non-spam emails.

The project uses the Naive Bayes classifier and Support Vector Machines to classify the emails. In phase 3, our models will also use sentiment analysis to improve the accuracy of the classification.

# To run the code:

Access and run `web_server/app.py` to start the gateway server for our JavaFX application and then go to `GUI_java/src/App.java` and run the java file. From this point, our application will start and you will be able to test our service.

NOTE : JavaFX is required in order to be able to run our app. Make sure to have it's library installed before running our code.
