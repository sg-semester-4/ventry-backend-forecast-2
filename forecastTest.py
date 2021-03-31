import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from fbprophet import Prophet
from sklearn import metrics

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


dataset = pd.read_csv("dataset.csv")
dataset

sampleDataset = dataset[['timestamp', 'quantity']]
sampleDataset.columns = ['ds', 'y']
sampleDataset['ds'] = pd.to_datetime(sampleDataset['ds'])
sampleDataset = sampleDataset.resample("D", on="ds").sum().reset_index()
sampleDataset
sampleDataset.plot.line('ds', 'y')

# define the model
model = Prophet()
# fit the model
model.fit(sampleDataset)

future = model.make_future_dataframe(periods=int(len(sampleDataset) * 0.5))

# use the model to make a forecast
forecast = model.predict(future)
# summarize the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())
# plot forecast
model.plot(forecast)
plt.show()

# calculate MSE between expected and predicted values for december
y_true = sampleDataset['y'][0:len(sampleDataset)].values
y_pred = forecast['yhat'].iloc[0:len(sampleDataset)].values
mse = metrics.mean_squared_error(y_true, y_pred)
print('MSE: %.3f' % (mse))
# plot expected vs actual
plt.plot(y_true, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.legend()
plt.show()


# define the period for which we want a prediction
# t0 = sampleDataset['ds'].iloc[0]
# t1 = sampleDataset['ds'].iloc[1]
# timeDiff = t1-t0
# future = [[sampleDataset['ds'].iloc[-1] + timeDiff]]
# for i in range(1, 12):
#     date = future[i-1][0] + timeDiff
#     future.append([date])
# future = pd.DataFrame(future)
# future.columns = ['ds']
# future
