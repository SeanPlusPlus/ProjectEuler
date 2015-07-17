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
	N := 1000
	for x := 3; x <= N; x++ {
		y := x + 1
		z := y + 1
		for z <= N {
			for z*z < x*x+y*y {
				z = z + 1
			}
			if z*z == x*x+y*y {
				fmt.Println(x)
				fmt.Println(y)
				fmt.Println(z)
				fmt.Println(x * y * z)
				fmt.Println("\n")
				if x+y+z == 1000 {
					return
				}
			}
			y = y + 1
		}
	}
}
