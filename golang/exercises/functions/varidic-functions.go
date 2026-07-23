package main

import "fmt"

func sumAll(numbers ...int) int {
    total := 0
    // 'numbers' behaves as a slice []int inside the function
    for _, num := range numbers {
        total += num
    }
    return total
}

func main() {
    fmt.Println(sumAll(1, 2, 3))        // Output: 6
    fmt.Println(sumAll(10, 20, 30, 40)) // Output: 100

    // Unpacking a slice into a variadic argument
    nums := []int{5, 10, 15}
    fmt.Println(sumAll(nums...))        // Output: 30
}