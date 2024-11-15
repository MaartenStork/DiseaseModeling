import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.fft import fft, fftfreq

# Class for the basic SIR Model
class SIRModel:
    """
    A class to represent the basic SIR (Susceptible-Infected-Recovered) epidemiological model.
    
    Attributes:
    -----------
    beta : float
        The transmission rate of the disease.
    gamma : float
        The recovery rate of the disease.
    initial_conditions : list
        Initial values for the Susceptible, Infected, and Recovered populations.
    """
    def __init__(self, beta, gamma, initial_conditions):
        """
        Constructs all the necessary attributes for the SIR model.
        
        Parameters:
        -----------
        beta : float
            Transmission rate.
        gamma : float
            Recovery rate.
        initial_conditions : list
            Initial conditions for [S, I, R].
        """
        self.beta = beta
        self.gamma = gamma
        self.initial_conditions = initial_conditions

    def sir_equations(self, y, t):
        """
        Defines the system of differential equations for the SIR model.
        
        Parameters:
        -----------
        y : list
            Current values of [S, I, R].
        t : float
            Current time step.
        
        Returns:
        --------
        list
            Derivatives [dS/dt, dI/dt, dR/dt].
        """
        S, I, R = y
        dSdt = -self.beta * S * I
        dIdt = self.beta * S * I - self.gamma * I
        dRdt = self.gamma * I
        return [dSdt, dIdt, dRdt]

    def simulate(self, t):
        """
        Simulates the SIR model over a given time period.
        
        Parameters:
        -----------
        t : ndarray
            Array of time points.
        """
        self.results = odeint(self.sir_equations, self.initial_conditions, t)

    def plot_results(self, t):
        """
        Plots the time evolution of the Susceptible, Infected, and Recovered populations.
        
        Parameters:
        -----------
        t : ndarray
            Array of time points.
        """
        S, I, R = self.results.T
        plt.figure(figsize=(10, 6))
        plt.plot(t, S, label='Susceptible')
        plt.plot(t, I, label='Infected')
        plt.plot(t, R, label='Recovered')
        plt.xlabel('Time')
        plt.ylabel('Proportion of Population')
        plt.title('SIR Model')
        plt.legend()
        plt.show()

    def plot_phase_portrait(self):
        """
        Plots the phase portrait of the Susceptible vs. Infected populations.
        """
        S, I, _ = self.results.T
        plt.figure(figsize=(10, 6))
        plt.plot(S, I, label='Phase Portrait')
        plt.xlabel('Susceptible')
        plt.ylabel('Infected')
        plt.title('Phase Portrait of SIR Model')
        plt.legend()
        plt.show()