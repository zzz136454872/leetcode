/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */
#include"cpptools.h"
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
class Book
{
    public:
        Book(int start, int end)
        {
            this->start=start;
            this->end=end;
        }
        
        int getStart()
        {
            return start;
        }
        
        int getEnd()
        {
            return end;
        }

        int cmp(Book& b)
        {
            if(b.getStart()!=start)
                return start-b.getStart();
            return end-b.getEnd();
        }

        void print()
        {
            cout<<"start: "<<start<<" end: "<<end<<endl;
        }

    private:
        int start;
        int end;
};

class MyCalendar {
public:
    MyCalendar() {

    }
    
    bool book(int start, int end) {
        int l=0;
        int r=(int)books.size()-1;
        int mid;
        Book book = Book(start,end);
        int result;
        while(l<=r)
        {
            mid=(l+r)/2;
            result=book.cmp(books[mid]);
            if(result>0)
                l=mid+1;
            else if(result<0)
                r=mid-1;
            else
                return false;
        }
        if(l>0&&books[l-1].getEnd()>book.getStart())
        {
            return false;
        }
        if(l<(int)books.size()&&books[l].getStart()<book.getEnd())
        {
            return false;
        }
        vector<Book>::iterator iter=books.begin();
        books.insert(iter+l,book);
        return true;
    }
private:
    vector<Book> books;
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    MyCalendar mc;
    cout<<mc.book(37, 50)<<endl; // returns false
    cout<<mc.book(33, 50)<<endl; // returns false
    //cout<<mc.book(20, 30)<<endl; // returns true
#endif 
    return 0;
}

