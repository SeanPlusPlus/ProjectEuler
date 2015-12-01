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

func isPalindrome(num int, distance int) int {

	num_str := strconv.Itoa(num)
	left_idx := distance
	right_idx := len(num_str) - 1 - distance

	if (right_idx - left_idx) < 1 {
		fmt.Println(num_str)
		return num
	}

	left_char := string(num_str[left_idx])
	right_char := string(num_str[right_idx])

	if left_char == right_char {
		distance += 1
		return isPalindrome(num, distance)
	} else {
		fmt.Println(num_str)
		return 0
	}
}

func main() {

	largest_palindrome := 0
	x := 998
	y := 999
	for {
		fmt.Println(x)
		fmt.Println(y)
		answer := isPalindrome((x * y), 0)
		if answer != 0 {
			if answer > largest_palindrome {
				largest_palindrome = answer
			}
		}
		x -= 1
		if x == 100 {
			y -= 1
			x = y - 1
		}
		if y == 101 {
			fmt.Println(largest_palindrome)
			return
		}
	}

}
