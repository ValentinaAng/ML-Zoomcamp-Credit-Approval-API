import random
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder

# Set random state
RANDOM_STATE = 42
random.seed(RANDOM_STATE)


# Function to load dataset
def load_data(file_path: str) -> pd.DataFrame:
    """Load the dataset."""
    return pd.read_csv(file_path)


# Function to split the dataset into X (features) and y (target)
def split_data(df: pd.DataFrame, target_col: str) -> tuple[pd.DataFrame, pd.Series]:
    """Split dataset into features and target."""
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y


# Function to preprocess data and use the best model with the best hyperparameters
def train_best_model(X: pd.DataFrame, y: pd.Series) -> Pipeline:
    """Train the Random Forest model with the best hyperparameters."""
    # Split columns into categorical and numerical
    categorical_columns = list(X.select_dtypes("object").columns)
    numerical_columns = list(X.select_dtypes("number").columns)

    # Drop unnecessary columns
    columns_to_drop = ["other_parties", "checking_status"]

    cat_cols = [i for i in categorical_columns if i not in columns_to_drop]

    # Defining pipelines for categorical and numerical features
    categorical_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OrdinalEncoder()),
        ],
    )

    numerical_pipe = Pipeline(
        steps=[
            ("imputer", KNNImputer(n_neighbors=5)),
            ("scaler", MinMaxScaler()),
        ],
    )

    # Define preprocessor
    preprocessor = ColumnTransformer(
        [
            ("num", numerical_pipe, numerical_columns),
            ("cat", categorical_pipe, cat_cols),
        ],
        remainder="drop",
    )

    # Best model pipeline
    pipe = Pipeline(
        steps=[
            ("preprocessing", preprocessor),
            ("feature_selection", SelectKBest(f_classif, k=min(10, X.shape[1]))),
            (
                "clf",
                RandomForestClassifier(
                    criterion="entropy",
                    n_estimators=20,
                    max_depth=5,
                    min_samples_split=3,
                    min_samples_leaf=1,
                    class_weight="balanced",
                    random_state=RANDOM_STATE,
                ),
            ),
        ],
    )

    # Train the model
    pipe.fit(X, y)

    return pipe


# File to store the current version
VERSION_FILE = Path("version.txt")


def get_next_version() -> str:
    # Check if the version file exists
    if VERSION_FILE.exists():
        with VERSION_FILE.open() as file:
            current_version = file.read().strip()
        major, minor = map(int, current_version.split("."))
        next_version = f"{major}.{minor + 1}"  # Increment the minor version
    else:
        next_version = "1.0"  # Start with version 1.0

    # Save the next version to the file
    with VERSION_FILE.open("w") as file:
        file.write(next_version)

    return next_version


if __name__ == "__main__":
    # Generate the version
    version = get_next_version()

    # Get the data
    data_path = Path("C:/Users/Dell/ML-Zoomcamp/data/data_cleaned.csv")

    # Model path
    MODEL_PATH = f"best_model_v{version}.pkl"

    # Load and preprocess data
    data = load_data(str(data_path))
    target_col = "accepted"
    X, y = split_data(data, target_col)

    # Train the model
    best_model = train_best_model(X, y)

    # Save the model to a file
    joblib.dump(best_model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH} with version {version}")  # noqa:T201
