import pandas as pd
import numpy as np

data = pd.read_csv('D:/PowerBi/Project1-Learning/ecommerce_data.csv', encoding='latin1')
data['order_date'] = pd.to_datetime(data['order_date'], format='%d-%m-%Y')
data['ship_date'] = pd.to_datetime(data['ship_date'], format='%d-%m-%Y')

output_file_path = 'D:/PowerBi/Project1-Learning/ecommerce_data_transformed.csv'
data.to_csv(output_file_path, index=False)

print(f'Transformed dataset saved to {output_file_path}')