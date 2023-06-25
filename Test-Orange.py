def calculer_checksum(ids_boites):
    compte_deux = 0
    compte_trois = 0

    # Parcourir chaque id de la boîte
    for id_boite in ids_boites:
        compte_caracteres = {}

        # Compter les occurrences de chaque caractère dans l id de la boîte
        for caractere in id_boite:
            if caractere in compte_caracteres:
                compte_caracteres[caractere] += 1
            else:
                compte_caracteres[caractere] = 1

        a_deux = False
        a_trois = False

        # Vérifier s il y a des caractères qui apparaissent exactement deux ou trois fois
        for compte in compte_caracteres.values():
            if compte == 2:
                a_deux = True
            elif compte == 3:
                a_trois = True

        # Mettre à jour les compteurs
        if a_deux:
            compte_deux += 1
        if a_trois:
            compte_trois += 1

    # Calculer le checksum en multipliant les compteurs de caracteres à deux et à trois
    checksum = compte_deux * compte_trois

#Test
ids_boites = ["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]

checksum = calculer_checksum(ids_boites)


print("Checksum :", checksum)