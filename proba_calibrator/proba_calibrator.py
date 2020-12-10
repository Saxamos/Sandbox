"""https://jmetzen.github.io/2015-04-14/calibration.html"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.calibration import calibration_curve, CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense

### fix the seed
np.random.seed(0)

### simulate the data
X, y = datasets.make_classification(
    n_samples=100000, weights=[0.97], n_features=20, n_informative=2, n_redundant=10, random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
bins = 12


### define keras neural network architecture
def keras_model(optimizer="rmsprop", init="glorot_uniform"):
    model = Sequential()
    model.add(Dense(12, input_dim=20, kernel_initializer=init, activation="relu"))
    model.add(Dense(8, kernel_initializer=init, activation="relu"))
    model.add(Dense(1, kernel_initializer=init, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])
    return model


def plot_prob_curve_with_and_without_calibration(estimator, name):
    # baseline_log_reg = LogisticRegression(C=1., solver='lbfgs')
    isotonic_calibration = CalibratedClassifierCV(estimator, cv=2, method="isotonic")
    # sigmoid_calibration = CalibratedClassifierCV(estimator, cv=2, method='sigmoid')

    plt.figure(figsize=(9, 9))
    ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)
    ax2 = plt.subplot2grid((3, 1), (2, 0))

    ax1.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
    for clf, name in [
        # (baseline_log_reg, 'Logistic'),
        (estimator, name),
        (isotonic_calibration, name + " + Isotonic"),
        # (sigmoid_calibration, name + ' + Sigmoid')
    ]:
        clf.fit(X_train, y_train)
        prob_pos = clf.predict_proba(X_test)[:, 1]
        logloss = log_loss(y_test, prob_pos)
        roc = roc_auc_score(y_test, prob_pos)

        fraction_of_positives, mean_predicted_value = calibration_curve(y_test, prob_pos, n_bins=bins)
        ax1.plot(mean_predicted_value, fraction_of_positives, label=f"{name}: logloss({logloss:1.3f}) auc({roc:1.3f})")
        ax2.hist(prob_pos, range=(0, 1), bins=bins, label=name, histtype="step", lw=2)

    ax1.set_ylabel("Fraction of positives")
    ax1.set_ylim([-0.05, 1.05])
    ax1.legend(loc="lower right")
    ax1.set_title("Calibration plots (reliability curve)")

    ax2.set_xlabel("Mean predicted value")
    ax2.set_ylabel("Count")
    ax2.legend(loc="upper center", ncol=2)

    plt.tight_layout()
    plt.savefig("calibration_isotonic.png")
    plt.show()


classifiers = [GaussianNB(), LogisticRegression()]

for clf in classifiers:
    plot_prob_curve_with_and_without_calibration(clf, clf.__class__.__name__)
