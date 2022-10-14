using System;
using System.Collections.Generic;
using System.Text;

namespace SD_Übungen
{
    class Lehrling
    {

        public void fegeWerkstatt()
        {
            Console.WriteLine("Jahwohl");
            this.fegtWerkstatt();
            Console.WriteLine("Fertig");
        }

        private void fegtWerkstatt()
        {
            Console.WriteLine("Feg, feg, feg");
        }
    }
}
