# Divide and conquer familiy of algorithms

def swap(x, y):
    tmp = y
    y = x
    x = tmp

class sort:
    def __init__(self, array = [12, 14, 10, 3, 5, 19, 21]):
        self.n = array

    def median(self, n = [12, 14, 10, 3, 5, 19, 21]):
        print "median is:", len(n)

    def select(self, n, size = 5):
        length = len(n);
        size = max(length, size)

    def quick_sort(self, n):
        self.quick_sort_internal(n, 0, len(n)-1)

    def quick_sort_internal(self, n, p, r):
        print "p:", p, "r:", r
        if p >= r :
            return
        i = self.partition_internal(n, p, r)
        self.quick_sort_internal(n, p, i-1)
        self.quick_sort_internal(n, i+1, r)

    def partition(self, n):
        return self.partition_internal(n,0,len(n)-1)
##  returns the index of the partition element
    def partition_internal(self, n, p, r):
        if p == r:
            return p;
        if p > r:
            return -1
        x = n[r];    
        i = p-1;
        for j in range(p, r):
            if n[j] <= x:
                i = i+1
                n[j], n[i] = n[i], n[j]
        if (i+1) <= r :
            i = i+1
            n[r], n[i] = n[i], n[r]
        return i

    def interval_sort(self):
        self.interval_sort_internal(self.n, 0, len(self.n)-1)

    def interval_sort_internal(self, n, p, r):
        if p >= r:
            return
        t = self.interval_pivot(n, p, r)
        self.interval_sort_internal(n, p, t-1)
        self.interval_sort_internal(n, t+1, r)

    def interval_pivot(self, n, p, r):
        if p == r:
            return p
        if p > r:
            return -1

        i = p-1
        x = n[r][0]
        for j in range (p, r):
            if n[j][0] <= x:
                i = i+1
                n[i],n[j] = n[j],n[i]
        if i+1 <= r:
            i = i+1
            n[i], n[r] = n[r], n[i]
        return i

    def qsort(self):
        self.qsort_internal(self.n, 0, len(self.n)-1)

    def qsort_internal(self, n , p, r):
        if p >= r:
            return
        p2,r2 = self.qsort_pivot(n, p, r)
        self.qsort_internal(n, p, p2)
        self.qsort_internal(n, r2+1, r)

#   quick sort for equal elements. 
# maintains three sections < = > elements 
    def qsort_pivot(self, n, p, r):
        if p > r :
            return -1, -1
        if p == r:
            return p, p
        i = p-1
        k = i
        x = n[r]
        for j in range(p, r):
            if n[j] < x:
                i = i+1
                k = k+1
                n[k], n[j] = n[j], n[k]
                n[i], n[k] = n[k], n[i]
            elif n[j] == x:
                k = k+1
                n[k], n[j] = n[j], n[k]
        if k+1 <= r: 
            k = k+1
            n[k], n[r] = n[r], n[k]
        return i, k

if __name__ == '__main__' :
    print "started"
