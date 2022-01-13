# 6893-Big Data Analytics: Pokémon Battle Result Prediction

## Contents

1. [Introduction](#introduction)
2. [Methodology](#methodology)
3. [Datasets](#datasets)
4. [Quick Start](#quick-start)
5. [Contact us](#contact-us)

## Introduction

Project of the course EECS-6893-Big Data Analytics, the goal of the project is to predict battle result of Pokémon, analyze the importance of using machine learning algorithms, and build a Web UI to visualize the prediction of Pokémon battle result.

## Methodology

Machine learning algorithms: KNN, LDA, Random Forest, SVM.

Web UI: HTML, JSON, CSS, Django, Python.

## Datasets

Stored in the algorithm_code folder for your convenience, see data descriptions in README.md under the same directory of datasets.

## Quick Start

The machine learning models code locates in the algorithm_code folder, the web UI code locates in the frontend_code folder. 

### algorithm_code folder

"plain_" prefix files: combine two Pokémons attributes into a vector as features, the actual input data structure into the model is:

```python
final_stats = ["HP1","Attack1","Defense1","Sp. Atk1","Sp. Def1","Speed1","Legendary1","HP2","Attack2",
                   "Defense2","Sp. Atk2","Sp. Def2","Speed2","Legendary2"]
temp_list.append((first.tolist()+second.tolist()))
```

"diff_" prefix files: use the difference of two Pokémons attributes as features, the actual input data structure into the model is:

```python
final_stats = ["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Legendary"]
temp_list.append(((first-second).tolist()))
```

To switch whether to consider Pokémons types, In preprocess() function, commenting these tow rows means not considering the Pokémons types: 

```python
first[1] = first[1] * adv_coefficient
first[3] = first[3] * adv_coefficient
```
### frontend_code folder

Run the command to start the server:

```
python manage.py runserver
```

An address should appear in your terminal, go to the address in your local machine's browser should take you to the web interface. There you can start playing around with the web app.

## Contact us

Wenpu Wang: ww2569@columbia.edu

Ruilin Fan: rf2756@columbia.edu

Zikai Zhu: zz2765@columbia.edu
