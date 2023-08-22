import numpy as np
from flask import Flask, request, render_template
import pickle

#create an app object using the Flask class
app = Flask(__name__)

#Load the train model(Pickle file)
model = pickle.load(open('models/model.pkl','rb'))

# Define the route to be home
# The decorator below links the relative route of the URL to the function it is decorating 
# Here, home function is with '/ ',our root directory
# Running the app sends us to index,html
# Note that render_template means it looks for the file in the templates folder

#use the route() decorator to tell Flask what URL should trigger our function
@app.route('/')#by default this will trigger when we hit the URL
def home():
    return render_template('index.html')

# this function was written to take data through file submitted
# @app.route('/predict',methods=['GET','POST'])
# def predict():                                    
#     file = request.files['file']
#     output=file.readlines()

#     return render_template("index.html",prediction_text="{}".format(output))

@app.route('/predict',methods=["GET","POST"])
def predict():
    # global output

    if request.method=="GET":
        return render_template('index.html')
    else:
        print(request.form.values())
        int_features = [float(x) for x in request.form.values()]
        features = np.array(int_features)
        x_reshaped_features=features[np.newaxis,:] #this line will add a new row vector, it converts to 2D
        prediction = model.predict(x_reshaped_features)

        if prediction == 0:
            output = 'Patient is having chronic kidney disease'
        else:
            output = 'Patient is not having chronic kidney disease'

    return render_template('index.html',prediction_text=output)
    

# Main function
if __name__=="__main__":
        app.run(debug=True)
    #this will automatically debug the code once you make any changes in it
    
