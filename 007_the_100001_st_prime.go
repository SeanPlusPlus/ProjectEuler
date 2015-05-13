package main

import "fmt"

// https://projecteuler.net/problem=7
//
// By listing the first six prime numbers:
// 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//
// What is the 10 001st prime number?

func isPrime(num int) bool {
	for i := 2; i <= num; i++ {
		if i == num {
			return true
		}
		if num%i == 0 {
			return false
		}
	}
}

func main() {
	for i := 2; i <= 12; i++ {
		fmt.Println(i)
		fmt.Println(isPrime(i))
	}
}
