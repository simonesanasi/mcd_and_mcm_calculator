import sys

# La funzione MCD (mcd) è il modo corretto per implementare l'algoritmo euclideo
def calcola_mcd(num1, num2):
    """Calcola il Massimo Comun Divisore (MCD) usando l'Algoritmo di Euclide."""
    
    # Usiamo nomi descrittivi per le variabili locali
    a_val, b_val = num1, num2
    
    while b_val != 0:
        remainder = a_val % b_val
        a_val = b_val
        b_val = remainder
        
    return a_val

def calcola_mcm(num1, num2, mcd_result):
    """Calcola il Minimo Comune Multiplo (mcm) basandosi sul risultato del MCD."""
    # Formula: mcm(a, b) = (|a * b|) / MCD(a, b)
    # Usiamo abs() per essere sicuri, anche se gli input sono positivi
    # Usiamo // per l'integer division (il risultato è sempre intero)
    if mcd_result == 0:
        # Caso estremo di input 0, sebbene tu abbia specificato numeri positivi
        return 0
        
    risultato_mcm = abs(num1 * num2) // mcd_result
    return risultato_mcm


# --- Blocco Principale di Esecuzione ---
if __name__ == "__main__":
    try:
        # Prende gli input
        a_originale = int(input("Inserisci il primo numero (A): "))
        b_originale = int(input("Inserisci il secondo numero (B): "))
        
        if a_originale <= 0 or b_originale <= 0:
            print("Errore: Inserisci numeri interi positivi.")
            sys.exit(1)
            
        # 1. Calcola il MCD
        risultato_mcd = calcola_mcd(a_originale, b_originale)
        
        # 2. Calcola il MCM (passando il risultato MCD)
        risultato_mcm = calcola_mcm(a_originale, b_originale, risultato_mcd)
        
        # 3. Output (Stampa solo nel blocco principale)
        print("-" * 30)
        print(f"MCD({a_originale}, {b_originale}): {risultato_mcd}")
        print(f"mcm({a_originale}, {b_originale}): {risultato_mcm}")
        print("-" * 30)

    except ValueError:
        print("Errore: Inserisci solo numeri interi validi.")
    except Exception as e:
        print(f"Si è verificato un errore inaspettato: {e}")