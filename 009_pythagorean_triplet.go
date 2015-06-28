package main

import "fmt"

// https://projecteuler.net/problem=9
//
// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//
// a2 + b2 = c2
// For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

func main() {

	var nums [3]int
	nums[0] = 3
	nums[1] = 4
	nums[2] = 5

	for i := 0; i < len(nums); i++ {
		fmt.Println(nums[i] * nums[i])
	}

	fmt.Println(nums)
}
