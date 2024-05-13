#include<stdio.h>
#include<stdlib.h>

int checkHit(int incomingPage,int queue[],int occupied)
{
    int i;
    for(i=0;i<occupied;i++)
    {
        if(incomingPage==queue[i])
        {
            return 1;
        }
    }
    return 0;
}

void print_frame(int queue[],int occupied)
{
    int i;
    for(i=0;i<occupied;i++)
    {
        printf("%d\t",queue[i]);
    }
}

int predict(int incomingStream[],int queue[],int pages,int index,int occupied)
{
    int farthest=index,result=-1;
    for(int i=0;i<occupied;i++)
    {
        int j;
        for(j=index;j<pages;j++)
        {
            if(queue[i]==incomingStream[j])
            {
                if(j>farthest)
                {
                    farthest=j;
                    index=i;
                }
                break;
            }
        }
        if(j==pages)
        return i;
    }
    return (result==-1?0:result);
}

void optimalPage(int incomingStream[],int pages,int queue[],int frames)
{
    int occupied=0,fault=0,hit=0;
    for(int i=0;i<pages;i++)
    {
        if(checkHit(incomingStream[i],queue,occupied))
        {
            hit++;
            print_frame(queue,occupied);
        }
        else if(occupied<frames)
        {
            queue[occupied]=incomingStream[i];
            occupied++;
            fault++;
            print_frame(queue,occupied);
        }
        else{
            int pos=predict(incomingStream,queue,pages,i+1,occupied);
            queue[pos]=incomingStream[i];
            fault++;
            print_frame(queue,occupied);
        }
         printf("\n");
    }
    printf("hit percentage: %.2f%%",((float)hit/pages)*100);
    printf("fault percentage: %.2f%%",((float)fault/pages)*100);

}

int main()
{
    int frames,pages,incomingStream[100];
    printf("enter the number of frames: ");
    scanf("%d",&frames);
    printf("enter the number of pages: ");
    scanf("%d",&pages);
    printf("enter pages: ");
    for(int i=0;i<pages;i++)
        scanf("%d",&incomingStream[i]);
    int queue[frames];
    optimalPage(incomingStream,pages,queue,frames);
}