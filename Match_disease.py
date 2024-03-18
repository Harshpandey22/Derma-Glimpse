import json
with open(r'C:\Users\harsh\Desktop\Hackathon\EDD Nail\data\database.json', 'r') as file:
    data = json.load(file)

def disease_name(prediction):
    n = len(data)
    for i in range(n):
        d_name = data[i].get('disease_name')
        if prediction == d_name:
            return data[i]