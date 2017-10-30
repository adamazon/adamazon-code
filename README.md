# Influencing factors of product's reviews

**Group:** Victor Le, Quentin de Longraye, Karttikeya Mangalam

## Abstract
Product's review are often in the middle of polemical situations, because of the
high subjectivity it could bring. The review can also be faked, exaggerated or unknowingly
influenced by others' opinion (see the [social proof](https://en.wikipedia.org/wiki/Social_proof)).
The purpose of this project is to understand the factors that influence online
reviews of products and to what degree. Examples of such factors are rating history for a single product, rating
history of an individual or metadata about the product itself, extracted
information about product's picture, such as its color and others. Based on these factors,
the objective is to investigate the reliability of an evaluation and to what extent can the evaluation's range be predicted.

## Research questions
- Which factors can influence an online product review?
- Can a review's score be predicted based on product metadata and reviews?
- Can subjectivity of an evaluation be outlined from other's evaluations and
  product category?
- Can the review score of an evaluator for a specific product be
  anticipated, based on the product and its review history?

## Dataset
- Amazon's review: http://jmcauley.ucsd.edu/data/amazon/
  - Using the cluster, we will extract the most evaluated products and some of the
    most productive evaluators to provide our analysis.
  - The dataset has ratings and reviews for a product with reviews both stars and textual. Moreover, many reviews have **meta-reviews** i.e. an estimate of the quality of the review, which can be used for training an automatic evaluator for the review to predict the **meta-review** score.
  - The product image is also available in most cases, which will be used to derive basic graphics features such as colour-contrast and presentation that can affect the product's ability to attract customers and therefore, sales.
  - We would likely be using simple *Machine Learning* algorithms for finding patterns and checking the prediction-ability of the final score given the data.

## A list of internal milestones up until project milestone 2
![Gantt diagram](https://github.com/Coac/epfl-ada/raw/master/Project/gantt.png)

We will in a first part focus on data extraction, to be able to visualize the data early (using basic plots). 4 main resources will be extracted: products, reviews, reviewers and categories. This will allow us to learn how to work with Spark. This milestone includes also the data cleaning part, handling the missing datas for example. Then, we will start working on data matching, descriptive data analysis and visualization of matched data. It will be useful to understand how data is distributed and visualize disparity based on several parameters including: time, reviewers, categories, products, … and make relevant data groupments. Finally, we will search for insight based on the descriptive analysis to prepare the next milestone, by searching for correlations based on the raw data, and analyse how data will have to be analysed and transformed to get responses to our research questions.

## Questions for TAa
No question so far.
