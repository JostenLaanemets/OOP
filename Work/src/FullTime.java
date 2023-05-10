
public class FullTime implements Worker {
    String Name;
    String workType;
    double Salary;
    double taxRate=20;

    public FullTime(String Name,String workType ,double Salary) {
        this.Name = Name;
        this.workType=workType;
        this.Salary = Salary;
    }
    @Override
    public double getPay() {
        return this.Salary;
    }
    @Override
    public double getNetPay() {
        return this.Salary-(this.Salary/100*this.taxRate);
    }
    @Override
    public void setTaxRate(double taxRate) {
        this.taxRate=taxRate;
    }
    @Override
    public String toStr() {
        return "FullTime{" +
                "Name='" + this.Name + '\'' +
                ", workType='" + this.workType + '\'' +
                ", Salary=" + this.Salary +
                ", taxRate=" + this.taxRate +
                '}';
    }
}
