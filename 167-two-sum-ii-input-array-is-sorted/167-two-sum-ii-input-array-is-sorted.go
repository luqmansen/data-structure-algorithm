func twoSum(numbers []int, target int) []int {
    for i := 0; i< len(numbers); i++{
        for j := i+1; j <len(numbers); j++{
            if j != i{
                if numbers[j] + numbers[i] == target{
                    return []int{i+1,j+1}
                }
            }
        }
    }
    
    return []int{}
    
}