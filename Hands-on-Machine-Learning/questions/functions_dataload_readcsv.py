import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv") # HOUSING_PATH를 인자로 받아서 넘김.
    return pd.read_csv(csv_path)