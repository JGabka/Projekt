import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from projekt import Dom

params = {'pomieszczenia': {'pokoj_1': [0, 40, 0, 50,293],
                            'łazienka': [0, 40, 50, 80,293],
                            'pokoj_2': [40, 80, 0, 30,293],
                            'salon': [40, 90, 30, 80,293],
                            'pokoj_3': [80, 120, 0, 30,293],
                            'ppokoj': [90, 120, 30, 50,290],
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

          'maska': {'pokoj_1': 285, 'łazienka': 285, 'pokoj_2': 285,'salon': 285, 'pokoj_3': 285, 'ppokoj': 285,
                    'kuchnia': 285},
          'diffusion': 1,
          'current_time':0,
          'dziedzina': {'siatka':np.meshgrid(np.linspace(0,1,120),np.linspace(0,1,80)),
                        'dx':1},
          'funkcja_grzejnik': lambda x: np.where(
              x==1, 15, np.where(
                  x==2, 15, np.where(
                      x==3, 15, np.where(
                        x==4, 15, np.where(
                            x==5, 15, np.where(
                              x==6, 15, np.where(
                                  x==7, 15, np.where(
                                    x==8, 15, np.where(
                                        x==9, 15, 0
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



params1 = {'pomieszczenia': {'pokoj_1': [0, 40, 0, 50,293],
                            'łazienka': [0, 40, 50, 80,293],
                            'pokoj_2': [40, 80, 0, 30,293],
                            'salon': [40, 90, 30, 80,293],
                            'pokoj_3': [80, 120, 0, 30,293],
                            'ppokoj': [90, 120, 30, 50,290],
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

          'maska': {'pokoj_1': 285, 'łazienka': 285, 'pokoj_2': 285,'salon': 285, 'pokoj_3': 285, 'ppokoj': 285,
                    'kuchnia': 285},
          'diffusion': 1,
          'current_time':0,
          'dziedzina': {'siatka':np.meshgrid(np.linspace(0,1,120),np.linspace(0,1,80)),
                        'dx':1},
          'funkcja_grzejnik': lambda x: np.where(
              x==1, 30, np.where(
                  x==2, 30, np.where(
                      x==3, 30, np.where(
                        x==4, 30, np.where(
                            x==5, 30, np.where(
                              x==6, 30, np.where(
                                  x==7, 30, np.where(
                                    x==8, 30, np.where(
                                        x==9, 30, 0
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


params2 = {'pomieszczenia': {'pokoj_1': [0, 40, 0, 50,293],
                            'łazienka': [0, 40, 50, 80,293],
                            'pokoj_2': [40, 80, 0, 30,293],
                            'salon': [40, 90, 30, 80,293],
                            'pokoj_3': [80, 120, 0, 30,293],
                            'ppokoj': [90, 120, 30, 50,290],
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

          'maska': {'pokoj_1': 285, 'łazienka': 285, 'pokoj_2': 285,'salon': 285, 'pokoj_3': 285, 'ppokoj': 285,
                    'kuchnia': 285},
          'diffusion': 1,
          'current_time':0,
          'dziedzina': {'siatka':np.meshgrid(np.linspace(0,1,120),np.linspace(0,1,80)),
                        'dx':1},
          'funkcja_grzejnik': lambda x: np.where(
              x==1, 20, np.where(
                  x==2, 0, np.where(
                      x==3, 0, np.where(
                        x==4, 20, np.where(
                            x==5, 15, np.where(
                              x==6, 15, np.where(
                                  x==7, 20, np.where(
                                    x==8, 0, np.where(
                                        x==9, 15, 0
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

params3 = {'pomieszczenia': {'pokoj_1': [0, 40, 0, 50,293],
                            'łazienka': [0, 40, 50, 80,293],
                            'pokoj_2': [40, 80, 0, 30,293],
                            'salon': [40, 90, 30, 80,293],
                            'pokoj_3': [80, 120, 0, 30,293],
                            'ppokoj': [90, 120, 30, 50,290],
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

          'maska': {'pokoj_1': 285, 'łazienka': 285, 'pokoj_2': 285,'salon': 285, 'pokoj_3': 285, 'ppokoj': 285,
                    'kuchnia': 285},
          'diffusion': 1,
          'current_time':0,
          'dziedzina': {'siatka':np.meshgrid(np.linspace(0,1,120),np.linspace(0,1,80)),
                        'dx':1},
          'funkcja_grzejnik': lambda x: np.where(
              x==1, 10, np.where(
                  x==2, 10, np.where(
                      x==3, 10, np.where(
                        x==4, 10, np.where(
                            x==5, 10, np.where(
                              x==6, 10, np.where(
                                  x==7, 10, np.where(
                                    x==8, 10, np.where(
                                        x==9, 10, 0
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
dom1 = Dom(params1)
dom2 = Dom(params2)
dom3 = Dom(params3)
dt = 0.25
frames = 10
def update(frame):
     dom.evolve(1, dt)
     im.set_array(dom.macierz['mieszkanie'])
     return im,

fig, ax = plt.subplots()
im = ax.imshow(dom.macierz['mieszkanie'], animated=True)

def update1(frame):
    dom1.evolve(1, dt)
    im1.set_array(dom1.macierz['mieszkanie'])
    return im1,



fig1, ax1 = plt.subplots()
im1 = ax1.imshow(dom1.macierz['mieszkanie'], animated=True)

def update2(frame):
    dom2.evolve(1, dt)
    im2.set_array(dom2.macierz['mieszkanie'])
    return im2,



fig2, ax2 = plt.subplots()
im2 = ax2.imshow(dom2.macierz['mieszkanie'], animated=True)


def update3(frame):
    dom3.evolve(1, dt)
    im3.set_array(dom3.macierz['mieszkanie'])
    return im3,



fig3, ax3 = plt.subplots()
im3 = ax3.imshow(dom3.macierz['mieszkanie'], animated=True)

dom.build_mask_matrix()
dom1.build_mask_matrix()
dom2.build_mask_matrix()
dom3.build_mask_matrix()
ani = anm.FuncAnimation(fig, update, frames=frames, blit=True, interval=1)
ani1 = anm.FuncAnimation(fig1, update1, frames=frames, blit=True, interval=1)
ani2 = anm.FuncAnimation(fig2, update2, frames=frames, blit=True, interval=1)
ani3 = anm.FuncAnimation(fig3, update3, frames=frames, blit=True, interval=1)
plt.colorbar(im)
plt.colorbar(im1)
plt.colorbar(im2)
plt.colorbar(im3)
plt.show()


