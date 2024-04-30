def get_stated_choice_list():
    import csv

    csv_link = "static/optimal_design.csv"
    f = open(csv_link)
    data_csv = list(csv.DictReader(f))

    return data_csv

def get_max_Block(optimal_design: list):
    max_number = 0
    for row in optimal_design:
        if int(row['Block']) >max_number:
            max_number=int(row['Block'])

    return max_number


def creating_session():
    optimal_design = get_stated_choice_list()
    id_list = [4,2,3,5,8,1]

    choice_sets= list()
    max_Block = get_max_Block(optimal_design)
    for i in id_list:
        for row in optimal_design:
            if int(row['Block']) == max_Block+1-int(i):
                choice_sets.append(row)


    for i in id_list:
        j=1
        for row in choice_sets:
            if int(row['Block']) == max_Block+1-int(i):
                print(str(row))
                print('Block:'+str(row['Block']))
                print('choice_set '+str(j)+" of player "+str(i))
                print('Alt1_price: ' + str(row['alt1_A'])+" as "+str(type(row['alt1_A'])))
                print('Alt1_detect: ' + str(row['alt1_B'])+" as "+str(type(row['alt1_B'])))
                print('Alt1_corr: ' + str(row['alt1_C']) + " as " + str(type(row['alt1_C'])))
                print('alt1_elect: ' + str(row['alt1_D']) + " as " + str(type(row['alt1_D'])))
                j =j+1


creating_session()

class C:
    ###important links##
    csv_link = "/static/optimal_design.csv"