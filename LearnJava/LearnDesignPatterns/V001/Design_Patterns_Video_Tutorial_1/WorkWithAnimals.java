package V001.Design_Patterns_Video_Tutorial_1;

public class WorkWithAnimals {
    public static void main(String[] args) {
        Dog fido = new Dog();

        fido.setName("Fido");
        System.out.println(fido.getName());

        fido.digHole();
        fido.setWeight(-1);

        int randNum = 10;
        fido.changeVar(randNum);
        System.out.println("randNum after method call: " + randNum);

        System.out.println("Name before method call: " + fido.getName());
        changeObjectName(fido);
        System.out.println("Name after method call: " + fido.getName());

    }

    public static void changeObjectName(Dog fido) {
        fido.setName("Marcus");
    }
}
