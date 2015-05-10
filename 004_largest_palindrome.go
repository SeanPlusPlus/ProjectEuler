package main

import (
	"fmt"
	"strconv"
)

// https://projecteuler.net/problem=4
//
// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.

func isPalindrome(num int) bool {
	s := strconv.Itoa(num)
	distance := 0
	start := string(s[distance])
	end := string(s[len(s)-1-distance])
	if start == end {

	}
	return true
}

func main() {

	x := 998
	y := 999
	for {
		if isPalindrome((x * y)) {
			break
		} else {
			x -= 1
			y -= 1
		}
	}

}
