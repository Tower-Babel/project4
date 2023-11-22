import streamlit as st
from PIL import Image

st.title(" :blue[Project 4:] ")
st.title(" :blue[Optiver - Trading at the Close - Part B] ")


image1 = Image.open("project4/Picture1.png")
image2 = Image.open("project4/Picture2.png")
image3 = Image.open("project4/Picture3.png")
image4 = Image.open("project4/Picture4.png")
image5 = Image.open("project4/Picture5.png")
image6 = Image.open("project4/Picture6.png")
st.header("Intro")
st.write(

    """
        This notebook uses Marcos Lopez De Prado's Hierarachical Risk Parity (HRP) approach 
        to address the asset allocation. It is hierarachical 
        clustering to determine the best correlation among certain stocks.

        The concept would be used to gain insights into the data set.

        
    
    """
)

st.header("Cluster Analysis")
st.write(
    """
       

        The goal of cluster analysis is to group a set into disjoint clusters, 
        based on similarities. Objects in the same cluster are very similar to each other, 
        while objects from different clusters have low similarity.

        Partitional vs. hierarchical algorithms. Partitional algorithms produce flat partition, 
        where an element belongs to only one cluster where as, hierarchinal create a multilayered partition 
        with clusters of elements at the bottom level, clusters of clusters at the next level and it continues to the top of the hierarchy.

        https://quantdare.com/hierarchical-clustering/ http://quantdare.com/k-means-algorithm/ 

        Suppose you work at an emergency center, and your is to tell the pilots or firefighter helicopters to take off. 
        The emergency is a fire and a helicopter and pilot will put it out. Which helicopter will arrive first to the fire? 
    
    """
         
    )

st.image(image1, caption=None)
st.write(
    
    """
        You need to choose which pilot has to do this work. It is obvios that the farther helicopters in 
        grey will arrive 
        later then the closer red helicopters but you do not know exatcly which is closet.
    """
    )
st.image(image2, caption=None)
st.write(
    """
        To find the answer to this type of problem it associates all the helicopters to a polygonal cell where all points included are closer to one helicopter than the others. 
        Using the Euclidean distance to define the intersection of all half planes.
    
    """
)

st.header("Data Understanding")
st.write("  ")
st.image(image3, caption=None)

st.header("Pre-proccessing")
st.write(
    """
        Not all stocks have data for every timestamp are replaced with 0 and NA is removed.
    """
    )

st.header("Modeling")
st.write(
    """
        The Voronoi disgram is used in clustering.

        There are 2 options to set initial points: 1.1 Choose k (two-dimensional) points 1.2 Generate k random points
        Calculate Voronoi cells for the initial points
        Calculate midpoint of all points included in each region
        Calculate Voronoi cells for the midpoints
        Repead 3 and 4 while mid points are changing

    K-means algorithm could be used in financial time series. You can create a 2d scatter plat to show the weekly returns and the shift in weeks. It would be benifitial to cluster the returns into 5 classes:

        - Upward
        - Downward
        - No trend
        - Low Upward
        - Low Downward

    """

)
st.image(image4, caption=None)
st.image(image5, caption=None)

st.header("Clustering Analysis Story")
st.write("  ")


st.header("Impact")
st.write("""  
         This feature can be used to improve feature selection for time series forcasting. If two stocks or two features are
         within the same cluster that means they are prositivly correlated. We can visual validate the effectiveness of our clustering.
         We expeced to see distinct blocks for stocks that fall within the same cluster to suggest what cluster moves similarly.
        
         """)
st.image(image6, caption=None)

st.header("References")
st.write("""
         https://github.com/jackblandin/research
         https://www.kaggle.com/code/onurrr90/optiver-exploring-stock-correlations
         https://www.kaggle.com/code/verracodeguacas/sectors-industries-fiesta-pca-magic
         https://www.kaggle.com/code/soyabulislamlincoln/optiver-eda
         https://quantdare.com/hierarchical-clustering/
         """)

st.header("Code")
st.write(" https://www.kaggle.com/code/helloomoto/hcpresearch ")