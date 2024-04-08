if __name__ == '__main__':
    # Add your code here
    students = list(map(int, input().split()))
    sandwiches = list(map(int, input().split()))
    n_loop = 0
    while n_loop != len(students):
        if sandwiches[0]==students[0]:
            students.pop(0)
            sandwiches.pop(0)
            n_loop=0
        else:
            students.append(students.pop(0))
            n_loop+=1
    print(len(students))