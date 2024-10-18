package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	port := "8080"

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		hostname, err := os.Hostname()
		if err != nil {
			http.Error(w, "Could not get hostname", http.StatusInternalServerError)
			return
		}
		helloMessage := fmt.Sprintf("Hello from the %s", hostname)
		fmt.Println(helloMessage)
		w.Header().Set("Content-Type", "text/html")
		w.Write([]byte(helloMessage))
	})

	fmt.Printf("Web server is listening at port %s\n", port)
	err := http.ListenAndServe(":"+port, nil)
	if err != nil {
		fmt.Println("Error starting the server:", err)
	}
}
