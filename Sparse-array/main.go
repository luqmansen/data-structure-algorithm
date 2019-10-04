package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"

	"strings"
)

//Idea behind this function
// - convert strings  as dictionary, for ease of search
// - if key is exist, add its value +1
// - iterate for each item in query, find the value of the key
func matchingStrings(strings []string, queries []string) []int {

	result := make([]int, len(queries))
	input := make(map[string]int, len(strings))

	for _, s := range strings {
		if _, ok := input[s]; ok {
			input[s] += 1
		} else {
			input[s] = 1
		}
	}

	for i, k := range(queries){
		if _, ok := input[k]; ok{
			result[i] = input[k]
		}
	}

	return result
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024 * 1024)

	stringsCount, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)

	var strings []string

	for i := 0; i < int(stringsCount); i++ {
		stringsItem := readLine(reader)
		strings = append(strings, stringsItem)
	}

	queriesCount, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)

	var queries []string

	for i := 0; i < int(queriesCount); i++ {
		queriesItem := readLine(reader)
		queries = append(queries, queriesItem)
	}

	//This is for testing purposes
	//s := []string{"aba","baba", "aba","xzxb"}
	//q := []string{ "aba", "xzxb", "ab"}

	//matchingStrings(s, q)
	res := matchingStrings(strings, queries)


	for i, resItem := range res {
		fmt.Fprintf(writer, "%d", resItem)

		if i != len(res) - 1 {
			fmt.Fprintf(writer, "\n")
		}
	}

	fmt.Fprintf(writer, "\n")

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
