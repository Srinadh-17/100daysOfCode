bool isHappy(int n){
    int i=0,sum=0,num,r;
    while(n>0&&i!=15)
    {
        while(n>0)
        {
            r=n%10;
            sum=sum+r*r;
            n=n/10;
        }
        num=sum;
        if(num==1){
            return true;
        }
        else
        {
            i++;
            sum=0;
            n=num;
        }
    }
   return false;
}