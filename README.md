# 6893-Big Data Analytics: Pokémon Battle Result Prediction

## Introduction

Project of the course EECS-6893-Big Data Analytics, the goal of the project is to predict battle result of Pokémon, using machine learning algorithms, and build a web UI to predict Pokémon battle result. 

The machine learning models code locate in the algorithm_code folder, the web UI code locate in the frontend_code folder.

## Methodology

Machine learning algorithms: KNN, LDA, Random Forest, SVM.

Web UI: HTML, JSON, CSS, Django, Python.

## Datasets

Stored in the algorithm_code folder, see data descriptions in README.md under the same directory of datasets.

## About Training Models

### Jupyter notebook files Naming and corresponding Code

differences of two kinds of files locate in: final_stats, list append (both in preprocess() function)

1. "plain_" prefix files，combine two Pokémons attributes into a vector as features, the actual input data structure into the model is:

   ```python
   final_stats = ["HP1","Attack1","Defense1","Sp. Atk1","Sp. Def1","Speed1","Legendary1","HP2","Attack2",
                      "Defense2","Sp. Atk2","Sp. Def2","Speed2","Legendary2"]
   ```

   another difference: temp_list.append((first.tolist()+second.tolist()))

2. "diff_" prefix files, use the difference of two Pokémons attributes as features, the actual input data structure into the model is:

   ```python
   final_stats = ["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Legendary"]
   ```

   another difference: temp_list.append(((first-second).tolist()))

### Switching whether to consider Pokémons types

4 situations in total: consider/ not consider Pokémons types，take difference of Pokémons attributes/combine Pokémons attributes into a vector , combining these two options so there are 2 x 2 situations. 

We use Cross Validation to find best parameters, then test with test data, to find the best model.

In preprocess() function, commenting these tow rows means not considering the Pokémons types: 

```python
        first[1] = first[1] * adv_coefficient
        first[3] = first[3] * adv_coefficient
```
