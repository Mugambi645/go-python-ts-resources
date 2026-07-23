package main

import (
	"errors"
	"fmt"
)

func divide(numerator, denominator float64) (float64, error) {
	if denominator == 0 {
		return 0, errors.New("cannot divide by zero")
	}
	return numerator / denominator, nil
}

func main() {
	result, err := divide(10, 2)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println("Result:", result)
}