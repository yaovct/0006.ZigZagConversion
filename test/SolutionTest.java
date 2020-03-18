// put source in src/Solution.java
// put test in test/SolutionTest.java
// https://stackoverflow.com/questions/42430188/junit-error-initializationerrororg-junit-runner-junitcommandlineparseresult
// javac src/Solution.java;javac -cp "junit-4.13.jar; hamcrest-core-1.3.jar;src/Solution.class;." test/SolutionTest.java;java -cp "junit-4.13.jar;hamcrest-core-1.3.jar;src/Solution.class;test/SolutionTest.class;." org.junit.runner.JUnitCore test.SolutionTest
package test;
import static org.junit.Assert.*;
import org.junit.*;
import src.Solution;

public class SolutionTest {
	Solution myClass = new Solution();
	
	@Test
	public void convert1() {
		String[] msg = new String[] {"ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya"};
		int[] row = {2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4};
		String[] ans = new String[] {"ACB","PAHNAPLSIIGYIR","PYAIHRNAPLSIIG","PINALSIGYAHRPI","abcbabcbb","bbbbb","pewkww","ddvf","bbbaldtu","nmfdppi","dedgfvf","jbbnwdpw","uvjukmecu","tumzxmt","omhdlvjh","avanij","ypfrzssuary"};

    for(int i=0; i<msg.length; i++) {
    	assertEquals(ans[i], myClass.convert(msg[i],row[i]));
    }
	}
}
