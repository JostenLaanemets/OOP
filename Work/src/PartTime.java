public class PartTime implements Worker{
    String Name;
    String workType;
    double Salary;
    double taxRate=20;

    public PartTime(String Name ,String workType , double Salary) {
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
        this.taxRate = taxRate;
    }
    @Override
    public String toStr() {
        return "PartTime{" +
                "Name='" + Name + '\'' +
                ", workType='" + workType + '\'' +
                ", Salary=" + Salary +
                ", taxRate=" + taxRate +
                '}';
    }
}
