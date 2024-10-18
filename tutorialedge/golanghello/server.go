package main

import (
    "fmt"
    //"html"
    "log"
    "net/http"
)

func main() {

        http.Handle("/", http.FileServer(http.Dir("./static")))

    //http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    //    http.ServeFile(w, r, r.URL.Path[1:])
    //})


    //http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    //    fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
    //})

    http.HandleFunc("/hi", func(w http.ResponseWriter, r *http.Request){
        fmt.Fprintf(w, "Hi")
    })

    log.Fatal(http.ListenAndServe(":8000", nil))

}
