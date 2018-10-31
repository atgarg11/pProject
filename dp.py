from binaryTree import btree ## importing self created classes

class dp:
    ##  function to dermine the longes common subsequence 
    ##  of two given strings
    def lcs(self, seq1="bdcaba", seq2="abcbdab"):
        seq11="0"+seq1
        seq22="0"+seq2
        x = len(seq11)
        y = len(seq22)
        res =""
##      initialisation for LCS
        self.lcs_length = [[0]*y for n in range(x)]
    
##      seq11 is represented as rows and seq22 as columns        
##      for each substring n X what is the lCS
##      if X[i] == Y[j], lcs = X[i-1] Y[j-1]

        maxc = 0
        for i in range(1,x):
            for j in range(1,y):
                #print i, j, seq11[i], seq22[j]
                if seq11[i] == seq22[j]:
                    self.lcs_length[i][j] = 1+self.lcs_length[i-1][j-1] 
                    if self.lcs_length[i][j] > maxc:
                        res = res + seq11[i]
                        maxc += 1 
                        print i, j
                else:
                    self.lcs_length[i][j] = max(
                            self.lcs_length[i-1][j], 
                            self.lcs_length[i][j-1])

        print "longest common subsequence length :", 
        print self.lcs_length[i][j]
        return "subsequence: " + res 

##      These two for loops below cover all the substrings in 
##      a string. substring from str[i] to str[i+n]

#   longest increasing subsequence
    def lis(self, string=[10, 22, 9, 33, 21, 50, 41, 60, 80]):
        res = ""
        length = len(string)

##      initialise the length of longest increasing subsequence
        self.lis_length = [0 for i in range(length)] 
        for i in range(length):
            self.lis_length[i] = 1;

        max_index = 0
##      logic to determine the LIS
        for i in range (1, length):
            maxc = self.lis_length[i];
            for j in range (i): 
                if(string[j] < string[i]):
                    if (maxc < (self.lis_length[j] +1)) : 
                        self.lis_length[i] = self.lis_length[j]+1
                        maxc = self.lis_length[i]
                        if self.lis_length[max_index] < maxc :
                            maxc_index = i

        print "longest increasing subsequence length: ", 
        print self.lis_length[max_index] 
        print "Sub sequence: ",
        for j in range(length):
            print string[i],

    def obst(self):
        print "Optimal binary search Tree"
    
    def fib(self, n = 10):
        self.fibno = [0 for i in range(n)]
        self.fibno[0] = 1;
        self.fibno[1] = 1;
        for i in range (2,n):
            self.fibno[i] = self.fibno[i-1]+self.fibno[i-2]

        for i in range(n):
            print self.fibno[i],


if __name__ == '__main__' :
    print "started"
