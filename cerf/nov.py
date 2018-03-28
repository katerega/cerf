"""
Calculate Net Operation Value for a technology.

Copyright (c) 2018, Battelle Memorial Institute

Open source under license BSD 2-Clause - see LICENSE and DISCLAIMER

@author:  Nino Zuljevic (nino.zuljevic@pnnl.gov)
"""

import os

class Nov:

    def __init__(self, cerf_output=None):
        return None

    def Get_AF(self):
        """
        Calculates the annuity factor.

        :@param d:        constant - discount rate
        :@param n:        constant - transmission lifetime
        :@returns:        annuity factor
        """
   
        return self.d * pow(1.0 + self.d, self.n) / (pow(1.0 + self.d, self.n) - 1)

    def Get_LF_L(self, AF, L):
        """
        Calculates the levelizing factor for LMP. - NOT USED

        :@param d:        constant - discount rate
        :@param n:        constant - transmission lifetime
        :@param AF:       annuity factor
        :@param L:        Locational Marginal Price (LMP)
        :@returns:        levelizing factor for LMP
        """
        
        k = (1 + L) / (1 + self.d)
        return k * (1 - pow(k, self.n)) * AF / (1 - k)
    
    def Get_LF_T(self, AF, V_T):
        """
        Calculates the levelizing factor for technology.

        :@param d:        constant - discount rate
        :@param n:        constant - transmission lifetime
        :@param AF:       annuity factor
        :@param V_T:      variable cost escalation rate - technology
        :@returns:        levelizing factor for technology
        """
        
        k = (1 + V_T) / (1 + self.d)
        return k * (1 - pow(k, self.n)) * AF / (1 - k)

    def Get_LF_F(self, AF, E_F):
        """
        Calculates the levelizing factor for fuel.

        :@param d:        constant - discount rate
        :@param n:        constant - transmission lifetime
        :@param AF:       annuity factor
        :@param E_F:      fuel price escalation rate
        :@returns:        levelizing factor for fuel
        """
                
        k = (1 + EF) / (1 + self.d)
        return k * (1 - pow(k, self.n)) * AF / (1 - k)

    def Get_LF_C(self, AF, E_C):
        """
        Calculates the levelizing factor for carbon

        :@param d:        constant - discount rate
        :@param n:        constant - transmission lifetime
        :@param AF:       annuity factor
        :@param E_C:      constant - carbon tax escalation rate
        :@returns:        levelizing factor for carbon
        """
                
        k = (1 + E_C) / (1 + self.d)
        return k * (1 - pow(k, self.n)) * AF / (1 - k)

    def Get_NOV_T(U_T, CF_T, LMP_Z, LF_L, VOM_T, LF_T, HR_T, P_F, LF_F, C, CC_F, LF_C, CCR_T):
        """
        Calculates the net operational value (NOV).

        :@param U_T:      unit size in MW - technology
        :@param CF_T:     capacity factor - technology
        :@param LMP_Z:    locational marginal price for the
                          selected grid cell
                          (power zone LMP based on the selected
                          technology capacity factor)
        :@param LF_L:     levelizing factor for LMP
        :@param VOM_T     variable O&M - technology
        :@param LF_T:     levelizing factor for technology
        :@param HR_T:     heat rate - technology
        :@param P_F:      fuel price by fuel type - technology
        :@param LF_F:     levelizing factor for fuel
        :@param C:        constant - carbon tax
        :@param CC_F:     fuel CO2 content by fuel type - technology
        :@param LF_C:     levelizing factor for carbon
        :@param CCR_T:    carbon capture rate - technology
        :@returns:        net operational value for the
                          selected grid cell and technology
        """
        term1 = U_T * CF_T * 8760
        term2 = LMP_Z * LF_L
        term3 = VOM_T * LF_T
        term4 = HR_T * (P_F / 1000) * LF_F
        term5 = (C * CC_F * HR_T  * LF_C / 1000000) * (1 - CCR_T)

        return term1 * (term2 - (term3 + term4 + term5))

























