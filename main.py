import math

directory = 'data/'


class Neighbour:
    distance = 0
    name = " "

    def __init__(self, distance, name):
        self.distance = distance
        self.name = name

    def get_distance(self):
        return self.distance


def read_files(file_name):
    with open(file_name, 'r') as f:
        list = [line.strip() for line in f]
        return list


def euklides(v1, v2):
    s1 = v1.split(';')
    s2 = v2.split(';')
    size = len(s1)

    to_square = 0

    for i in range(size - 1):
        to_square = to_square + math.pow(float(s1[i]) - float(s2[i]), 2)

    return math.sqrt(to_square)


def neighbour_list(vector, list):
    neighbours = []
    for i in range(len(list)):
        split = training_list[i].split(';')
        neighbours.append(Neighbour(euklides(vector, list[i]), split[len(split) - 1]))
    neighbours.sort(key=lambda o: o.get_distance(), reverse=False)
    return neighbours


def get_nn(list, n):
    counts = dict()
    for i in range(n):
        counts[list[i].name] = counts.get(list[i].name, 0) + 1
    nearest = max(counts, key=counts.get)
    return nearest


def accuracy_cal():
    correct = 0
    for i in range(len(training_list)):
        n_list = neighbour_list(training_list[i], training_list)
        split = training_list[i].split(";")
        if get_nn(n_list, int(n)) == split[len(split) - 1]:
            correct = correct + 1
    accuracy = correct / len(training_list)
    return round(accuracy, 2)


def vector_classifier(vector):
    n_list = neighbour_list(vector, training_list)
    print(get_nn(n_list, int(n)))


test_data = input("Enter test data file: ")
training_data = input("Enter training data file: ")
n = input("Enter n: ")

test_list = read_files(directory + test_data + ".txt")
training_list = read_files(directory + training_data + ".txt")

print("Accuracy: " + str(accuracy_cal() * 100) + "%")

new_v = input("Enter new vector: ")

vector_classifier(new_v)
exit(0)
