## Visualizing Network Data with Kumu

[![Visualizing network data with Kumu](https://i.ytimg.com/vi_webp/OndB17bigkc/sddefault.webp)](https://youtu.be/OndB17bigkc
<youtube_summary>This tutorial introduces Kumu, a tool for visualizing complex relationships between entities, such as social network analysis, by mapping connections and communities. The focus here is on preparing data for Kumu using IMDB data of actors in Indian movies to explore relationships like co-acting and indirect connections.

The process begins by importing libraries (NumPy, pandas) and loading IMDB datasets, filtering for Indian movies and actors. Each movie has a unique identifier (tconst), and each actor has a unique identifier (nconst). The key task is creating a square matrix where rows and columns represent actors, and each element indicates how many movies two actors have acted in together. This is done through matrix multiplication: starting with a binary matrix where rows are movies and columns are actors (1 if the actor acted in the movie, 0 otherwise), multiplying this matrix by its transpose yields the co-acting counts. Diagonal elements represent the number of movies an actor has acted in.

Because the resulting matrix is large and sparse (many zeros), the tutorial explains using the Compressed Sparse Row (CSR) format to efficiently store and process the matrix by keeping only nonzero elements and their indices, significantly reducing memory usage.

The code filters actors who have acted in at least 10 movies and pairs who have acted together in at least 3 movies to reduce data size. The final output is a data frame listing actor pairs (from node to node) with the strength of their connection (number of movies together), suitable for uploading to Kumu.

In Kumu, this data visualizes actor networks showing clusters and connections, allowing exploration of direct and indirect relationships. For example, searching for South Indian superstar Mohanlal reveals his direct and indirect co-actors and connection paths. This helps understand complex networks of relationships.

The tutorial concludes by mentioning future sessions on community detection within such networks to analyze how communities form and relate.

In summary, this tutorial covers:
- Introduction to Kumu for network visualization
- Preparing and filtering IMDB actor-movie data focused on Indian movies
- Creating actor co-acting matrices via matrix multiplication
- Using sparse matrix formats for efficiency
- Filtering data for meaningful network size
- Uploading and visualizing the network in Kumu
- Exploring actor connections and network structure
- Previewing future tutorials on community detection in networks</youtube_summary>
)

- [Kumu](https://kumu.io)
- [IMDB data](https://developer.imdb.com/non-commercial-datasets/)
- [Jupyter Notebook](https://colab.research.google.com/drive/1CHR68fw7lZC9H2JtVW4LXpUvNwfM_VE-?usp=sharing)

[![Network analysis – filtering by year](https://i.ytimg.com/vi_webp/oi4fDzqsCes/sddefault.webp)](https://youtu.be/oi4fDzqsCes
<youtube_summary>The speaker discusses executing code block-by-block, focusing on filtering data by year and language. They address a common issue where the Network adjacency function is missing in the latest SK Network package version; the solution is to install version 0.24 explicitly. The speaker encourages learners to research updated functions themselves for better understanding.

They explain downloading datasets via wget for data preparation and loading a large titles dataset containing movies and series with various types. The goal is to filter this dataset for movies released after a chosen year, e.g., 1950. They demonstrate filtering a pandas DataFrame using Boolean indexing, explaining how to create a Boolean vector by checking conditions on columns.

A problem arises because the 'startYear' column is stored as strings with newline characters ("\n"), which prevents numeric comparisons. To fix this, the speaker shows how to clean the data by stripping unwanted characters using string methods and lambda functions, or by removing rows with invalid entries. They try methods like converting the column using pandas' pd.to_numeric, and using string replace or strip functions to clean the data before conversion.

They highlight that filtering operations on string columns (like using greater-than comparisons) are unreliable, so converting columns to numeric types is necessary for accurate filtering. After cleaning and converting the 'startYear' column, they successfully filter the dataset for movies released after 1950.

For filtering by language or region, the process is similar but applied to another dataset (region DataFrame). The existing function for extracting actor pairs has a language parameter, where you can specify a language code (e.g., 'in' for Indian movies). To use this filter effectively, you should explore the unique values in the language column of the relevant DataFrame.

Throughout, the speaker emphasizes the importance of using Google and documentation as essential resources in data science and coding, encouraging learners to explore and solve issues themselves for better understanding. They also mention sharing the code in a repository for later access.</youtube_summary>
)
