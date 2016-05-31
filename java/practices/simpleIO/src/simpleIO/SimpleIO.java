package simpleIO;

import java.io.*;
	
class SimpleIO{
	public static void main(String[] arg) throws Exception{
		BufferedReader keybd = new BufferedReader( new InputStreamReader(System.in));
		System.out.println(keybd.readLine());
	}
}
