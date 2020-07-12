file_nicknames = "data_nickname.txt"
file_results = "results.txt"


def read_file_record(file):
    with open(file, "r") as fil:
        lines = fil.readlines()
        players_info = []
        for line in lines:
            item = line.strip("\n").split(",")
            players_info.append(item)
     
    return players_info 



def add_new_record(data, file):
    with open(file, 'a') as fil:
        record = []
        for key in data:
            record.append(data[key])
        row = ",".join(map(str, record))
        fil.write(row + "\n")
