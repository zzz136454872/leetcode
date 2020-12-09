package main

import(
    "fmt"
    "strings"
    //"sort"
)

var testMod=false;

func test() {
    
}

func findWords(words []string) []string {
    out:=[]string{}
    log:=[26]int{}
    for _,v:= range "asdfghjkl" {
        log[v-'a']=1
    }
    for _,v:= range "zxcvbnm" {
        log[v-'a']=2
    }
    for _,word := range words {
        lower_word:=strings.ToLower(word)
        sameLine:=true
        for _,letter := range lower_word {
            if log[letter-'a']!=log[lower_word[0]-'a'] {
                sameLine=false
                break
            }
        }
        if sameLine {
            out=append(out,word)
        }
    }
    return out
}

func main() {
    if testMod {
        test()
    }
    inp:=[]string{"Hello", "Alaska", "Dad", "Peace"}
    fmt.Println(findWords(inp));
}
