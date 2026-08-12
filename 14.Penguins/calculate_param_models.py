from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC


def calculate_param_models(X_train,y_train):
    models = {

        'KNN': {
            'model': KNeighborsClassifier(),
            'params': {
                'n_neighbors': [3, 5, 7, 9],
                'p': [1, 2, 3]
            }
        },

        'Decision Tree': {
            'model': DecisionTreeClassifier(),
            'params': {
                'max_depth': [3, 5, 10, 20],
                'min_samples_leaf': [2, 5, 10, 15]
            }
        },

        'Random Forest': {
            'model': RandomForestClassifier(n_estimators=1000, n_jobs=-1),
            'params': {
                'max_depth': [3, 5, 10, 20],
                'min_samples_leaf': [3, 5, 10, 15]
            }
        },

        'SVC': {
            'model': SVC(),
            'params': {
                'C': [0.01, 0.1, 1, 10],
                'kernel': ['linear', 'rbf', 'poly']
            }
        },

        'AdaBoost': {
            'model': AdaBoostClassifier(),
            'params': {
                'n_estimators': [50, 100, 200, 500, 1000],
                'learning_rate': [0.01, 0.1, 1]
            }
        }
    }
    best_models = {}

    for name, config in models.items():

        grid = GridSearchCV(
            estimator=config['model'],
            param_grid=config['params'],
            scoring='f1_macro',
            cv=5,
            n_jobs=-1,
            verbose=1
        )

        grid.fit(X_train, y_train)

        best_models[name] = grid.best_estimator_

    return best_models