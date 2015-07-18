package main

import "fmt"

// https://projecteuler.net/problem=10
//
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.

// Send the sequence 2, 3, 4, ... to channel 'ch'.
func Generate(ch chan<- int) {
	for i := 2; ; i++ {
		ch <- i // Send 'i' to channel 'ch'.
	}
}

// Copy the values from channel 'in' to channel 'out',
// removing those divisible by 'prime'.
func Filter(in <-chan int, out chan<- int, prime int) {
	for {
		i := <-in // Receive value from 'in'.
		if i%prime != 0 {
			out <- i // Send 'i' to 'out'.
		}
	}
}

// The prime sieve: Daisy-chain Filter processes.
func main() {
	ceiling := 2000000
	ch := make(chan int) // Create a new channel.
	go Generate(ch)      // Launch Generate goroutine.
	sum := 0
	for {
		prime := <-ch
		fmt.Println(prime)

		if prime > ceiling {
			fmt.Println("* sum *")
			fmt.Println(sum)
			break
		}

		sum += prime
		ch1 := make(chan int)
		go Filter(ch, ch1, prime)
		ch = ch1
	}
}
