import pandas as pd
from scripts.llm import generate_training_data
import os

def create_training_data(task_requirements):
    if not os.path.exists("data"):
        os.makedirs("data")
    training_data = generate_training_data(task_requirements)
    df = pd.DataFrame(training_data)
    csv_file_path = 'data/training_data.csv'
    df.to_csv(csv_file_path, index=False)
    return csv_file_path