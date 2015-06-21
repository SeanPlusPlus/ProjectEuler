package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// https://projecteuler.net/problem=8
//
// The four adjacent digits in the 1000-digit number that have the greatest
// product are 9 × 9 × 8 × 9 = 5832.
//
//73167176531330624919225119674426574742355349194934
// ...
//71636269561882670428252483600823257530420752963450
//
// Find the thirteen adjacent digits in the 1000-digit number that have
// the greatest product. What is the value of this product?

func numAsString() string {

	// save s to string
	s :=
		`73167176531330624919225119674426574742355349194934
 		96983520312774506326239578318016984801869478851843
 		85861560789112949495459501737958331952853208805511
 		12540698747158523863050715693290963295227443043557
 		66896648950445244523161731856403098711121722383113
 		62229893423380308135336276614282806444486645238749
 		30358907296290491560440772390713810515859307960866
 		70172427121883998797908792274921901699720888093776
 		65727333001053367881220235421809751254540594752243
 		52584907711670556013604839586446706324415722155397
 		53697817977846174064955149290862569321978468622482
 		83972241375657056057490261407972968652414535100474
 		82166370484403199890008895243450658541227588666881
 		16427171479924442928230863465674813919123162824586
 		17866458359124566529476545682848912883142607690042
 		24219022671055626321111109370544217506941658960408
 		07198403850962455444362981230987879927244284909188
 		84580156166097919133875499200524063689912560717606
 		05886116467109405077541002256983155200055935729725
 		71636269561882670428252483600823257530420752963450`

	// remove newlines, tabs, and whitespace
	s = strings.Replace(s, "\n", "", -1)
	s = strings.Replace(s, "\t", "", -1)
	s = strings.Replace(s, " ", "", -1)
	return s
}

func main() {

	// get the numbers and build array
	numbers := make(chan string)
	go func() { numbers <- numAsString() }()
	str := <-numbers
	arr := strings.Split(str, "")

	// init variables to solver our problem
	highest_product := 0
	series_length := 13
	end_idx := (len(arr) - (series_length - 1))

	for start_idx := 0; start_idx < end_idx; start_idx++ {
		p := 1
		var nums []string

		// build array of nums
		for i := 0; i <= (series_length - 1); i++ {
			num := arr[start_idx+i]
			nums = append(nums, num)

			// cast num to int and build product
			number, err := strconv.Atoi(num)
			if err != nil {
				fmt.Println(err)
				os.Exit(2)
			}
			p *= number
		}

		// check if this product is now champion
		if p > highest_product {
			highest_product = p
			fmt.Println(p)
			fmt.Println(nums)
		}
	}
}
