package main

import (
	"bufio"
	"fmt"
	"io"
	"strconv"
	"strings"
)

/*
 * Complete the timeConversion function below.
 */

// Sorry this code is total mess and highly inefficient,
func timeConversion(s string) string {

	if strings.Contains(s ,"PM"){
		newString := strings.Split(s, "")
		x := newString[0] + newString[1]
		hour,_ := strconv.ParseInt(x, 10,0)
		var newhour int64
		if hour < 12{
			newhour = hour + 12
		} else {
			newhour = hour
		}
		newString[0] = string(strconv.Itoa(int(newhour))[0])
		newString[1] = string(strconv.Itoa(int(newhour))[1])
		ssss := strings.Join(newString, "")
		return strings.Replace(ssss, "PM", "", -1)
	} else{
		newString := strings.Split(s, "")
		x := newString[0] + newString[1]
		hour,_ := strconv.ParseInt(x, 10,0)
		var newhour int64
		if hour >= 12{
			newhour = hour - 12
		} else {
			newhour = hour
		}
		if newhour <= 9{
			newString[0] = "0"
			newString[1] = string(strconv.Itoa(int(newhour)))
		} else{
			newString[0] = string(strconv.Itoa(int(newhour))[0])
			newString[1] = string(strconv.Itoa(int(newhour))[1])
		}
		ssss := strings.Join(newString, "")
		return strings.Replace(ssss, "AM", "", -1)
	}
}

func main() {
	//reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)
	//
	//outputFile, err := os.Create(os.Getenv("OUTPUT_PATH"))
	//checkError(err)
	//
	//defer outputFile.Close()
	//
	//writer := bufio.NewWriterSize(outputFile, 1024 * 1024)
	//
	//s := readLine(reader)
	s := "12:05:45PM"
	//s := "06:05:45AM"
	fmt.Println(timeConversion(s))
	//result := timeConversion(s)

	//fmt.Fprintf(writer, "%s\n", result)
	//
	//writer.Flush()
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
