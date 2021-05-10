package V001.Design_Patterns_Video_Tutorial_1;

public class Animal {
    private String name;

    private int weight;
    private String sound;

    public Animal() {
    }

    public Animal(String name, int weight, String sound) {
        this.name = name;
        this.weight = weight;
        this.sound = sound;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getWeight() {
        return this.weight;
    }

    public void setWeight(int weight) {
        if (weight > 0) {
            this.weight = weight;
        } else {
            System.out.println("Weight must be bigger than 0");
        }
    }

    public String getSound() {
        return this.sound;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

}