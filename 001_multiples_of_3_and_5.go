package main

import (
	"fmt"

	"github.com/dustin/go-humanize"
)

// https://projecteuler.net/problem=1
//
// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

func main() {
	var limit int = 1000
	var sum int = 0
	for i := 1; i < limit; i++ {
		if i%3 == 0 {
			sum += i
		}
		if i%5 == 0 {
			sum += i
		}
	}
	var sum64 = int64(sum)
	fmt.Printf("%s\n", humanize.Comma(sum64))
}
