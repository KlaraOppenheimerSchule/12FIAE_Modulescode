public class Adapter implements Energiequelle {

    private final int spannung = 230; // Zielspannung
    private Stromquelle stromquelle;

    public Adapter(Stromquelle stromquelle) {
        this.stromquelle = stromquelle;
    }

    @Override
    public int getSpannung() {
        return spannung;
    }

    @Override
    public double getMaximalerStrom() {
        double faktor = (double) stromquelle.getSpannung() / spannung;
        return faktor * stromquelle.getMaximalerStrom();
    }
}