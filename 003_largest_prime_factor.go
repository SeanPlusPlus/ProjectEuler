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

	target := 13195

	primes, err := readLines("primes/list1000.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	i, err := strconv.Atoi(primes[2])
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	}

	if (target % i) == 0 {
		fmt.Println(target / i)
	}

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
