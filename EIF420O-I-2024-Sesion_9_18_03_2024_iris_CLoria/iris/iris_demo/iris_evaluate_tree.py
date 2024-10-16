from sklearn.metrics import (accuracy_score, 
                            precision_score, 
                            recall_score, 
                            f1_score)
                            
from sklearn.metrics import (confusion_matrix,ConfusionMatrixDisplay, 
                            roc_curve, 
                            roc_auc_score, 
                            precision_recall_curve)
                            
import matplotlib.pyplot as plt


def test_tree(tree, class_names, X_test, y_test):
    print(f"{X_test.shape=:} {y_test.shape=:}")
    # Make predictions
    y_pred = tree.predict(X_test)
    dict_classes = {n:i for i, n in enumerate(class_names)}
    # Compute metrics
    accuracy = accuracy_score(y_test, y_pred)
    
    average_type = 'weighted' # None, binary, micro, macro
    precision = precision_score(y_test, y_pred, average = average_type)
    recall = recall_score(y_test, y_pred, average = average_type)
    f1 = f1_score(y_test, y_pred, average = average_type)
    
    #
    cm = confusion_matrix(y_test, y_pred, labels = [0,1,2])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=class_names)
    
    try:
        # ROC curve and AUC
        y_proba = tree.predict_proba(X_test)[:, 1]
        fpr, tpr, thresholds_roc = roc_curve(y_test, y_proba)
        auc_roc = roc_auc_score(y_test, y_proba)
    
        # Precision-Recall curve (not working!!)
        precision_pr, recall_pr, thresholds_pr = precision_recall_curve(y_test, y_proba)
    except Exception as e:
        e = f"NA: --{e}--"
        fpr, tpr, thresholds_roc,auc_roc = (e,e,e,e)
        precision_pr, recall_pr, thresholds_pr = (e,e,e)
    
    # Print metrics
    print("Total of y-samples:", y_test.shape[0])
    print("Classes:", class_names)
    
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)
    print("Confusion Matrix:")
    print(cm)
    print("AUC-ROC Score:", auc_roc)
    
    return {
     "accuracy":accuracy,
     "precision":precision,
     "recall":recall,
     "cm":cm,
     "cm_plot": disp,
     "auc_roc":auc_roc
    }
    


def tree_auc_roc(metrics):
    # Plot ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(metrics.fpr, metrics.tpr, label='ROC Curve (AUC = {:.2f})'.format(metrics.auc_roc))
    plt.plot([0, 1], [0, 1], 'k--', label='Random Guessing')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.show()

def tree_precision_recall(metrics):    
    # Plot Precision-Recall curve
    plt.figure(figsize=(8, 6))
    plt.plot(metrics.recall_pr, metrics.precision_pr, label='Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.show()