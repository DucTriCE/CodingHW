
if __name__ == '__main__':

    while(int(input())!=0):
        carOrder = list(map(int, input().split()))
        i=0
        currentCar = 1
        st = []
        while i < len(carOrder):
            if carOrder[i]!=currentCar:
                if len(st)==0:
                    st.append(carOrder[i])
                    i+=1
                else:
                    if st[-1] == currentCar:
                        st.pop()
                        currentCar+=1
                    elif st[-1] > carOrder[i]:
                        st.append(carOrder[i])
                        i+=1
                    else:
                        break
            else:
                i+=1
                currentCar+=1
        
        while len(st)!=0:
            if st[-1] == currentCar:
                st.pop()
                currentCar+=1
            else:
                break

        if currentCar-1 == len(carOrder):
            print('yes')
        else:
            print('no')


            

    
