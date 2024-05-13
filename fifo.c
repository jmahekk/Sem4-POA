#include<stdio.h>
int np,nf,i,j,fifo_pointer=0,hit=0,fault=0;
int frames[100],pages[100];

int find(int x)
{
    int k;
    for(k=0;k<nf;k++)
    {
        if(frames[k]==x)
        {
            return 1;
        }
    }
    return 0;
}

void print_frame()
{
    int k;
    for(k=0;k<nf;k++)
    {
        if(frames[k]==-1)
        {
            printf("-/t");
        }
        else{
            printf("%d\t",frames[k]);
        }
    }
    printf("\n");
}


void main()
{
    printf("enter the number of frames: ");
    scanf("%d",&nf);
    printf("enter the number of pages: ");
    scanf("%d",&np);
    printf("enter the pages: ");
    for(i=0;i<np;i++)
    {
        scanf("%d",&pages[i]);
    }

    for(i=0;i<nf;i++)
    {
        frames[i]=-1;
    }

    for(i=0;i<nf;i++)
    {
        printf("%d\t",i+1);
    }
    printf("\n");

    for(i=0;i<np;i++)
    {
        if(find(pages[i]))
        {
            hit++;
            print_frame();
        }

        else
        {
            for(j=0;j<nf;j++)
            {
                if(frames[i]==-1)
                {
                    fault++;
                    frames[j]=pages[i];
                    print_frame();
                    break;
                }
            }

            if(j==nf)
            {
                fault++;
                frames[fifo_pointer]=pages[i];
                fifo_pointer=(fifo_pointer+1)%nf;
                print_frame();
            }
        }
    }

float hits=(hit/np)*100;
float faults=(fault/np)*100;
printf("page hits are %d",hits);

printf("page fauts are %d",faults);







}