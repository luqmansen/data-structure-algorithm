package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strings"
    "math"
)

/*
 * Complete the 'makeAnagram' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING a
 *  2. STRING b
 */

func makeAnagram(a string, b string) int32 {
    stringA := strings.Split(a, "")
    stringB := strings.Split(b, "")

    stringDictA := make(map[string]int)
    stringDictB := make(map[string]int)

    for _, val := range stringA {
        if _, found := stringDictA[val]; found {
            stringDictA[val] = stringDictA[val] + 1
        } else {
            stringDictA[val] = 1
        }

    }
    for _, val := range stringB {
        if _, found := stringDictB[val]; found {
            stringDictB[val] = stringDictB[val] + 1
        } else {
            stringDictB[val] = 1
        }
    }
    

    var toRemove int32
    for keyA, amtA := range stringDictA {
        if amtB, found := stringDictB[keyA]; found {
            if amtA > amtB {
                toRemove += int32(math.Abs(float64(amtA - amtB)))                
            } 

        } else {
            toRemove += int32(amtA)

        }
    }

    for keyB, amtB := range stringDictB {
        if amtA, found := stringDictA[keyB]; found {
            if amtB > amtA {
                toRemove += int32(math.Abs(float64(amtA - amtB)))
            }
        } else {
            toRemove += int32(amtB)

        }
    }
    
    return toRemove
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    a := readLine(reader)

    b := readLine(reader)

    res := makeAnagram(a, b)

    fmt.Fprintf(writer, "%d\n", res)

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
