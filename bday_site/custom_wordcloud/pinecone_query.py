from pinecone import Pinecone;
from sentence_transformers import SentenceTransformer;
from django.conf import settings;
import os;
import joblib;

class PineconeQuery:

    def __init__(self, text):
        self.text = text
        
        # self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        model_path = os.path.join(settings.STATICFILES_DIRS[0], "model.pkl")
        self.model = model = joblib.load(model_path)
        
        # create pinecone vector database
        api = os.path.join(settings.STATICFILES_DIRS[0], "pinecone_api.txt")
        with open(api, 'r') as file:
            api_key = file.read().replace('\n', '')
        pc = Pinecone(api_key = api_key)
        self.index_name = 'happy-bday-2024'
        self.index= pc.Index('happy-bday-2024')
        self.vector = self.model.encode(text)

        

    def query(self):
        # using ID because original plan changed, can also use pinecone similarity to find the closest match
        self.vector = self.vector.tolist()
        self.response  = self.index.query(vector=self.vector, top_k=1)['matches'][0]['id']
        self.score = self.index.query(vector=self.vector, top_k=1)['matches'][0]['score']
    

        # text_file = os.path.join(settings.STATICFILES_DIRS[0], "data.txt")
        # with open(text_file, 'r') as file:
        #     data = file.readlines()
        # self.match = data[int(response)]

        if settings.DEBUG:
            print(f'The query selected: {self.response}')
            print(f'similarity score is {self.score}')
            
        # return self.match, self.score
        return self.response, self.score