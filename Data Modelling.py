import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from DataExploration import dur,ts
import warnings
def arima_model(X,arima_order):
    size = int(len(X) * 0.90)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = []
    for i in range(len(test)):
        model = ARIMA(history,order=arima_order)
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        predictions.append(output[0])
        history.append(test[i])
    #print('predicted=%f, expected=%f' % (output[0], test[i]))
    error = mean_squared_error(test, predictions)
    return error

def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p,d,q)
                print(order)
                mse = arima_model(dataset, order)
                print(mse,order)
                if mse < best_score:
                    best_score, best_cfg = mse, order
                print('ARIMA%s MSE=%.3f' % (order,mse))
    print('Best ARIMA%s MSE=%.3f' % (best_cfg, best_score))

data = pd.Series(dur)
p_values = [0, 1, 2, 4, 6, 8, 10]
d_values = range(0, 3)
q_values = range(0, 3)
warnings.filterwarnings("ignore")
error = arima_model(data,(1,1,0))
#evaluate_models(data, p_values, d_values, q_values)
