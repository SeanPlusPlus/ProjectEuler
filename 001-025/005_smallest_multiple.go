package main

import "fmt"

// https://projecteuler.net/problem=5
//
// 2520 is the smallest number that can be divided by each of the
// numbers from 1 to 10 without any remainder.
//
// What is the smallest positive number that is evenly divisible
// by all of the numbers from 1 to 20?

func divisibleByRange(num int, rangeBound int) bool {
	for i := 1; i <= rangeBound; i++ {
		if num%i != 0 {
			return false
		}
	}
	return true
}

func main() {

	num := 20
	rangeBound := 20

	for {
		if divisibleByRange(num, rangeBound) {
			fmt.Println(num)
			return
		} else {
			num += 1
		}
	}

}
