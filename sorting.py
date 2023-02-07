import random

import timestamp as timestamp

names_dictionary = ('Łukasz', 'Jan', 'Marta', 'Magdalena', 'Filip', 'Dorota', 'Jacek',
                    'Małgorzata', 'Jerzy', 'Mariola', 'Krzysztof', 'Tomasz', 'Monika', 'Rafał',
                    'Kazimierz', 'Tadeusz', 'Stefan', 'Kazimiera')


def generate_test_table(size_of_generated_data):
    result = []
    for x in range(size_of_generated_data):
        random_name = names_dictionary[random.randint(0, len(names_dictionary) - 1)]
        result.append(random_name)
    return result


def find_v1(input, name):
    result = -1;
    for i in range(len(input)):
        if input[i] == name:
            result = i
    return result


def find_v2(input, name):
    for i in range(len(input)):
        if input[i] == name:
            return i
    return -1


test_data = generate_test_table(10000000)

# print(test_data)
def run(count):
    start_timestamp = timestamp()
    for i in range(count):
        find_v1(test_data, 'Jan')
    processing_time = timestamp() - start_timestamp
    avg_processing_time = processing_time / count
    return avg_processing_time


def run2(count):
    start_timestamp2 = timestamp()
    for i in range(count):
        find_v2(test_data, 'Jan')
    processing_time2 = timestamp() - start_timestamp2
    avg_processing_time2 = processingTime2 / count
    return avg_processing_time2

print(f"AVERAGE PROCESSING TIME FOR {100} REPEATS IS {run2(100)}")

no_of_repeats = 100
avgProcessingTime = run(no_of_repeats)
print(f"Average processing time for {no_of_repeats} repeats is {avgProcessingTime}")


# oblicz czas - processingTime = endTime - startTime

startTimestamp2 = timestamp()
print(find_v2(test_data, 'Jan'))
processingTime2 = timestamp() - startTimestamp2

print('Processing time of find_v2:', processingTime2)
