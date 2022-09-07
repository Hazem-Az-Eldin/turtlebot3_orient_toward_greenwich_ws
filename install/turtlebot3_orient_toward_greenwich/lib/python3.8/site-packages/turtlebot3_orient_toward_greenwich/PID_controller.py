
class PID():
    """
    PID Controller
    """
    def __init__(self,kp,ki,kd):
        
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def clear(self): 
        pass

    def update_controller(self,error):
        P_term = self.kp * error
        control_input = P_term
        return control_input