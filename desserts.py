"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    #class attribute to cupcake 
    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""
        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    #Create an instance method no need to add qty bc its an integer   
    def __init__(self, name, flavor, price):

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

    #we want to add the amount to self.qty
      self.qty += amount

    #we want to create another instance method called "sell"
    def sell(self, amount):

    #amount: is a local variable of how many cupcakes we want to sell 
    #self.qty: is the cupcakes we have in stock ß
      
      if self.qty == 0:
        print(f'Sorry, these cupcakes are sold out')

      #if we want to sell 5 cupcakes then we need to check we have the amount in stock 
      if self.qty < amount:
        #if our inventory = 0 then we want to return   
        self.qty = 0
        return
        #we are subtracting from our inventory the cupcakes we sold 
      self.qty -= amount 

    
      #when calling a static method, two things to remember, DO NOT pass self
      #and make sure you put the decorated @staticmethod
      @staticmethod
      def scale_recipe(ingredients, amount):
        """return a tuple with (ingredient_name, ingredient_qty) in a list"""


        #multiplying the ingredient quantity with the amount of cupcackes we want to make 
        ingredient_list = []

        #We want to loop throuh ingredients and quantity in our list ingredients 
        for ingredient, quantity in ingredients:
            #multiply my ingredient and quantity to the amount 
            final = (ingredient, quantity * amount)
            #append it to my empty list 
            ingredient_list.append(final)
        #return my final list of ingredients 
        return ingredient_list


        #when writing a class method, we need to add "@classmethod" on top of my function 
        #and pass "cls" 
        @classmethod
        def get(cls, name):

          if name not in cls.cache:
            print(f'Sorry, that cupcake doesnt exist')
            return 

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
