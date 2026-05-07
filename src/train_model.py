import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, recall_score, confusion_matrix

def main():
    # Load the dataset
    df = pd.read_csv('data/processed/model_ready_data.csv')

    # Define features and target variable
    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                         y, 
                                                         test_size=0.2, 
                                                         random_state=42,
                                                         stratify=y)
    # Random Forest tuning grid
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [5, 10 , None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'class_weight': ['balanced']
    }

    #Tune model using GridSearchCV
    grid_search = GridSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_grid=param_grid,
        cv=3,
        n_jobs=-1,
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    # Evaluate the model
    predictions = best_model.predict(X_test)

    print("Best Hyperparameters:", grid_search.best_params_)
    print(classification_report(y_test, predictions))
    print("Recall Score:", recall_score(y_test, predictions))
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
    
    # Save the model
    joblib.dump(best_model, 'models/churn_model.pkl')

    # Save the feature names
    joblib.dump(X.columns.tolist(), 'models/feature_names.pkl')

if __name__ == "__main__":
    main()