from operator import itemgetter


def handle_list_of_tuples(data):
    """function takes list of tuples (e.g. handle_list_of_tuples(list))
    and sort it based on the next rules: name / age / height / weight"""

    lst_sorted_by_height_and_weight = sorted(data, key=itemgetter(2, 3),
                                             reverse=True)
    sorted_list = sorted(lst_sorted_by_height_and_weight, key=itemgetter(0, 1))
    print 'Result:\n[\n\t{0},\n]'.format(
        ',\n\t'.join(str(tup) for tup in sorted_list))


if __name__ == '__main__':
    lst = [
        ("Tom", "19", "167", "54"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98"),
    ]
    handle_list_of_tuples(lst)
