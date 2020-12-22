package main

import(
    "fmt"
    //"strings"
    //"sort"
)

func int_min(inp... int) int {
    out:=inp[0]
    for _,v := range inp {
        if out>v {
            out=v
        }
    }
    return out
}

var testMod=false;

func test() {
}

func main() {
    test()
    fmt.Printf("%d\n",1);
}
