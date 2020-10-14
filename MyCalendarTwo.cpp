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
        int start;
        int end;
        //int type;

        Book(int start, int end)
        {
            this->start=start;
            this->end=end;
        }
        
        int cmp(Book& b)
        {
            if(b.start!=start)
                return start-b.start;
            return end-b.end;
        }

        void print()
        {
            cout<<"start: "<<start<<" end: "<<end<<endl;
        }
};

class MyCalendarTwo {
public:
    MyCalendarTwo() {}
    
    bool book(int start, int end) 
    {
        int l=0;
        int r=(int)books.size()-1;
        int mid;
        Book book = Book(start,end);
        int result;
        bool flag=false;
        if(start==60&&end==70)
            flag=true;
        while(l<=r)
        {
            mid=(l+r)/2;
            result=book.cmp(books[mid]);
            if(result>=0)
                l=mid+1;
            else if(result<0)
                r=mid-1;
        }
        if(flag)
        {
            for(int i=0;i<(int)books.size();i++)
                books[i].print();
        }
        int i;
        int leftMax=0;
        int rightMin=123456789;
        int leftCover=0;
        int rightCover=0;
        for(i=0;i<l;i++)
        {
            if(books[i].end>start)
            {
                if(++leftCover>=2)
                    return false;
                leftMax=max(leftMax,books[i].end);
            }
        }
        for(i=l;i<(int)books.size();i++)
        {
            if(books[i].start<end)
            {
                if(++rightCover>=2)
                    return false;
                rightMin=min(rightMin,books[i].start);
            }
        }
        if(leftMax>rightMin)
            return false;
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
    MyCalendarTwo mc;
    cout<<mc.book(33 ,44 )<<endl;
    cout<<mc.book(85 ,95 )<<endl;
    cout<<mc.book(20 ,37 )<<endl;
    cout<<mc.book(91 ,100)<<endl;
    cout<<mc.book(77 ,87 )<<endl;
    cout<<mc.book(42 ,61 )<<endl;
    cout<<mc.book(70 ,82 )<<endl;
    cout<<mc.book(5  ,17 )<<endl;
    cout<<mc.book(16 ,26 )<<endl;
    cout<<mc.book(96 ,100)<<endl;
    cout<<mc.book(44 ,55 )<<endl;
    cout<<mc.book(58 ,73 )<<endl;
    cout<<mc.book(60 ,70 )<<endl;
#endif 
    return 0;
}

