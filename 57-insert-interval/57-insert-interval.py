


class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [ni]

        s = None # start idx
        f = None # finish idx
        mid = False
        
        for i, itv in enumerate(intervals):
            a,b = itv
            
            c = None
            if i+1 < len(intervals):
                c = intervals[i+1][0]
            
            n = ni[0]
            m = ni[1]
            if s is None:
                if n < a:
                    if m < a:
                        s = -1
                        break
                    else:
                        s = i
                        intervals[i][0] = n
                        
                elif a <= n <= b:
                    s = i
                elif c is not None and n >= b and m <= c:
                    s = i+1
                    mid = True
                    break
           
            # firs item hasn't found, skip until its found
            if s is None:
                continue
            
            if a <= m:
                if m <= b:
                    f = i
                    intervals[i][1] = max(b, m)
                    break
                    
                else: # greater than b
                    if c is not None:
                        if m < c:
                            f = i
                            intervals[i][1] = max(b, m)
                            break
                        else:
                            continue
                    elif c is None:
                        f =i
                        intervals[i][1] = max(b, m)
                    
        # print(s,f, mid)
        # print(intervals)
        if mid:
            new = [*intervals[:s], ni, *intervals[s:]]
            
        elif s is not None and f is not None:
            merged = [intervals[s][0],intervals[f][1]]
            # print(merged)
            new = [*intervals[:s], merged, *intervals[f+1:]]
                
        else:
            if -1 in [s,f]:
                new = [ ni, *intervals]
            else:
                new = [*intervals, ni]

        return new
                
                    
                    

                    
                