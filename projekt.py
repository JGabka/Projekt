import numpy as np

class Dom:
    def __init__(self,params):
        self.macierze={}
        for key in params['indeksy_graniczne'].keys():
            ind_row_min = min(tup[0] for tup in params['indeksy_graniczne'][key])
            ind_row_max = max(tup[0] for tup in params['indeksy_graniczne'][key])
            ind_col_min = min(tup[1] for tup in params['indeksy_graniczne'][key])
            ind_col_max = max(tup[1] for tup in params['indeksy_graniczne'][key])
            self.macierze[key] = np.zeros((ind_row_max-ind_row_min, ind_col_max-ind_col_min))
            self.macierze[key] = params['maska'][key]


k = 80
n = 120
params = {'indeksy_graniczne':{'pokoj_1':[(0,0), (0,5/8*k), (n/3,5/8*k), (n/3,0)],
                               'łazienka': [(0,5/8*k), (0,k), (n/3,k), (n/3, 5/8*k)],
                               'pokoj_2':[(n/3,0), (n/3,3/8*k), (2/3*n, 3/8*k), (2/3*n,0)],
                               'salon':[(n/3,3/8*k), (n/3,k), (3/4*n, k), (3/4*n,3/8*k)],
                               'pokoj_3':[(2/3*n,0), (2/3*n,3/8*k), (n,3/8*k), (n,0)],
                               'ppokoj':[(3/4*n, 3/8*k), (3/4*n, 5/8*k), (n, 5/8*k), (n,3/8*k)],
                               'kuchnia': [(3/4*n, 5/8*k), (3/4*n, k), (n,k), (n, 5/8*k)]},
          'rozdzielczość':{},
          'maska':{'pokoj_1':1, 'łazienka':1,'pokoj_2':1, 'salon':1, 'pokoj_3':1, 'ppokoj':1, 'kuchnia':1 }
          }


if __name__ =='main':
