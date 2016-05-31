import java.io.*;
import java.net.*;

class OpenCommercial {
	public static void main(String[] arg) throws Exception {

		BufferedReader keyboard;
		String inputLine;

		keyboard = new BufferedReader(new InputStreamReader(System.in));

		System.out.print("Please enter the name of a company (without spaces): ");
		System.out.flush();        /* Make sure the line is printed immediately. */
		inputLine = keyboard.readLine();
		keyboard.close();

		String webSite;
		webSite = ("http://www." + inputLine + ".com");
		URL webPage = new URL(webSite);
		URLConnection conn = webPage.openConnection();


		String[] bufferString;
		bufferString = new String[5];
		
		BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
		int bufferStringCount;
		for (bufferStringCount = 0; bufferStringCount < 5;bufferStringCount++){
			if((bufferString[bufferStringCount] = br.readLine()) == null) break;
		}
		if (bufferStringCount == 5){
			for(int i = 4; i >= 0; i--){
				System.out.println(bufferString[i]);
			}
		} else {
			for(int i = bufferStringCount; i >= 0; i--){
				System.out.println(bufferString[i]);
			}
		}

	}
}