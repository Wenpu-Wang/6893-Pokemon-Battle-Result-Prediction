from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
# our home page view
def home(request):
    return render(request, 'test.html')

res = ['none','none']
le = [1,1]
# custom method for generating predictions



def get_stats(name):
     stat = []
     u = "https://pokeapi.co/api/v2/pokemon/{}"
     response = requests.get(u.format(name))
     pokemon_info = json.loads(response.text)
     s = pokemon_info['stats']
     for i in range(6):
        stat.append(s[i]['base_stat'])
     return stat

def getPredictions(name1, name2):
    import pickle
    #model = pickle.load(open("titanic_survival_ml_model.sav", "rb"))
    #scaled = pickle.load(open("scaler.sav", "rb"))
    url = "https://pokeapi.co/api/v2/pokemon/{}"
    data = np.empty(12)
    data.astype(np.int64)
    for i in range(6):
        response = requests.get(url.format(name1))
        pokemon_info = json.loads(response.text)
        temp = pokemon_info['stats'][i]['base_stat']
        if i == 0:
            data[i] = (temp * 2 + 20)*le[0]/100 + 10 + le[0]
        else:
            data[i] = (temp * 2 + 20)*le[0]/100 + 5
    for i in range(6):
        response = requests.get(url.format(name2))
        pokemon_info = json.loads(response.text)
        temp = pokemon_info['stats'][i]['base_stat']
        if i == 0:
            data[i+6] = (temp * 2 + 20)*le[1]/100 + 10 + le[1]
        else:
            data[i+6] = (temp * 2 + 20)*le[1]/100 + 5
    model = pickle.load(open("/Users/ruilinfan/Desktop/Big_Data_Project/mysite/mysite/lr.sav", "rb"))
    pred = model.predict(data.reshape((1,12)))
    if pred == 0:
        winner = name1
    elif pred == 1:
        winner = name2
    return winner
def get_pic(name):
    u = "https://pokeapi.co/api/v2/pokemon/{}"
    response = requests.get(u.format(name))
    a = json.loads(response.text)['id']
    if a > 99:
        id = str(a)
    elif a < 10:
        id = '00' + str(a)
    else :
        id = '0' + str(a)
    url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/' + id
    url = url + '.png'
    return url

# our result page view
def result1(request):
    #pokemon2 = int(request.POST['pk2'])
    name = request.GET['pk1']
    le[0] = int(request.GET['level1'])
    name = name.lower()
    res[0] = name
    url = get_pic(name)
    if res[1] == 'none':
        return render(request, 'refresh.html', {'first_url':url,'first_poke_name': name.capitalize()})
    else:
        return render(request, 'refresh2.html', {'first_url':get_pic(res[0]), 'second_url':get_pic(res[1]),'first_poke_name': res[0].capitalize(),'second_poke_name':res[1].capitalize()})
    #return render(request, 'result.html', {'result':'result'})

def result2(request):

    name = request.GET['pk2']
    le[1] = int(request.GET['level2'])
    name = name.lower()
    res[1] = name

    url2 = get_pic(res[1])
    if res[0] == 'none':
        return render(request, 'refresh1.html', {'second_url':url2,'second_poke_name': name.capitalize()})
    #result = getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)
    else:
        return render(request, 'refresh2.html', {'first_url':get_pic(res[0]), 'second_url':url2,'first_poke_name': res[0].capitalize(),'second_poke_name':res[1].capitalize()})

def result(request):

    name1 = res[0]
    name2 = res[1]
    url1 = get_pic(res[0])
    url2 = get_pic(res[1])
    winner = getPredictions(name1,name2)

    return render(request, 'result.html', {'first_url':url1, 'second_url':url2,'first_poke_name': name1.capitalize(),'second_poke_name':name2.capitalize(),'winner':winner.capitalize()})

def reset(request):
    res[0] = 'none'
    res[1] = 'none'
    le[0] = 1
    le[1] = 1
    return render(request, 'test.html')