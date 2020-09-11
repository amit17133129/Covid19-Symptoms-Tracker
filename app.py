from flask import Flask, render_template, redirect, url_for, request
# import pickle
# from keras.preprocessing.sequence import pad_sequences
import numpy as np
from keras.models import model_from_json
from keras import backend as K


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    K.clear_session()
    category = None
    if request.method == 'POST':
        if request.form['que1']:
            json_file = open('model_scientific.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            # load weights into new model
            loaded_model.load_weights("model_scientific.h5")
            print("Loaded model from disk")

            name = str(request.form['name'])
            email = str(request.form['email'])

            #Age processed
            age = int(request.form['age'])
            age_list = []
            for i in range(10,100,10):
                if age >= i and age < i+10:
                    age_list.append(1)
                else :
                    age_list.append(0)

            
            
            gender = int(request.form['gender'])
            que1 = int(request.form['que1'])
            que2 = int(request.form.get('que2'))
            

            #que3 processed
            que3 = str(request.form.get('que3'))
            que3 = que3.split(",")
            for i in range(len(que3)):
                 que3[i] = int(que3[i])

            #que4 processed
            que4 = str(request.form.get('que4'))
            que4 = que4.split(",")
            for i in range(len(que4)):
                 que4[i] = int(que4[i])

            #que5 processed
            que5 = str(request.form.get('que5'))
            que5 = que5.split(",")
            for i in range(len(que5)):
                 que5[i] = int(que5[i])

            #que6 processed
            que6 = str(request.form.get('que6'))
            que6 = que6.split(",")
            for i in range(len(que6)):
                 que6[i] = int(que6[i])


            que7 = int(request.form.get('que7'))
            que8 = int(request.form.get('que8'))
            que9 = int(request.form.get('que9'))
            que10 = int(request.form.get('que10'))
            que11 = int(request.form.get('que11'))
            que12 = int(request.form.get('que12'))
            que13 = int(request.form.get('que13'))
            que14 = int(request.form.get('que14'))
            que15 = int(request.form.get('que15'))
            que16 = int(request.form.get('que16'))
            que17 = int(request.form.get('que17'))
            que18 = int(request.form.get('que18'))
            que19 = int(request.form.get('que19'))
            que20 = int(request.form.get('que20'))
    
            #que21 processed
            que21 = str(request.form.get('que21'))
            que21 = que21.split(",")
            for i in range(len(que21)):
                 que21[i] = int(que21[i])
                 
            que22 = int(request.form.get('que22'))
            que23 = int(request.form.get('que23'))
            que24 = int(request.form.get('que24'))
            que25 = int(request.form.get('que25'))

            
            #que26 processed
            que26 = str(request.form.get('que26'))
            que26 = que26.split(",")
            for i in range(len(que26)):
                 que26[i] = int(que26[i])


            que27 = int(request.form.get('que27'))


            #que28 processed
            que28 = str(request.form.get('que28'))
            que28 = que28.split(",")
            for i in range(len(que28)):
                 que28[i] = int(que28[i])


            #que29 processed
            que29 = str(request.form.get('que29'))
            que29 = que29.split(",")
            for i in range(len(que29)):
                 que29[i] = int(que29[i])


            to_predict=[]
            to_predict.extend(age_list)
            to_predict.extend([que1, que2])
            to_predict.extend(que3)
            to_predict.extend(que4)
            to_predict.extend(que5)
            to_predict.extend(que6)
            to_predict.extend([que7,que8,que9,que10,que11,que12,que13,que14,que15,que16,que17,que18,que19,que20])
            to_predict.extend(que21)
            to_predict.extend([que22,que23,que24,que25])
            to_predict.extend(que26)
            to_predict.extend([que27])
            to_predict.extend(que28)
            to_predict.extend(que29)


            to_predict = np.array([to_predict])
            # to_predict = np.array([[que1,que2,que3,que4,que5,que6,que7,que8,que9,que10,
            # que11,que12,que13,que14,que15,que16,que17,que18,que19,que20,
            # que21,que22,que23,que24,que25,que26,que27,que28,que29,que30,
            # que31,que32,que33,que34,que35,
            # ]])  
            pred = loaded_model.predict(to_predict)
            print(pred[0])
            labels= ['Low Risk', 'High Risk', 'Not Confirm']
            category = labels[np.argmax(pred[0])]
            print(category)
            category = category

        else:
            category = "Enter Data"
    return render_template('home.html', category=category)






@app.route('/general', methods=['GET', 'POST'])
def general():
    K.clear_session()
    category = None
    if request.method == 'POST':
        if request.form['que1']:
            json_file_general = open('model_general.json', 'r')
            loaded_model_json_general = json_file_general.read()
            json_file_general.close()
            loaded_model_general = model_from_json(loaded_model_json_general)
            # load weights into new model
            loaded_model_general.load_weights("model_general.h5")
            print("Loaded model from disk")

            name = str(request.form['que1'])
            email = str(request.form.get('que2'))

            age = int(request.form.get('que3'))
            age_list = []
            for i in range(10,100,10):
                if age >= i and age < i+10:
                    age_list.append(1)
                else :
                    age_list.append(0)


            gender = int(request.form.get('que4'))

            fever = str(request.form.get('que5'))
            fever = fever.split(",")

            for i in range(len(fever)):
                 fever[i] = int(fever[i])


            dry_cough = int(request.form.get('que6'))
            sore_throat = int(request.form.get('que7'))
            weaknes = int(request.form.get('que8'))
            breathing_problem = int(request.form.get('que9'))
            drowsiness = int(request.form.get('que10'))
            chest_pain = int(request.form.get('que11'))
            loss_sense_smell = int(request.form.get('que12'))
            appetide_change = int(request.form.get('que13'))
            progressed = int(request.form.get('que14'))
            kidney_disease = int(request.form.get('que15'))
            heart_disease = int(request.form.get('que16'))
            lung_disease = int(request.form.get('que17'))
            diabetes = int(request.form.get('que18'))
            high_blood_pressure = int(request.form.get('que19'))
            stroke = int(request.form.get('que20'))
            travel_history = int(request.form.get('que21'))

            data = [gender, dry_cough, sore_throat, weaknes, breathing_problem, drowsiness, 
            chest_pain, travel_history, diabetes, heart_disease, lung_disease, stroke, 
            progressed, high_blood_pressure, kidney_disease, appetide_change, loss_sense_smell]

            data.extend(age_list)
            data.extend(fever)



            pred = loaded_model_general.predict([[data]])

            pred = list(pred[0]) #converted from a 2D array with one row only to a 1D list 

            pred = pred.index(max(pred))
            labels= ['No Risk', 'Medium Risk', 'High Risk']
            category = labels[np.argmax(pred)]

        else:
            category = "Enter Data"

    return render_template('general.html', category=category)



if __name__ == '__main__':
    app.run(debug = True)
