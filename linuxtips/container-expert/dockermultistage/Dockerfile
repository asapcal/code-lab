# syntax=docker/dockerfile:1
FROM golang:1.23 AS build
WORKDIR /src 
COPY <<EOF /src/main.go
packge main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
EOF
RUN go build -o /bin/hello ./main.go

FROM scratch
COPY --from=build /bin/hello /bin/hello
CMD ["/bin/hello"]