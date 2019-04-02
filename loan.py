# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 11:21:59 2019

@author: SONALI
"""

import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
from sklearn.externals.six import StringIO 
from IPython.display import Image

path = "F:/Imarticus learntron Final Projects/Python Project Material/XYZCorp_LendingData.txt"
loan = pd.read_csv(path,sep = '\t')

len(loan)       # show nrows
loan.shape      # show rows and columns
loan.describe() #Descride the summary of dataset

loan.dtypes     #to know datatype of each column in dataset
loan.info()     # To check columns information

loan.index
#Check missing values
no_missing =100 - (100*loan.count()/len(loan))
missing_var = no_missing[no_missing > 0]      # % of missing values in each column
missing_var.count()     # missing values in 31 columns 


#Drop columns which contains more than 60% missing values(20 columns)
missing_val_col = no_missing[no_missing > 50]
missing_val_col.count()
loan.drop(missing_val_col.index, axis = 1, inplace = True)
loan.shape

loan.head(5)
# Gives count of levels of column
loan.groupby('term').size()
loan.groupby('verification_status').size()
loan.groupby('pymnt_plan').size()    # Delete column
loan.groupby('home_ownership').size()
loan.groupby('application_type').size()
loan.groupby('addr_state').size()
loan.groupby('earliest_cr_line').size()
loan.groupby('next_pymnt_d').size()
loan.groupby('last_pymnt_amnt').size()
loan.groupby('last_credit_pull_d').size()
loan.policy_code.describe()
loan.groupby('default_ind').size()
loan.columns
loan.info()
# Remove Unwanted columns(5)
var_to_be_remove = [ 'id', 'member_id','emp_title','pymnt_plan','title',
                    'policy_code','application_type','acc_now_delinq',
                    'zip_code']

loan.drop(var_to_be_remove, axis = 1, inplace = True)


# Data Visualization

loan.boxplot('collections_12_mths_ex_med')
plt.hist(loan.collections_12_mths_ex_med)

loan.total_rev_hi_lim.describe()

loan.boxplot('issue_d')
plt.hist(loan.issue_d)

# Replacing NULL's from numeric columns with median
weight_median = loan['revol_util'].median()
loan.revol_util[loan.revol_util.isnull()] = weight_median

wt_median = loan['last_pymnt_amnt'].median()
loan.last_pymnt_amnt[loan.last_pymnt_amnt.isnull()] = wt_median

wt_median = loan['collections_12_mths_ex_med'].median()
loan.collections_12_mths_ex_med[loan.collections_12_mths_ex_med.isnull()] = wt_median

wt_median = loan['tot_coll_amt'].median()
loan.tot_coll_amt[loan.tot_coll_amt.isnull()] = wt_median

wt_median = loan['tot_cur_bal'].median()
loan.tot_cur_bal[loan.tot_cur_bal.isnull()] = wt_median

wt_median = loan['total_rev_hi_lim'].median()
loan.total_rev_hi_lim[loan.total_rev_hi_lim.isnull()] = wt_median
loan.info()

#Replacing NULL's from object(factor) columns with unknown level
loan.last_pymnt_d[loan.last_pymnt_d.isnull()] = "Unknown"
loan.next_pymnt_d[loan.next_pymnt_d.isnull()] = "Unknown"
loan.last_credit_pull_d[loan.last_credit_pull_d.isnull()] = "Unknown"

#convert datatype to object
#loan[['default_ind']] = loan[['default_ind']].apply(pd.to_object)
############################ Model Building ####################

#Divide dataset into train(June 2007 - May 2015) & test(June 2015 - Dec 2015)

loan.groupby('issue_d').size()
oot_test_months = ['Jun-2015', 'Jul-2015', 'Aug-2015', 'Sep-2015',
                   'Oct-2015', 'Nov-2015', 'Dec-2015']

train = loan.loc [ -loan.issue_d.isin(oot_test_months) ]
test = loan.loc [ loan.issue_d.isin(oot_test_months) ]

train.shape
test.shape
train.columns
# split the train and test into X and Y variables
train_x = train.iloc[:,0:42]; train_y = train.iloc[:,43-1]
test_x  = test.iloc[:,0:42];  test_y = test.iloc[:,43-1]
train_x.columns
test_x.shape
#########################  Logistic Regression #####################

# random_state --> tells if the same data be used each time or different
# ---------------------------------------------------
logreg = LogisticRegression(random_state=0)
logreg.fit(train_x, train_y)
