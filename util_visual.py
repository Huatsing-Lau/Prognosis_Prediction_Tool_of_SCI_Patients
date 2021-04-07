# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")

from util_widgets import *
from IPython.display import display
import random
import pandas as pd
import numpy as np
import joblib
import os

from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values


class Visual():
    def __init__(self):
        dir_result = './early_prediction_deploy'#结果保存路径
        final_allsave_filename = os.path.join(dir_result, 'all_python_vars.npy')
        result_vars_first = np.load(final_allsave_filename, allow_pickle=True)
        self.sc_params_first = result_vars_first.item()['sc_params']#数据标准化预处理：均值和标注差
        self.clf_first = joblib.load(os.path.join(dir_result,'Simplified_Esb_Clf.model'))
        
        dir_result = './recent_prediction_deploy'#结果保存路径
        final_allsave_filename = os.path.join(dir_result, 'all_python_vars.npy')
        result_vars_last = np.load(final_allsave_filename, allow_pickle=True)
        self.sc_params_last = result_vars_last.item()['sc_params']#数据标准化预处理：均值和标注差
        self.clf_last = joblib.load(os.path.join(dir_result,'Simplified_Esb_Clf.model'))
        
        # grid_page_0
        self.grid_p0 = GridspecLayout(10, 2)
        self.p0_left = [
            w_p0_Age,
            w_p0_Morphine_Sulfate, # Y/N
            w_p0_Albumin,
            w_p0_GCS_total,
            w_p0_PH,# Y/N
            w_p0_Cefazolin,
            w_p0_Ca,
            w_p0_Mechanical_Ventilation, # Y/N
            w_p0_Free_Ca,
            w_p0_Kcl, # Y/N
        ]
        self.p0_right = [w_p0_submit, w_p0_result, w_p0_c1, w_p0_c2, w_p0_c3]
        for i, w in enumerate(self.p0_left):
            self.grid_p0[i, 0] = w
        for i, w in enumerate(self.p0_right):
            self.grid_p0[i, 1] = w
        
        # grid_page_1
        self.grid_p1 = GridspecLayout(10, 2)
        self.p1_left = [
            w_p1_Los_Hospital,
            w_p1_Age,
            w_p1_Fio2,
            w_p1_Albumin,
            w_p1_BUN,
            w_p1_Glucose_Blood,
            w_p1_RDW,
            w_p1_GCS_Total,
            w_p1_HR,
            w_p1_Sum_Diagnosis
        ]
        self.p1_right = [w_p1_submit, w_p1_result, w_p1_c1, w_p1_c2, w_p1_c3]
        for i, w in enumerate(self.p1_left):
            self.grid_p1[i, 0] = w
        for i, w in enumerate(self.p1_right):
            self.grid_p1[i, 1] = w

        # tab:
        self.tab = widgets.Tab()
        self.tab.children=[self.grid_p0, self.grid_p1]
        self.tab.set_title(0, 'Early Prediction')# Early Prediction of ICU Discharge Location of SCI patient
        self.tab.set_title(1, 'Recent Prediction')# Recent Prediction of ICU Discharge Location of SCI patient
        # inference:
        w_p0_submit.on_click(self.p0_inference)
        w_p1_submit.on_click(self.p1_inference)
        # value control(input number)
        ## tab 0:(text)
        w_p0_Age.observe(self.on_p0_Age_change, names='value')
        w_p0_Albumin.observe(self.on_p0_Albumin_change, names='value')
        w_p0_GCS_total.observe(self.on_p0_GCS_total_change, names='value')
        w_p0_PH.observe(self.on_p0_PH_change, names='value')
        w_p0_Ca.observe(self.on_p0_Ca_change, names='value')
        w_p0_Free_Ca.observe(self.on_p0_Free_Ca_change, names='value')
        ## tab 1:(text)
        w_p1_Los_Hospital.observe(self.on_p1_Los_Hospital_change, names='value')
        w_p1_Age.observe(self.on_p1_Age_change, names='value')
        w_p1_Fio2.observe(self.on_p1_Fio2_change, names='value')
        w_p1_Albumin.observe(self.on_p1_Albumin_change, names='value')
        w_p1_BUN.observe(self.on_p1_BUN_change, names='value')
        w_p1_Glucose_Blood.observe(self.on_p1_Glucose_Blood_change, names='value')
        w_p1_RDW.observe(self.on_p1_RDW_change, names='value')
        w_p1_GCS_Total.observe(self.on_p1_GCS_Total_change, names='value')
        w_p1_HR.observe(self.on_p1_HR_change, names='value')
        w_p1_Sum_Diagnosis.observe(self.on_p1_Sum_Diagnosis_change, names='value')
        
        
        # lock class value
        w_p0_c1.observe(self.on_p0_c1_change, names='value')
        w_p0_c2.observe(self.on_p0_c2_change, names='value')
        w_p0_c3.observe(self.on_p0_c3_change, names='value')
        w_p1_c1.observe(self.on_p1_c1_change, names='value')
        w_p1_c2.observe(self.on_p1_c2_change, names='value')
        w_p1_c3.observe(self.on_p1_c3_change, names='value')
        # init
        self.p0_c1_value = 0
        self.p0_c2_value = 0
        self.p0_c3_value = 0
        self.p1_c1_value = 0
        self.p1_c2_value = 0
        self.p1_c3_value = 0
        display(self.tab, w_out)
        
    def p0_inference(self, b):
        w_out.clear_output()
        with w_out:      
            X_data = [w.value for w in self.p0_left]
            X_description = [w.description for w in self.p0_left]
        X_data = np.array([X_data])
        features = ['age', 'Morphine.Sulfate', 'Albumin', 'GCS.total', 'PH',
                    'cefazolin', 'Ca', 'Mechanical.ventilation', 'Free.Ca', 'Kcl']
        X_deploy_test = pd.DataFrame(data=X_data, index=[0] ,columns=features) 
        with w_out:
            display(X_deploy_test)

        proba = self.predict_proba_discharge_location_first(X_deploy_test)
        self.p0_c1_value = proba[0]
        self.p0_c2_value = proba[1]
        self.p0_c3_value = proba[2]
        w_p0_c1.value = self.p0_c1_value
        w_p0_c2.value = self.p0_c2_value
        w_p0_c3.value = self.p0_c3_value
    def p1_inference(self, b):
        w_out.clear_output()
        with w_out:      
            X_data = [w.value for w in self.p1_left]
            X_description = [w.description for w in self.p1_left]
        X_data = np.array([X_data])
        features = ['los_hospital', 'age', 'Fio2', 'Albumin', 'BUN',
                    'Glucose.Blood', 'RDW', 'GCS.total', 'HR', 'sum_diagnosis']
        X_deploy_test = pd.DataFrame(data=X_data, index=[0] ,columns=features)  
        with w_out:
            display(X_deploy_test)
        proba = self.predict_proba_discharge_location_last(X_deploy_test)
        self.p1_c1_value = proba[0]
        self.p1_c2_value = proba[1]
        self.p1_c3_value = proba[2]
        w_p1_c1.value = self.p1_c1_value
        w_p1_c2.value = self.p1_c2_value
        w_p1_c3.value = self.p1_c3_value
    # left"
    ## tab 0:
    def on_p0_Age_change(self, change):
        if w_p0_Age.value < 0:
            w_p0_Age.value = 0
        if w_p0_Age.value > 120:
            w_p0_Age.value = 120   
    def on_p0_Albumin_change(self, change):
        if w_p0_Albumin.value < 0:
            w_p0_Albumin.value = 0
    def on_p0_GCS_total_change(self, change):
        if w_p0_GCS_total.value < 0:
            w_p0_GCS_total.value = 0
    def on_p0_Albumin_change(self, change):
        if w_p0_Albumin.value < 0:
            w_p0_Albumin.value = 0         
    def on_p0_PH_change(self, change):
        if w_p0_PH.value < 0:
            w_p0_PH.value = 0
    def on_p0_Ca_change(self, change):
        if w_p0_Ca.value < 0:
            w_p0_Ca.value = 0
    def on_p0_Free_Ca_change(self, change):
        if w_p0_Free_Ca.value < 0:
            w_p0_Free_Ca.value = 0
        
    ## tab 1:
    def on_p1_Los_Hospital_change(self, change):
        if w_p1_Los_Hospital.value < 0:
            w_p1_Los_Hospital.value = 0
    def on_p1_Age_change(self, change):
        if w_p1_Age.value < 0:
            w_p1_Age.value = 0
        if w_p1_Age.value > 120:
            w_p1_Age.value = 120
    def on_p1_Fio2_change(self, change):
        if w_p1_Fio2.value < 0:
            w_p1_Fio2.value = 0
    def on_p1_Albumin_change(self, change):
        if w_p1_Albumin.value < 0:
            w_p1_Albumin.value = 0
    def on_p1_BUN_change(self, change):
        if w_p1_BUN.value < 0:
            w_p1_BUN.value = 0
    def on_p1_Glucose_Blood_change(self, change):
        if w_p1_Glucose_Blood.value < 0:
            w_p1_Glucose_Blood.value = 0  
    def on_p1_RDW_change(self, change):
        if w_p1_RDW.value < 0:
            w_p1_RDW.value = 0
    def on_p1_GCS_Total_change(self, change):
        if w_p1_GCS_Total.value < 0:
            w_p1_GCS_Total.value = 0
    def on_p1_HR_change(self, change):
        if w_p1_HR.value < 0:
            w_p1_HR.value = 0
    def on_p1_Sum_Diagnosis_change(self, change):
        if w_p1_Sum_Diagnosis.value < 0:
            w_p1_Sum_Diagnosis.value = 0
    
    # right:        
    def on_p0_c1_change(self, change):
        w_p0_c1.value = self.p0_c1_value
    def on_p0_c2_change(self, change):
        w_p0_c2.value = self.p0_c2_value
    def on_p0_c3_change(self, change):
        w_p0_c3.value = self.p0_c3_value
    def on_p1_c1_change(self, change):
        w_p1_c1.value = self.p1_c1_value
    def on_p1_c2_change(self, change):
        w_p1_c2.value = self.p1_c2_value
    def on_p1_c3_change(self, change):
        w_p1_c3.value = self.p1_c3_value
        
    def predict_proba_discharge_location_first(self,X):
        """问题0的预测"""
        X = (X-self.sc_params_first.loc['mean_'].values)/self.sc_params_first.loc['scale_'].values# standard scale
        proba = self.clf_first.predict_proba(X).squeeze()
        return proba
    def predict_proba_discharge_location_last(self,X):
        """问题1的预测"""
        X = (X-self.sc_params_last.loc['mean_'].values)/self.sc_params_last.loc['scale_'].values# standard scale
        proba = self.clf_last.predict_proba(X).squeeze()
        return proba
