import "strconv"

func evalRPN(tokens []string) int {
    var stack []int
    
    for _, t := range tokens {
        switch t {
            case "+":
                x := stack[len(stack)-1]
                y := stack[len(stack)-2]
                stack = stack[:len(stack)-2]
                stack = append(stack, x+y)
            case "-":
                x := stack[len(stack)-1]
                y := stack[len(stack)-2]
                stack = stack[:len(stack)-2]
                stack = append(stack, y-x)
            case "*":
                x := stack[len(stack)-1]
                y := stack[len(stack)-2]
                stack = stack[:len(stack)-2]
                stack = append(stack, x*y)
            case "/":
                x := stack[len(stack)-1]
                y := stack[len(stack)-2]
                stack = stack[:len(stack)-2]
                stack = append(stack, y/x)
            default:
                val, _ := strconv.Atoi(t)
                stack = append(stack, val)
        }
    }
    
    return stack[0]
}