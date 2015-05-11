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

func isPalindrome(num int, distance int) bool {
	s := strconv.Itoa(num)
	distance := 0
	start := string(s[distance])
	end := string(s[len(s)-1-distance])

	// return true

	// check next value
	if start == end {
		return number + isPalindrome(number-1)
	} else {
		return false
	}
}

func main() {

	x := 998
	y := 999
	for {
		answer := isPalindrome((x * y), 0)
		if answer == true {
			break
		} else {
			x -= 1
			y -= 1
		}
	}

}
