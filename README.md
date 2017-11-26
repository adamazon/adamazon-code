# Investigating factors behind product reviews

## Milestone 2 

**Group:**  Karttikeya Mangalam, Victor Le, Quentin de Longraye

### Goals:

- We aim to build a regression model based on the review scores to automatically assign a predicted "helpfulness" rating to each comment. Moreover, we also aim to merge this rating with the actual human assigned value in a real system to re-arrange reviews in a more useful way hopefully.
- Using the above model or otherwise, we also aim to investigate the use of short summary of review and the role it plays along with the actual long review in determining the usefulness. For ex: A short comment like - *Requires in game purchases* can be pretty helpful with no actual long review and it would be interesting to see if we can quantify that. 

**Motivation** : 
The reason human scores themselves are not always very reliables is because even though the rating is supposed to be a measure of "helpfulness", people can still vote up a comment if it's not helpful but says something funny/creative/interesting. While, this sort of behavior is common and not looked down upon, it still deafeats the basic purpose of scoring reviews. <br>
Our proposed system can curb such behavior by assigning a low score to the comment. 

**Proposed Approach** : 
- We already wet our hands with TF-IDF clusteing to explore the review data on helpfulness. As expected, TF-IDF is unstable for such short document lengths (@Quentin : Can you comment on the document length distribution here? mean and std should be good). We propose t such more sophiticated word embeddings such as - [Star Space](https://github.com/facebookresearch/StarSpace) to capture text
- Once the embeddings are a god representation of text, we propose to cluster/regress over thr=e proposed features on an identified similar group of products in the same category as follows.
- The dataset has product metadata such as sub categories etc. We propose to induce a graph over the products with Gaussian distance as a metric for similarity and use a off the shelf classifier such as K- Nearest neighbour to identify a cluster that is sufficiently large in terms of number of product reviews starting from the most reviewed products. ( *PlayStation 500 GB* in *Video Games* etc.)

**Till Now : Exploratory and Descriptive Analysis*




## Milestone 1

## Abstract
Product's review are often polemical situations because of the
high level of subjectivity involved. Reviews can also be exaggerated even faked or unknowingly
influenced by others' opinion (see the [social proof](https://en.wikipedia.org/wiki/Social_proof)).
The purpose of this project is to understand the factors that influence online
reviews of products and to what degree. Examples of such factors are rating history for a single product, rating
history of an individual or metadata about the product itself, extracted
information about product's picture, such as its color and others. Based on these factors,
the objective is to investigate the reliability of an evaluation and to what extent can the evaluation's range be predicted.

## Research questions
- Which factors can influence an online product review? Both qualitatively and a rough quantative estimate. 
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

We will in a first part focus on data extraction, to be able to visualize the data early (using basic plots). 4 main resources will be extracted: products, reviews, reviewers and categories. This will allow us to learn how to work with Spark. This milestone includes also the data cleaning part, handling missing data for example. Then, we will start working on data matching, descriptive data analysis and visualization of matched data. It will be useful to understand how data is distributed and visualize disparity based on several parameters including: time, reviewers, categories, products, … and make relevant data groupments. Finally, we will search for insights based on the descriptive analysis to prepare the next milestone, by searching for correlations based on the raw data, and analyse how data will have to be analysed and transformed to get responses to our research questions.

## Questions for TA
- If such relevant studies have been carried out on either Amazon review dataset or other similar data pools, it would be great if we could be pointed to such resources.
