# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:31:45 2024

@author: HP
"""

# Columns explanation : 

# CUST_ID: Identification of Credit Card holder (Categorical)
# BALANCE_FREQUENCY: How frequently the Balance is updated, score between 0 and 1 (1 = frequently updated, 0 = not frequently updated)
# PURCHASES: Amount of purchases made from account 
# CASH_ADVANCE: Cash in advance given by the user
# CREDIT_LIMIT: Limit of Credit Card for user 
# PAYMENTS: Amount of Payment done by user 

# Instructions:
    
# Import you data and perform basic data exploration phase
# Perform the necessary data preparation steps ( Corrupted and missing values handling, data encoding, outliers handling ... )
# Perform hierarchical clustering to identify the inherent groupings within your data. Then, plot the clusters. (use only 2 features. For example, try to cluster the customer base with respect to 'PURCHASES' and 'credit limit')
# Perform partitional clustering using the K-means algorithm. Then, plot the clusters
# Find the best k value and plot the clusters again.
# Interpret the results