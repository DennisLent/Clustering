import numpy as np
from utils.linkage import single_linkage, complete_linkage, average_linkage

def _construct_distance_matrix(clusters, linking_func):
    """
    Private function to construct a distance matrix from the clusters

    Parameters
    ----------

    clusters : list
        a list of lists that contain the elements within each cluster
    
    linking_func : function
        a function to specify what type of linking is supposed to be used. The linking function is specified through the clustering. This can be:
            
            * complete linkage
            * single linkage
            * average linkage
    
    Returns
    -------
    distance_matrix : ndarray
        (n by n) matrix that contains the distances from each cluster to each other cluster. Distances between the same cluster are initialized as infinity
    """
    #initialize distance matrix
    num_clusters = len(clusters)
    distance_matrix = np.zeros((num_clusters, num_clusters), float)
    np.fill_diagonal(distance_matrix, np.inf)

    #initialize distances to each cluster
    for i in range(num_clusters):
        for j in range(num_clusters):
            if i != j:
                distance = linking_func(clusters[i], clusters[j])
                distance_matrix[i][j] = distance
    return distance_matrix

def hierarchical_clustering(objects: list, dim=2, linkage="complete", verbose=False):
    """
    Function that will custer a list of objects based on a chosen linking method

    Parameters
    ----------

    objects : list
        List of all the objects that should be clustered
    
    dim : int (optional)
        dimensionality of the points, by default is set to 2 (for the purpose of this dataset)
    
    linkage : str (optional)
        specify the type of linkage function that is supposed to be used. By default it is complete

        * "complete" -> complete linkage
        * "single" -> single linkage
        * "average" -> average linkage
    
    verbose : bool (optional)
        specify if the function should print intermediate steps to see inside workings. By default it is set to False
    """
    if verbose:
        print("------------------------------")
    if linkage:
        match linkage:
            case "complete":
                linking_func = complete_linkage
                if verbose:
                    print("Using complete linkage")
            case "single":
                linking_func = single_linkage
                if verbose:
                    print("Using single linkage")
            case "average":
                linking_func = average_linkage
                if verbose:
                    print("Using average linkage")

    # initialize all points as separate clusters and create distance matrix
    # also initialize the nodes in the binary tree to hold data (cluster, None)
    clusters = [[point] for point in objects]
    distance_matrix = _construct_distance_matrix(clusters, linking_func)
    
    if verbose:
        print(distance_matrix)
        print("\n")
        print(clusters)
    
    #while there is more than 1 cluster
    history = []
    while len(clusters) > 1:
        if verbose:
            print(len(clusters))

        # find two closest clusters and merge
        index = np.unravel_index(np.argmin(distance_matrix, axis=None), distance_matrix.shape)
        min_distance = np.min(distance_matrix)

        if verbose:
            print(f"smallest index @ {index}")

        # create new cluster from closest pair
        index_from, index_to = index
        new_cluster = clusters[index_from] + clusters[index_to]

        # remove two merged clusters
        cluster_to, cluster_from = clusters[index_to], clusters[index_from]
        clusters.remove(cluster_to)
        clusters.remove(cluster_from)

        # update cluster list
        clusters.append(new_cluster)

        history.append((cluster_from, cluster_to, min_distance))

        if verbose:
            print(clusters)

        # update distance matrix
        distance_matrix = _construct_distance_matrix(clusters, linking_func)

    return (history, clusters[0])

        
