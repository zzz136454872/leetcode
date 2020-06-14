package main

import (
    "fmt"
    "sort"
)

func canBeEqual(target []int, arr []int) bool {
    sort.Ints(target)
    sort.Ints(arr)
    for i:=0;i<len(arr);i++  {
        if arr[i]!=target[i] {
            return false
        }
    }
    return true
}

func main() {
    target:= [...]int{1,2,3,4}
    arr:= [...]int{2,4,1,3}
    out:=canBeEqual(target[:],arr[:])
    fmt.Printf("%t\n",out);
    fmt.Printf("%d\n",1)
    fmt.Printf("%d\n",1)
}
