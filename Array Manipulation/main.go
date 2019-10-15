package main

import (
	"bufio"
	"fmt"
	"io"
	"sort"
	"strconv"
	"strings"
)

// Complete the arrayManipulation function below.

func arrayManipulation(n int, queries [][]int) int {

	arr := make([]int, n)

	for j := 0; j < len(queries); j++ {
		for k := queries[j][0] - 1; k <= queries[j][1]-1; k++ {
			arr[k] += queries[j][2]
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	return arr[0]
}

func arrayManipulation2(n int, queries [][]int) int {

	arr := make([]int, n+2)

	for j := 0; j < len(queries); j++ {

		arr[queries[j][0]] += queries[j][2]
		arr[(queries[j][1])+1] -= queries[j][2]

	}
	for i:= 1; i < len(arr); i++{
		arr[i] += arr[i-1]
	}
	sort.Slice(arr, func(i,j int) bool {
		return  arr[i] > arr[j]
	})
	return arr[0]

}

func main() {
	//q := [][]int{{1, 2, 100}, {2, 5, 100}, {3, 4, 100}}
	//q := [][]int{{2, 6, 8}, {3, 5, 7}, {1, 8, 1}, {5, 9, 15}}
	//x := arrayManipulation2(5, q)
	//fmt.Println(x)
	reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

	//stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	stdout, err := os.Create("OUTPUT_PATH")
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024 * 1024)

	nm := strings.Split(readLine(reader), " ")

	nTemp, err := strconv.ParseInt(nm[0], 10, 64)
	checkError(err)
	n := int32(nTemp)

	mTemp, err := strconv.ParseInt(nm[1], 10, 64)
	checkError(err)
	m := int32(mTemp)

	var queries [][]int32
	for i := 0; i < int(m); i++ {
		queriesRowTemp := strings.Split(readLine(reader), " ")

		var queriesRow []int32
		for _, queriesRowItem := range queriesRowTemp {
			queriesItemTemp, err := strconv.ParseInt(queriesRowItem, 10, 64)
			checkError(err)
			queriesItem := int32(queriesItemTemp)
			queriesRow = append(queriesRow, queriesItem)
		}

		if len(queriesRow) != int(3) {
			panic("Bad input")
		}

		queries = append(queries, queriesRow)
	}

	result := arrayManipulation(n, queries)

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
