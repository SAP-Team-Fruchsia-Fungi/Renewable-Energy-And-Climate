import csv

with open('/users/diago/Documents/GitHub/Renewable-Energy-And-Climate/GreenData/climateperceptions.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    scarborough_not_concerned_count = 0
    scarborough_concerned_count = 0
    scarborough_not_informed_count = 0
    scarborough_informed_count = 0

    etobicoke_not_concerned_count = 0
    etobicoke_concerned_count = 0
    etobicoke_not_informed_count = 0
    etobicoke_informed_count = 0

    toronto_not_concerned_count = 0
    toronto_concerned_count = 0
    toronto_not_informed_count = 0
    toronto_informed_count = 0

    #this first section is seeing how many people are concerned or not concerned about
    #climate change in the survey and splits them into groups for Scarborough, Toronto, and Etobicoke

    for line in csv_reader:

        #SCARBOROUGH
        if line['area'] == 'Scarborough' and line['Q1r1'] == 'Not very concerned':
            scarborough_not_concerned_count = scarborough_not_concerned_count + 1

        elif line['area'] == 'Scarborough' and line['Q1r1'] == 'Very concerned' or line['Q1r1'] == 'Extremely concerned':
            scarborough_concerned_count = scarborough_concerned_count + 1

        if line['area'] == 'Scarborough' and line['Q2'] == 'Not very informed':
            scarborough_not_informed_count = scarborough_not_informed_count + 1

        elif line['area'] == 'Scarborough' and line['Q2'] == 'Very informed' or line['Q2'] == 'Extremely informed':
            scarborough_informed_count = scarborough_informed_count + 1



        #ETOBICOKE
        if line['area'] == 'Etobicoke' and line['Q1r1'] == 'Not very concerned':
            etobicoke_not_concerned_count = etobicoke_not_concerned_count + 1

        elif line['area'] == 'Etobicoke' and line['Q1r1'] == 'Very concerned' or line['Q1r1'] == 'Extremely concerned':
            etobicoke_concerned_count = etobicoke_concerned_count + 1

        if line['area'] == 'Etobicoke' and line['Q2'] == 'Not very informed':
            etobicoke_not_informed_count = etobicoke_not_informed_count + 1

        elif line['area'] == 'Etobicoke' and line['Q2'] == 'Very informed' or line['Q2'] == 'Extremely informed':
            etobicoke_informed_count = etobicoke_informed_count + 1


        #TORONTO
        if line['area'] != 'Etobicoke' and line['area'] != 'Scarborough' and line['Q1r1'] == 'Not very concerned':
            toronto_not_concerned_count = toronto_not_concerned_count + 1

        elif line['area'] != 'Etobicoke' and line['area'] != 'Scarborough' and line['Q1r1'] == 'Very concerned' or line['Q1r1'] == 'Extremely concerned':
            toronto_concerned_count = toronto_concerned_count + 1

        if line['area'] != 'Etobicoke' and line['area'] != 'Scarborough' and line['Q2'] == 'Not very informed':
            toronto_not_informed_count = toronto_not_informed_count + 1

        elif line['area'] != 'Etobicoke' and line['area'] != 'Scarborough' and line['Q2'] == 'Very informed' or line['Q2'] == 'Extremely informed':
            toronto_informed_count = toronto_informed_count + 1

    #percentage calculations for toronto
    toronto_total = toronto_not_concerned_count + toronto_concerned_count
    toronto_Nconcerned_pct = (toronto_not_concerned_count / toronto_total) * 100
    toronto_Nconcerned_pct = round(toronto_Nconcerned_pct, 2)

    toronto_concerned_pct = (toronto_concerned_count / toronto_total) * 100
    toronto_concerned_pct = round(toronto_concerned_pct, 2)

    toronto_total2 = toronto_not_informed_count + toronto_informed_count
    toronto_Ninformed_pct = (toronto_not_informed_count / toronto_total2) * 100
    toronto_Ninformed_pct = round(toronto_Ninformed_pct, 2)

    toronto_informed_pct = (toronto_informed_count / toronto_total2) * 100
    toronto_informed_pct = round(toronto_informed_pct, 2)


    #percentage calculations for scarborough
    scarborough_total = scarborough_concerned_count + scarborough_not_concerned_count
    scarborough_Nconcerned_pct = (scarborough_not_concerned_count / scarborough_total) * 100
    scarborough_Nconcerned_pct = round(scarborough_Nconcerned_pct, 2)

    scarborough_concerned_pct = (scarborough_concerned_count / scarborough_total) * 100
    scarborough_concerned_pct = round(scarborough_concerned_pct, 2)

    scarborough_total2 = scarborough_informed_count + scarborough_not_informed_count
    scarborough_Ninformed_pct = (scarborough_not_informed_count / scarborough_total2) * 100
    scarborough_Ninformed_pct = round(scarborough_Ninformed_pct, 2)

    scarborough_informed_pct = (scarborough_informed_count / scarborough_total2) * 100
    scarborough_informed_pct = round(scarborough_informed_pct, 2)

    #percentage calculations for etobicoke
    etobicoke_total = etobicoke_concerned_count + etobicoke_not_concerned_count
    etobicoke_Nconcerned_pct = (etobicoke_not_concerned_count / etobicoke_total) * 100
    etobicoke_Nconcerned_pct = round(etobicoke_Nconcerned_pct, 2)

    etobicoke_concerned_pct = (etobicoke_concerned_count / etobicoke_total) * 100
    etobicoke_concerned_pct = round(etobicoke_concerned_pct, 2)

    etobicoke_total2 = etobicoke_informed_count + etobicoke_not_informed_count
    etobicoke_Ninformed_pct = (etobicoke_not_informed_count / etobicoke_total2) * 100
    etobicoke_Ninformed_pct = round(etobicoke_Ninformed_pct, 2)

    etobicoke_informed_pct = (etobicoke_informed_count / etobicoke_total2) * 100
    etobicoke_informed_pct = round(etobicoke_informed_pct, 2)


    #RESULTS OF DATA:
    print("")
    print("How Many People In The GTA Are Concerned About Climate Change?")
    print("")
    print(f'People in Scarborough who feel that climate change is not a major threat: {scarborough_Nconcerned_pct}%')
    print(f'People in Scarborough who feel that climate change is a big issue: {scarborough_concerned_pct}%')
    print("")
    print(f'People in Etobicoke who feel that climate change is not a major threat: {etobicoke_Nconcerned_pct}%')
    print(f'People in Etobicoke who feel that climate change is a big issue: {etobicoke_concerned_pct}%')
    print("")
    print(f'People in Toronto who feel that climate change is not a major threat: {toronto_Nconcerned_pct}%')
    print(f'People in Toronto who feel that climate change is a big issue: {toronto_concerned_pct}%')
    print("")
    print("")
    print("This Area Displays How Many People Are Informed About Climate Change:")
    print("")
    print(f'People in Scarborough who claim to be informed about climate change: {scarborough_informed_pct}%')
    print(f'People in Scarborough are not informed about climate change: {scarborough_Ninformed_pct}%')
    print("")
    print(f'People in Etobicoke who claim to be informed about climate change: {etobicoke_informed_pct}%')
    print(f'People in Etobicoke are not informed about climate change: {etobicoke_Ninformed_pct}%')
    print("")
    print(f'People in Toronto who claim to be informed about climate change: {toronto_informed_pct}%')
    print(f'People in Toronto are not informed about climate change: {toronto_Ninformed_pct}%')
