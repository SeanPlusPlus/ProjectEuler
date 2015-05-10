package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

// https://projecteuler.net/problem=3
//
// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

func main() {

	//target := 13195
	target := 600851475143
	var factors []int
	var primes []int

	// get primes from text file as slice of str elements
	primes_string, err := readLines("primes/list1000.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	// build primes slice with int elements
	for _, element := range primes_string {
		i, err := strconv.Atoi(element)
		if err == nil {
			primes = append(primes, i)
		} else {
			fmt.Println(err)
			os.Exit(2)
		}
	}

	// walk through primes, and if factor, append to slice
	for _, element := range primes {
		if (target % element) == 0 {
			target = (target / element)
			factors = append(factors, element)
		}
		if target == 1 {
			break
		}
	}

	// show us the factors
	fmt.Println(factors)
}

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {

	file, err := os.Open(path)

	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}
