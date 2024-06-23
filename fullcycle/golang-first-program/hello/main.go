package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Carro struct {
	Nome   string
	Modelo string
	Ano    int
}

func (c Carro) Andar() {
	fmt.Println("O carro " + c.Nome + " está andando")
}

func (c Carro) Parar() {
	fmt.Println("O carro " + c.Nome + " está parando")
}

func main() {
	//carro1 := Carro{Nome: "Ford", Modelo: "Mustang", Ano: 1969}
	carro2 := Carro{Nome: "Chevrolet", Modelo: "Camaro", Ano: 1969}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		json.NewEncoder(w).Encode(carro2)
	})

	//carro2.Andar()
	//carro1.Parar()

	//fmt.Println(carro1.Nome)
	//fmt.Println(carro2.Nome)

	//fmt.Println(carro1.Nome)
	//fmt.Println(carro2.Nome)

	http.ListenAndServe(":8080", nil)
}
