# Pokémon Project

## .ipynb命名及其代码对应内容

两种文件差别在于两处，final_stats，和list append处，都在preprocess()函数内

1. plain_ 前缀的文件，使用两个宝可梦数值左右拼合为一个向量的形式，实际输入到模型的数据结构顺序为：

   ```python
   final_stats = ["HP1","Attack1","Defense1","Sp. Atk1","Sp. Def1","Speed1","Legendary1","HP2","Attack2",
                      "Defense2","Sp. Atk2","Sp. Def2","Speed2","Legendary2"]
   ```

   这行代码也不同：temp_list.append((first.tolist()+second.tolist()))，拼合

2. diff_前缀的文件，使用两个宝可梦数值做差的形式，实际输入到模型的数据结构顺序为：

   ```python
   final_stats = ["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Legendary"]
   ```

   这行代码也不同：temp_list.append(((first-second).tolist()))，做差

## TODO

共四种情况：考虑/不考虑宝可梦属性，宝可梦数值做差/不做差 互相组合，Cross Validation, 用最好的参数来算test error，最后得出最佳的是哪一种方法

1. TODO: 添加模型保存与读取功能，**具体在**模型训练那部分下面注释里

2. TODO: 在考虑/不考虑宝可梦属性的情况下，得到KNN，LDA，RF，SVM的准确率与保存模型，注释掉两行即可切换

   preprocess() 函数中，此两行**注释掉**就是**不考虑**宝可梦属性的模型，不进行补正

   ```python
           first[1] = first[1] * adv_coefficient
           first[3] = first[3] * adv_coefficient
   ```

3. TODO: 宝可梦数值做差/不做差情况下，得到KNN，LDA，RF，SVM的准确率与保存模型，不同前缀文件对应数值是否做差

