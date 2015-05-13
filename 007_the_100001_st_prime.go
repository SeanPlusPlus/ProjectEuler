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
	return false
}

func main() {
	var primes []int
	i := 2
	for {
		if isPrime(i) {
			primes = append(primes, i)
		}
		if len(primes) == 10001 {
			break
		}
		i += 1
	}
	fmt.Println(primes[len(primes)-1])
}
