public class Calculator {
	Equation[] history;
	int cursor;

	public Calculator(){
		history = new Equation[100];
		cursor = 0;
	}

	public void clearHistory() {
		history = new Equation[100];
		cursor = 0;
	}

	public void showHistory(){
		for(int i = 0; i<cursor; i++){
			System.out.println(history[i].format());
		}
	}

	public double calculate(double a, Operator op, double b){
		Equation e = new Equation(a,b,op);
		history[cursor] = e;
		cursor ++ ;
		return e.res;
	}


	public static void main(String[] args) {
		Calculator c = new Calculator();
		Operator plus = new Operator("+");
		c.calculate(4,plus,6);
		c.showHistory();
	}
}

