import java.util.Arrays;
public class Operator{
	String symbol;
	static String[] ALL_SYMBOLS = new String[]{"+","-","*","/","^", "log"};

	public Operator(String s){
		this.symbol = s;
		if (! Arrays.asList(ALL_SYMBOLS).contains(s)) {
			throw new IllegalArgumentException("Error, " + s + " is not a recognized symbol");
		}
	}

	public double calculate(double a, double b){
		switch (symbol){
			case "+":
				return a + b;
			case "-":
				return a - b;
			case "*":
				return a * b;
			case "/":
				return a / b;
			case "^":
				return Math.pow(a, b);
			case "log":
				return Math.log(b)/Math.log(a);
			default:
				return 0;
		}
	}

	public String format(double a, double b){
		if (symbol == "log"){
			return "log "+a+" " + b;
		}
		return ""+a+" "+ symbol + " " + b;
	}
}