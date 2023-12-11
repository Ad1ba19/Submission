# -*- coding: utf-8 -*-
"""Python task 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1blC1-xIpAYnHyRMO2odRlzdPDnQKaCbF

**Python Task 2**

Question 1: Distance Matrix Calculation
"""

import pandas as pd
def calculate_distance_matrix(file_path):
    df = pd.read_csv(file_path)
    distance_matrix = df.pivot_table(values='distance', index='id_start', columns='id_end', fill_value=0)
    distance_matrix += distance_matrix.T
    distance_matrix.values[[range(len(distance_matrix)), range(len(distance_matrix))]] = 0
    return distance_matrix
file_path = 'dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(file_path)
print(result_distance_matrix)

"""Question 2: Unroll Distance Matrix"""

def unroll_distance_matrix(distance_matrix):
    distance_matrix_reset = distance_matrix.reset_index()
    unrolled_df = pd.melt(distance_matrix_reset, id_vars='id_start', var_name='id_end', value_name='distance')

    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']]

    return unrolled_df

file_path = 'dataset-3.csv'
distance_matrix = calculate_distance_matrix(file_path)
unrolled_result = unroll_distance_matrix(distance_matrix)
print(unrolled_result)

"""Question 3: Finding IDs within Percentage Threshold"""

import pandas as pd

def find_ids_within_ten_percentage_threshold(distance_matrix, reference_value):
    reference_rows = distance_matrix[distance_matrix['id_start'] == reference_value]
    reference_avg_distance = reference_rows['distance'].mean()
    threshold = 0.1 * reference_avg_distance
    within_threshold = distance_matrix[
        (distance_matrix['distance'] >= reference_avg_distance - threshold) &
        (distance_matrix['distance'] <= reference_avg_distance + threshold)
    ]

    result_ids = within_threshold['id_start'].unique()
    result_ids.sort()
    return result_ids


reference_value = 1  # Replace with the desired reference value
result_within_threshold = find_ids_within_ten_percentage_threshold(unrolled_result, reference_value)
print(result_within_threshold)

"""Question 4: Calculate Toll Rate"""

def calculate_toll_rate(input_df):
    result_df = input_df.copy()
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle_type, rate_coefficient in rate_coefficients.items():
        result_df[vehicle_type] = result_df['distance'] * rate_coefficient

    return result_df

file_path = 'dataset-3.csv'
distance_matrix = calculate_distance_matrix(file_path)  # Assuming you have the calculate_distance_matrix function
unrolled_result = unroll_distance_matrix(distance_matrix)  # Assuming you have the unroll_distance_matrix function
toll_rate_result = calculate_toll_rate(unrolled_result)
print(toll_rate_result)

