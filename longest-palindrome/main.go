package main

import (
	"fmt"
	"github.com/luqmansen/data-structure-algorithm/utils"
	"strings"
	"time"
)

func longestPalindrome(s string) string {
	split := strings.Split(s, "")

	if len(utils.ListToSet(split)) == 1 {
		return strings.Join(split, "")
	}

	i := 0
	j := 0
	maxLen := 0
	var maxPalindr []string
	for j < len(split) {
		substr := split[i : j+1]
		//join := strings.Join(substr, "")
		//fmt.Println(join)
		//if len(substr) > 1 { // one char must be palindrome
		if isPalindrome(substr) {
			if len(substr) > maxLen {
				maxLen = len(substr)
				maxPalindr = substr
			}
		}
		//}

		if j < len(split) {
			j++
			if j >= len(split) {
				j = i + 1 // reset j
				i++
			}
		}
	}
	return strings.Join(maxPalindr, "")

}
func isPalindrome(s []string) bool {
	//s := strings.Split(str, "")
	for i := 0; i < len(s); i++ {
		if s[i] == s[len(s)-1-i] {
			continue
		} else {
			return false
		}
	}
	return true
}

func main() {

	//fmt.Println(longestPalindrome("aabc")) // aa
	//fmt.Println(longestPalindrome("babad")) // bab
	//fmt.Println(longestPalindrome("cbbd")) // bb
	start := time.Now()
	fmt.Println(longestPalindrome("ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy")) // bb
	fmt.Println(time.Since(start))

	//fmt.Println(longestPalindrome("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")) // bb
}
