/* PrimVsKruskal.java
   CSC 226 - Spring 2019
   Assignment 2 - Prim MST versus Kruskal MST Template
   
   The file includes the "import edu.princeton.cs.algs4.*;" so that yo can use
   any of the code in the algs4.jar file. You should be able to compile your program
   with the command
   
	javac -cp .;algs4.jar PrimVsKruskal.java
	
   To conveniently test the algorithm with a large input, create a text file
   containing a test graphs (in the format described below) and run
   the program with
   
	java -cp .;algs4.jar PrimVsKruskal file.txt
	
   where file.txt is replaced by the name of the text file.
   
   The input consists of a graph (as an adjacency matrix) in the following format:
   
    <number of vertices>
	<adjacency matrix row 1>
	...
	<adjacency matrix row n>
	
   Entry G[i][j] >= 0.0 of the adjacency matrix gives the weight (as type double) of the edge from 
   vertex i to vertex j (if G[i][j] is 0.0, then the edge does not exist).
   Note that since the graph is undirected, it is assumed that G[i][j]
   is always equal to G[j][i].


   R. Little - 03/07/2019
*/

 import edu.princeton.cs.algs4.*;

import java.util.Arrays;
import java.util.Scanner;
 import java.io.File;

//Do not change the name of the PrimVsKruskal class
public class PrimVsKruskal{

	/* PrimVsKruskal(G)
		Given an adjacency matrix for connected graph G, with no self-loops or parallel edges,
		determine if the minimum spanning tree of G found by Prim's algorithm is equal to 
		the minimum spanning tree of G found by Kruskal's algorithm.
		
		If G[i][j] == 0.0, there is no edge between vertex i and vertex j
		If G[i][j] > 0.0, there is an edge between vertices i and j, and the
		value of G[i][j] gives the weight of the edge.
		No entries of G will be negative.
	*/
	static boolean PrimVsKruskal(double[][] G){
		int n = G.length;
		int count = 0;
		double[][] tmp = new double[n][n];
		/* Build the MST by Prim's and the MST by Kruskal's */
		/* (You may add extra methods if necessary) */
		System.out.printf("Prim Tree:\n");
		//Create an array of edges
		Edge[] edgeArrayPrim = new Edge[n - 1];
		Edge[] edgeArrayKruskal = new Edge[n - 1];
		
		//Initialize the array of edges
		for (int x = 0; x < n - 1; x++) {
			edgeArrayPrim[x]= new Edge(0, 0, 0.0);
			edgeArrayKruskal[x] = new Edge(0, 0, 0.0);
		}
		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				tmp[r][c] = G[r][c];
			}
		}
		MSTbyPrim(G, 0, n, count, edgeArrayPrim);
		
		System.out.printf("Kruskal Tree:\n");
		MSTbyKruskal(tmp, n, edgeArrayKruskal); 
		int sameEdge = 0;
		
		/* Determine if the MST by Prim equals the MST by Kruskal */
		boolean pvk = false;
		for (int i = 0; i < n - 1; i++) {
			int Primthis = edgeArrayPrim[i].either();
			int Primthat = edgeArrayPrim[i].other(Primthis);
			for (int j = 0; j < n - 1; j++) {
				int Kruskalthis = edgeArrayKruskal[j].either();
				int Kruskalthat = edgeArrayKruskal[j].other(Kruskalthis);
				if ((Primthis == Kruskalthis && Primthat == Kruskalthat) || 
						(Primthis == Kruskalthat && Primthat == Kruskalthis)) {
					sameEdge++;
					continue;
				} 
			}
		}
		if (sameEdge == n - 1) {
			pvk = true;
		}
		return pvk;	
	}
	
	//Build the MST by Prim's
	static void MSTbyPrim(double[][]G, int vertexX, int n, int count, Edge[] edgeArray) {
		int currentX = vertexX;
		IndexMinPQ<Double> pq = new IndexMinPQ<Double>(n);
		int[] predecessor = new int[n];
		pq.insert(0, Double.MAX_VALUE);
		Edge tmp = new Edge(0, 0, 0.0);
		double minCost = 0.0;
		
		//run until all vertices are inside the MST
		//ie there are 9 edges in total
		while (edgeArray[n - 2].compareTo(tmp) == 0) {
			//Delete the row in the matrix for the chosen vertex
			//by replace their weight as 0
			for (int i = 0; i < n; i++) {
				G[currentX][i] = 0;
			}
			double minWeight = Double.MAX_VALUE;
			int nextX = currentX;
			
			
			//Push all the distance from current vertex to its adjacent vertices
			for (int j = 0; j < n; j++) {
				//Miss a case when all weight of that column = 0
				//Then those vertices in the PQ has the same other vertex
				//a different other vertex 
				//How to determine that next vertex is adjacent to which already scanned one
				if (j != currentX && G[j][currentX] > 0) {
					//If the other vertex has already in the PQ
					//Check its weight
					//If lower, update. Skip otherwise
					if (pq.contains(j)) {
						if (pq.keyOf(j) > G[j][currentX]) {
							pq.changeKey(j, G[j][currentX]);
							predecessor[j] = currentX;
						}
						
					} else {
						pq.insert(j, G[j][currentX]);
						predecessor[j] = currentX;
					}
					
				}
			}
			
			
			//get the minimum edge
			minWeight = pq.minKey();
			minCost+= minWeight;
			//System.out.printf("MinWeight: %f\n", minWeight);
			//get the correspondent vertexX
			nextX = pq.minIndex();
			//System.out.printf("nextX:%d\n", nextX);
			//delete the edge that has already put into the MST
			pq.delMin();
			edgeArray[count] = new Edge(predecessor[nextX], nextX, minWeight);
			System.out.printf( edgeArray[count].toString() + "\n");
			count++;
			//Update the vertex for the next loop
			
			currentX = nextX;
		} 
		System.out.printf("%f\n", minCost);
	}
	
	//Build the MST by Kruskal
	static void MSTbyKruskal(double[][]G, int n, Edge[] edgeArray) {
		Edge minEdge = new Edge(0,0, 0.0);
		Edge tmp = new Edge(0, 0, 0.0);

		MinPQ<Edge> pq = new MinPQ<Edge>();
		UF uf = new UF(n);
		int count = 0;
		double minCost = 0.0;
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i != j && G[i][j] >0) {
					pq.insert(new Edge(i, j, G[i][j]));
				}
			}
		}
		while (edgeArray[n - 2].compareTo(tmp) == 0) {
			minEdge = pq.delMin();
			int v = minEdge.either();
			int w = minEdge.other(v);
			if (!uf.connected(v, w)) {
				uf.union(v, w);
				edgeArray[count] = minEdge;
				System.out.println(edgeArray[count].toString());
				count++;
				minCost += minEdge.weight();
			}
		}
		System.out.printf("%f\n", minCost);
	}
		
	/* main()
	   Contains code to test the PrimVsKruskal function. You may modify the
	   testing code if needed, but nothing in this function will be considered
	   during marking, and the testing process used for marking will not
	   execute any of the code below. 
	*/
   public static void main(String[] args) {
		Scanner s;
		if (args.length > 0){
			try{
				s = new Scanner(new File(args[0]));
			} catch(java.io.FileNotFoundException e){
				System.out.printf("Unable to open %s\n",args[0]);
				return;
			}
			System.out.printf("Reading input values from %s.\n",args[0]);
		}else{
			s = new Scanner(System.in);
			System.out.printf("Reading input values from stdin.\n");
		}
		
		int n = s.nextInt();
		double[][] G = new double[n][n];
		int valuesRead = 0;
		for (int i = 0; i < n && s.hasNextDouble(); i++){
			for (int j = 0; j < n && s.hasNextDouble(); j++){
				G[i][j] = s.nextDouble();
				if (i == j && G[i][j] != 0.0) {
					System.out.printf("Adjacency matrix contains self-loops.\n");
					return;
				}
				if (G[i][j] < 0.0) {
					System.out.printf("Adjacency matrix contains negative values.\n");
					return;
				}
				if (j < i && G[i][j] != G[j][i]) {
					System.out.printf("Adjacency matrix is not symmetric.\n");
					return;
				}
				valuesRead++;
			}
		}
		
		if (valuesRead < n*n){
			System.out.printf("Adjacency matrix for the graph contains too few values.\n");
			return;
		}	
		
        boolean pvk = PrimVsKruskal(G);
        System.out.printf("Does Prim MST = Kruskal MST? %b\n", pvk);
    }
}
