#---coding:utf-8----

class q2(object):
    result = 0;
    n = 0
    m = 0
    def main(self):
        nm = raw_input("")
        sxsy = raw_input("")
        self.n = int(nm.split(" ")[0])
        self.m = int(nm.split(" ")[1])
        sx = int(sxsy.split(" ")[0])-1
        sy = int(sxsy.split(" ")[1])-1
        hm_str = []
        for i in range(0, self.n):
            hm_str.append(raw_input(""))
        hm = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(0, self.n):
            for j in range(0, self.m):
                hm[i][j] = int(hm_str[i].split(" ")[j])
        self.helper(sx, sy, hm)
        print self.result

    def helper(self, x, y, hm):
        if hm[x][y] > self.result:
            self.result = hm[x][y]
        if(x>0 and hm[x-1][y]>=hm[x][y]):
            helper(x-1, y, hm)
        if(x<(self.n-1) and hm[x+1][y]>=hm[x][y]):
            helper(x+1, y, hm)
        if(y>0 and hm[x][y-1]>=hm[x][y]):
            helper(x, y-1, hm)
        if(y<(self.m-1) and hm[x][y+1]>=hm[x][y]):
            helper(x, y+1, hm)
        return 1

test = q2()
test.main()
