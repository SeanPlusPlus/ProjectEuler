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

	a := 3
	b := 4
	c := 5

	multiplier := 1

	for {
		x := a * multiplier
		y := b * multiplier
		z := c * multiplier
		multiplier = (multiplier + 1)

		//a_sq := x * x
		//b_sq := y * y
		//c_sq := z * z

		//fmt.Println(a_sq)
		//fmt.Println(b_sq)
		//fmt.Println(c_sq)

		fmt.Println(x)
		fmt.Println(y)
		fmt.Println(z)

		sum := x + y + z
		fmt.Println(sum)
		fmt.Printf("\n")

		if sum >= 1000 {
			return
		}

	}
}
