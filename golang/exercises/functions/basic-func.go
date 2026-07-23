package main

import "fmt"

func add(a int, b int) int {
	return a + b
}
func main() {
	result := add(4, 6)
	fmt.Println(result)
}