package V002.Design_Patterns_Video_Tutorial_2;

public class WorkWithAnimals {

    int justANum = 10;

    public static void main(String[] args) {
        Animal doggy = new Dog();
        Animal kitty = new Cat();

        System.out.println("doggy says: " + doggy.getSound());
        System.out.println("kitty says: " + kitty.getSound());

        Animal[] animals = new Animal[4];
        for (int i = 0; i < 4; i++) {
            animals[i] = new Dog();
            animals[++i] = new Cat();
        }
        for (int i = 0; i < 4; i++) {
            System.out.println(animals[i].getSound());
        }
        speakAnimal(doggy);

        // ! Animal.digHole() WRONG
        // ? doggy.digHole();
        // * Dog.digHole() CORRECT
        ((Dog) doggy).digHole();

        // ! CAN'T USE NON STATIC VARIABLE IN STATIC METHOD
        // ? System.out.println(justANum);
        // ! CAN'T USE NON STATIC METHOD IN STATIC METHOD
        // ? sayHello();

        // ! NOT VISIBLE
        Dog fido = new Dog();
        // ? fido.bePrivate();

        // ! VISIBLE
        fido.accessPrivate();

        Giraffe giraffe = new Giraffe();
        giraffe.setName("Frank");
        System.out.println(giraffe.getName());
    }

    public static void changeObjectName(Dog fido) {
        fido.setName("Marcus");
    }

    public static void speakAnimal(Animal randAnimal) {
        System.out.println(randAnimal.getSound());
    }

    public void sayHello() {
        System.out.println("Hello");
    }
}
