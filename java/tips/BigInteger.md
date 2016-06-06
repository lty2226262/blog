#JAVA BIGINTEGER


##Big integer factorial

input: a number m

output: factorial of m

	import java.io.*;  
	import java.math.BigInteger;  
	import java.util.*;  
	  
	public class Main  
	{  
	    public static void main(String args[])  
	    {  
	        Scanner cin = new Scanner(System.in);     
	        int n = cin.nextInt();  
	        BigInteger ans = BigInteger.ONE;  
	        for(int i = 1; i <= n; ++i)  
	            ans = ans.multiply(BigInteger.valueOf(i));  
	        System.out.println(ans);  
	    }  
	}  
	
##Compare two big integers

	import java.io.*;
	import java.math.BigInteger;
	import java.util.*;
	
	public class Main
	{
		public static void main(String args[])
		{
			Scanner cin = new Scanner(System.in);	
			while(cin.hasNext())
			{
				BigInteger a = cin.nextBigInteger();
				BigInteger b = cin.nextBigInteger();
				if(a.equals(BigInteger.ZERO) && b.equals(BigInteger.ZERO))
					break;
				int flag = a.compareTo(b);
				if(flag == -1)
					System.out.println("a<b");
				else if(flag == 0)
					System.out.println("a==b");
				else
					System.out.println("a>b");
			}
		}
	}
	
##Big integer add

	import java.math.BigInteger;  
	import java.util.*;  
	import java.io.*;  
	  
	public class Main  
	{  
	    public static void main(String args[])  
	    {  
	        Scanner in = new Scanner(System.in);  
	        int n = in.nextInt();         
	        for(int i = 1; i <= n; ++i)  
	        {  
	            BigInteger a = in.nextBigInteger();  
	            BigInteger b = in.nextBigInteger();  
	            BigInteger ans = a.add(b);  
	            System.out.println("Case " + i + ":");  
	            System.out.println(a + " + " + b + " = " +ans);  
	        }  
	    }  
	}  