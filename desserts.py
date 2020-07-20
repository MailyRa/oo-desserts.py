"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    #class attribute to cupcake 
    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""
        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    #Create an instance method no need to add qty bc its an integer   
    def __init__(self, name, flavor, price)

    #Instance attributes, we don't need to add an attribute to the parameter if its
    #already defined. In this example qty is zero
    self.name = name
    self.flavor = flavor
    self.price = price 
    self.qty = 0

    #adding the cupcakes to self.cache, making this an instance 
    self.cache[name] = self 


    #adding another instance method name "Add_stock"
    def add_stock(self, amount):

    #we want to add amount to self.qty
      self.qty += amount


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
