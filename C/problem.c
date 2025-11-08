#include <stdio.h>

char* checkLeap(int n) {
    if (n % 100 == 0) {
        if (n % 400 == 0) {
            return "Leap Year";
        } else {
            return "Not Leap Year";
        }
    } else {
        if (n % 4 == 0) {
            return "Leap Year";
        } else {
            return "Not Leap Year";
        }
    }
}
int sample(int data){
    switch(data){
        case 1:
            printf("hello");
            break;
        case 2:
            printf("boy");
            break;
        default:
            printf("default");
            
    }
}
int main() {
    int m;
    printf("Enter the Year: ");
    scanf("%d", &m);
    printf("%s\n", checkLeap(m));
    sample(m);
    return 0;
}
// sum of digits
 int n=123,sum=0;
    while (n>0){
        sum+=n%10;
        n=n/10;
    }
    printf("%d",sum);
//armstrong number
#include <stdio.h>
#include <math.h>
void main(){
    int n=153,digit=0,sum=0,c=0;
    c=n;
    while(c>0){
        c=c/10;
        digit++;
    }
    c=n;
    while(c>0){
        sum=sum+pow((c%10),digit);
        c=c/10;
    }
    c=n;
    if(c==n){
        printf("armstrong number");
    }
    else{
        printf("not a armstrong number");
    }
}

