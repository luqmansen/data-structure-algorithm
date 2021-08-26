package main

import (
	"fmt"
	"sort"
	"strings"
)

func countSentences(wordSet []string, sentences []string) []int {

	anagramDict := make(map[string][]string)
	for _, word := range wordSet {
		w := strings.Split(word, "")
		sort.Strings(w)
		key := strings.Join(w, "")
		anagramDict[key] = append(anagramDict[key], word)
	}

	numSentence := make([]int, 0)
	for _, s := range sentences {
		split := strings.Split(s, " ")
		comb := 1
		for _, word := range split {
			w := strings.Split(word, "")
			sort.Strings(w)
			key := strings.Join(w, "")
			if _, found := anagramDict[key]; found {
				comb = comb * len(anagramDict[key])
			}
		}
		numSentence = append(numSentence, comb)
	}

	fmt.Println(numSentence)
	return numSentence
}

func main() {

}
