package main
import "fmt"

func modifyValue(val int) {
	val = 100 // Changes local copy only
}
func modifyPointer(val *int) {
	*val = 100 // Mutates value at the underlying memory address
}

func main() {
	x := 10
	modifyValue(x)
	fmt.Println(x)

	modifyPointer(&x)
	fmt.Println(x)
}