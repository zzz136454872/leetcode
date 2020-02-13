#include<stdio.h>
#include<stdlib.h>


double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int loc1=0, loc2=0;
    int loc = (nums1Size+nums2Size) >> 1;
    int even=0;
    if(loc << 1 == nums1Size + nums2Size)
    {
        even=1;
    }
    else
    {
        loc+=1;
    }
    double out;
    int min;
    printf("%d\n",loc);
    //pout = (double*)malloc(sizeof(double)*nums);
    while(loc-- > 0)
    {
        if(loc1<nums1Size&&loc2<nums2Size)
        {
            if(nums1[loc1]<nums2[loc2])
            {

                min=nums1[loc1];
                loc1++;
            }
            else
            {
                min=nums2[loc2];
                loc2++;
            }
        }
        else if(loc1 < nums1Size)
        {
            min=nums1[loc1];
            loc1++;
        }
        else 
        {
            min=nums2[loc2];
            loc2++;
        }
    }
    out = min;
    if(even)
    {
        if(loc1<nums1Size&&loc2<nums2Size)
        {
            if( nums1[loc1] < nums2[loc2])
            {

                min=nums1[loc1];
                loc1++;
            }
            else
            {
                min=nums2[loc2];
                loc2++;
            }
        }
        else if(loc1 < nums1Size)
        {
            min=nums1[loc1];
            loc1++;
        }
        else 
        {
            min=nums2[loc2];
            loc2++;
        }
    }
    out = (out+min)/2;
    return out; 
}

int main()
{
    int nums1[] = {1, 2};
    int nums2[] = {3, 4};
    double test= findMedianSortedArrays(nums1,2,nums2,2);
    printf("%lf\n",test);
    return 0;
}




