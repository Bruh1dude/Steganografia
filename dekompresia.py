from PIL import Image
def spracuj_riadok(riadok_text):
    cisla = list(map(int, riadok_text.split()))
    vysledny_riadok = ""
    farba = "0"  
    
    for pocet in cisla:
        vysledny_riadok += farba * pocet
        farba = "1" if farba == "0" else "0"
        
    return vysledny_riadok

def dekomprimuj_obrazok(vstupny_subor, vystupny_subor):
    with open(vstupny_subor, 'r') as f_in, open(vystupny_subor, 'w') as f_out:
            
        prvy_riadok = f_in.readline().split()
        if not prvy_riadok:
            return
            
        sirka = int(prvy_riadok[0])
        vyska = int(prvy_riadok[1])      
           
        f_out.write(f"{sirka} {vyska}\n")
            
        for riadok in f_in:
            if riadok.strip():
                dekomprimovany = spracuj_riadok(riadok)
                f_out.write(dekomprimovany + "\n")
                    
dekomprimuj_obrazok('dekompresia_obrazka_1.txt', 'dekompresia_obrazka_vystup.txt')