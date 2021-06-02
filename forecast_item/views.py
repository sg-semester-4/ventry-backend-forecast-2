from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from .tools import CursorExtras
import numpy as np
import pandas as pd
from fbprophet import Prophet
from sklearn import metrics


class SalesForecast(APIView):
    def post(self, request, item_id):
        cursor = connection.cursor()

        try:
            cursor.execute(
                '''
            select i.id as id, i.name as name, (pt.quantity*pi.quantity) as quantity, pt.updated_at as timestamp
            from product_transaction pt
            inner join product_item pi on pi.product_id=pt.product_id
            inner join item i on i.id=pi.item_id
            where pi.item_id=%s
            order by 4 asc
            ''', [item_id])

            dataset = CursorExtras(cursor).dffetchall()

            sampleDataset = dataset[['timestamp', 'quantity']]
            sampleDataset.columns = ['ds', 'y']
            sampleDataset['ds'] = pd.to_datetime(sampleDataset['ds'])
            sampleDataset = sampleDataset.resample(
                request.data.get('interval'), on="ds").sum().reset_index()

            # define the model
            model = Prophet()
            # fit the model
            model.fit(sampleDataset)

            future = model.make_future_dataframe(
                periods=request.data.get('periods'), freq=request.data.get('interval'))

            # use the model to make a forecast
            forecast = model.predict(future)

            # metrics between expected and predicted values
            y_true = sampleDataset['y'][0:len(sampleDataset)].values
            y_pred = forecast['yhat'].iloc[0:len(sampleDataset)].values
            # 1. calculate MSE
            MSE = metrics.mean_squared_error(y_true, y_pred)
            # 2. calculate R^2
            R2 = metrics.r2_score(y_true, y_pred)

            observedDataset = sampleDataset[['ds', 'y']]
            observedDataset.columns = ['x', 'y']
            observedDataset = observedDataset.to_dict(orient='records')
            forecastedDataset = forecast[['ds', 'yhat']]
            forecastedDataset.columns = ['x', 'y']
            forecastedDataset = forecastedDataset.to_dict(orient='records')

            data = {
                'status': 200,
                'message': "Read item sales forecast succeed",
                'data': {
                    "observed": observedDataset,
                    "forecasted": forecastedDataset,
                    "mse": MSE,
                    "r2": R2
                }
            }
            print("[SalesForecast] Succeed: %s" % ("OK"))
        except Exception as e:
            data = {
                'status': 403,
                'message': "Read item sales forecast failed",
                'data': None
            }
            print("[SalesForecast] Failed: %s" % (e))

        return Response(data)


class StocksForecast(APIView):
    def post(self, request, item_id):
        cursor = connection.cursor()

        try:
            cursor.execute(
                '''
            select i.id as id, i.name as name, ic.quantity as quantity, ic.updated_at as timestamp
            from inventory_control ic
            inner join item i on ic.item_id=i.id
            where i.id=%s
            order by 4 asc
            ''', [item_id])

            dataset = CursorExtras(cursor).dffetchall()

            sampleDataset = dataset[['timestamp', 'quantity']]
            sampleDataset.columns = ['ds', 'y']
            sampleDataset['ds'] = pd.to_datetime(sampleDataset['ds'])
            sampleDataset = sampleDataset.resample(
                request.data.get('interval'), on="ds").sum().reset_index()

            # define the model
            model = Prophet()
            # fit the model
            model.fit(sampleDataset)

            future = model.make_future_dataframe(
                periods=request.data.get('periods'), freq=request.data.get('interval'))

            # use the model to make a forecast
            forecast = model.predict(future)

            # metrics between expected and predicted values
            y_true = sampleDataset['y'][0:len(sampleDataset)].values
            y_pred = forecast['yhat'].iloc[0:len(sampleDataset)].values
            # 1. calculate MSE
            MSE = metrics.mean_squared_error(y_true, y_pred)
            # 2. calculate R^2
            R2 = metrics.r2_score(y_true, y_pred)

            observedDataset = sampleDataset[['ds', 'y']]
            observedDataset.columns = ['x', 'y']
            observedDataset = observedDataset.to_dict(orient='records')
            forecastedDataset = forecast[['ds', 'yhat']]
            forecastedDataset.columns = ['x', 'y']
            forecastedDataset = forecastedDataset.to_dict(orient='records')

            data = {
                'status': 200,
                'message': "Read item stocks forecast succeed",
                'data': {
                    "observed": observedDataset,
                    "forecasted": forecastedDataset,
                    "mse": MSE,
                    "r2": R2
                }
            }
            print("[StocksForecast] Succeed: %s" % ("OK"))
        except Exception as e:
            data = {
                'status': 403,
                'message': "Read item stocks forecast failed",
                'data': None
            }
            print("[StocksForecast] Failed: %s" % (e))

        return Response(data)
