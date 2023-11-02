def insertionsort(massiiv):

    for i in range(1, len(massiiv)):
        temp = massiiv[i]				#Massiivi esimene element võetakse mällu
        j = i - 1
                
        while j >= 0 and temp < massiiv[j]:		# Võrreldakse, kas massiivi esimene element on väiksem kui teine ning kui
            massiiv[j + 1] = massiiv[j]			# on, tõstetakse ümber, siis võrreldakse kahe esimese elemendiga kolmandat
            j = j - 1
        
        massiiv[j + 1] = temp
        print(massiiv)
massiiv = [12, 11, 13, 5, 6, 7]
print("Algne massiiv on: ", massiiv)
insertionsort(massiiv)
print("Sorditud massiiv on: ", massiiv)