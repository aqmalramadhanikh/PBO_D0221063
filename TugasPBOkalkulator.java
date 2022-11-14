
package tugaspbokalkulator;

import java.util.Scanner;

public class TugasPBOkalkulator {

    public static void main(String[] args) {
        Scanner masukan = new Scanner(System.in);   
        int angka1,angka2,operator;
        System.out.println("KALKULATOR SEDERHANA");
        System.out.println("1. penumlahan");
        System.out.println("2. pengurangan");
        System.out.println("3. perkalian");
        System.out.println("4. pembagian");       
        
        System.out.print("masukan angka1 :");
        angka1=masukan.nextInt();
        System.out.print("masukan angka operator di atas :");
        operator=masukan.nextInt();         
        System.out.print("masukan angka2 :");
        angka2=masukan.nextInt();
        
        
        
        if(operator == 1){
            System.out.println("Hasil =" +(angka1 + angka2));            
        }
        else if(operator == 2){
            System.out.println("Hasil =" +(angka1 - angka2));
        }
        else if(operator == 3){
            System.out.println("Hasil =" +(angka1 * angka2));
        }
        else if(operator == 4){
            System.out.println("Hasil =" +(angka1 / angka2));
        }
        else{
            System.out.println("kode operator yang anda masukan salah");
        }
        
    }

    }
    

