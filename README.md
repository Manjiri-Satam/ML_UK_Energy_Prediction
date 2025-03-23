# Machine Learning - UK Household Energy Consumption Prediction
This repository contains the code, documentation, and final report for our Machine Learning project (Spring 2024) on predicting UK household energy consumption. The project explores various modeling techniques to understand and forecast energy usage based on household-level data.

## Group Members: 
Manjiri Satam, Miriam Runde, Jackson Luckey, Aditya Narayan Rai

## Project Objective
To predict electricity consumption at the household level in the UK using statistical and machine learning models. The goal is to explore:
- Model performance across different aggregation levels (daily vs. monthly)
- The impact of temporal and household-level features
- Trade-offs between model complexity, interpretability, and performance

## Unit of Analysis:
Each row of our dataset is a smart-meter reading covering half an hour of electricity consumption. Each row includes the date-time of the reading, the number of kilowatt hours consumed, and geographic/demographic information (e.g. what part of the UK the meter is in, whether the meter is for a household or not).

## Folder Structure
- documentation/ :	Contains the project proposal, memo, and brief submitted to the professor
- src/ :	Main codebase for data cleaning, modeling, and evaluation
- src/data-prep/ :	Data wrangling, reshaping, and merging scripts
- src/ models/ :	All scripts and notebooks related to modeling and evaluation
- data/ :	(Not included here) Raw or processed data files — not pushed due to size/sensitivity
- UK_Energy_Prediction_Final.pdf	📄 Final report with methods, results, and discussion

