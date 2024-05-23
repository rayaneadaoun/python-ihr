# Données 

samedi={"A":[(10,12),(15,18)],
        "B":[(10,12)],
        "C":[(13,15)]
        }

dimanche={"A":[],
          "B":[(14,17)],
          "C":[(9,11),(13,14)]


}

def compare_creneau(c_p,c_d):
    debut_p, fin_p = c_p
    debut_d, fin_d = c_d
    if ( debut_d >= debut_p and fin_d <= fin_p):
        return True
    else: 
        return False


def creneau(jour):
    res={}
    for i in range(9,19):
        c_demi_heure=(i,i+1)
        for key,value in jour.items():
            for creneau in value:
                if (compare_creneau(creneau,c_demi_heure)):
                    if(not c_demi_heure in res.keys()):
                        res[c_demi_heure]=[]
                    res[c_demi_heure]=res[c_demi_heure]+[key]
                    break
    return res

print(creneau(samedi))