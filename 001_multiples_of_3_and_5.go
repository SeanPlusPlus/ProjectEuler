package main

import (
	"fmt"

	"github.com/dustin/go-humanize"
)

// https://projecteuler.net/problem=1

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
