using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SoloLearn
{
   // private, public, protected, internal
   class Program
   {
         // Similar to the ref keyword, the out keyword is used both when defining the method and when calling it.
         static void name(ref type1 par1CallByRefrence, out int par2, … , typeN parN)
         {
            //List of statements of method (func)
            par2 = par1CallByRefrence;
         }

         // lambda:
         public decimal sum(decimal a, decimal b) => a + b; 

      static void Main(string[] args)
      {
         const double y = 20; // decimal, uint, string, bool 
         string input = Console.ReadLine(); // This function always save as string.
         int x = Convert.ToInt16(input); /* Convert.ToXxx */
         var num = 15; // Var typed makes the compiler determine the type of the variable and this variables must be initialized with a value. 

         int x = 3;
         int y = x++;
         // x is 4, y is 3.

         Console.WriteLine("x = {0}; y = {1}", x, y); // This will go to next line automatically,
         Console.Write("x = {0}; y = {1}", x, y);     // but this won't.


      }
   }
}