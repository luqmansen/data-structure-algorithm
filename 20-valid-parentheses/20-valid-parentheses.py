# {[][]}
# {{}()}([]{})
# {[}][]

# stack [ ( ] ) ( ) ( )
# [ ( ] ) ( ) ( )
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        close = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        
        st = []
        
        for p in s:
            # print(p, st)
            if len(st) == 0:
                st.append(p)
                continue
            else:
                if p in close and st[-1] == close[p]:
                    st.pop()
                else:
                    st.append(p)
                    
        return len(st) == 0
                       
                