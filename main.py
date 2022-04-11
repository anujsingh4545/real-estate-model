from flask import Flask , request
import pickle
import pandas as pd
import sklearn as sd


Andhrap = pickle.load(open('Andhra.pkl', 'rb'))
Arunachalp = pickle.load(open('Arunachal.pkl', 'rb'))
Assamp = pickle.load(open('Assam.pkl', 'rb'))
Bengalp = pickle.load(open('Bengal.pkl', 'rb'))
Biharp = pickle.load(open('Bihar.pkl', 'rb'))
Chattisgarhp = pickle.load(open('chhatisgarh.pkl', 'rb'))
Goap = pickle.load(open('Goa.pkl', 'rb'))
Gujratp = pickle.load(open('Gujrat.pkl', 'rb'))
Haryanap = pickle.load(open('Haryana.pkl', 'rb'))
Jharkhandp = pickle.load(open('Jharkhand.pkl', 'rb'))
Karnatkap = pickle.load(open('Karnataka.pkl', 'rb'))
Kerelap = pickle.load(open('Kerela.pkl', 'rb'))
Madhyap = pickle.load(open('Madhya.pkl', 'rb'))
Maharashtrap = pickle.load(open('Maharashtra.pkl', 'rb'))
Manipurp = pickle.load(open('Manipur.pkl', 'rb'))
Meghalayap = pickle.load(open('Meghalaya.pkl', 'rb'))
Mizoramp = pickle.load(open('Mizoram.pkl', 'rb'))
Nagalandp = pickle.load(open('Nagaland.pkl', 'rb'))
Orissap = pickle.load(open('Orissa.pkl', 'rb'))
Punjabp = pickle.load(open('Punjab.pkl', 'rb'))
Rajasthanp = pickle.load(open('Rajasthan.pkl', 'rb'))
Sikkimp = pickle.load(open('Sikkim.pkl', 'rb'))
Tamilp = pickle.load(open('Tamil.pkl', 'rb'))
Telanganap = pickle.load(open('Telangana.pkl', 'rb'))
Tripurap = pickle.load(open('Tripura.pkl', 'rb'))
Upp = pickle.load(open('UP.pkl', 'rb'))
Uttrakhandp = pickle.load(open('Uttrakhand.pkl', 'rb'))


app = Flask(__name__)
@app.route("/")
def hello():
    return   "Hello world"


@app.route("/Andhra", methods=["POST"])
def Andhra():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Andhrap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Arunachal", methods=["POST"])
def Arunachal():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Arunachalp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Assam", methods=["POST"])
def Assam():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Assamp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Bengal", methods=["POST"])
def Bengal():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Bengalp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Bihar", methods=["POST"])
def Bihar():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Biharp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Chhatisgarh", methods=["POST"])
def Chhatisgarh():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Chattisgarhp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Goa", methods=["POST"])
def Goa():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Goap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Gujrat", methods=["POST"])
def Gujrat():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Gujratp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Haryana", methods=["POST"])
def Haryana():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Haryanap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)

@app.route("/Jharkhand", methods=["POST"])
def Jharkhand():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Jharkhandp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)


@app.route("/Karnatka", methods=["POST"])
def Karnatka():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Karnatkap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)  

@app.route("/Kerela", methods=["POST"])
def Kerela():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Kerelap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)  


@app.route("/Madhya", methods=["POST"])
def Madhya():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Madhyap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)   


@app.route("/Maharashtra", methods=["POST"])
def Maharashtra():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Maharashtrap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results) 


@app.route("/Manipur", methods=["POST"])
def Manipur():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Manipurp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results) 


@app.route("/Meghalaya", methods=["POST"])
def Meghalaya():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Meghalayap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)


@app.route("/Mizoram", methods=["POST"])
def Mizoram():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Mizoramp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)   


@app.route("/Nagaland", methods=["POST"])
def Nagaland():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Nagalandp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)  


@app.route("/Orissa", methods=["POST"])
def Orissa():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Orissap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results) 


@app.route("/Punjab", methods=["POST"])
def Punjab():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Punjabp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)


@app.route("/Rajasthan", methods=["POST"])
def Rajasthan():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Rajasthanp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results) 


@app.route("/Sikkim", methods=["POST"])
def Sikkim():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Sikkimp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)


@app.route("/Tamil", methods=["POST"])
def Tamil():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Tamilp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results) 


@app.route("/Telangana", methods=["POST"])
def Telangana():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Telanganap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results)  


@app.route("/Tripura", methods=["POST"])
def Tripura():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Tripurap.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results) 

@app.route("/UttarPardesh", methods=["POST"])
def UttarPardesh():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Upp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results) 


@app.route("/Uttrakhand", methods=["POST"])
def Uttrakhand():
    if request.is_json:

        req = request.get_json()
        area = req['area']
        bhk = req['bhk']
        bathroom = req['bathroom']
        balcony = req['balcony']
        parking = req['parking']
        furnishing = req['furnishing']
        results = Uttrakhandp.predict([[area,bhk,bathroom,balcony,parking,furnishing]])
        return   str(results) 


      

if __name__ ==  "__main__":
    app.run(debug=True)