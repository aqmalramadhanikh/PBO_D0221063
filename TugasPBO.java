
package tugaspbo;

import java.util.Scanner;

public class TugasPBO {

    public static void main(String[] args) {
         Scanner input = new Scanner(System.in);
        int panjang, lebar, luas, masukan, r;
        double luas1,phi=3.14;
        float alas,tinggi,luas2;
        
        System.out.println("1.Persegi");
        System.out.println("2.Lingkaran");
        System.out.println("3.Segitiga");
        
        
        System.out.println("Masukan pilihan anda : ");
        masukan=input.nextInt();
        
        
        if(masukan == 1){
            
            System.out.print("masukan panjang : ");
            panjang=input.nextInt();
            
            System.out.print("masukan lebar : ");
            lebar=input.nextInt();
            
            luas = panjang * lebar;
            System.out.print("Luas persegi adalah : "+luas);
            
        } 
        else if(masukan == 2){
            System.out.println("Masukan jari-jari : ");
            r=input.nextInt();
            
            luas1 = phi*r*r;
            System.out.println("luas Lingkaran :"+luas1);
        }
        else if(masukan == 3){
            System.out.println("Masukan nilai alas : ");
            alas=input.nextFloat();
            
            System.out.println("Masukan nilai tinggi : ");
            tinggi=input.nextFloat();
            
            luas2 = alas*tinggi/2;
            System.out.println("Luas segitiga adalah : "+luas2);
            }
        else{
            System.out.println("kode yang anda masukan salah");
        }
        }
 
    }
    

