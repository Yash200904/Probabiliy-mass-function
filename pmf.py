def checkPmf():

    probability = {0:0.25 ,1:0.25 ,2:-0.25 ,3:0.25 }

    sum =0

    for value in probability.values():
        if value < 0:
            print("This is not a Probabilty Mass Function")
            return 

        sum += value

    if sum == 1:
        print("This is a Probabilty Mass Function")

    else:
        print("This is not a Probabilty Mass Function")
        
checkPmf()
