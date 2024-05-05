#codigo 20 salto atras

class CSP:
    def __init__(self, var,domi,cons):
        self.var= var 
        self.domi= domi
        self.cons= cons
        self.assignment={}

    def complx(self):
        return len (self.assignment)== len(self.var)
    def assign(self,vars,val):
        for cons in self.cons[vars]:
            if not cons(self.assignment):
                return False
        return True
    def salto_atras(self):
        if self.complx():
            return self.assignment
        
        vars = self.select()
        for val in self.order(vars):
            if self.complx(vars,val):
                self.assignment[vars]=val
                res= self.salto_atras()
                if res is not None :
                    return res
            del self.assignment
        return None
    def select(self):
        for vars in self.var:
            if vars not in self.assignment:
                return vars
    def order(self,vars):
        return self.domi[vars]
    
def main():
    var =['a','b','c']
    domi ={
        'a':[1,2,3],
        'b':[1,2,3],
        'c':[1,2,3]
          }
    cons = {
        'a': [lambda assignment: assignment['a'] != assignment['b']],
        'b': [lambda assignment: assignment['a'] != assignment['b'],
              lambda assignment: assignment['b']!=  assignment['c']],
        'c': [lambda assignment: assignment['b'] != assignment['c']],
    }
    csp = CSP(var,domi,cons)
    solucion = csp.salto_atras()
    if solucion is not None:
        print('se encontro la solucion:')
        for vars,val in solucion.items():
            print(f'{vars}:{val}')

if  __name__ == '__main__':
    main()

    
            
