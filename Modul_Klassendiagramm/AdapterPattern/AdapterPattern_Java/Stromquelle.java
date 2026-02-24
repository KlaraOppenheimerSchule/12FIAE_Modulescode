public class Stromquelle implements Energiequelle {

    private int spannung;
    private double maximalerStrom;

    public Stromquelle(int spannung, double maximalerStrom) {
        this.spannung = spannung;
        this.maximalerStrom = maximalerStrom;
    }

    @Override
    public int getSpannung() {
        return spannung;
    }

    @Override
    public double getMaximalerStrom() {
        return maximalerStrom;
    }
}