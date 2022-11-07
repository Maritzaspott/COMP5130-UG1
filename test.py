def create_dataset(file_path):
    """
        :param file_path: a full file directory path to the imported data file used to run the algorithm
        :return: a dataset of items in a comma separated list
    """
    dataset = []
    with open(file_path, newline='') as custfile:
        rows = csv.reader(custfile)
        for row in rows:
            items = row[0].split(',')
            dataset.append(set(items))
    return dataset

