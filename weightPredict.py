import pickle

def weigthPredict(height):
    model = pickle.load(open ('model.pkl','rb'))
    weight = model.predict(height)
    print(weight[0])
    weightinKg = lb_to_kg(weight[0])
    return weightinKg

def lb_to_kg(pounds):
    kilograms = pounds * 0.45359237
    return kilograms


