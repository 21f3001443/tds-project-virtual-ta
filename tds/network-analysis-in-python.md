## Network Analysis in Python

[![Talk: Exploring the Movie Actor Network in Python](https://i.ytimg.com/vi_webp/uPL3VuRqOy4/sddefault.webp)](https://youtu.be/uPL3VuRqOy4
<youtube_summary>This tutorial demonstrates building and analyzing a network of actors based on the IMDB database, where each node represents an actor and edges indicate co-acting in movies. The goal is to identify clusters (communities) of actors and understand how these clusters connect.

Key steps and concepts covered:

1. **Data Preparation**: 
   - Actors and movies data from IMDB is used, focusing on movies (excluding TV series).
   - Each actor and movie has a unique identifier.
   - Data is subset by language (e.g., Indian movies, US English) and filtered by criteria like minimum number of movies acted.

2. **Matrix Representation**:
   - A binary matrix is created with rows as movies and columns as actors, where a cell denotes whether an actor appeared in a movie.
   - Multiplying this matrix by its transpose produces an actor-actor matrix, where entry Aij indicates the number of movies actors i and j have acted together.
   - This matrix efficiently represents actor relationships using sparse matrix format (CSR).

3. **Network Construction**:
   - Using the sknetwork library, the actor pairs (edges) are converted into an adjacency matrix representing the network.
   - This adjacency matrix is symmetric and encodes co-acting relationships.

4. **Community Detection**:
   - Clustering algorithms (e.g., Louvain method) are applied to detect communities (clusters) within the actor network.
   - Results show meaningful clusters corresponding to film industries or language groups, e.g., Hollywood actors, Bollywood actors, Telugu actors, etc.

5. **Cluster Analysis and Interpretation**:
   - Each actor is assigned a cluster label.
   - Analysis includes counting how many movies an actor has acted in and the proportion within their cluster versus outside clusters.
   - Identifying actors who connect multiple clusters is done by focusing on those with many movies but a low percentage within their own cluster, highlighting actors bridging different communities.

6. **Applications**:
   - The approach can be adapted to other domains, such as social network analysis in villages to understand relationships that influence group behaviors, like loan repayments in microfinance.
   - The tutorial emphasizes the power of network analysis to reveal complex relationships and structures in data.

In summary, the tutorial covers constructing an actor network from movie data, detecting clusters, analyzing cross-cluster connections, and exploring broader applications of network analysis using efficient matrix operations and clustering algorithms.</youtube_summary>
)

You'll learn how to use network analysis to identify clusters and connections between nodes in a dataset, covering:

- **Network Construction**: Build a network from the IMDB database, where nodes represent actors and edges represent shared movie appearances.
- **Clustering**: Apply clustering techniques to detect communities within the network, using scikit-learn's network library.
- **Matrix Operations**: Utilize matrix operations to efficiently analyze actor relationships and interactions.
- **Community Detection**: Implement algorithms to identify and interpret clusters, examining how different actor clusters are connected.
- **Application of Findings**: Explore practical applications of network analysis, such as social network analysis and its potential uses in various domains.

Here are links used in the video:

- [Jupyter Notebook](https://colab.research.google.com/drive/1VRlAOfREGwflv7v2VmN-6O_wqRno4Xcq?usp=sharing)
- [Exploring the Movie Actor Network in Python](https://youtu.be/6hzLw80qxto
<youtube_summary>Anand, a Python programmer and movie enthusiast, explores the intersection of these interests by analyzing actor connections and clusters using data from the Internet Movie Database (IMDb). He investigates how actors connect through co-stars and whether there are clusters of actors who predominantly work together. 

Using IMDb's datasets—title.basics.tsv.gz (basic title info), title.principals.tsv.gz (film cast and crew), and name.basics.tsv.gz (actor details)—he filters for movies (excluding shorts and TV series) and actors/actresses only. Due to a Python gzip module bug, he decompresses files using the zlib module and loads data with pandas.

He constructs a graph of actors and movies using NetworkX, representing actors and titles as nodes connected by edges. This graph enables finding shortest paths between actors via common co-stars. For example, the shortest connection between Robin Williams and Angelina Jolie passes through co-stars like Ethan Hawke and Robert De Niro. Functions convert IMDb IDs to readable names and allow querying shortest paths by actor names. Anand demonstrates similar connections for other actors, highlighting degrees of separation.

Next, Anand explores actor clusters—groups of actors who mainly work together—using clustering algorithms from the scikit-network library. He compares multiple algorithms (Louvain, propagation, k-means, hierarchical) on sample networks and selects the Louvain method for its reasonable, intuitive results.

To apply clustering, he creates an adjacency matrix of actors-to-movies (rows=movies, columns=actors, entries=1 if actor acted in movie) using pandas categories and scipy's sparse CSR matrix. Multiplying this matrix by its transpose yields an actor-to-actor matrix indicating how many movies pairs of actors have co-starred in. Setting diagonal elements to zero removes self-connections. This matrix is used for clustering.

Anand develops utilities to tag actors by region, language, and era (e.g., Indian, South Indian, Tamil, Japanese) to name clusters meaningfully. The clustering reveals distinct actor groups such as Hollywood, Spanish/Mexican, Japanese, Indian (north/south), Chinese/Korean, and others. He notes that some clusters rarely interact, e.g., Filipino actors form the most isolated cluster, while Hollywood connects with many others. Some clusters, like Hollywood porn actors, are surprisingly disconnected from mainstream Hollywood.

He visualizes connections between top actor clusters worldwide, showing frequencies of cross-cluster collaborations and highlighting isolated or closely connected film industries. This network analysis provides insights into global film industry actor collaborations and cluster structures.

Anand encourages experimenting with this approach to explore actor connections and clusterings for other actors or industries. He offers to help with implementation challenges and hopes the project is both fun and educational.</youtube_summary>
)
- [Jupyter Notebook - Shortest Path](https://colab.research.google.com/drive/1-b0pA1O6rCS-ZwU_MWdCzx0CEI_WnyZ2)
- [Jupyter Notebook - Actor network](https://colab.research.google.com/drive/1Lps2fkRlyPAnR63hDOihzCaMvo_RU6Ds)
- [IMDb Datasets](https://developer.imdb.com/non-commercial-datasets/)
- Learn about the [`sknetwork` package](https://scikit-network.readthedocs.io/en/latest/use_cases/votes.html)
- Learn about the [scipy.sparse matrices](https://cmdlinetips.com/2018/03/sparse-matrices-in-python-with-scipy/) and [video](https://youtu.be/v_S7cOL5ZWU
<youtube_summary>The speaker responds to a viewer's request to explain in detail the calculations behind a previous Monte Carlo simulation video that modeled stock price behavior assuming normally distributed returns. Instead of looping through price changes, they used a complicated matrix equation to vectorize the process, which is common in solving linear systems repeatedly encountered in various fields.

They plan to review the code for the Monte Carlo simulation, explain the matrix approach in detail, and later apply the same math to a physics problem involving diffusion and heat flow in a one-dimensional beam, highlighting the similarity in linear system treatment.

The explanation begins with linear equations involving three variables (x1, x2, x3) and their representation as matrix equations. They clarify matrix multiplication rules, showing how the system of equations corresponds to multiplying a coefficient matrix by a vector of unknowns to yield a vector of known values.

The concept of solving such systems by multiplying both sides by the matrix inverse is introduced, analogous to dividing both sides by a scalar in simple algebra. They define the identity matrix and demonstrate that multiplying a matrix by its inverse yields the identity matrix, which leaves the unknown vector unchanged.

Using NumPy, they generate a random 4x4 matrix, calculate its inverse via the linear algebra module, and verify that multiplying the matrix by its inverse returns the identity matrix. Then, given a known vector, they solve for the unknown vector by multiplying the inverse matrix by the known vector, confirming the solution satisfies the original equations. They also mention NumPy's built-in solve function as a shortcut to find the unknowns directly.

Next, the speaker connects this linear algebra approach to the stock price simulation and the heat diffusion partial differential equation (PDE). They note that while dense matrices (mostly non-zero entries) become computationally infeasible for very large sizes (due to memory and operation counts scaling as n² and n³), most real-world problems yield sparse matrices with many zeros, enabling efficient storage and computation using specialized algorithms.

Returning to the stock simulation, they explain the basic model: the stock price on day i+1 depends on the price on day i, a risk-free rate, volatility, and a random normal variable. They set parameters like initial stock price, annual risk-free rate, annual volatility, and convert these to daily equivalents. Using a for loop, they simulate stock prices for five days, storing results in a list and plotting them.

They then rewrite the iterative stock price equations as a system of linear equations, showing the linearity and constructing the corresponding matrix form, which results in a sparse matrix with ones and minus ones on main and sub-diagonals. This matrix form can be efficiently handled using sparse matrix libraries.

The speaker imports SciPy's sparse matrix library and its diagonal matrix constructor function (diags). They illustrate how to create diagonal arrays and assemble the sparse matrix representing the system. They create the vector of known values with the initial stock price and zeros elsewhere.

Using the sparse linear algebra solver (spsolve), they solve the system to find the stock prices and plot the results, verifying they match the earlier iterative simulation. They note that this sparse matrix approach is more efficient and necessary for larger problems, such as PDEs with large matrices.

Finally, they conclude this part, planning to continue with a full Monte Carlo simulation generalizing to many stock paths and then applying the method to solve the heat equation PDE, emphasizing the computational advantages of the sparse matrix method.</youtube_summary>
)
- [Introduction to Kumu](https://youtu.be/fwiz7PnipgQ
<youtube_summary>Torie Beatty provides an introduction to Kumu, a data visualization platform used to create interactive relationship maps similar to Google Data Studio and Microsoft Power BI. The interface includes links to pricing, a gallery of examples, and a manifesto. Kumu offers three account types: personal (unlimited public projects, full feature access, contributors only), organizational (group projects/users, admin management, read-only user access), and enterprise (for large organizations with special security needs). Signing up requires an email, username, and password.

The dashboard includes a "Zero to Kumu" tutorial for beginners, as the interface is not very intuitive. To start a project, users name it, choose public or private status, then select from map templates such as system maps (visualizing cause and effect), stakeholder maps (showing involved parties and connections), and SN maps (identifying influencers and power structures). Torie demonstrates creating a simple stakeholder map by adding elements (e.g., people) with customizable types, descriptions, and images, and connecting these elements with labeled relationships. Text length appears unlimited, aiding complex projects. Connections can be detailed, and data can also be imported from spreadsheets or Google Sheets, encouraging collaboration but with risks of public editing.

Deleting projects is not straightforward; it requires navigating through the admin panel. Torie highlights a complex example from the gallery, a large global situational analysis map, showcasing detailed elements, relationships, and interactive features that reveal extensive contextual information. Such advanced maps likely require experienced users and significant time investment.

Overall, Kumu is a powerful but somewhat complex tool, best suited for users willing to engage with tutorials and invest time in learning. Torie encourages exploring the gallery examples to assess if Kumu fits one's needs.</youtube_summary>
)
- [Network analysis with Kumu](https://docs.kumu.io/guides/disciplines/sna-network-mapping)
- [Introduction to Systems and Network Mapping with Kumu](https://www.coursera.org/projects/systems-network-kumu)
