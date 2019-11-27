import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.calibration import calibration_curve
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

### fix the seed
np.random.seed(0)

### simulate the data
X, y = datasets.make_classification(n_samples=100000, n_features=20, n_informative=2, n_redundant=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_train, X_cv, y_train, y_cv = train_test_split(X_train, y_train, test_size=0.3, random_state=42)
bins = 15

### fit naive bayes classifier
clf = GaussianNB()
clf.fit(X_train, y_train)
clf_proba = clf.predict_proba(X_cv)[:, 1]

### fit isotonic regression
isotonic_regression = IsotonicRegression(y_min=0, y_max=1, increasing=True)
isotonic_regression.fit(clf_proba, y_cv)

### predict probabilities
uncalibrated_prob = clf.predict_proba(X_test)[:, 1]
calibrated_prob = isotonic_regression.predict(uncalibrated_prob)

### compute score
logloss = log_loss(y_test, uncalibrated_prob)
roc = roc_auc_score(y_test, uncalibrated_prob)
calibrated_loss = log_loss(y_test, calibrated_prob)
calibrated_roc = roc_auc_score(y_test, calibrated_prob)

### plot calibration curve
plt.plot([0, 1], [0, 1], 'k:', label='Perfectly calibrated')

fraction_of_positives, mean_predicted_value = calibration_curve(y_train, clf.predict_proba(X_train)[:, 1], n_bins=bins)
plt.plot(mean_predicted_value, fraction_of_positives, label='Naive Bayes on train data')

isotonic_regression.fit(clf.predict_proba(X_train)[:, 1], y_train)
calibrated_prob = isotonic_regression.predict(clf.predict_proba(X_test)[:, 1])
fraction_of_positives, mean_predicted_value = calibration_curve(y_train, clf.predict_proba(X_train)[:, 1], n_bins=bins)
plt.plot(mean_predicted_value, fraction_of_positives, label='calib on train data')

fraction_of_positives, mean_predicted_value = calibration_curve(y_test, uncalibrated_prob, n_bins=bins)
plt.plot(mean_predicted_value, fraction_of_positives, label=f'Naive Bayes: logloss({logloss:1.3f}) auc({roc:1.3f})')
fraction_of_positives, mean_predicted_value = calibration_curve(y_test, calibrated_prob, n_bins=bins)
plt.plot(mean_predicted_value, fraction_of_positives,
         label=f'Calibrated Naive Bayes: logloss({calibrated_loss:1.3f}) auc({calibrated_roc:1.3f})')
plt.ylabel('Empirical probability')
plt.xlabel('Predicted Probability')
plt.legend(loc='lower right')
plt.show()
