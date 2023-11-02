def bubblesort(massiiv):		# Defineerin bubble sorti
    
  for i in range(len(massiiv)):				# For loop massiivis olevatele arvudele ligi pääsemiseks

    for j in range(0, len(massiiv) - i - 1):	# Võrdleme massiivi elemente

      if massiiv[j] > massiiv[j + 1]:			# Kui massiivi esimene element on suurem kui teine element

        massiiv[j], massiiv[j+1] = massiiv[j+1], massiiv[j]	# Võtame esimese ning teise elemendi. Kui esimene on teisest suurem, siis vahetame nende kohad ära
        print(massiiv)			# Peale igat sammu prindime saadud massiivi


massiiv = [64, 34, 25, 12, 22, 11, 90]		# Massiiv, mis on ette antud

bubblesort(massiiv)
