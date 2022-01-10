import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble
class TestNerClient(unittest.TestCase):
    
    #method get a string as input and output datastructure containing entity names 
    
    def test_get_ents_returns_dict_given_an_empty_string(self):
        """
        we are making an assertion that our get_ents method returns a dictionary (test the rtype)
        """        
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])# given empty string causes empty
        ner = NamedEntityClient(model)
    
        ents = ner.get_ents("")
        self.assertIsInstance(ents,dict)  
        
        
    def test_get_ents_returns_given_not_empty_string(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Missoula is a City in Montana")
        self.assertIsInstance(ents,dict)  
        
    
    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_PERSON(self):
        #given doc_ents we get back from spacy, our client should get back expected_result
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'Meriem Said', 'label':'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Meriem Said', 'label':'Person'}], 'html':""}
        self.assertListEqual(result['ents'], expected_result['ents'])
        

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        #given doc_ents we get back from spacy, our client should get back expected_result
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'Tunisian', 'label':'NORP'}]        
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Tunisian', 'label':'Group'}], 'html':""}    
        self.assertListEqual(result['ents'], expected_result['ents'])
        
    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        #given doc_ents we get back from spacy, our client should get back expected_result
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'Tunisia', 'label':'LOC'}]        
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Tunisia', 'label':'Location'}], 'html':""}    
        self.assertListEqual(result['ents'], expected_result['ents'])