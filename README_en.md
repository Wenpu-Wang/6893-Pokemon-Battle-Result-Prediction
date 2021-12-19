# Pokémon Project 6893

## .ipynb Naming and Code corresponding

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

## Switching whether to consider Pokémons types

4 situations in total: consider/ not consider Pokémons types，take difference of Pokémons attributes/combine Pokémons attributes into a vector , combining these two options so there are 2$\times$2 situations. 

We use Cross Validation to find best parameters, then test with test data, to find the best model.

In preprocess() function, commenting these tow rows means not considering the Pokémons types: 

```python
        first[1] = first[1] * adv_coefficient
        first[3] = first[3] * adv_coefficient
```
