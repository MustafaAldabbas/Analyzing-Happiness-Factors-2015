# SQL-Happiness_indicators-2015
[presentation](https://docs.google.com/presentation/d/1aBNPlcYGfaX04Y_FsO-AF34vyIzdeIG6mFWgjNMbCrI/edit?usp=sharing)

# Analyzing Happiness Factors

## Project Overview

This project aims to analyze the factors that contribute to happiness across different countries using data from the World Happiness Report 2015. The primary goal is to identify key determinants of happiness and how they vary globally.

## Dataset

The dataset for this project is sourced from the World Happiness Report 2015 and includes data on:
- Economy (GDP per Capita)
- Family Support
- Health (Life Expectancy)
- Freedom
- Trust in Government (Corruption Levels)
- Generosity
- Happiness Scores and Ranks

## Business Problem

The primary business problem addressed in this project is understanding the key factors that significantly impact happiness across different countries. By identifying these factors, policymakers and organizations can implement strategies to improve overall happiness and well-being.

## Hypotheses

1. Higher GDP per capita leads to higher happiness scores.
2. Better health conditions (life expectancy) are positively correlated with happiness.
3. Countries with higher freedom scores have higher happiness ranks.
4. Trust in government and lower corruption levels positively affect happiness.
5. Stronger family support correlates with higher happiness.
6. Generosity levels contribute positively to happiness.

## Data Acquisition and Processing

- **Data Sources**: The primary data source is Kaggle.
- **Data Cleaning**: Cleaning and preprocessing the data to ensure accuracy and consistency.
- **Database Creation**: 
  - Creating the database and its structure.
  - Designing an Entity-Relationship Diagram (ERD).
- **Data Upload**: Uploading the cleaned data to the database.
- **Data Integration**: Merging various datasets on the 'Country' column.
- **Query Writing**: Writing SQL queries to ensure consistency and alignment across sources.
- **Python Integration**: Connecting Python with MySQL for data analysis and visualization.

## Database Design & Data Transformation

The database design includes the following tables and relationships:
- **Country** (Primary Key)
- **Happiness Rank**
- **Happiness Score**
- **Economy (GDP per Capita)**
- **Family Support**
- **Health (Life Expectancy)**
- **Freedom**
- **Trust (Government Corruption)**
- **Generosity**

## Visualizations

The project includes various visualizations to present the data and test the hypotheses:
- Data Overview
- Hypotheses Testing
- Correlation Matrix

## Correlation Analysis

The analysis reveals:
- **Strong Positive Correlations**: GDP per capita, family support, and life expectancy have the strongest positive correlations with happiness scores.
- **Moderate Positive Correlations**: Freedom and trust in government show moderate positive correlations.
- **Weak Positive Correlations**: Generosity has a weaker positive correlation with happiness.
- **Negative Correlation**: The negative correlation between happiness rank and happiness score indicates that better ranks (lower numbers) are associated with higher happiness scores.

## Conclusion

The analysis highlights that economic stability, social support, and health are the strongest predictors of happiness. These findings emphasize the importance of these factors in improving national well-being.

## Author

Mustafa Aldabbas

## Acknowledgments

- World Happiness Report
- Kaggle for providing the dataset
