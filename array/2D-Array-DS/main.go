package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
)

// Complete the hourglassSum function below.
func hourglassSum(a [][]int32) int32 {
	var sum []int32
	for i, b := range a {
		if i > 0 && i < len(a)-1 {
			for j := range b {
				if j > 0 && j < len(b)-1 {
					up := a[i-1][j-1] + a[i-1][j] + a[i-1][j+1]
					mid := a[i][j]
					down := a[i+1][j-1] + a[i+1][j] + a[i+1][j+1]
					sum = append(sum, up+mid+down)
					fmt.Println(sum)
				}
			}
		}
		fmt.Println("\n")
	}
	sort.Slice(sum, func(i, j int) bool { return sum[i] < sum[j] })
	ret := sum[len(sum)-1]
	fmt.Println(sum)
	return ret
}

func main() {

	//arr := [][]int32{
	//	{-1, -1, 0, -9, -2, -2},
	//	{-2, -1, -6, -8, -2, -5},
	//	{-1, -1, -1, -2, -3, -4},
	//	{-1, -9, -2, -4, -4, -5},
	//	{-7, -3, -3, -2, -9, -9},
	//	{-1, -3, -1, -2, -4, -5},
	//}
	//
	//ret := hourglassSum(arr)
	//fmt.Print(ret)

	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create("output")
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	var arr [][]int32
	for i := 0; i < 6; i++ {
		arrRowTemp := strings.Split(readLine(reader), " ")

		var arrRow []int32
		for _, arrRowItem := range arrRowTemp {
			arrItemTemp, err := strconv.ParseInt(arrRowItem, 10, 64)
			checkError(err)
			arrItem := int32(arrItemTemp)
			arrRow = append(arrRow, arrItem)
		}

		if len(arrRow) != int(6) {
			panic("Bad input")
		}

		arr = append(arr, arrRow)
	}

	result := hourglassSum(arr)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
