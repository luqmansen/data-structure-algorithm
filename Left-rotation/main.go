package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func leftRotation(arr []int32, d int) []int32 {

	if len(arr) == d {
		return arr
	} else {
		for i := 0; i < d; i++ {
			temp := arr[0]
			for j := 0; j < len(arr)-1; j++ {
				arr[j] = arr[j+1]
			}
			arr[len(arr)-1] = temp
		}
	}
	return arr
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	nd := strings.Split(readLine(reader), " ")

	nTemp, err := strconv.ParseInt(nd[0], 10, 64)
	checkError(err)
	n := int32(nTemp)

	dTemp, err := strconv.ParseInt(nd[1], 10, 64)
	checkError(err)
	d := int32(dTemp)

	aTemp := strings.Split(readLine(reader), " ")

	var a []int32

	for i := 0; i < int(n); i++ {
		aItemTemp, err := strconv.ParseInt(aTemp[i], 10, 64)
		checkError(err)
		aItem := int32(aItemTemp)
		a = append(a, aItem)
	}

	//For testing purposes
	//a := []int32{1, 2, 3, 4, 5}
	//fmt.Println(leftRotation(a, int(4)))

	ar := leftRotation(a, int(d))
	for _, k := range ar {
		fmt.Print(k, " ")
	}

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
