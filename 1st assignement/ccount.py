import argparse
import string


from loguru import logger




# Buona norma usare il "with" quando si apre un file
# La funzione count_characters(file_path) legge il file.txt e stampa sul terminale il numero di caratteri
def count_characters(file_path):
    counts = {char: 0 for char in string.ascii_lowercase} # <--- Molto pythonico
    # Rough equivalent
    # counts = []
    # for char in string.ascii_lowercase:
    #    counts[char] = 0
    with open(file_path) as input_file:
        logger.debug(f'Reading input data from {file_path}...')
        data = input_file.read()
    logger.debug(f'Done, {len(data)} character(s) found')
    logger.info('Counting characters')
    for char in data.lower(): # "data.lower()" serve per mettere tutto il testo in lettere minuscole
        if char in counts: # Sto chiedendo se la stringa "chat" è tra le chiavi del dizionario "counts". Serve per contare solo le lettere minuscole e non gli spazi o i punti.
            counts[char] +=1
    logger.info(f'Character counts: {counts}')
    num_characters = sum(counts.values())
    logger.info(f'Total number of characters: {num_characters}')
    for key, value in counts.items():
        counts[key] = value/ num_characters
    logger.info(f'Character frequences: {counts}')








# il __name__ == "main" vuol dire che se questo modulo lo sto eseguendo e non semplicemente importando allora fai tutto quello che viene dopo il ":"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Count the characters in a text file')
    parser.add_argument('file')
    args = parser.parse_args()
    count_characters(args.file)






## comando da mandare su shell:  python ccount.py pg1497.txt
