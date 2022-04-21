/**
 * @author f4prime
 * @email zzz136454872@163.com
 */
#include"cpptools.h"
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>
#include<set>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
class Solution {
public:
    string toGoatLatin(string sentence) {
        int prev=0;
        vector<string> ss;
        for(int i=0;i<(int)sentence.size();i++) {
            if(sentence[i]==' ') {
                ss.push_back(sentence.substr(prev,i-prev));
                prev=i+1;
            }
        }
        ss.push_back(sentence.substr(prev));
        set<char> vowel=set<char>{'a','e','i','o','u','A','E','I','O','U'};
        string res="";
        string as="a";
        for(int i=0;i<(int)ss.size();i++) {
            string tmp;
            if(vowel.find(ss[i][0])==vowel.end()){
                tmp=ss[i].substr(1)+ss[i].substr(0,1);
            } else {
                tmp=ss[i];
            }
            tmp+="ma"+as;
            as+="a";
            res+=tmp;
            if(i!=(int)ss.size()-1) {
                res+=" ";
            }
        }
        return res;
    }
private:
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string sentence="I speak Goat Latin";
    // sentence = "The quick brown fox jumped over the lazy dog";
    cout<<sl.toGoatLatin(sentence)<<endl;
#endif 
    return 0;
}

