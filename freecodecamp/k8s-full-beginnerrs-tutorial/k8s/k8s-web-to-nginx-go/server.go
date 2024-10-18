package main

import (
	"fmt"
	"io/ioutil"
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

	http.HandleFunc("/nginx", func(w http.ResponseWriter, r *http.Request) {
		url := "http://nginx"
		resp, err := http.Get(url)
		if err != nil {
			http.Error(w, "Error fetching from nginx", http.StatusInternalServerError)
			return
		}
		defer resp.Body.Close()
		body, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			http.Error(w, "Error reading nginx response", http.StatusInternalServerError)
			return
		}
		w.Write(body)
	})

	http.HandleFunc("/jsonplaceholder", func(w http.ResponseWriter, r *http.Request) {
		url := "https://jsonplaceholder.typicode.com/todos"
		resp, err := http.Get(url)
		if err != nil {
			http.Error(w, "Error fetching from JSONPlaceholder", http.StatusInternalServerError)
			return
		}
		defer resp.Body.Close()
		body, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			http.Error(w, "Error reading JSONPlaceholder response", http.StatusInternalServerError)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		w.Write(body)
	})

	fmt.Printf("Web server is listening at port %s\n", port)
	err := http.ListenAndServe(":"+port, nil)
	if err != nil {
		fmt.Println("Error starting the server:", err)
	}
}
