
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []
        
        ops = {"+", "-", "*", "/"}
        
        for t in tokens:
            
            if t not in ops:
                st.append(int(t))
            else:
                if t == "+":
                    a = st.pop()
                    b = st.pop()
                    st.append(a + b)
                    
                elif t == "*":
                    a = st.pop()
                    b = st.pop()
                    st.append(a * b)
                    
                elif t == "-":
                    a = st.pop()
                    b = st.pop()
                    st.append(b - a)
                
                elif t == "/":
                    a = st.pop()
                    b = st.pop()
                    st.append(int(b / a))
                    
        return st[0]

                
            
            
        
        
        