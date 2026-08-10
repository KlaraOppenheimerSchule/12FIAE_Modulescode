public class Main {

    public static void main(String[] args) {

        // Amerikanische Stromquelle: 110 V, 20 A
        Stromquelle amerika = new Stromquelle(110, 20);

        // Deutsches Gerät an amerikanischer Steckdose
        Geraet foehnGermany = new Geraet(amerika);
        foehnGermany.einschalten();

        System.out.println("\n--- Adapter wird verwendet ---\n");

        // Adapter in die amerikanische Steckdose stecken
        Adapter adapter = new Adapter(amerika);

        // Gerät an den Adapter anschließen
        foehnGermany.aendereStromquelle(adapter);

        // Gerät erneut einschalten
        foehnGermany.einschalten();
    }
}