// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        FullTime Employ1= new FullTime("Elon","Dev",1000);
        System.out.println(Employ1.getPay());
        System.out.println(Employ1.getNetPay());
        Employ1.setTaxRate(30);
        System.out.println(Employ1.getNetPay());
        System.out.println(Employ1.toStr());
        PartTime Employ2 = new PartTime("Mark","deV",200);
        System.out.println(Employ2.getPay());
        System.out.println(Employ2.getNetPay());
        Employ2.setTaxRate(30);
        System.out.println(Employ2.getNetPay());
        System.out.println(Employ2.toStr());
    }
}