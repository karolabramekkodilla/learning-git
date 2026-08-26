import matplotlib.pyplot as plt
from numpy import hstack, arange, meshgrid, where

def plot_classification_surface(X_plot, y_plot, trained_model):
    plt.figure(figsize=(12,7))
    # określanie graniz zbioru
    min1, max1 = X_plot[:,0].min()-1,X_plot[:,0].max()+1
    min2, max2 = X_plot[:,1].min()-1, X_plot[:,1].max()+1
    # skalowanie dla obu osi
    x1grid = arange(min1,max1,0.1)
    x2grid = arange(min2,max2,0.1)
    #  utworzenie siatki
    xx, yy = meshgrid(x1grid,x2grid)
    #  przetworzenie siatki w wektor
    r1, r2 = xx.flatten(), yy.flatten()
    r1,r2 = r1.reshape((len(r1), 1)), r2.reshape((len(r2),1))

    # stworzenie zmiennych objaśniających dla modelu
    grid = hstack((r1,r2))

    # predykcja modelu zbioru
    yhat = trained_model.predict(grid)
    # przetworzenie predykcji na decyzji dla konkretnego punktu wykresu
    zz = yhat.reshape(xx.shape)
    # wizualizacja siatki z przyporządkowaną klasą
    plt.contourf(xx,yy,zz, cmap='Paired')
    # tworzenie wykresu punktowego dla klas ze zbioru X
    for class_value in range (2):
        # przyporzadkowanie klasy (y) do obserwacji (X)
        row_ix = where(y_plot == class_value)
        # stworzenie wykresu punktowego
        plt.scatter(X_plot[row_ix,0], X_plot[row_ix,1], cmap='Paired', alpha=0.3, label= class_value)
    #  wizualizacja wykresu
    plt.legend(loc='upper right')
    plt.show()