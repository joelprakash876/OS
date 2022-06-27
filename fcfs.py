def findWaitingTime(processes, n,bt, wt):
    wt[0] = 0
    for i in range(1, n ):
        wt[i] = bt[i-1] + wt[i-1]
def findTurnAroundTime(processes, n,bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
def findavgTime( processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n,bt, wt, tat)
    print( "Processes  Burst_time " +
                  " Waiting_time " +
                " Turn around time")
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print("    " + str(processes[i]) + "\t\t   " +
                    str(bt[i]) + "\t\t\t " +
                    str(wt[i]) + "\t\t\t\t " +
                    str(tat[i]))
    print( "Average waiting time = "+
                   str(total_wt / n))
    print("Average turn around time = "+
                     str(total_tat / n))
if __name__ =="__main__":
    processes=list(map(int,input("input of processes :").split()))
    n = len(processes)
    burst_time=list(map(int,input("input of burst time :").split()))
    findavgTime(processes, n, burst_time)
 
