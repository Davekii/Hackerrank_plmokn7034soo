if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    str_match = [s for s in student_marks if query_name in s]
    import code # TODO
    code.interact(local=dict(globals(), **locals())) # TODO


    #print(scores)
    #mean = statistics.mean(scores)

    scores = student_marks['query_name']
    mean = sum(scores)/float(len(scores))


    print('%.2f' % mean)




