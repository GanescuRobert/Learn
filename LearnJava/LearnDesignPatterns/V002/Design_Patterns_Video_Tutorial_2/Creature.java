package V002.Design_Patterns_Video_Tutorial_2;

abstract public class Creature {
    protected String name;
    protected int weight;
    protected String sound;

    public abstract void setName(String newName);
    public abstract String getName();

    public abstract void setWeight(double Weight);
    public abstract void getWeight();
}
