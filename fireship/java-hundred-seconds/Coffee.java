// The exemple code for fireship.io

//public class Coffee {
//
//  String blend;
//  boolean decaf;
//  int price;
//
//  Coffee(int price) {
//    price = price;
//  }
//
//  String brew() {
//    return ''
//  }
//
//}
//
//Coffee joe = new Coffee();
//
//coffeeMachine.listen(
//  (coffee) -> System.out.println("It's hot! ♨️ ")
//);

//Code fixing for the ChatGPT 4

public class Coffee {

    String blend;
    boolean decaf;
    int price;
  
    Coffee(int price) {
        this.price = price;
    }
  
    String brew() {
        return "Brewing...";
    }
  
    public static void main(String[] args) {
        Coffee joe = new Coffee(5);
        
        // Assuming coffeeMachine is an instance of a class with a listen method that takes a lambda
        CoffeeMachine coffeeMachine = new CoffeeMachine();
        coffeeMachine.listen((coffee) -> System.out.println("It's hot! ♨️"));
    }
  }
  
  class CoffeeMachine {
    // Assuming the CoffeeMachine has a listen method
    void listen(CoffeeListener listener) {
        Coffee coffee = new Coffee(5); // Simulate brewing a coffee
        listener.onBrewed(coffee);
    }
  }
  
  interface CoffeeListener {
    void onBrewed(Coffee coffee);
  }
  