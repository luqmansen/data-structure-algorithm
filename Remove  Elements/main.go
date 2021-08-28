package main

import "fmt"

//func deleteElementAtIdx(arr []int, idx int){
//	for i, _ := range arr {
//		if i == idx{
//			if idx == 0 {
//				for j := i; j < len(arr)-1; j++ {
//					arr[j] = arr[j+1]
//				}
//			} else {
//				for j := i + 1; j < len(arr); j++ {
//					arr[j-1] = arr[j]
//				}
//			}}}
//	arr[len(arr)-1] = 0
//}
//var lenght int

//func removeElement(nums []int, val int) int {
//
//	for i, v := range nums {
//		if v == val{
//			deleteElementAtIdx(nums, i)
//			lenght++
//		}
//	}
//	for _, v := range nums{
//		if v == val{
//			removeElement(nums, val)
//		}
//	}
//
//	return len(nums) - lenght
//}

//func removeElement(nums []int, val int) int {
//	i := 0
//	n := len(nums) -1
//
//	for i<n{
//		if nums[i] == val{
//			nums[i] = nums[n-1]
//			n--
//		} else {
//			i++
//		}
//	}
//	return n
//}

func removeElement(nums []int, val int) int {
	n := 0
	// 0, 1, 2, 2, 3, 0, 4, 2
	// del 2
	for _, elem := range nums {
		if elem != val {
			nums[n] = elem
			n++
		}
	}
	return n
}

func removeElement2(nums []int, val int) int {

	res := make([]int, 0)
	for _, num := range nums {
		if num != val {
			res = append(res, num)
		}
	}
	copy(nums, res)
	return len(res)

}

func main() {
	//x := []int{2,2,3,0}
	//deleteElementAtIdx(x, 2)
	//fmt.Println(reflect.DeepEqual(x , []int{2,2,0,0}))
	//
	//x = []int{2,4,2,3,0}
	//deleteElementAtIdx(x, 1)
	//fmt.Println(reflect.DeepEqual(x , []int{2,2,3,0,0}))
	//
	//x = []int{2,2,3,9,2,8}
	//deleteElementAtIdx(x, 5)
	//fmt.Println(reflect.DeepEqual(x , []int{2,2,3,9,2,0}))
	//
	//x = []int{2,2,3,5,6,0}
	//deleteElementAtIdx(x, 0)
	//fmt.Println(reflect.DeepEqual(x , []int{2,3,5,6,0,0}))

	//x := []int{3,2,2,3}
	//deleteElementAtIdx(x, 0)
	//fmt.Println(reflect.DeepEqual(x , []int{2,2,3,0}))

	//x := []int{3,2,2,3}
	//res := removeElement(x, 3)
	//fmt.Println(x)
	//fmt.Println(res)

	x := []int{0, 1, 2, 2, 3, 0, 4, 2}
	res := removeElement2(x, 2)
	fmt.Println(x)
	//k := []int{0, 1, 2, 2, 3, 0, 4, 2}
	//res = removeElement(k, 2)
	fmt.Println(res)

}
