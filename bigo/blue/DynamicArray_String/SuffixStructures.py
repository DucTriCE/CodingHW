#Transform s to t
#array: Swap 
#automaton: remove
#both: together
#need\ntree: None

    
if __name__ == '__main__':
    # s, t = input(), input()
    # automaton = array = needtree = False

    # for i in range(26):
    #     s_count = s.count(chr(i+ord('a')))
    #     t_count = t.count(chr(i+ord('a')))

    #     if t_count > s_count:
    #         needtree=True
    #     elif s_count > t_count:
    #         automaton=True

    # start = -1
    # for i in range(len(t)):
    #     index_found = s.find(t[i], start+1)
    #     if index_found > start:
    #         start = index_found
    #     else:
    #         array=True
    
    # if needtree:
    #     print("need tree")
    # elif array and automaton:
    #     print("both")
    # elif automaton:
    #     print("automaton")
    # else:
    #     print("array")

    
    s = input()
    t = input()
    
    needtree = automaton = array = False

    for i in range(26):
        s_count = s.count(chr(i+ord('a')))
        t_count = t.count(chr(i+ord('a')))

        if t_count > s_count:
            needtree=True
        elif s_count > t_count:
            automaton=True
    
    currentIndexFound = -1
    for i in range(len(t)):
        IndexFound = s.find(t[i], currentIndexFound+1)
        if currentIndexFound > IndexFound:
            array=True
        else:
            currentIndexFound = IndexFound
    
    if needtree:
        print("need tree")
    elif array and automaton:
        print("both")
    elif automaton:
        print("automaton")
    else:
        print("array")
        

