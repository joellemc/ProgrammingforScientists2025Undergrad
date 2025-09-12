import csv
import pandas as pd

def process_electoral_votes(file_path):
    """
    takes in a file path with the csv file with the first col as the state
    and the second col with how many votes that state gets
    this will return a dictionary mapping states to how many votes they get
    """
    result = dict()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            state = row[0]
            votes = row[1]
            result[state] = votes

    return result

def process_poll_results(file_path):
    """
    takes in a file path with the csv file with first col = state, second col = candidate 1 results,
    third col = candidate 2 results. returns a dictionary mapping states to candidate results
    dictionary key = state, value = c1 results
    """
    result = dict()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            state = row[0]
            c1_results = row[1]
            result[state] = c1_results
    return result


# chat gpt code with an unclear prompt: write a python function that processes election polling data
def process_polling_data(filepath: str):
    """
    Process election polling data from a CSV file.

    Expected columns in CSV:
        - 'Candidate': name of candidate
        - 'Poll': polling percentage (float or int)
        - 'Date': date of the poll (YYYY-MM-DD)

    Args:
        filepath (str): Path to the CSV file containing polling data.

    Returns:
        dict: Summary of results including average poll numbers and latest trends.
    """
    # Load data
    df = pd.read_csv(filepath, parse_dates=['Date'])

    # Clean data: drop missing values
    df = df.dropna(subset=['Candidate', 'Poll', 'Date'])

    # Aggregate: average polling percentage per candidate
    avg_polls = df.groupby('Candidate')['Poll'].mean().to_dict()

    # Find most recent poll per candidate
    latest_polls = (
        df.sort_values('Date')
        .groupby('Candidate')
        .tail(1)
        .set_index('Candidate')['Poll']
        .to_dict()
    )

    # Compute polling trend (difference between latest and average)
    trends = {cand: latest_polls[cand] - avg_polls[cand]
              for cand in avg_polls if cand in latest_polls}

    return {
        "average_polls": avg_polls,
        "latest_polls": latest_polls,
        "trends": trends
    }

# chat gpt code with a better prompt: write a python function that takes in file path as a string and returns a dictionary mapping states to the results of candidate 1. the csv file is in the format of state, candidate1 results, candidate 2 results, and only use the csv library module
def candidate1_results(filepath: str) -> dict:
    """
    Reads a CSV file with election results and returns a dictionary
    mapping each state to Candidate 1's results.

    CSV format:
        state, candidate1_results, candidate2_results

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        dict: {state: candidate1_results}
    """
    results = {}
    with open(filepath, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        # Skip header row (if present)
        header = next(reader)
        if header[0].lower() != "state":
            # If no header, rewind file and re-read from the top
            f.seek(0)
            reader = csv.reader(f)

        # Build dictionary
        for row in reader:
            state = row[0].strip()
            try:
                candidate1 = float(row[1])  # convert to float for numbers
            except ValueError:
                candidate1 = row[1]  # keep raw if not numeric
            results[state] = candidate1

    return results
