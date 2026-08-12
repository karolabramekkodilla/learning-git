import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, f1_score


metrics_dataframe = pd.DataFrame(columns = ['Model', 'F1_score'])
metrics_dataframe

def calculate_metrics(model, name, X_checked, y_checked):

    global metrics_dataframe
    predictions = model.predict(X_checked)
    # Classification report
    print(classification_report(y_checked, predictions))
    # Confusion matrix
    plt.figure()
    cm = confusion_matrix(y_checked, predictions)
    ax = sns.heatmap(
        cm,
        annot=True,
        cmap='Blues',
        fmt='.0f'
    )
    ax.set_title('Confusion Matrix\n\n')
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values')
    plt.show()
    # F1
    f1_metric = f1_score(
        y_checked,
        predictions,
        average='weighted'
    )
    metrics_dataframe.loc[len(metrics_dataframe)] = {
        'Model': name,
        'F1_score': f1_metric
    }

    return metrics_dataframe
    
