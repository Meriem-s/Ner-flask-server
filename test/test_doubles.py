class NerModelTestDouble:
    """
    Test double for spaCy NLP Model
    """
    
    def __init__(self, model):
        self.model = model
        
        
    def returns_doc_ents(self, ents):
        #our test model is a new 
        self.ents = ents
    
    def __call__(self, sentence):
        return DocTestDouble(sentence , self.ents)

class DocTestDouble:
    """
    Test double for spaCy Doc
    """

    def __init__(self, sentence, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label']) for ent  in ents]
        
    def patch_method(self, attr, return_value):
        """
        patch the attr ents
        """        
        def patched(): return return_value
        setattr(self, attr, patched)
        return self
    

class SpanTestDouble:
    
    def __init__(self, text, label):
        self.text = text
        self. label = label