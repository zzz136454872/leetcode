package main

import(
    "fmt"
    //"sort"
)

var testMod=false;

func test() {
}

func main() {
    if testMod {
        test()
    }
    fmt.Printf("%d\n",1);
}
