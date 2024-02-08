using System;

namespace SD_Übungen
{
    class Program
    {
        static void Main(string[] args)
        {
            Lehrling christoph = new Lehrling();
            Meister stefan = new Meister(christoph);
        }
    }
}
