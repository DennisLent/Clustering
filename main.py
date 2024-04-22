from data.data_gen import prep_data
from utils.hierarchical import hierarchical_clustering
from utils.plotting import make_dendogram
import argparse

def main():
    parser = argparse.ArgumentParser(description="Hierarchical Clustering of German Cities")
    parser.add_argument("-p", "--pop_limit", type=int, default=200_000, help="Population limit for clustering")
    parser.add_argument("-v", "--verbose", type=bool, default=False, help="Print debugging info while running")
    parser.add_argument("-l", "--linkage", type=str, default="complete", help="The type of linkage to be used \
                        \n - complete : complete linkage \
                        \n - single : single linkage \
                        \n - average : average linkage")
    args = parser.parse_args()

    cities = prep_data(pop_limit=args.pop_limit)
    
    history, final_cluster = hierarchical_clustering(cities, verbose=args.verbose, linkage=args.linkage)
    
    make_dendogram(final_cluster, history)

if __name__ == "__main__":
    main()