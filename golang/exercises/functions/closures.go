package main

import "fmt"

func makeCounter() func() int {
	count := 0 // Enclosed variable
	return func() int {
		count++
		return count
	}

}

func main() {
    counterA := makeCounter()
    fmt.Println(counterA()) // Output: 1
    fmt.Println(counterA()) // Output: 2

    counterB := makeCounter() // Separate instance and counter state
    fmt.Println(counterB()) // Output: 1
}