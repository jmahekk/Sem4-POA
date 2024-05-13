#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
int checkHit(int incomingPage,int queue[],int occupied)
{
    for(int i=0;i<occupied;i++)
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
    for(int i=0;i<occupied;i++)
    {
        printf("%d\t",queue[i]);
    }
}

void main()
{
    int n,pages,frames,queue[200],incomingStream[200],occupied=0,fault=0,hit=0;
    printf("enter the no of frames: ");
    scanf("%d",&frames);
    printf("enter the no of page references: ");
    scanf("%d",&pages);
    printf("enter the pages :");
    for(int i=0;i<pages;i++)
    {
        scanf("%d",&incomingStream[i]);
    }

    printf("F1\tF2\tF3\n");

    for(int i=0;i<pages;i++)
    {
        if(checkHit(incomingStream[i],queue,occupied))
        {
            hit++;
            print_frame(queue,occupied);
        }
        else if (occupied<frames)
        {
            queue[occupied]=incomingStream[i];
            fault++;
            occupied++;
            print_frame(queue,occupied);
        }
        else
        {
            int max=INT_MIN,dist[200],k,index,j;
            for(j=0;j<frames;j++)
            {
                dist[j]=0;
                for(k=i-1;k>=0;k--)
                {
                    ++dist[j];
                    if(queue[j]==incomingStream[k])
                    {
                        break;
                    }
                }

                if(dist[j]>max)
                {
                    max=dist[j];
                    index=j;
                }

            }

            queue[index]=incomingStream[i];
            print_frame(queue,occupied);
            fault++;
        }
        printf("\n");
    }

    printf("hit percentage: %.2f%%",((float)hit/pages)*100);
    printf("fault percentage: %.2f%%",((float)fault/pages)*100);



}