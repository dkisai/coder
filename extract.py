import requests
import pandas as pd
import logging


API_KEY = 'f29d2a34d2f0fcf9db7c748ca09c7a1a'

class ExtractData:  


    def extract(self, id_movie): 

        self.id_movie = id_movie
        logging.basicConfig(
        filename='app.log',  # Nombre y ubicación del archivo de registro
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        self.logger = logging.getLogger(__name__)

        req = requests.get(f'https://api.themoviedb.org/3/movie/{self.id_movie}?language=es-MX&api_key={API_KEY}')
        if req.status_code == 200:
            logging.info(f"se encontro pelicula para el id {self.id_movie}")
        else:
             logging.warning(f"no existe pelicula para el id {self.id_movie}")


        movie = pd.json_normalize(req.json())
        df_movie = pd.DataFrame(movie)
        movie_genres = df_movie['genres'].explode('genres')
        df_genres = pd.DataFrame(movie_genres.tolist())
        df_movie_order = df_movie[['id','title','original_title',
                                'release_date','poster_path','budget',
                                'revenue','runtime','tagline']]
        df_overview = df_movie[['id', 'overview']]

        # Para crear el df de la tabla intemedia

        valor_movie_id = df_overview['id'].iloc[0]
        df_genres['movie_id'] = valor_movie_id
        df_movie_genres =  df_genres[['movie_id','id']]
        df_movie_genres = df_movie_genres.rename(columns={'id':'genre_id'})
        logging.info(f"Se extrae la informacion de manera correcta")
        # Regresara los data frames que se solicitan en una tupla

        return (df_movie_order,df_overview,df_movie_genres)