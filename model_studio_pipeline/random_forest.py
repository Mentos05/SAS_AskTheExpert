# Python or R code based on the Language property.
#
# Note that a few lines of Python or R code are added before your code; for example:
# Python:
#  dm_class_input = ["class_var_1", "class_var_2"]
#  dm_interval_input = ["numeric_var_1", "numeric_var_2"]
# R:
#  dm_class_input <- c("class_var_1", "class_var_2")
#  dm_interval_input <- c("numeric_var_1", "numeric_var_2")
#
# For Python, use the Node Configuration section of the Project Settings to prepend
# any configuration code, which is executed before the above code. During execution,
# this code is automatically prepended to every node that runs Python code.
#
# After running the node, the Python or R code window in the node results displays
# the actual code that was executed. START ENTERING YOUR CODE ON THE NEXT LINE.

# Builds RandomForest model with 100 trees
# THIS EXAMPLE DUMMY ENCODES CATEGORICAL VARIABLES

from sklearn import ensemble

# Get full data with inputs + partition indicator
dm_input.insert(0, dm_partitionvar)
fullX = dm_inputdf.loc[:, dm_input]

# Dummy encode categorical variables
fullX_enc = pd.get_dummies(fullX, columns=dm_class_input, drop_first=True)

# Training data
X_enc = fullX_enc[fullX_enc[dm_partitionvar] == dm_partition_train_val]
X_enc = X_enc.drop(dm_partitionvar, 1)

# Labels
y = dm_traindf[dm_dec_target]

# Fit RandomForest model w/ training data
params = {'n_estimators': 100}
dm_model = ensemble.RandomForestClassifier(**params)
dm_model.fit(X_enc, y)
print(dm_model)

# Save VariableImportance to CSV
varimp = pd.DataFrame(list(zip(X_enc, dm_model.feature_importances_)), columns=['Variable Name', 'Importance'])
varimp.to_csv(dm_nodedir + '/rpt_var_imp.csv', index=False)

# Score full data
fullX_enc = fullX_enc.drop(dm_partitionvar, 1)
dm_scoreddf = pd.DataFrame(dm_model.predict_proba(fullX_enc), columns=['P_ARR_DEL150', 'P_ARR_DEL151'])
