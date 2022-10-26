from collections import Counter


def get_the_one_loved_beer(answers) -> list:
    one_liked_beers = []
    for count, all_worker_answers in enumerate(answers):
        counter = all_worker_answers.count('Y')
        if counter == 1:
            one_liked_beers.append(answers[count].index('Y') + 1)
    return one_liked_beers


def find_liked_beers_by_workers(answers, workers, beers):

    # Creating array of workers with their liked beers

    liked_beers_by_worker_index = []

    # Creating array of likes beers

    liked_beers = []

    for i in range(workers):
        worker_beers = []
        for j in range(beers):
            if answers[i][j] == "Y":
                worker_beers.append((j + 1))
                liked_beers.append(j + 1)
        liked_beers_by_worker_index.append(worker_beers.copy())
        worker_beers.clear()
    return liked_beers_by_worker_index, liked_beers


# Check weather lists have some similar elements on crossing
def lists_have_same_values(list1, list2):
    return True if set(list1) & set(list2) else False


# Create new list of elements on crossing
def find_crossing(list1, list2):
    return list((Counter(list1) & Counter(list2)).elements())


def get_final_list_of_beers(results, liked_by_index, liked_beers):
    for elem in liked_by_index:
        if lists_have_same_values(results, elem):
            continue
        else:
            crossing_beers = find_crossing(elem, liked_beers)
            res = crossing_beers[0]
            results.append(res)
    return results


def print_final_result(final_result):
    f = open('output.txt', 'w')
    f.write(str(len(final_result)))
    print(str(len(final_result)))


if __name__ == '__main__':
    # Getting data from file and giving it to our variables

    file = open("Lab3\input.txt")
    line = file.read()

    workers = int(line.split('\n')[0].split(' ')[0])
    print('Workers:', workers)

    beers = int(line.split('\n')[0].split(' ')[1])
    print('Beers:', beers)

    answers = line.split('\n')[1].split(' ')
    print('Y-N answers: ', answers)

    results = get_the_one_loved_beer(answers)

    liked_beers_by_worker_index, liked_beers = find_liked_beers_by_workers(answers, workers, beers)

    get_final_list_of_beers(results, liked_beers_by_worker_index, liked_beers)

    print_final_result(results)
