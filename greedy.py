from dp import dp

class greedy:
    def job_scheduling(self, jobs=[[1,4], [3,5], [0,6], [5,7],[3,8],[5,9], [6,10], [8,11], [8,12], [2,13],[12,14]]):
        self.j = []
        length = len(jobs)
        i = 0
        self.j.append(i);
        while i < length:
            for j in range (i,length):
                if (jobs[i][1] <= jobs[j][0]):
                    i = j
                    self.j.append(i);
                    break;
            i = i+1
        
        print "interval_scheduling done"
        for i in range(len(self.j)):
            print jobs[self.j[i]], 

if __name__ == '__main__' :
    print "started"
