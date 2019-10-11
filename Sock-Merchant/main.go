package main

import (
"bufio"
"fmt"
"io"
	"os"
	"strconv"
	"strings"
)

func matchSock(n int32, ar []int32) int32 {

	var pair int32
	list := make(map[int32]int)

	for _, val := range ar {
		if _, ok := list[val]; ok {
			list[val] += 1
		} else {
			list[val] = 1
		}
	}
	fmt.Println(list)

	for _, value := range list {
		if value >= 2 {
			if value%2 == 1 {
				pair += int32((value - 1) / 2)
			} else {
				pair += int32(value/2)
			}
		} else {
			continue
		}
	}

	return pair

}

func main() {

	////sock := []int32{10, 20, 20, 10, 10, 30, 50, 10, 20}
	//sock2 := []int32{1, 1, 3, 1, 2, 1, 3, 3, 3, 3}
	//fmt.Println(matchSock(6, sock2))

	reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

	stdout, err := os.Create("OUTPUT_PATH")
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024 * 1024)

	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	n := int32(nTemp)

	arTemp := strings.Split(readLine(reader), " ")

	var ar []int32

	for i := 0; i < int(n); i++ {
		arItemTemp, err := strconv.ParseInt(arTemp[i], 10, 64)
		checkError(err)
		arItem := int32(arItemTemp)
		ar = append(ar, arItem)
	}

	result := matchSock(n, ar)

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

