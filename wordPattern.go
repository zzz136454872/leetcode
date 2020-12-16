package main

import(
    "fmt"
    "strings"
    //"sort"
)

var testMod=false;

func test() {

}

func wordPattern(pattern string, s string) bool {
    strs:=strings.Split(s," ");
    if len(pattern)!=len(strs) {
        return false;
    }
    log:=map[rune]string{}
    log2:=map[string]rune{}
    for i,letter:=range pattern {
        if value,exists:=log[letter];exists {
            if value!=strs[i] {
                return false
            }
        } else {
            if _,exists:=log2[strs[i]];exists {
                return false;
            }
            log[letter]=strs[i]
            log2[strs[i]]=letter
        }
    }
    return true;
}

func main() {
    test()
    pattern := "aaaa"
    str := "dog cat cat dog"
    fmt.Println(wordPattern(pattern, str))
}
