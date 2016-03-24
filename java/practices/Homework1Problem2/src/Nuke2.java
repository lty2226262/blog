import java.io.*;

public class Nuke2 {
	public static void main(String[] arg) throws Exception{
		BufferedReader keyboardInput;
		keyboardInput = new BufferedReader(new InputStreamReader(System.in));

		String inputLine;
		inputLine = keyboardInput.readLine();
		if (inputLine.length() < 2){
			System.out.println(inputLine);
		} else {
			System.out.println(inputLine.substring(0,1) + inputLine.substring(2));
		}
	} 
}
