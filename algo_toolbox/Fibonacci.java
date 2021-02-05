import java.util.*;
public class Fibonacci {
	static List<Integer> fibs = new ArrayList<Integer>(){{add(0); add(1);}};
	public static int calculate(int n) {
		if (n > fibs.size()) {
			int first = calculate(n - 1);
			int second = calculate(n - 2);
			fibs.add(first + second);
		} 
		return fibs.get(n - 1);
	}

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter a number: ");
		int n = s.nextInt();
		if (n < 1) {
			System.out.println("Invalid number");
			return;
		}
		System.out.println("The n-th element of the Fibonacci sequence is: " + calculate(n));
	}
}