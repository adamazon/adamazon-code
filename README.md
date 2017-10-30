# Influencing factors of product's reviews

**Group:** Victor Le, Quentin de Longraye, Karttikeya Mangalam

## Abstract
Product's review are often in the middle of polemical situations, because of the
high subjectivity it could bring. The review can also be faked, exaggerated or unknowingly
influenced by others' opinion (see the [social proof](https://en.wikipedia.org/wiki/Social_proof)).
The purpose of this project is to understand the factors that influence online
reviews of products and to what degree. Exmaples of such factors are rating history for a single product, rating
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
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

- Amazon's review: http://jmcauley.ucsd.edu/data/amazon/
  - Using the cluster, we will extract the most evaluated products and some of the
    most productive evaluators to provide our analysis.
  - The dataset has ratings and reviews for a product with reviews both stars and textual. Moreover, many reviews have **meta-reviews** i.e. an estimate of the quality of the review, which can be used for training an automatic evaluator for the review to predict the **meta-review** score.
  - The product image is also available in most cases, which will be used to derive basic graphics features such as colour-contrast and presentation that can affect the product's ability to attract customers and therefore, sales. 
  - We would likely be using simple *Machine Learning* algorithms for finding patterns and checking the prediction-ability of the final score given the data.

## A list of internal milestones up until project milestone 2
We plan to have a clear cut pipeline for the project, and remove the all "can" and "could" to "would" and "would-not" and revies the data sields that are useful and how to enrich them. 

## Questions for TAa
Add here some questions you have for us, in general or project-specific.
