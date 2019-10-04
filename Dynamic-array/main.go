package main

/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

//func dynamicArray(n int32, queries [][]int32) []int32  {
//	var ret []int32
//	var lastAns int
//	var s1, s0 []int32
//
//	for i, a:= range queries{
//		if a[0] == 1{
//
//			if i % 2 ==0 {
//				lastAns = ((int(a[1])^ lastAns)%2)
//				s0 = append(s0, a[2])
//			} else {
//				s1 = append(s1, a[2])
//			}
//		} else {
//			if ((int(a[1]) ^ lastAns)%2) == 1{
//				lastAns = int(s1[a[2]])
//				ret = append(ret, int32(lastAns))
//			} else {
//				lastAns = int(s0[a[2]])
//				ret = append(ret, int32(lastAns))
//			}
//		}
//	}
//
//	return ret
//}
//
//func main() {
//	reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)
//
//	stdout, err := os.Create("output")
//	checkError(err)
//
//	defer stdout.Close()
//
//	writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)
//
//	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")
//
//	nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
//	checkError(err)
//
//	n := int32(nTemp)
//
//	qTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
//	checkError(err)
//	q := int32(qTemp)
//
//	var queries [][]int32
//	for i := 0; i < int(q); i++ {
//		queriesRowTemp := strings.Split(strings.TrimRight(readLine(reader)," \t\r\n"), " ")
//
//		var queriesRow []int32
//		for _, queriesRowItem := range queriesRowTemp {
//			queriesItemTemp, err := strconv.ParseInt(queriesRowItem, 10, 64)
//			checkError(err)
//			queriesItem := int32(queriesItemTemp)
//			queriesRow = append(queriesRow, queriesItem)
//		}
//
//		if len(queriesRow) != 3 {
//			panic("Bad input")
//		}
//
//		queries = append(queries, queriesRow)
//	}
//
//	result := dynamicArray(n, queries)
//
//	for i, resultItem := range result {
//		fmt.Fprintf(writer, "%d", resultItem)
//
//		if i != len(result) - 1 {
//			fmt.Fprintf(writer, "\n")
//		}
//	}
//
//	fmt.Fprintf(writer, "\n")
//
//	writer.Flush()
//
//}
//
//func readLine(reader *bufio.Reader) string {
//	str, _, err := reader.ReadLine()
//	if err == io.EOF {
//		return ""
//	}
//
//	return strings.TrimRight(string(str), "\r\n")
//}
//
//func checkError(err error) {
//	if err != nil {
//		panic(err)
//	}
//}
