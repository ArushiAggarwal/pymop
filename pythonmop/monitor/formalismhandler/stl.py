from pythonmop.monitor.formalismhandler.base import Base
import rtamt

class Stl(Base):
    def __init__(self, formula, variables):
        super().__init__()
        self.formula = formula
        self.monitor = rtamt.STLSpecification()
        
        for var in variables:
            self.monitor.declare_var(var, 'float')
            
        self.monitor.spec = self.formula
        self.monitor.parse()
        
    def update_signals(self, time_step, signal_data):
        robustness = self.monitor.update(time_step, signal_data)
        return robustness < 0
