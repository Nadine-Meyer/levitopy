import numpy as np

from scipy.constants import epsilon_0 as e0
from scipy.constants import speed_of_light as c
from scipy.constants import h
from scipy.constants import hbar

pi = np.pi


# ------------------------------------------------------------------------------------------------------%%
def part(Diam, PartOmega):
    class particle:
        Diameter = Diam
        Radius = Diameter / 2
        Omega = PartOmega
        RefrIndx = 1.45
        Dens = 2200  # [kg / m ^ 3]
        Vol = 4 / 3 * pi * Radius ** 3  # [m³]
        Mass = Dens * Vol  # [kg]
        alpha = 4 * pi * e0 * Radius ** 3 * (RefrIndx ** 2 - 1) / (RefrIndx ** 2 + 2)

    return particle


# ------------------------------------------------------------------------------------------------------%%
def trap(Lambda_exp, Power_exp):
    class tweezer:
        Lambda = Lambda_exp
        Power = Power_exp
        NAcorr = 1 / 1.5
        NA = 0.8
        omega = 2 * pi * c / Lambda
        Wavevec = 2 * pi / Lambda
        Waist = Lambda / (pi * NA)
        Int0 = 2 * Power / (pi * Waist ** 2)
        RayleighRg = pi * Waist ** 2 / Lambda

    return tweezer


# ------------------------------------------------------------------------------------------------------%%
def cav(Pout, coupling_eff, Kappa, Lambda_exp, fsr):
    class cavity:
        FSR = fsr
        kappa = Kappa  # FWHM
        coupl_eff = coupling_eff
        P_out = Pout
        Lambda = Lambda_exp
        MirrCurv = 25e-3  # confocal cavity curvature = Length
        omega = 2 * pi * c / Lambda
        Lifetime = 1 / kappa
        Finesse = FSR / kappa
        Length = 2 * pi * c / (2 * FSR)
        Wavevec = 2 * pi / Lambda
        PhotonEner = h * c / Lambda
        Waist = np.sqrt(Length * Lambda / (2 * pi))  # https://spie.org/samples/TT53.pdf chapter 2.3
        #       Cav.Waist       =sqrt(Cav.Length*Cav.Lambda/(2*pi) * (2*Cav.MirrCurv-Cav.Length)/Cav.Length);   # by far too small http://thesis.library.caltech.edu/2240/1/Buck_2003.pdf
        ModeVol = (pi * Length * Waist ** 2) / 4  # Romero-Isart PRA 83 013803 (2011) / Chang too
        RayleighRg = pi * Waist ** 2 / Lambda

        R = np.linspace(0.99995, 0.99999999, 1000000)
        kappatest = (1 - R) / np.sqrt(R) * c / Length

        indexOfMin = np.argmin(np.abs(kappatest - kappa))

        Reflectivity = R[indexOfMin]
        Absorption = np.sqrt(coupl_eff * (1 - Reflectivity) ** 2)
        Transmission = 1 - (Reflectivity + Absorption)
        Roundtriptime = 2 * Length / c
        n_ph_intra = P_out * Roundtriptime / (hbar * omega * Transmission);
        P_circ = P_out / Transmission
        Int = P_circ / (pi * Waist ** 2)

    return cavity
