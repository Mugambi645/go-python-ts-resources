package main

import (
	"net/http"
	"log"
	"io/ioutil"
	"fmt"
)
func main() {

	http.HandleFunc("/", func(rw http.ResponseWriter, r *http.Request) {
		log.Println("Hello World")
		d, err := ioutil.ReadAll(r.Body)
		if err != nil {
			log.Printf("Error reading body: %v", err)
			http.Error(rw, "Error reading body", http.StatusInternalServerError)
			return
		}
		log.Printf("Data %s", d)
		fmt.Fprintf(rw, "Hello %s", d)
	})
	http.HandleFunc("/goodbye", func(_ http.ResponseWriter, _ *http.Request) {
		log.Println("Goodbye World")
	})
	http.ListenAndServe(":9090", nil)

}