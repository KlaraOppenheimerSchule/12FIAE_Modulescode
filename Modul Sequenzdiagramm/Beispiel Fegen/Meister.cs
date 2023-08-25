using System;
using System.Collections.Generic;
using System.Text;

namespace SD_Übungen
{
    class Meister
    {
        public Meister(Lehrling eins)
        {
            Console.WriteLine("Hey, fege die Werkstatt!");
            eins.fegeWerkstatt();
            
        }
    }
}
