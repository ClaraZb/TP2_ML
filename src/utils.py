import random

def print_dataset_extract(df, rows_count = 7):
    """Prints a random extract from the dataset"""
    rows_to_print = rows_count
    random_index = random.randint(0, len(df) - 1 - rows_to_print)
    print(df.iloc[random_index : random_index + 7])

