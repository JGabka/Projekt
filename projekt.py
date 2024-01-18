import numpy as np

class Dom:
    def __init__(self,params):
        self.params=params
        self.macierz={}
        self.macierze = {}


    #def build_partial_matrix(self):

    #def build_result_matrix(self):


params = {'pomieszczenia':{'pokoj_1': [0,40,0,50],
                            'łazienka': [0,40,50,80],
                            'pokoj_2': [40,80,0,30],
                            'salon': [40,90,30,80],
                            'pokoj_3': [80,120,0,30],
                            'ppokoj': [90,120,30,50],
                            'kuchnia': [90,120,50,80]},
          'ściany': {'ściana1':[0,2,0,20],
                     'ściana2':[0,2,30,60],
                     'ściana3':[0,2,70,80],
                     'ściana4':[118,120,0,10],
                     'ściana5':[118,120,20,60],
                     'ściana6': [118,120,70,80],
                     'ściana7': [2,10,0,2],
                     'ściana8': [20,55,0,2],
                     'ściana9': [65,90,0,2],
                     'ściana10': [100,120,0,2],
                     'ściana11': [2,10,78,80],
                     'ściana12': [20,55,78,80],
                     'ściana13': [70,120,78,80],
                     'ściana14': [2,39,49,51],
                     'ściana15': [39,41,2,35],
                     'ściana16': [39,41,40,60],
                     'ściana17': [39,41,65,80],
                     'ściana18': [41,60,29,31],
                     'ściana19': [65,82,29,31],
                     'ściana20': [87,120,29,31],
                     'ściana21': [79,81,2,29],
                     'ściana22': [89,91,31,35],
                     'ściana23': [89,91,40,65],
                     'ściana24': [89,91,70,80],
                     'ściana25': [91,120,49,51]},

          'okna': {'okno1':[0,2,20,30],
                   'okno2':[0,2,60,70],
                   'okno3':[10,20,0,2],
                   'okno4':[10,20,78,80],
                   'okno5':[55,65,0,2],
                   'okno6':[55,70,78,80],
                   'okno7':[90,100,0,2],
                   'okno8':[118,120,10,20],
                   'okno9':[118,120,60,70]
                   },
          'grzejniki': {'grzejnik1':[2,4,20,30],
                        'grzejnik2':[2,4,60,70],
                        'grzejnik3':[10,20,2,4],
                        'grzejnik4':[10,20,76,78],
                        'grzejnik5':[55,65,2,4],
                        'grzejnik6':[55,70,76,78],
                        'grzejnik7':[90,100,2,4],
                        'grzejnik8':[116,118,10,20],
                        'grzejnik9':[116,118,60,70]
                        },
          'drzwi': {'drzwi1':[39,41,35,40],
                    'drzwi2':[39,41,60,65],
                    'drzwi3':[60,65,29,31],
                    'drzwi4':[82,87,29,31],
                    'drzwi5':[89,91,35,40],
                    'drzwi6':[89,91,65,70]
                    },
          'maska': {'pokoj_1': 1, 'łazienka': 1,'pokoj_2': 1, 'salon': 1, 'pokoj_3': 1, 'ppokoj': 1, 'kuchnia': 1}
          }


#if __name__ =='main':

