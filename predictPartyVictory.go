package main

import(
    "fmt"
    //"strings"
    //"sort"
)

var testMod=true;

func test() {

}

type node struct {
   name rune
   next *node
}

//Radiant(天辉)和 Dire(夜魇)
func predictPartyVictory(senate string) string {
    //table:=map[uint8]uint8{'D':'R','R':'D'}
    outTable:=map[rune]string{'D':"Dire",'R':"Radiant"}
    var head *node=nil
    var tail *node=nil
    for _,v := range senate {
        if head!=nil {
            tail.next=&node{v,nil}
            tail=tail.next
        } else {
            head=&node{v,nil}
            tail=head
        }
    }
    tail.next=head
    tmp:=head
    for true {
        other:=tmp
        for other.next.name==tmp.name {
            other=other.next
            if other.next==tmp {
                return outTable[tmp.name]
            }
        }
        //delete other.next
        other.next=other.next.next
        tmp=tmp.next
    }
    return "error"
}

func main() {
    test()
    inp:="RDD"
    fmt.Println(predictPartyVictory(inp))
}
