#simple model from sklearn to send data to 

# random forest for making predictions for regression
import logging
import traceback
from datetime import datetime, timedelta, date
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor



def ai_test(data_points : list):
    """
    send the data to the model
    example
    [-0.89483109,-1.0670149,-0.25448694]
    """
    logging.info("(AWC) endpoint ai_test -Started-  :"+ str(datetime.now()))
    
    #set the total score
    try:   
        # define dataset
        X, y = make_regression(n_samples=1000, n_features=3, n_informative=3, noise=0.1, random_state=2)
        # define the model
        model = RandomForestRegressor()

        # fit the model on the whole dataset
        model.fit(X, y)

        # make a single prediction
        #row = [[-0.89483109,-1.0670149,-0.25448694]]
        row = [data_points]
        yhat = model.predict(row)
        result = {'Prediction ': yhat[0]}
        return result


    except Exception as e:
        traceback.print_exc()
        logging.error("(AWC) endpoint risk_score -Error-  :"+ str(e))
        return None


#print (ai_test([0.4,-1.0,6.25448694]))