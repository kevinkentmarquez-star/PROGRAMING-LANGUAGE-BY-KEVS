import java.util.Scanner;

public class Main {
  public static void main(String[] args) {

    System.out.println("=======================================");
    System.out.println("STUDENT PERFORMANCE MONITORING SYSTEM");
    System.out.println("=======================================");

    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter your name: ");
    String name = scanner.nextLine();
    
    System.out.print("Enter your age: ");
    int age = Integer.parseInt(scanner.nextLine());

    System.out.print("Enter your HCI SCORE ( 0 - 100): ");
    double hci = Double.parseDouble(scanner.nextLine());

    System.out.print("Enter your CC103 Score (0 - 100): ");
    double CC103 = Double.parseDouble(scanner.nextLine());
    
    System.out.print("Enter your NET2 Score (0 - 100): ");
    double net2 = Double.parseDouble(scanner.nextLine());

    double average = (hci + CC103 + net2) / 3.0;

    System.out.println("\n === STUDENT SUMMARY ===");
    System.out.println("Name: "+ name);
    System.out.println("Age: "+ age);
    System.out.println("HCI SCORE: "+ hci);
    System.out.println("CC103: "+ CC103);
    System.out.println("NET2: "+ net2);
    System.out.printf("Average Score: % 2f\n", average);

    if (average >= 75.0) {
      System.out.println("STATUS: PASSED");
    }
    else {
      System.out.println("STATUS: FAILED");
    }
  }
}

