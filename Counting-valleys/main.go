package main

import (
	"bufio"
	"fmt"
	"io"
	"strings"
)

// Complete the countingValleys function below.
func countingValleys(n int32, s string) int32 {

	var valley int32
	var count int

	r := bufio.NewReader(strings.NewReader(s))
	for {
		if c, _, err := r.ReadRune(); err != nil {
			if err == io.EOF {
				break
			} else {
				fmt.Println(err)
			}
		} else {
			if string(c) == "U" {
				if count == -1 {
					valley++
				}
				count++
			} else {
				count--
			}
		}
	}

	return valley
}
