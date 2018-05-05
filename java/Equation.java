public class Equation{
	double a;
	Operator op;
	double b;
	double res;
	public Equation(double a, double b, Operator op){
		this.a = a;
		this.b = b;
		this.op = op;
		this.res = op.calculate(a,b);
	}

	public String format(){
		return op.format(a,b) + " = " + res;   
	} 

}