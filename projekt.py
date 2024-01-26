import numpy as np
import matplotlib.pyplot as plt


class Dom:
    def __init__(self, params):
        self.params = params
        self.macierz = {'mieszkanie': np.zeros((120,80))}
        self.macierze = {}
        self.maska_grzejniki = np.zeros((120,80))
        self.build_partial_matrix()
        self.build_result_matrix()

    def build_mask_matrix(self):
        for w in self.params['grzejniki'].keys():
            self.maska_grzejniki[self.params['grzejniki'][w][0]:self.params['grzejniki'][w][1],
            self.params['grzejniki'][w][2]:self.params['grzejniki'][w][3]] = self.params['grzejniki'][w][-1]
        return self


    def build_partial_matrix(self):
        for key in self.params['pomieszczenia'].keys():
            if key not in self.macierze.keys():
                self.macierze[key] = self.params['maska'][key] + np.random.random((self.params['pomieszczenia'][key][1]-self.params['pomieszczenia'][key][0],
                                                                                  self.params['pomieszczenia'][key][3]-self.params['pomieszczenia'][key][2]))
            else: # metoda ktora robi self.macierze z self.macierz
                self.macierze[key] = self.macierz['mieszkanie'][self.params['pomieszczenia'][key][0]:self.params['pomieszczenia'][key][1],
                self.params['pomieszczenia'][key][2]:self.params['pomieszczenia'][key][3]]
        # for key in self.params['okna'].keys():
        #     self.macierz['mieszkanie'][self.params['okna'][key][0]:self.params['okna'][key][1],
        #     self.params['okna'][key][2]:self.params['okna'][key][3]] = self.macierze[key]

        return self

    def build_result_matrix(self): #metoda ktora robi self.macierz z self.macierze
        for key in self.params['pomieszczenia'].keys():
            self.macierz['mieszkanie'][self.params['pomieszczenia'][key][0]:self.params['pomieszczenia'][key][1],
            self.params['pomieszczenia'][key][2]:self.params['pomieszczenia'][key][3]] = self.macierze[key]
        return self




    def evolve(self,n,dt):
        for n in range(n):
            self.unit_evolve(dt)
            self.params['current_time'] +=dt
        return self

    def unit_evolve(self,dt):
        f = self.params['funkcja_grzejnik'](self.maska_grzejniki)
        ct= self.params['diffusion']*dt/self.params['dziedzina']['dx']**2
        for w in self.params['okna'].keys():
            self.macierz['mieszkanie'][self.params['okna'][w][0]:self.params['okna'][w][1],
                                        self.params['okna'][w][2]:self.params['okna'][w][3]] = 273+np.cos(24*self.params['current_time']/3600)
        self.build_partial_matrix()
        for p in self.params['pomieszczenia'].keys():
            if np.mean(self.macierze[p])>self.params['pomieszczenia'][p][-1]:
                f[
                self.params['pomieszczenia'][p][0]:self.params['pomieszczenia'][p][1],
                self.params['pomieszczenia'][p][2]:self.params['pomieszczenia'][p][3]
                ]=0
            self.macierze[p][1:-1,1:-1] = self.macierze[p][1:-1, 1:-1] +ct * (self.macierze[p][2:, 1:-1]+self.macierze[p][:-2, 1:-1]
                                            + self.macierze[p][1:-1, 2:] + self.macierze[p][1:-1,:-2]
                                            - 4*self.macierze[p][1:-1, 1:-1]) +dt*f[
                                              self.params['pomieszczenia'][p][0]+1:self.params['pomieszczenia'][p][1]-1,
                                              self.params['pomieszczenia'][p][2]+1:self.params['pomieszczenia'][p][3]-1
                                              ]
            self.macierze[p][0,:] = self.macierze[p][1,:]
            self.macierze[p][-1,:] = self.macierze[p][-2,:]
            self.macierze[p][:,0] = self.macierze[p][:,1]
            self.macierze[p][:, -1] = self.macierze[p][:, -2]
        self.build_result_matrix()
        for d in self.params['drzwi'].keys():
            self.macierz['mieszkanie'][self.params['drzwi'][d][0]:self.params['drzwi'][d][1],
                                        self.params['drzwi'][d][2]:self.params['drzwi'][d][3]] = np.mean(
                                        self.macierz['mieszkanie'][self.params['drzwi'][d][0]:self.params['drzwi'][d][1],
                                        self.params['drzwi'][d][2]:self.params['drzwi'][d][3]])
        self.build_partial_matrix()
        return self


params = {'pomieszczenia': {'pokoj_1': [0, 40, 0, 50,293],
                            'łazienka': [0, 40, 50, 80,293],
                            'pokoj_2': [40, 80, 0, 30,293],
                            'salon': [40, 90, 30, 80,293],
                            'pokoj_3': [80, 120, 0, 30,293],
                            'ppokoj': [90, 120, 30, 50,293],
                            'kuchnia': [90, 120, 50, 80,293]},

          'ściany': {'ściana1': [0, 2, 0, 20],
                     'ściana2': [0, 2, 30, 60],
                     'ściana3': [0, 2, 70, 80],
                     'ściana4': [118, 120, 0, 10],
                     'ściana5': [118, 120, 20, 60],
                     'ściana6': [118, 120, 70, 80],
                     'ściana7': [2, 10, 0, 2],
                     'ściana8': [20, 55, 0, 2],
                     'ściana9': [65, 90, 0, 2],
                     'ściana10': [100, 120, 0, 2],
                     'ściana11': [2, 10, 78, 80],
                     'ściana12': [20, 55, 78, 80],
                     'ściana13': [70, 120, 78, 80],
                     'ściana14': [2, 39, 49, 51],
                     'ściana15': [39, 41, 2, 35],
                     'ściana16': [39, 41, 40, 60],
                     'ściana17': [39, 41, 65, 80],
                     'ściana18': [41, 60, 29, 31],
                     'ściana19': [65, 82, 29, 31],
                     'ściana20': [87, 120, 29, 31],
                     'ściana21': [79, 81, 2, 29],
                     'ściana22': [89, 91, 31, 35],
                     'ściana23': [89, 91, 40, 65],
                     'ściana24': [89, 91, 70, 80],
                     'ściana25': [91, 120, 49, 51]},

          'okna': {'okno1': [0, 2, 20, 30],
                   'okno2': [0, 2, 60, 70],
                   'okno3': [10, 20, 0, 2],
                   'okno4': [10, 20, 78, 80],
                   'okno5': [55, 65, 0, 2],
                   'okno6': [55, 70, 78, 80],
                   'okno7': [90, 100, 0, 2],
                   'okno8': [118, 120, 10, 20],
                   'okno9': [118, 120, 60, 70]
                   },

          'grzejniki': {'grzejnik1': [2, 4, 20, 30,1],
                        'grzejnik2': [2, 4, 60, 70,2],
                        'grzejnik3': [10, 20, 2, 4,3],
                        'grzejnik4': [10, 20, 76, 78,4],
                        'grzejnik5': [55, 65, 2, 4,5],
                        'grzejnik6': [55, 70, 76, 78,6],
                        'grzejnik7': [90, 100, 2, 4,7],
                        'grzejnik8': [116, 118, 10, 20,8],
                        'grzejnik9': [116, 118, 60, 70,9]
                        },

          'drzwi': {'drzwi1': [39, 41, 35, 40],
                    'drzwi2': [39, 41, 60, 65],
                    'drzwi3': [60, 65, 29, 31],
                    'drzwi4': [82, 87, 29, 31],
                    'drzwi5': [89, 91, 35, 40],
                    'drzwi6': [89, 91, 65, 70]
                    },

          'maska': {'pokoj_1': 280, 'łazienka': 280, 'pokoj_2': 280,'salon': 280, 'pokoj_3': 280, 'ppokoj': 280,
                    'kuchnia': 280},
          'diffusion': 1,
          'current_time':0,
          'dziedzina': {'siatka':np.meshgrid(np.linspace(0,1,120),np.linspace(0,1,80)),
                        'dx':1},
          'funkcja_grzejnik': lambda x: np.where(
              x==1, 0.1, np.where(
                  x==2, 0.2, np.where(
                      x==3, 0.3, np.where(
                        x==4, 0.4, np.where(
                            x==5, 0.1, np.where(
                              x==6, 0.2, np.where(
                                  x==7, 0.3, np.where(
                                    x==8, 0.4, np.where(
                                        x==9, 0.5, 0
                                          )
                                      )
                                  )
                              )
                          )
                      )
                  )
              )
          )
          }




dom = Dom(params)
Dom.evolve(dom,10,0.1)


plt.imshow(dom.macierz['mieszkanie'])



plt.show()
#if __name__ =='main':
