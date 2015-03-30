class A:
    """
    This is the class definition
    
    this is where mehtods and class attributes are defined
    """
    
    class_attribute_2 = 'I am a class attribute'
    
    def __init__(self, argument_1):
        """
        This is the class initializer
        
        this is where typically instance attributes are defined
        """
        
        self.instance_attribute_1 = 'I am an instance attribute'
        self.instance_attribute_2 = argument_1
        
        
a = A('argument')  # instantiating a new instace of 'A'
b = A(6)

# attrbute access
a.instance_attribute_2  # ==> 'argument'
b.instance_attribute_2  # ==> 6

a.class_attribute_2  # ==> 'I am a class attribute'
b.class_attribute_2  # ==> 'I am a class attribute'

a.instance_attribute_1 == b.instance_attribute_1  # ==> True

# setting the attribute
a.instance_attribute_1 = 5

a.instance_attribute_1 == b.instance_attribute_1  # ==> False