public class Geraet {

    private static final int BENOETIGTE_SPANNUNG = 230;
    private static final int BENOETIGTE_LEISTUNG = 1800;

    private Energiequelle stromquelle;
    private double benoetigterStrom;

    public Geraet(Energiequelle stromquelle) {
        this.stromquelle = stromquelle;
        this.benoetigterStrom = (double) BENOETIGTE_LEISTUNG / BENOETIGTE_SPANNUNG;
    }

    public void aendereStromquelle(Energiequelle stromquelle) {
        this.stromquelle = stromquelle;
    }

    private boolean checkLeistung() {
        return stromquelle.getMaximalerStrom() >= benoetigterStrom;
    }

    private boolean checkSpannung() {
        return stromquelle.getSpannung() >= BENOETIGTE_SPANNUNG;
    }

    public void einschalten() {
        if (checkLeistung() && checkSpannung()) {
            System.out.println("Funktioniert! Nutze " 
                + stromquelle.getSpannung() + " V und " 
                + benoetigterStrom + " A");
        } else {
            System.out.println("Funktioniert nicht! Benoetige mindestens "
                + BENOETIGTE_SPANNUNG + " V und " 
                + benoetigterStrom + " A. Bekomme nur "
                + stromquelle.getSpannung() + " V und "
                + stromquelle.getMaximalerStrom() + " A");
        }
    }
}