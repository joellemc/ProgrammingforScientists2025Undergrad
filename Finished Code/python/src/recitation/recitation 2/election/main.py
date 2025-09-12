import random  # for generating random numbers
from election_io import *  # for reading from files

def main() :
    print("reading csv files!")
    # file paths for our csv files
    electoral_votes_file_path = "data/electoralVotes.csv"
    conventions_file_path = "data/conventions.csv"
    debates_file_path = "data/debates.csv"
    early_polls_file_path = "data/earlyPolls.csv"

    # using our own function that we wrote
    electoral_votes = process_electoral_votes(electoral_votes_file_path)
    print("electoral_votes", electoral_votes)

    # using our own function that we wrote
    convention = process_poll_results(conventions_file_path)
    print("convention", convention)

    # using chat gpt code with an unclear prompt
    # need to comment out next two lines because it crashes since it doesn't know what the csv file format is
    debate = process_polling_data(debates_file_path)
    print("debate", debate)

    # using chat gpt code with a clearer and stronger prompt
    early_poll = candidate1_results(early_polls_file_path)
    print("early_poll", early_poll)

if __name__ == "__main__":
    main()